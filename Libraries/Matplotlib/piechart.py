import matplotlib.pyplot as plt

teams = ["Mercedes","Mclaren","Ferrari","Redbull"]
data = [34,24,56,98]

plt.pie(data,labels=teams)
plt.show()