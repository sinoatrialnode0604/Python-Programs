#importing numpy library

import numpy as np

#creating numpy array

arr = np.array([16,3,44,23])

#getting numpy array element.

print(arr[2])

#reshaping array.

arr1 = np.array([[1,2,3],[3,4,5]])
print(arr1.shape)
arr2 = arr1.reshape(3,2)
print(arr2)

#iterating array

for i in arr:
    print(i)

#joining numpy array
arr_1 = np.array([23,2,32])
arr_2 = np.array([45,45])

joined_arr = np.concatenate((arr_1,arr_2))
print(joined_arr)

#splitting numpy array

list = np.array([34,2,45,3211,45,34])
list_1 = np.split(list,2)

print(list_1)

#searching array

nums = np.array([23,34,56])
print(np.where(nums == 34))

#sorting array.
print(np.sort(nums))
