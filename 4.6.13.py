def readint(prompt,min,max):
    while True:
        try:
            value = input(prompt)
            if  min <= value <= max:
                return 
            else:
                raise OverflowError
                    
        except OverflowError:
            print("Error: not within permitted range (-10..10)")
        except ValueError:
            print("Error: not a number")
        except KeyboardInterrupt:
            print("Wymuszono zakonczenie programu")
            return 
v = readint("Enter number from range -10 to 10: ", -10, 10)
if v:
    print(v)
