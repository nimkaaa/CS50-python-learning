import sys

def main():
   if len(sys.argv) < 2:
      sys.exit("Too few arguments")

   for arg in sys.argv[1:]:
      print("hello, my name is", arg)


main()