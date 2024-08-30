#MadLib.py
#Name: Eden Pfannes
#Date: 8/30/24
#Assignment: Editing Lab #1

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun and a period: ")
  noun2 = input("Enter a plural noun and a period: ")
  noun3 = input("Enter a place and a period: ")
  name1 = input("Enter a name and a period: ")
  verb1 = input("Enter a verb+ing and an exclamation point: ")
  verb2 = input("Enter a verb and a period: ")
  verb3 = input("Enter a verb+ed and an exclamation point: ")
  adjective1 = input("Enter an adjective and an a comma: ")
  #Print the story with the user supplied words.
  print("Once upon a time there was a", noun1)
  print("His name was", name1)
  print("He knew everything there was to know about", noun2)
  print("He was planning to share his expertise at the grand", noun3)
  print("That day, he was so nervous he was", verb1)
  print("Finally, it was his turn to", verb2)
  print("His presentation was so", adjective1)
  print("everyone watching", verb3)
  print("The End!")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
