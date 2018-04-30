def count_time_stamp(filename):
    hist = dict()
    file_handle = open(filename)
    for line in file_handle:
        if 'From ' not in line:
            continue
        words = line.split()
        time_stamp = words[5].split(":")
        hour = time_stamp[0]
        hist[hour] = hist.get(hour, 0) + 1
    file_handle.close()
    hist = sorted(hist.items())
    return hist
