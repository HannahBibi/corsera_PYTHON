x = "X-DSPAM-Confidence:    0.8475"
y = x.find("0")
num = x[y:]
float(num)
print(num)
