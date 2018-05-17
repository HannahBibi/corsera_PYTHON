import re


def extract_sum(filename):
    file_handle = open(filename)
    count_sum = 0
    for line in file_handle:
        extract = re.findall('[0-9]+', line)
        for number in extract:
            num = int(number)
            count_sum = count_sum + num
    file_handle.close()
    return count_sum
