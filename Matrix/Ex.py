import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter the number of rows for {name}: "))
    cols = int(input(f"Enter the number of columns for {name}: "))
    print(f"Enter the elements of {name} (separated by space):")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))  # ใช้ float เพื่อรองรับค่าทศนิยม
        matrix.append(row)
    return np.array(matrix)

def matrix_addition(matrix1, matrix2):
    return matrix1 + matrix2

def matrix_subtraction(matrix1, matrix2):
    return matrix1 - matrix2

def matrix_multiplication(matrix1, matrix2):
    return matrix1 * matrix2

def matrix_division(matrix1, matrix2):
    return matrix1 / matrix2

def matrix_transpose(matrix):
    return matrix.T

def matrix_inverse(matrix):
    return np.linalg.inv(matrix)

def display_menu():
    print("\nSelect the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication (Element-wise)")
    print("4. Division (Element-wise)")
    print("5. Transpose")
    print("6. Inverse")
    print("7. Exit")

def matrix_operations():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice in ['1', '2', '3', '4']:
            matrix1 = input_matrix("Matrix 1")
            matrix2 = input_matrix("Matrix 2")
            
            if matrix1.shape != matrix2.shape:
                print("Matrices must have the same dimensions for this operation.")
                continue
            
            if choice == '1':
                result = matrix_addition(matrix1, matrix2)
                print("Result of Addition:\n", result)
            elif choice == '2':
                result = matrix_subtraction(matrix1, matrix2)
                print("Result of Subtraction:\n", result)
            elif choice == '3':
                result = matrix_multiplication(matrix1, matrix2)
                print("Result of Multiplication (Element-wise):\n", result)
            elif choice == '4':
                result = matrix_division(matrix1, matrix2)
                print("Result of Division (Element-wise):\n", result)

        elif choice == '5':
            matrix = input_matrix("Matrix")
            result = matrix_transpose(matrix)
            print("Result of Transpose:\n", result)

        elif choice == '6':
            matrix = input_matrix("Matrix")
            if matrix.shape[0] != matrix.shape[1]:
                print("Matrix must be square to calculate the inverse.")
            else:
                result = matrix_inverse(matrix)
                print("Result of Inverse:\n", result)
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# เรียกใช้ฟังก์ชันหลัก
matrix_operations()