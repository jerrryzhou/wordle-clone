import random
alist=[]
x= input("Try to guess the five letter word. Type start to continue: ")


in_file = open('word.txt', 'r')
for line in in_file:
  line = line.strip()
  alist.append(line)
in_file.close()
#print(alist)... opens and reads the file

def wordle(x): # checks answers w iteration for each input
  i = 0
  space = 1
  wordlist = []
  number = random.randint(1,488)
  space1 = " "
  space2 = " "
  space3 = " "
  space4 = ' '
  space5 = ' '
  space6 = ' '
  space7 = ' '
  space8 = ' '
  space9 = ' '
  space10 = ' '
  space11 = ' '
  space12 = ' '
  space13 = ' '
  space14 = ' '
  space15 = ' '
  space16 = ' '
  space17 = ' '
  space18 = ' '
  space19 = ' '
  space20 = ' '
  space21 = ' '
  space22 = ' '
  space23 = ' '
  space24 = ' '
  space25 = ' '
  space26 = ' '
  space27 = ' '
  space28 = ' '
  space29 = ' '
  space30 = ' '
  if x == "start":
    print()
    print("if the letter turns yellow, it means that letter is in the word, but in the wrong position. if it's green, congrats! you got the right letter and the right position.")
    print()
    
    print ('(' + space1 +') (' + space2 + ') (' + space3 + ') (' + space4 +') (' + space5 + ')')

    print ('(' + space6 +') (' + space7 + ') (' + space8 + ') (' + space9 + ') (' + space10 +')')

    print ('(' + space11 +') (' + space12 + ') (' + space13 + ') (' + space14 + ') (' + space15 +')')

    print ('(' + space16 +') (' + space17 + ') (' + space18 + ') (' + space19 + ') (' + space20 +')')

    print ('(' + space21 +') (' + space22 + ') (' + space23 + ') (' + space24 + ') (' + space25 +')')

    print ('(' + space26 +') (' + space27 + ') (' + space28 +') (' + space29 + ') (' + space30 +')')
    word = alist[number]
    for each in word:
      wordlist.append(each)
    print(wordlist)
    while i < 6:
      inputlist=[] # the words that the user inputs
      r = input("enter a five letter word: ")
      for each in r:
        inputlist.append(each)
      #print(inputlist)
      if inputlist == wordlist:
        return(" ======== \n YOU WIN! \n ========")
        break
      #print(inputlist)
      elif inputlist != wordlist:
        if space == 1:
          space1 = inputlist[0]
          space2 = inputlist[1]
          space3 = inputlist[2]
          space4 = inputlist[3]
          space5 = inputlist[4]
          if inputlist[0] == wordlist[0]:
            space1 = "\033[0;32;40m" + space1 + "\033[0;37;40m"
          elif inputlist[0] == wordlist[1] or inputlist[0]== wordlist[2] or inputlist[0] == wordlist[3] or inputlist[0] == wordlist[4]:
            space1 = "\033[0;33;40m" + space1 + "\033[0;37;40m"
          if inputlist[1] == wordlist[1]:
            space2 = "\033[0;32;40m" + space2 + "\033[0;37;40m"
          elif inputlist[1] == wordlist[0] or inputlist[1] == wordlist[2] or inputlist[1] == wordlist[3] or inputlist[1]== wordlist[4]:
           space2 = "\033[0;33;40m" + space2 + "\033[0;37;40m"
          if inputlist[2] == wordlist[2]:
            space3 = "\033[0;32;40m" + space3 + "\033[0;37;40m"
          elif inputlist[2] == wordlist[0] or inputlist[2]== wordlist[1] or inputlist[2] == wordlist[3] or inputlist[2]== wordlist[4]:
           space3 = "\033[0;33;40m" + space3 + "\033[0;37;40m"
          if inputlist[3] == wordlist[3]:
            space4 = "\033[0;32;40m" + space4 + "\033[0;37;40m"
          elif inputlist[3]== wordlist[0] or inputlist[3] == wordlist[1] or inputlist[3] == wordlist[2] or inputlist[3] == wordlist[4]:
            space4 = "\033[0;33;40m" + space4 + "\033[0;37;40m"
          if inputlist[4] == wordlist[4]:
            space5 = "\033[0;32;40m" + space5 + "\033[0;37;40m"
          elif inputlist[4] == wordlist[0] or inputlist[4] == wordlist[1] or inputlist[4] == wordlist[2] or inputlist[4] == wordlist[3]:
            space5 = "\033[0;33;40m" + space5 + "\033[0;37;40m"
          print ('(' + space1 +') (' + space2 + ') (' + space3 + ') (' + space4 +') (' + space5 + ')')
          print ('(' + space6 +') (' + space7 + ') (' + space8 + ') (' + space9 + ') (' + space10 +')')
          print ('(' + space11 +') (' + space12 + ') (' + space13 + ') (' + space14 + ') (' + space15 +')')
          print ('(' + space16 +') (' + space17 + ') (' + space18 + ') (' + space19 + ') (' + space20 +')')
          print ('(' + space21 +') (' + space22 + ') (' + space23 + ') (' + space24 + ') (' + space25 +')')
          print ('(' + space26 +') (' + space27 + ') (' + space28 +') (' + space29 + ') (' + space30 +')')
          space +=1
          i +=1
        
        elif space == 2:
          space6 = inputlist[0]
          space7 = inputlist[1]
          space8 = inputlist[2]
          space9 = inputlist[3]
          space10 = inputlist[4]
          if inputlist[0] == wordlist[0]:
            space6 = "\033[0;32;40m" + space6 + "\033[0;37;40m"
          elif inputlist[0] == wordlist[1] or inputlist[0]== wordlist[2] or inputlist[0] == wordlist[3] or inputlist[0] == wordlist[4]:
            space6 = "\033[0;33;40m" + space6 + "\033[0;37;40m"
          if inputlist[1] == wordlist[1]:
            space7 = "\033[0;32;40m" + space7 + "\033[0;37;40m"
          elif inputlist[1] == wordlist[0] or inputlist[1] == wordlist[2] or inputlist[1] == wordlist[3] or inputlist[1]== wordlist[4]:
           space7 = "\033[0;33;40m" + space7 + "\033[0;37;40m"
          if inputlist[2] == wordlist[2]:
            space8 = "\033[0;32;40m" + space8 + "\033[0;37;40m"
          elif inputlist[2] == wordlist[0] or inputlist[2]== wordlist[1] or inputlist[2] == wordlist[3] or inputlist[2]== wordlist[4]:
           space8 = "\033[0;33;40m" + space8 + "\033[0;37;40m"
          if inputlist[3] == wordlist[3]:
            space9 = "\033[0;32;40m" + space9 + "\033[0;37;40m"
          elif inputlist[3]== wordlist[0] or inputlist[3] == wordlist[1] or inputlist[3] == wordlist[2] or inputlist[3] == wordlist[4]:
            space9 = "\033[0;33;40m" + space9 + "\033[0;37;40m"
          if inputlist[4] == wordlist[4]:
            space10 = "\033[0;32;40m" + space10 + "\033[0;37;40m"
          elif inputlist[4] == wordlist[0] or inputlist[4] == wordlist[1] or inputlist[4] == wordlist[2] or inputlist[4] == wordlist[3]:
            space10 = "\033[0;33;40m" + space10 + "\033[0;37;40m"
        
          print ('(' + space1 +') (' + space2 + ') (' + space3 + ') (' + space4 +') (' + space5 + ')')
          print ('(' + space6 +') (' + space7 + ') (' + space8 + ') (' + space9 + ') (' + space10 +')')
          print ('(' + space11 +') (' + space12 + ') (' + space13 + ') (' + space14 + ') (' + space15 +')')
          print ('(' + space16 +') (' + space17 + ') (' + space18 + ') (' + space19 + ') (' + space20 +')')
          print ('(' + space21 +') (' + space22 + ') (' + space23 + ') (' + space24 + ') (' + space25 +')')
          print ('(' + space26 +') (' + space27 + ') (' + space28 +') (' + space29 + ') (' + space30 +')')
          space +=1
          i +=1
          
        elif space == 3:
          space11 = inputlist[0]
          space12 = inputlist[1]
          space13 = inputlist[2]
          space14 = inputlist[3]
          space15 = inputlist[4]
          if inputlist[0] == wordlist[0]:
            space11 = "\033[0;32;40m" + space11 + "\033[0;37;40m"
          elif inputlist[0] == wordlist[1] or inputlist[0]== wordlist[2] or inputlist[0] == wordlist[3] or inputlist[0] == wordlist[4]:
            space11 = "\033[0;33;40m" + space11 + "\033[0;37;40m"
          if inputlist[1] == wordlist[1]:
            space12 = "\033[0;32;40m" + space12 + "\033[0;37;40m"
          elif inputlist[1] == wordlist[0] or inputlist[1] == wordlist[2] or inputlist[1] == wordlist[3] or inputlist[1]== wordlist[4]:
           space12 = "\033[0;33;40m" + space12 + "\033[0;37;40m"
          if inputlist[2] == wordlist[2]:
            space13 = "\033[0;32;40m" + space13 + "\033[0;37;40m"
          elif inputlist[2] == wordlist[0] or inputlist[2]== wordlist[1] or inputlist[2] == wordlist[3] or inputlist[2]== wordlist[4]:
           space13 = "\033[0;33;40m" + space13 + "\033[0;37;40m"
          if inputlist[3] == wordlist[3]:
            space14 = "\033[0;32;40m" + space14 + "\033[0;37;40m"
          elif inputlist[3]== wordlist[0] or inputlist[3] == wordlist[1] or inputlist[3] == wordlist[2] or inputlist[3] == wordlist[4]:
            space14 = "\033[0;33;40m" + space14 + "\033[0;37;40m"
          if inputlist[4] == wordlist[4]:
            space15 = "\033[0;32;40m" + space15 + "\033[0;37;40m"
          elif inputlist[4] == wordlist[0] or inputlist[4] == wordlist[1] or inputlist[4] == wordlist[2] or inputlist[4] == wordlist[3]:
            space15 = "\033[0;33;40m" + space15 + "\033[0;37;40m"
        
          print ('(' + space1 +') (' + space2 + ') (' + space3 + ') (' + space4 +') (' + space5 + ')')
          print ('(' + space6 +') (' + space7 + ') (' + space8 + ') (' + space9 + ') (' + space10 +')')
          print ('(' + space11 +') (' + space12 + ') (' + space13 + ') (' + space14 + ') (' + space15 +')')
          print ('(' + space16 +') (' + space17 + ') (' + space18 + ') (' + space19 + ') (' + space20 +')')
          print ('(' + space21 +') (' + space22 + ') (' + space23 + ') (' + space24 + ') (' + space25 +')')
          print ('(' + space26 +') (' + space27 + ') (' + space28 +') (' + space29 + ') (' + space30 +')')
          space +=1
          i +=1

        elif space == 4:
          space16 = inputlist[0]
          space17 = inputlist[1]
          space18 = inputlist[2]
          space19 = inputlist[3]
          space20 = inputlist[4]
          if inputlist[0] == wordlist[0]:
            space16 = "\033[0;32;40m" + space16 + "\033[0;37;40m"
          elif inputlist[0] == wordlist[1] or inputlist[0]== wordlist[2] or inputlist[0] == wordlist[3] or inputlist[0] == wordlist[4]:
            space16 = "\033[0;33;40m" + space16 + "\033[0;37;40m"
          if inputlist[1] == wordlist[1]:
            space17 = "\033[0;32;40m" + space17 + "\033[0;37;40m"
          elif inputlist[1] == wordlist[0] or inputlist[1] == wordlist[2] or inputlist[1] == wordlist[3] or inputlist[1]== wordlist[4]:
           space17 = "\033[0;33;40m" + space17 + "\033[0;37;40m"
          if inputlist[2] == wordlist[2]:
            space18 = "\033[0;32;40m" + space18 + "\033[0;37;40m"
          elif inputlist[2] == wordlist[0] or inputlist[2]== wordlist[1] or inputlist[2] == wordlist[3] or inputlist[2]== wordlist[4]:
           space18 = "\033[0;33;40m" + space18 + "\033[0;37;40m"
          if inputlist[3] == wordlist[3]:
            space19 = "\033[0;32;40m" + space19 + "\033[0;37;40m"
          elif inputlist[3]== wordlist[0] or inputlist[3] == wordlist[1] or inputlist[3] == wordlist[2] or inputlist[3] == wordlist[4]:
            space19 = "\033[0;33;40m" + space19 + "\033[0;37;40m"
          if inputlist[4] == wordlist[4]:
            space20 = "\033[0;32;40m" + space20 + "\033[0;37;40m"
          elif inputlist[4] == wordlist[0] or inputlist[4] == wordlist[1] or inputlist[4] == wordlist[2] or inputlist[4] == wordlist[3]:
            space20 = "\033[0;33;40m" + space20 + "\033[0;37;40m"
        
          print ('(' + space1 +') (' + space2 + ') (' + space3 + ') (' + space4 +') (' + space5 + ')')
          print ('(' + space6 +') (' + space7 + ') (' + space8 + ') (' + space9 + ') (' + space10 +')')
          print ('(' + space11 +') (' + space12 + ') (' + space13 + ') (' + space14 + ') (' + space15 +')')
          print ('(' + space16 +') (' + space17 + ') (' + space18 + ') (' + space19 + ') (' + space20 +')')
          print ('(' + space21 +') (' + space22 + ') (' + space23 + ') (' + space24 + ') (' + space25 +')')
          print ('(' + space26 +') (' + space27 + ') (' + space28 +') (' + space29 + ') (' + space30 +')')
          space +=1
          i +=1

        elif space == 5:
          space21 = inputlist[0]
          space22 = inputlist[1]
          space23 = inputlist[2]
          space24 = inputlist[3]
          space25 = inputlist[4]
          if inputlist[0] == wordlist[0]:
            space21 = "\033[0;32;40m" + space21 + "\033[0;37;40m"
          elif inputlist[0] == wordlist[1] or inputlist[0]== wordlist[2] or inputlist[0] == wordlist[3] or inputlist[0] == wordlist[4]:
            space21 = "\033[0;33;40m" + space21 + "\033[0;37;40m"
          if inputlist[1] == wordlist[1]:
            space22 = "\033[0;32;40m" + space22 + "\033[0;37;40m"
          elif inputlist[1] == wordlist[0] or inputlist[1] == wordlist[2] or inputlist[1] == wordlist[3] or inputlist[1]== wordlist[4]:
           space22 = "\033[0;33;40m" + space22 + "\033[0;37;40m"
          if inputlist[2] == wordlist[2]:
            space23 = "\033[0;32;40m" + space23 + "\033[0;37;40m"
          elif inputlist[2] == wordlist[0] or inputlist[2]== wordlist[1] or inputlist[2] == wordlist[3] or inputlist[2]== wordlist[4]:
           space23 = "\033[0;33;40m" + space23 + "\033[0;37;40m"
          if inputlist[3] == wordlist[3]:
            space24 = "\033[0;32;40m" + space24 + "\033[0;37;40m"
          elif inputlist[3]== wordlist[0] or inputlist[3] == wordlist[1] or inputlist[3] == wordlist[2] or inputlist[3] == wordlist[4]:
            space24 = "\033[0;33;40m" + space24 + "\033[0;37;40m"
          if inputlist[4] == wordlist[4]:
            space25 = "\033[0;32;40m" + space25 + "\033[0;37;40m"
          elif inputlist[4] == wordlist[0] or inputlist[4] == wordlist[1] or inputlist[4] == wordlist[2] or inputlist[4] == wordlist[3]:
            space25 = "\033[0;33;40m" + space25 + "\033[0;37;40m"
        
          print ('(' + space1 +') (' + space2 + ') (' + space3 + ') (' + space4 +') (' + space5 + ')')
          print ('(' + space6 +') (' + space7 + ') (' + space8 + ') (' + space9 + ') (' + space10 +')')
          print ('(' + space11 +') (' + space12 + ') (' + space13 + ') (' + space14 + ') (' + space15 +')')
          print ('(' + space16 +') (' + space17 + ') (' + space18 + ') (' + space19 + ') (' + space20 +')')
          print ('(' + space21 +') (' + space22 + ') (' + space23 + ') (' + space24 + ') (' + space25 +')')
          print ('(' + space26 +') (' + space27 + ') (' + space28 +') (' + space29 + ') (' + space30 +')')
          space +=1
          i +=1

        elif space == 6:
          space26 = inputlist[0]
          space27 = inputlist[1]
          space28 = inputlist[2]
          space29 = inputlist[3]
          space30 = inputlist[4]
          if inputlist[0] == wordlist[0]:
            space26 = "\033[0;32;40m" + space26 + "\033[0;37;40m"
          elif inputlist[0] == wordlist[1] or inputlist[0]== wordlist[2] or inputlist[0] == wordlist[3] or inputlist[0] == wordlist[4]:
            space26 = "\033[0;33;40m" + space26 + "\033[0;37;40m"
          if inputlist[1] == wordlist[1]:
            space27 = "\033[0;32;40m" + space27 + "\033[0;37;40m"
          elif inputlist[1] == wordlist[0] or inputlist[1] == wordlist[2] or inputlist[1] == wordlist[3] or inputlist[1]== wordlist[4]:
           space27 = "\033[0;33;40m" + space27 + "\033[0;37;40m"
          if inputlist[2] == wordlist[2]:
            space28 = "\033[0;32;40m" + space28 + "\033[0;37;40m"
          elif inputlist[2] == wordlist[0] or inputlist[2]== wordlist[1] or inputlist[2] == wordlist[3] or inputlist[2]== wordlist[4]:
           space28 = "\033[0;33;40m" + space28 + "\033[0;37;40m"
          if inputlist[3] == wordlist[3]:
            space29 = "\033[0;32;40m" + space29 + "\033[0;37;40m"
          elif inputlist[3]== wordlist[0] or inputlist[3] == wordlist[1] or inputlist[3] == wordlist[2] or inputlist[3] == wordlist[4]:
            space29 = "\033[0;33;40m" + space29 + "\033[0;37;40m"
          if inputlist[4] == wordlist[4]:
            space30 = "\033[0;32;40m" + space30 + "\033[0;37;40m"
          elif inputlist[4] == wordlist[0] or inputlist[4] == wordlist[1] or inputlist[4] == wordlist[2] or inputlist[4] == wordlist[3]:
            space30 = "\033[0;33;40m" + space30 + "\033[0;37;40m"
        
          print ('(' + space1 +') (' + space2 + ') (' + space3 + ') (' + space4 +') (' + space5 + ')')
          print ('(' + space6 +') (' + space7 + ') (' + space8 + ') (' + space9 + ') (' + space10 +')')
          print ('(' + space11 +') (' + space12 + ') (' + space13 + ') (' + space14 + ') (' + space15 +')')
          print ('(' + space16 +') (' + space17 + ') (' + space18 + ') (' + space19 + ') (' + space20 +')')
          print ('(' + space21 +') (' + space22 + ') (' + space23 + ') (' + space24 + ') (' + space25 +')')
          print ('(' + space26 +') (' + space27 + ') (' + space28 +') (' + space29 + ') (' + space30 +')')
          space +=1
          i +=1
          if i == 6 and inputlist != wordlist:
            return("YOU LOSE")
            print("The word was " + wordlist[0] + wordlist[1] + wordlist[2] + wordlist[3] + wordlist[4])
          y = input("Play again? Yes/No: ")
          if y == "Yes":
            x == "start"
            print(wordle(x))
        
        
  else:
    return ("that's not a valid input")
print(wordle(x))

#this was made in collaboration (2 people)