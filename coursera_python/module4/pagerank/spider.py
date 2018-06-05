import sqlite3
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

db_connection = sqlite3.connect('spider.sqlite')
cursor = db_connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Pages
    (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
     error INTEGER, old_rank REAL, new_rank REAL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Links
    (from_id INTEGER, to_id INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)''')

cursor.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
row = cursor.fetchone()
if row is not None:
    print("Restarting existing crawl.  Remove spider.sqlite to start a fresh crawl.")
else:
    start_url = input('Enter web url or enter: ')
    if len(start_url) < 1:
        start_url = 'http://www.dr-chuck.com/'
    if start_url.endswith('/'):
        start_url = start_url[:-1]
    web = start_url
    if start_url.endswith('.htm') or start_url.endswith('.html'):
        pos = start_url.rfind('/')
        web = start_url[:pos]

    if len(web) > 1:
        cursor.execute('INSERT OR IGNORE INTO Webs (url) VALUES ( ? )', ( web, ) )
        cursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( starturl, ) )
        db_connection.commit()

cursor.execute('''SELECT url FROM Webs''')
webs = list()
for row in cursor:
    webs.append(str(row[0]))

print(webs)

many = 0
while True:
    if many < 1:
        sval = input('How many pages:')
        if len(sval) < 1: break
        many = int(sval)
    many = many - 1

    cursor.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
    try:
        row = cursor.fetchone()
        # print row
        from_id = row[0]
        url = row[1]
    except:
        print('No unretrieved HTML pages found')
        many = 0
        break

    print(from_id, url, end=' ')

    # If we are retrieving this page, there should be no links from it
    cursor.execute('DELETE from Links WHERE from_id=?', (from_id, ) )
    try:
        document = urlopen(url, context=ctx)

        html = document.read()
        if document.getcode() != 200 :
            print("Error on page: ",document.getcode())
            cursor.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url) )

        if 'text/html' != document.info().get_content_type() :
            print("Ignore non text/html page")
            cursor.execute('DELETE FROM Pages WHERE url=?', ( url, ) )
            cursor.execute('UPDATE Pages SET error=0 WHERE url=?', (url, ) )
            db_connection.commit()
            continue

        print('('+str(len(html))+')', end=' ')

        soup = BeautifulSoup(html, "html.parser")
    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break
    except:
        print("Unable to retrieve or parse page")
        cursor.execute('UPDATE Pages SET error=-1 WHERE url=?', (url, ) )
        db_connection.commit()
        continue

    cursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( url, ) )
    cursor.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url))
    db_connection.commit()

    tags = soup('a')
    count = 0
    for tag in tags:
        href = tag.get('href', None)
        if href is None:
            continue

        up = urlparse(href)
        if len(up.scheme) < 1:
            href = urljoin(url, href)
        ipos = href.find('#')
        if ipos > 1:
            href = href[:ipos]
        if href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif'):
            continue
        if href.endswith('/'):
            href = href[:-1]
        # print href
        if len(href) < 1:
            continue

        found = False
        for web in webs:
            if href.startswith(web):
                found = True
                break
        if not found:
            continue

        cursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( href, ) )
        count = count + 1
        db_connection.commit()

        cursor.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', ( href, ))
        try:
            row = cursor.fetchone()
            toid = row[0]
        except:
            print('Could not retrieve id')
            continue
        # print fromid, toid
        cursor.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES ( ?, ? )', ( from_id, toid ) )


    print(count)

cursor.close()
