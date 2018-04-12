def count_mail(filename):
    hist = dict()
    file_handle = open(filename)
    for line in file_handle:
        if 'From ' not in line:
            continue
        words = line.split()
        email = words[1]
        hist[email] = hist.get(email, 0) + 1
    max_count = None
    max_email = None
    for addr, count in hist.items():
        if max_count is None or count > max_count:
            max_count = count
            max_email = addr
    return max_email + ' ' + str(max_count)
