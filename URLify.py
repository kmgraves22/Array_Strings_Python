# @author: Kevin Graves
# This program takes a string as input and returns a URLifyd version where
# spaces are replaced with '%20'.

def URLify(string):
   a = string.replace(" ", "%20")
   return a

def main():
   tempString = raw_input("Please enter a string to URLify with sufficients extra space: ")
   url = URLify(tempString)
   print url

if __name__ == '__main__':
   main()
