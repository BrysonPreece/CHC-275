file = open("days1-20.txt", "r")
buffer1_40 = file.readlines()
print(buffer1_40)
file.close()

MFST = (buffer1_40[0]).strip().split(", ")
AMSN = (buffer1_40[1]).strip().split(", ")
NVDA = (buffer1_40[2]).strip().split(", ")
MFSTsum = 0
AMSNsum = 0
NVDAsum = 0

print(f"{MFST}\n{AMSN}\n{NVDA}")

try:
    for i in range(len(MFST)):
        if MFST[1].isnumeric():
            MFST[1] = int(MFST[1])
    for i in range(len(AMSN)):
        if AMSN[1].isnumeric():
            AMSN[1] = int(AMSN[1])
    for i in range(len(MFST)):
        if NVDA[1].isnumeric():
            NVDA[1] = int(NVDA[1])
            
except Exception as e:
    print(f"An error has risen. Womp Womp.{e}")
else:
    MFSTsum = MFSTsum/len(MFST)
    AMSNsum = AMSNsum/len(AMSN)
    NVDAsum = NVDAsum/len(NVDA)
print(f"Here are the averages for days 1-20 for MFST {MFSTsum}, AMSN {AMSNsum}, and NVDA {NVDAsum}.")

