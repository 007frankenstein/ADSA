# Implementation of Optimal Binary Search Tree (OBST).
# The dynamic programming algorithm below runs in O(n^3) time.


# Import necessary modules
import sys
import math


def print_binary_search_tree(root, key, i, j, parent, is_left):

    """
    Recursive function to print a BST from a root table in preorder fashion.

    """
    if i > j or i < 0 or j > len(root) - 1:
        return

    node = root[i][j]
    
    print(key[node])
    print_binary_search_tree(root, key, i, node - 1, key[node], True)
    print_binary_search_tree(root, key, node + 1, j, key[node], False)


def find_optimal_binary_search_tree(words, freqs):

    """
    This function calculates and prints the optimal binary search tree.

    """


    n = len(words)

    keys = [words[i] for i in range(n)]

    # 2D array that stores the overall tree cost (which is as minimized as possible)
    # for a single key, cost is equal to frequency of the key.
    opt_sol = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]

    # sum[i][j] stores the sum of key frequencies between i and j inclusive in nodes array
    sum = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]

    # stores tree roots that will be used later for constructing binary search tree
    root = [[i if i == j else 0 for j in range(n)] for i in range(n)]

    for il in range(2, n + 1):
        for i in range(n - il + 1):
            j = i + il - 1

            opt_sol[i][j] = sys.maxsize  # set the value to "infinity"
            sum[i][j] = sum[i][j - 1] + freqs[j]

 
            for r in range(i, j + 1): # r is a temporal root
                left = opt_sol[i][r - 1] if r != i else 0  # optimal cost for left subtree
                right = opt_sol[r + 1][j] if r != j else 0  # optimal cost for right subtree
                cost = left + sum[i][j] + right
                cost = round(cost, 2)

                if opt_sol[i][j] > cost:
                    opt_sol[i][j] = cost
                    root[i][j] = r

    print(f"\nThe minimum expected total access time is {opt_sol[0][n - 1]}.")
    print("\nPreorder traversal of the BST that provides minimum expected total access time is: ")
    print_binary_search_tree(root, keys, 0, n - 1, -1, False)
    
  

# Function that checks whether two strings s1 and s2 are in alphabetical order or not.
def isAlphabaticOrder(s1, s2):
     
    # length of the strings s1 and s2 respectively
    n = len(s1)
    m = len(s2)
 

    if n <= m:
      for i in range(n):
        if (s1[i] < s2[i]):
          return True
        elif (s1[i] == s2[i]):
          continue
        else:
          return False
    else:
      for i in range(m):
        if (s1[i] < s2[i]):
          return True
        elif (s1[i] == s2[i]):
          continue
        else:
          return False



def main():

    print("How many strings do you want to insert in the BST?")
    n = int(input())

    words = [] # Stores the words
    freqs = [] # Stores the corresponding probabilities
    print(f"\nEnter {n} strings in sorted dictionary order along with their probabilities: ")
    for i in range(n):
      var1 = input()
      words.append(var1)
      var2 = float(input())
      freqs.append(var2)

    # Check if the word list is alphabetically sorted or not
    for i in range(n-1):
      if (isAlphabaticOrder(words[i], words[i+1]) == False):
        print("\nThe strings entered are not in sorted order.")
        return
    
    # Check whether the probabilities are distinct or not
    tempSet = set(freqs)
    if (len(freqs) != len(tempSet)):
      print("\nThe probabilities are not distinct.")
      return

    # Check whether the probabilities add up to 1 or not.
    prob_sum = math.fsum(freqs)
    if prob_sum != 1.0:
      print("\nThe probabilities don’t add up to 1.")
      return
    

    find_optimal_binary_search_tree(words, freqs)
    


if __name__ == "__main__":
    print("Note: ")
    print("\nFirst, we check whether the words are in sorted order or not.")
    print("Then, we check whether the probabilities are distinct or not.")
    print("Lastly, we check whether the probabilities add up to 1 or not.")
    print("If all these conditions are met then only we proceed to create an Optimal Binary Search tree for the given input.\n")
    main()