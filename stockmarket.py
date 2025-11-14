file = open("days1-20.txt", "r")
buffer1_20 = file.readlines()
print(buffer1_20)
file.close()

MSFT = (buffer1_20[0]).strip().split(", ")
AMZN = (buffer1_20[1]).strip().split(", ")
NVDA = (buffer1_20[2]).strip().split(", ")
MSFTsum = 0
AMZNsum = 0
NVDAsum = 0

print(f"{MSFT}\n{AMZN}\n{NVDA}")

try:
    for i in range(len(MSFT)):
        if MSFT[i].isnumeric():
            MSFT[i] = int(MSFT[i])
            MSFTsum = MSFTsum + MSFT[i]
    for i in range(len(AMZN)):
        if AMZN[i].isnumeric():
            AMZN[i] = int(AMZN[i])
            AMZNsum = AMZNsum + AMZN[i]
    for i in range(len(NVDA)):
        if NVDA[i].isnumeric():
            NVDA[i] = int(NVDA[i])
            NVDAsum = NVDAsum + NVDA[i]
except Exception as e:
    print(f"An error has risen. Womp Womp.{e}")
else:
    MSFTavg = MSFTsum/len(MSFT)
    AMZNavg = AMZNsum/len(AMZN)
    NVDAavg = NVDAsum/len(NVDA)
    print(f"Here are the averages for days 1-20 for MSFT {MSFTavg}, AMZN {AMZNavg}, and NVDA {NVDAavg}.")



file = open("days21-40.txt", "r")
buffer21_40 = file.readlines()
print(buffer21_40)
file.close()

MSFT21_40 = (buffer21_40[0]).strip().split(", ")
AMZN21_40 = (buffer21_40[1]).strip().split(", ")
NVDA21_40 = (buffer21_40[2]).strip().split(", ")
MSFTsum21_40 = 0
AMZNsum21_40 = 0
NVDAsum21_40 = 0

print(f"{MSFT21_40}\n{AMZN21_40}\n{NVDA21_40}")

try:
    for i in range(len(MSFT21_40)):
        if MSFT21_40[i].isnumeric():
            MSFT21_40[i] = int(MSFT21_40[i])
            MSFTsum21_40 = MSFTsum21_40 + MSFT21_40[i]
    for i in range(len(AMZN21_40)):
        if AMZN21_40[i].isnumeric():
            AMZN21_40[i] = int(AMZN21_40[i])
            AMZNsum21_40 = AMZNsum21_40 + AMZN21_40[i]
    for i in range(len(NVDA21_40)):
        if NVDA21_40[i].isnumeric():
            NVDA21_40[i] = int(NVDA21_40[i])
            NVDAsum21_40 = NVDAsum21_40 + NVDA21_40[i]
except Exception as e:
    print(f"An error has risen. Womp Womp.{e}")
else:
    MSFTavg21_40 = MSFTsum21_40/len(MSFT21_40)
    AMZNavg21_40 = AMZNsum21_40/len(AMZN21_40)
    NVDAavg21_40 = NVDAsum21_40/len(NVDA21_40)
    print(f"Here are the averages for days 1-20 for MFST {MSFTavg21_40}, AMSN {AMZNavg21_40}, and NVDA {NVDAavg21_40}.")

try:
    buys=[]
    if MSFTavg < MSFTavg21_40 and AMZNavg < AMZNavg21_40 and NVDAavg < NVDAavg21_40:
        buys.append("MSFT")
        buys.append("AMZN")
        buys.append("NVDA")
    elif MSFTavg < MSFTavg21_40 and AMZNavg < AMZNavg21_40:
        buys.append("MSFT")
        buys.append("AMZN")
    elif MSFTavg < MSFTavg21_40 and NVDAavg < NVDAavg21_40:
        buys.append("MSFT")
        buys.append("NVDA")
    elif NVDAavg < NVDAavg21_40 and AMZNavg < AMZNavg21_40:
        buys.append("NVDA")
        buys.append("AMZN")
    print(f"Stocks you should buy: {buys}")
    file = open("buys.txt", "w")
    file.writelines(buys)
    file.close()

except Exception as e:
    print(e)



