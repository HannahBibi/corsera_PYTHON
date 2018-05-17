fname = input("Enter file name: ")
fh = open(fname)

count = 0
running_total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find("0")
    n = line[pos:]
    count = count + 1
    running_total = running_total+float(n)

print("Average spam confidence", running_total / count)
