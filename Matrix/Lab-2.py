# import numpy as np

# # กำหนดเมตริกซ์
# A = np.array([[1, 1, -2, 3], [2, -1, 3, -1], [3, 4, -1, 2], [4, -2, 2, 5]])
# b = np.array([9, 8, 12, 7])

# # คำนวณอินเวิร์สของ A
# A_inv = np.linalg.inv(A)

# # แก้สมการ
# x = np.dot(A_inv, b)
# print("คำตอบโดยใช้ inv:", x)

# import numpy as np

# # กำหนดเมตริกซ์
# A = np.array([[1, 1, -2, 3], [2, -1, 3, -1], [3, 4, -1, 2], [4, -2, 2, 5]])
# b = np.array([9, 8, 12, 7])

# # แก้สมการ
# x = np.linalg.solve(A, b)
# print("คำตอบโดยใช้ solve:", x)

# import numpy as np

# # กำหนดเมตริกซ์
# A = np.array([[1, 2, 1], [2, -1, 3], [3, 4, -1]])
# b = np.array([6, 14, 10])

# # คำนวณอินเวิร์สของ A
# A_inv = np.linalg.inv(A)

# # แก้สมการ
# x = np.dot(A_inv, b)
# print("คำตอบโดยใช้ inv:", x)

import numpy as np

# กำหนดเมตริกซ์
A = np.array([[1, 2, 1], [2, -1, 3], [3, 4, -1]])
b = np.array([6, 14, 10])

# แก้สมการ
x = np.linalg.solve(A, b)
print("คำตอบโดยใช้ solve:", x)