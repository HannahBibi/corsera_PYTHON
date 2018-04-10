from corsera_python.other.PythonSum import sum
from corsera_python.other.PythonCount import count

def avg (l):
    curr_sum = 0
    curr_count = 0
    for i in l:
        curr_count = curr_count + 1
        curr_sum = curr_sum + i
    return curr_sum / curr_count

def avg2 (l):
    return sum(l) / count(l)
