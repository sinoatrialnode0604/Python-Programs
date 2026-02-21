import numpy as np
import matplotlib.pyplot as plt

x = ["JAVA","PYTHON","GOLANG"]
y = [12,4,8]

plt.bar(x,y,color = 'maroon',width = 0.6)
plt.title("Bar Graph")
plt.xlabel("Languages")
plt.ylabel("No of students")
plt.show()