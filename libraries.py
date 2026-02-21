# line plot
import matplotlib.pyplot as plt
import numpy as np
x = np.array([9,8,7,6])
y = np.array([8,7,6,5])
plt.plot(x,y)
plt.xlabel("the even")
plt.ylabel("the odd")
plt.title("the difference")
plt.show()
# bar chart
import matplotlib.pyplot as plt
import numpy as np
x= np.array (["aston martin","audi","ferrari","cadillac","mclaren","reb bull racing", "mercedes amg"])
y = np.array([5,8,2,8,9,10,10])
plt.bar(x,y)
plt.title("Fan rating of teams in 2026")
plt.xlabel("constructors")
plt.ylabel("rating")
plt.show()
# pie chart
import matplotlib.pyplot as plt
import numpy as np
x= np.array (["aston martin","audi","ferrari","cadillac","mclaren","reb bull racing", "mercedes amg"])
y = np.array([5,8,2,8,9,10,10])
plt.pie(y,labels=x)
plt.title("Fan rating of teams in 2026")
plt.show()
# scatter plot
import matplotlib.pyplot as plt
import numpy as np
x= np.array([1,4,2,6,11])
y= np.array([6,8,11,8,11])
x1= np.array([2,8,7,5,6])
y1= np.array([9,5,3,7,1])
plt.scatter(x,y,c="blue")
plt.scatter(x1,y1,c="red")
plt.xlabel("the x axis")
plt.ylabel("the y axis")
plt.title("scatter plot")
plt.show()

