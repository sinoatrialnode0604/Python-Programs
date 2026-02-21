import pandas as pd

data = [11,25,12,13,134]

df = pd.DataFrame(data)

print(df)

data1 = [["Alex",13],["Diddy",60],["Epstein",58]]
details = pd.DataFrame(data1,columns=["Name","Age"])
print(details)