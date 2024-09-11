import numpy as np
# pi = np.pi

# print (f"sin 90 = {np.sin(90)}");
# print (f"cos 180 = {np.cos(180)}");

# radians90 = np.radians(90)
# radians180 = np.radians(180)

# print (f"sin 90 = {np.sin(radians90)}");
# print (f"cos 180 = {np.cos(radians180)}");

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a , type(a) , a.ndim , a.shape , a.dtype , a.itemsize , a.size , a.nbytes)

a = np.array([[2,3],[4,6]])
b = np.array([5,10])

a_inv = np.linalg.inv(a)
x_inv = np.dot(a_inv,b)
print(x_inv)
