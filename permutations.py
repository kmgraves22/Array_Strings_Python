# @author: Kevin Graves
# Program name: Permutations
# This program takes in two strings as input and outputs whether
# or not they are permutations of each other.
# The permutations alogorithm assumes that capitilizations matters

def isPerm(string1, string2):
   if len(string1) != len(string2):
      return False
   a = sorted(string1)
   b = sorted(string2)
   if a == b:
      return True
   return False

def main():
   string1 = raw_input("Please enter the first string: ");
   string2 = raw_input("Please enter the second string: ");
   if isPerm(string1, string2):
      print("Yes, is a permutation!")
   else:
      print("NOT a permutation.")
      
if __name__ == '__main__':
   main()
