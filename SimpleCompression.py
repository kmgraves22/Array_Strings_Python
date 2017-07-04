# @author: Kevin Graves
# Program name: SimpleCompression
# This program takes in a single string as input and performs a simple compression
# This compression replaces repeated characters with the letter followed by the number of
# times they repeat.
# ex: aabcccccaaa becomes a2b1c5a3
# if the compressed string is longer than the input string, the original string is returned.
# 
def simpleCompress(string):
   c = ''
   count = 0
   toReturn = ''
   for x in string:
      if x == c:
         count += 1
      else:
         c = x
         if count > 0:
            toReturn += str(count)
         toReturn += c
         count = 1
   toReturn += str(count)
   return toReturn
      
def main():
   toComp = input("Enter a string to compress: ")
   compressed = simpleCompress(toComp)
   print(compressed)

if __name__ == '__main__':
   main()