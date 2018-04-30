import xml.etree.ElementTree as ET


def crawl_data(url_mock, url):
    html = url_mock.request.urlopen(url).read()
    tree = ET.fromstring(html)
    xml_tree = tree.findall('comments/comment')
    running_count = 0
    for comment in xml_tree:
        c = comment.find('count').text
        i = int(c)
        running_count = running_count + i
    return running_count
