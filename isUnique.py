# @author: Kevin Graves
# Program name: isUnique
# This program takes in a signle string as input and determines
# if all characters in the string are unique.  It uses a list
# to mark whether a character has been used to reduce time complexity

def isUnique(string):
   ascii_chars = [0] * 128;
   for c in string:
      if ascii_chars[ord(c)] == 0:
         ascii_chars[ord(c)] = 1
      else:
         return False
   return True

def main():
   userIn = raw_input("Enter a string to determine if it has all unique characters: ");
   if isUnique(userIn):
      print("ALL UNIQUE!")
   else:
      print("Not unique.")
   return

if __name__ == '__main__':
   main()
