#Import necessary modules
import math
from math import ceil, floor, log2
from math import sin, cos, pi
import numpy as np


# Function to multiply two polynomials in O(n^2) time
def naive_polynomial_multiplication(A, B, m, n):

    prod = [0] * (m + n - 1)
    
    # Multiply two polynomials term by term
    
    # Take every term of first polynomial
    for i in range(m):
        
        # Multiply the current term of first
        # polynomial with every term of
        # second polynomial.
        for j in range(n):
            prod[i + j] += A[i] * B[j]

    return prod

# Function to print a polynomial
def printPoly(poly, n):

    for i in range(n):
        print(poly[i], end = "")
        if (i != 0):
            print("x*", i, end = "")
        if (i != n - 1):
            print(" + ", end = "")

# Function to find 'N-value' that is greater than or equal to 'deg_1+deg_2+1'
def find_N(deg_1, deg_2):

    N = deg_1+deg_2+1
    while 1:
        if ceil(log2(N)) == floor(log2(N)):
            return N
        else:
            N = N+1


# 'roots' stores the N complex roots of unity
roots = []
# Function to compute N complex roots of unity
def find_complex_roots(N):

    # theta = 2*pi/n
    theta = math.pi * 2 / N
 
    # print all nth roots with 6 significant digits
    for k in range(0, N):
 
        # calculate the real and imaginary part of root
        real = math.cos(k * theta)
        img = math.sin(k * theta)

        number = (real, img)

        roots.append(number)

# Function to MULTIPLY two complex numbers
def multiply_complex_num(z1, z2): 
    return z1*z2

# Function to ADD two complex numbers
def add_complex_num(z1, z2):
    return z1+z2


# Function to compute the value of the polynomils at N complex roots of unity (A Divide-and-Conquer approach)
# Time Complexity O(nlogn)
def Eval(A, m, w):
    
    # Base case
    if m == 1:
        return [A[0]]
    else:
        # Divide the polynomials in half containing even and odd coefficients
        A_even = []
        A_odd = []
        for i in range(len(A)):
            if i%2 == 0:
                A_even.append(A[i])
            else:
                A_odd.append(A[i])

        # Recursive calls
        F_even = Eval(A_even, m//2, w*w)
        F_odd = Eval(A_odd, m//2, w*w)

        # 'F' is a list of size 'm' that stores the result
        F = [0]*int(m)

        # Evaluation according to the formula A(x) = A0(x^2) + xA1(x^2)
        x = 1
        for j in range(int(m/2)):
            F[j] = F_even[j] + x*F_odd[j]
            F[j+int(m/2)] = F_even[j] - x*F_odd[j]
            x = x*w

    return F


# Function for inverse FFT
def inverse_FFT(product_poly_evaluations, roots, N):

    rows = N
    cols = N

    # 'V' is the Vandermonde matrix (Zero initialization)
    V = [[0 for _ in range(cols)] for _ in range(rows)]

    u = 0
    for i in range(0, rows):
        v = 0
        for j in range(0, cols):
            V[i][j] = (1/pow(complex(roots[v][0], roots[v][1]),u))*(1/N) # Doing Inversion...
            v = v + 1
        u = u+1

    # 'Q' is the column matrix 
    Q = [[0 for _ in range(1)] for _ in range(rows)]

    t = 0
    for i in range(len(product_poly_evaluations)):
        Q[i][0] = product_poly_evaluations[t]
        t = t + 1

    # Matrix multiplication to solve the system of linear equations
    result = [[0 for _ in range(1)] for _ in range(rows)]
    for i in range(len(V)):
        for j in range(len(Q[0])):
            for k in range(len(Q)):
                result[i][j] = add_complex_num(result[i][j], (complex(V[i][k]) * complex(Q[k][j])))

    return result



    
# User input the 'degree value' of the first polynomial
print("Enter the degree of the first polynomial: ")
deg_1 = int(input())

# Take user input the coefficients of the first polynomial
print("\nPress ENTER after each 'degree value'.")
print("Enter the coefficients of the first polynomial in the increasing order of the degree of the monomials they belong to: ")
poly_1 = []
for x in range(deg_1+1):
    poly_1.append(int(input()))

# User input the 'degree value' of the second polynomial
print("\nEnter the degree of the second polynomial: ")
deg_2 = int(input())

# Take user input the coefficients of the second polynomial
print("\nPress ENTER after each 'degree value'.")
print("Enter the coefficients of the second polynomial in the increasing order of the degree of the monomials they belong to: ")
poly_2 = []
for x in range(deg_2+1):
    poly_2.append(int(input()))

# 'm' and 'n' are the lengths of the polynomial_1 and polynomial_2 respectively
m = len(poly_1)
n = len(poly_2)

# Print the first polynomial
print("\nFirst polynomial is: ")
printPoly(poly_1, m)

# Print the second polynomial
print("\nSecond polynomial is: ")
printPoly(poly_2, n)

naive_prod = naive_polynomial_multiplication(poly_1, poly_2, m, n)
# Print the resultant polynomial after multiplication via naive approach
print("\nThe product of the two polynomials obtained via naive polynomial multiplication is: ")
printPoly(naive_prod, m+n-1)

# Get the 'N-value'
N = find_N(deg_1, deg_2)



# Print the 'N-value'
print("\nN value: ")
print(N)



# Get the N complex roots of unity
find_complex_roots(N)



# Print N complex roots of unity
print("N complex roots of unity: ")
for i in range(len(roots)):
    print(str(roots[i][0])+"+"+str(roots[i][1])+"j")
    

# Append Zeros to the polynomials
if len(poly_1)<N:
    for i in range(len(poly_1), N):
        poly_1.append(complex(0,0))
if len(poly_2)<N:
    for i in range(len(poly_2), N):
        poly_2.append(complex(0,0))

# Get the evaluated polynomials at N complex roots of unity
poly_1_evaluations = Eval(poly_1, N, complex(roots[1][0], roots[1][1]))
poly_2_evaluations = Eval(poly_2, N, complex(roots[1][0], roots[1][1]))


"""
# Print the evaluated polynomials at N complex roots of unity
print("\nEvaluated polynomial_1 at N complex roots of unity:\n")
for i in range(len(poly_1_evaluations)):
    print(poly_1_evaluations[i])
print("\nEvaluated polynomial_2 at N complex roots of unity:\n")
for i in range(len(poly_2_evaluations)):
    print(poly_2_evaluations[i])
"""


# Get the evaluation of the product polynomial at the N complex roots of unity
product_poly_evaluations = []
for i in range(N):
    product_poly_evaluations.append(multiply_complex_num(poly_1_evaluations[i], poly_2_evaluations[i]))


"""
# Print the evaluated product polynomial at the N complex roots of unity
print("\nEvaluated product polynomial at N complex roots of unity:\n")
for i in range(len(product_poly_evaluations)):
    print(product_poly_evaluations[i])
"""

# Inverse FFT
fft_prod = inverse_FFT(product_poly_evaluations, roots, N)

# Print the polynomial after converting to coefficient representation from point-value reprsentation
print("\nFinal output: ")
for i in range(len(fft_prod)):
    print(fft_prod[i][0], end = "")
    if (i != 0):
        print("x*", i, end = "")
    if (i != len(fft_prod) - 1):
        print(" + ", end = "")

print("\nNote:")
print("The imaginary parts of the final output are NEARLY ZERO.")
print("The real parts of the final output are NEARLY equal to the desired value.")