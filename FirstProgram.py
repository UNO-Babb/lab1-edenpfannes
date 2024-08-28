#FirstProgram.py
#Name:
#Date:
#Assignment:

def main():
  print("First Program")
  #Say hello
  input("Hello, how are you?: ")
  #Ask for the user's name
  name = input("What is your name?: ")
  #Use the user's name in the program.
  print("Good to meet you", name)
  #Ask the user for their age.
  age = input("How old are you?: ")
  print("Wow, you are old!")
  #Tell the user what year they were born in.
  age = int(age)
  born = 2024 - age 
  #Assume that they have not had their birthday yet this year.
  print("You were born in", born)

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
