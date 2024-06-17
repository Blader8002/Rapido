import pandas as pd
sensorsFile = open("data/sensor.txt", "r")
sensorHeadings = open("data/sensorHeadings.txt", "r")
f = open("data/sensorTableOutput.csv", "w")
headings = sensorHeadings.readline().split(",")
data = []
i = 0


for line in sensorsFile:
    splittedString = line.split(",")
    print(i)
    data.append([splittedString[0], splittedString[1], splittedString[2], splittedString[3], splittedString[4], splittedString[5], splittedString[6], splittedString[7].strip()])
    i += 1
    
df = pd.DataFrame(data, columns=headings)
df.to_csv(f, encoding="utf-7")
print(df)