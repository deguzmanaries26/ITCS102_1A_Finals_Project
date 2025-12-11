#simple print
def activity1():
    print("Hello World!")
def activity2():
    singer =input("who is the greatest singer? ")
    print("Is that even a question?? You know there's only one right answer, and it's", singer)   
def activity3():
    name = input("Identify yourself: ")
    print("Hello", name, "Welcome to the Matrix")
def activity4():
    name = input("Type your name: ")
    print("your name has" ,len(name), "characters")

#calculations
def activity5():
    something = eval(input("Input a number: "))
    answer = 26 + something
    print("magic, naging" ,answer, "\npano nangyare yon?")
def activity6():
    print("4 horsemen of math")
    x1 = eval(input("Input a number:"))
    x2 = eval(input("Input another number:"))

    s = x1 + x2
    d = x1 - x2
    p = x1 * x2
    q = x1 / x2 

    solution = ((x1 / x2)*100-5)//300
    print("\nThe sum of" ,x1, "and" ,x2, "is" ,s)
    print("The difference of" ,x1, "and" ,x2, "is" ,d)
    print("The product of" ,x1, "and" ,x2, "is" ,p)
    print("The quotient of" ,x1, "and" ,x2, "is" ,q)
    print(x2, "exponent by" ,x2, "is" ,x1**x2)
    print("The remainder of" ,x1, "and" ,x2, "is" ,x1 % x2)
    print("The floordivision of" ,x1, "and" ,x2, "is" ,x1 // x2)
def activity7():
    x = 26
    print("The original value of x is", x)
    x += 6
    x -= 10
    x *= 7
    x /= 9
    print("The value of x is", x)
def activity8():
    print("Welcome to the ATM!")
    balance = 1000000
    amount = 0

    amount = int(input("Enter the amount to withdraw:"))
    print(balance >= amount)
    if balance >= amount:
        newbal = balance - amount
        print("withdrawal Granted! \nYour new balance is", newbal)
    elif balance <= amount:
        print("You currently don't have enough balance in your account.")
def activity10():
    print("Welcome to the fare calculator!")
    name = input("Type your name: ")
    isStudent = input("Are you a student? (Yes/No): ").lower()
    fare = eval(input("bayad mo: "))
    if isStudent == "yes" :
        discount = int((fare*.2)//1)
        new_fare = int(fare - discount)
        print("hello", name,",", discount, "is deducted for the student discount. Your new fare is", new_fare)
    else :
        print("sorry", name, "you're not discounted.")

#for in range pattern
def activity12():
    for ariana in range(1, 27, 1):
        print(ariana, "- Ariana Grande")
def activity13():
    num = 0
    print("Enter 10 numbers to sum up:")
    for i in range(1, 11):
        number = eval(input("Enter a number: "))    
        num += number
        print("The sum is", num)
    print("The total sum is", num)
def activity14():
    for x in range(20, 0, -1):
        print(x)
def activity15():
    print("Multiplcation Table.")
    number = int(input("enter a number: "))
    for i in range(1,11,1):
        result = number*i
        print(f"{number} x {i} = {result}")
def activity16():
    for x in range(1,11,1):
        for i in range(10,0,-1):
            print(i, end=' ')
        print()
def activity17():
    for x in range(1,11,1):
        for i in range(1,11,1):
            print(i, end=' ')
        print()
def activity18():
    for i in range(1,11,1):
        for y in range(1,i,1):
            print(y, end=' ')
        print()
def activity19():
    for i in range(1,11,1):
        for x in range(1,i,1):
            print("*", end=' ')
        print()
def activity20():
    for y in range(1,11,1):
        # for x in range(1,y,1):
        #     print(" ", end=" ")
        for z in range(10,y,-1):
            print("*", end=" ")
        print() 

#calculations - code challenge
def code_challenge2():
    print("Welcome to the ATM!")
    x = eval(input("Enter the amount you want to deposit: "))
    print("\nHere is a detailed breakdown in PH currency:")
    print("\n1000 --" ,x//1000)
    print("500  --" ,((x%1000)//500))
    print("200  --" ,(((x%1000)%500)//200))
    print("100  --" ,((((x%1000)%500)%200)//100))
    print("50   --" ,((((x%1000)%500)%200)%100)//50)
    print("20   --" ,(((((x%1000)%500)%200)%100)%50)//20)
    print("10   --" ,((((((x%1000)%500)%200)%100)%50)%20)//10)
    print("5    --" ,(((((((x%1000)%500)%200)%100)%50)%20)%10)//5)
    print("1    --" ,((((((((x%1000)%500)%200)%100)%50)%20)%10)%5)//1)
    print("Total amount:" ,x)
def code_challenge4():
    number = eval(input("Input a number: "))
    if number %2 == 0 :
        print("That is an even number.")
    else :
        print("That is an odd number.")
def code_challenge6():
    print("This program calculates the factorial of a number.")
    number = int(input("Enter a number: "))
    num = 1 
    for x in range(number, 1, -1):
        num *= x
    print("The factorial of", number, "is", num) 
def code_challenge7():
    print("ODD Number Summation")
    num = 0
    for x in range(1, 11, 1):
        number = int(input("Enter a number: "))
        if number % 2 != 0:
            num += number
    print("The sum of the odd numbers is", num)
def code_challenge8():
    print("MULTIPLICATION TABLE MAKER")
    number = int(input("Input a number: "))

    print("\nMultiplication Table for", number, ":")
    for a in range(1,11):
        num = number * a
        print(number, "x", a, "=", num)
def code_challenge9():
    print("⏳COUNTDOWN TIMER SIMULATOR")
    number = int(input("Enter a starting number for the countdown: "))
    print(number)
    print("\n⏳Countdown started:")
    for a in range(number, 0, -1):
        print(a)
    print("Liftoff!🚀")
def code_challenge14():
    name = input("Hello! What is your name? ")
    print("ODD number compiler, type '0' to terminate")
    Odd = True
    number = 0
    odd_number = []
    while Odd == True:
        num = int(input("Type a number: "))
        if num == 0:
            print("Program terminated.")
            break
        elif num % 2 == 0:
            print("Even number detected.")
            continue
        elif num % 2 == 1:
            print("Odd number detected.")
            number += num
            odd_number.append(num)
            continue
        else: 
            print("Invalid input, program terminated.")
            break
    print(f"Hello {name}, The sum of all ODD numbers you have entered is {number}.")
    print(f"All the ODD numbers you have entered are {odd_number}.")

#username input
def activity9():
    username = "ariana grande"
    password = "thebestsinger"

    name = input("Type your username:")
    password1 = input("Type your password:")
    print(username == name) and (password == password1)
def code_challenge3():
    from getpass import getpass
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    uname = 'blackianaisgone'
    pwd = 'glindakilledher'
    if uname == username and pwd == password :
        print("Access Granted!")
    else :
        print("Access Denied!")

#random - activity
def activity11():
    print("TEMPERATURE CHECKER")
    temp = int(input("Enter temperature: "))
    if temp >= 1 and temp <= 20:
        print("Temperature outside is cold.")
    elif temp >= 21 and temp <= 30:
        print("Temperature outside is lukewarm.")
    elif temp >= 31 and temp <= 40:
        print("Temperature outside is warm.")
    elif temp >= 41 and temp <= 50:
        print("Temperature outside is hot.")
    elif temp >= 51:
        print("Temperature is boiling hot.")
    else:
        print("Invalid temperature.")
def activity21():
    print("Laundry Cycle Simulator")
    isDirty = True 

    while isDirty == True:
        laundry = input("Are the clothes still dirty? (yes/no): ").lower()
        if laundry == "yes":
            print("Continuing the cycle...")
            continue
        elif laundry == "no":
            print("Cycle stops")
            break
        else:
            print("Invalid input, please answer with 'yes' or 'no'.")
def activity22():
    import random
    print("Welcome to the Number Guessing Game!")
    random_number = random.randint(1, 10)
    tries = 0
    tuloy = True

    while tuloy == True:
        guess = int(input("Guess a number between 1 and 10: "))
        tries += 1
        if guess < random_number:
            print("Too low! Try again.")
            continue
        elif guess > random_number:
            print("Too high! Try again.")
            continue
        elif guess == random_number:
            print(f"Congratulations! You've guessed the number {random_number} in {tries} tries.")
            break
def activity24():
    def greeter(name):
        print(f"Hello {name}, love you lots!")

        greeter("Ariana")
        greeter("Cynthia")
        greeter("Beyoncé")

#random - code challenge
def code_challenge1():
    name=input("Type your name: ")
    print("\t\t\t*\n\n\t\t*\t\t*\n\n\t*\t\t\t\t*\n\n*\t\t  hi, ", name, "\t\t*\n\n\t*\t\t\t\t*\n\n\t\t*\t\t*\n\n\t\t\t*")
def code_challenge5():
    print("Welcome to manga reader!")
    ans = input("Do you want me to recommend a manga?(Yes/No): ").lower()
    if ans == 'yes':
        print("Great! Now please answer these questions to your liking.")
        genre = input("What genre do you want?(Action/Sci-fi/Romcom): ").lower()
    #action
        if genre == "action":
            length = input("How long?(Short/Medium/Long): ").lower()
            if length == 'short':
                year = eval(input("Which decade?(2000/2010): "))
                if year == 2000:
                    print("I recommend 666 Satan (O-Parts Hunter, 76 ch, 2001–2007)")
                if year == 2010:
                    print("I recommend Attack on Titan: Before the Fall (17 vols, 2013–2019)")
            if length == 'medium':
                year = eval(input("Which decade?(2000/2010): "))
                if year == 2000:
                    print("I recommend Tenjou Tenge (136 ch, 1997–2010)")
                if year == 2010:
                    print("I recommend Seraph of the End (120+ ch, 2012–ongoing)")
            if length == 'long':
                year = eval(input("Which decade?(2000/2010): "))
                if year == 2000:
                    print("I recommend One Piece (1997–ongoing, 1000+ ch)")
                if year == 2010:
                    print("I recommend Black Clover (350+ ch, 2015–ongoing)")
    #Sci-fi
        elif genre == "sci-fi":
            length = input("How long?(Short/Medium/Long): ").lower()
            if length == 'short':
                year = eval(input("Which decade?(2000/2010): "))
                if year == 2000:
                    print("I recommend Blame! (66 ch, 1997–2003)")
                if year == 2010:
                    print("I recommend Ultraman (short arcs, 2011–ongoing)")
            if length == 'medium':
                year = eval(input("Which decade?(2000/2010): "))
                if year == 2000:
                    print("I recommend Eden: It’s an Endless World! (127 ch, 1998–2008)")
                if year == 2010:
                    print("I recommend DARWIN’S GAME (100+ ch, 2012–ongoing)")
            if length == 'long':
                year = eval(input("Which decade?(2000/2010): "))
                if year == 2000:
                    print("I recommend Fullmetal Alchemist (116 ch, 2001–2010 — technically medium but iconic long-read)")
                if year == 2010:
                    print("I recommend Dr. Stone (232 ch, 2017–2022)")
    #romcom
        elif genre == "romcom":
            length = input("How long?(Short/Medium/Long): ").lower()
            if length == 'short':
                year = eval(input("Which decade?(2000/2010): "))
                if year == 2000:
                    print("I recommend Midori Days (85 ch, 2002–2004)")
                if year == 2010:
                    print("I recommend Horimiya (122 ch, 2011–2021)")
            if length == 'medium':
                year = eval(input("Which decade?(2000/2010): "))
                if year == 2000:
                    print("I recommend Love Hina (118 ch, 1998–2001)")
                if year == 2010:
                    print("I recommend Kaguya-sama: Love is War (281 ch, 2015–2022)")
            if length == 'long':
                year = eval(input("Which decade?(2000/2010): "))
                if year == 2000:
                    print("I recommend Haruhi Suzumiya manga (2004–2013, many vols, romcom + supernatural)")
                if year == 2010:
                    print("I recommend Domestic Girlfriend (276 ch, 2014–2020, dramatic romcom)")

        else : 
            print("Sorry, I cannot find what you're looking for.")
    else:
        print("Please have fun reading at Manga Reader!")
def code_challenge10():
    print("\t\t   *")
    for i in range(1,11,1):
        for z in range(10,i,-1):
            print(" ", end=" ")
        for x in range(0,i,1):
            print("*", end=' ')
        for y in range(0,i,1):
            print("*", end=" ")
        print()
def code_challenge11():
    print("\t\t   *")
    for i in range(1,11,1):
        for z in range(10,i,-1):
            print(" ", end=" ")
        for x in range(0,i,1):
            print("*", end=' ')
        for y in range(0,i,1):
            print("*", end=" ")
        print()
    for i in range(1,10,1):
        for a in range(0,i,1):
            print(" ", end=" ")
        for b in range(10,i,-1):
            print("*", end=' ')
        for c in range(10,i,-1):
            print("*", end=' ')
        print()
    print("\t\t   *")
def code_challenge12():
    for i in range(1,7,1):
        for y in range(7,i,-1):
            print(" ", end=' ')
        for x in range(i,0,-1):
            print(x, end=' ')
        for z in range(2,i + 1,1):
            print(z, end=' ')
        print()
def code_challenge13():
    print("\t\t\t               *")
    for a in range(1,2,1):
        for b in range(20,a,-1):
            print(" ", end=" ")
        for c in range(0,a,1):
            print("*", end=' ')
        for d in range(0,a,1):
            print("*", end=" ")
        print()
    for e in range(3,1,-1):
            for f in range(e,21,1):
                print(" ", end=' ')
            for g in range(e,1,-1):
                print("*", end=' ')
            for h in range(e,1,-1):
                print("*", end=' ')
            print()
    print("\t\t\t               *")
    for a in range(1,11,1):
        for b in range(20,a,-1):
            print(" ", end=" ")
        for c in range(0,a,1):
            print("*", end=' ')
        for d in range(0,a,1):
            print("*", end=" ")
        print()
    for a in range(1,15,1):
        for b in range(20,a,-1):
            print(" ", end=" ")
        for c in range(0,a,1):
            print("*", end=' ')
        for d in range(0,a,1):
            print("*", end=" ")
        print()
    for i in range(1,7,1):
        for x in range(1,18,1):
            print(" ", end=' ')
        for y in range(1,7,1):
            print("*", end=' ')
        print()

#listing
def activity23():
    name = True 
    artist = []
    print("welcome to music artist list. type 'exit' to quit")
    while name == True: 
        artist = input("enter ur fav music artist: ").lower()
        if artist == 'exit':
            print("program terminated. goodbye!")
            break
        else: 
            print(f"'{artist}' has been added to your music artist list.")
            list.append
        
    fullname = 'Aries De Guzman'
    for a in fullname:
        print(a)
def activity26():
    programming_languages = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby']

    programming_language2 = {'madali': 'Python', 'masalimuot': 'C#', 'popular': 'JavaScript', 'matatag': 'Java', 'malikhain': 'Ruby'}
    print(programming_language2['madali'])
def activtity27():
    print("Adding data to a dictionary")
    print("--------------------------------")

    tuloy = True 
    empty_dict = {}
    def print_anime():
        for a,b in empty_dict.items():
            print(f"Code - {a} : Anime - {b}")
    def pangsearch():
        print(f"results shows {empty_dict[key].upper()} on our database.")
    while tuloy == True:
        keys = input("enter anime code: ")
        values = input("enter anime name: ")
        empty_dict[keys] = values
        choice = input("would you like to continiue?\ny - yes\nn - no\np - print\ns - search\nansewer: ").lower()

        if choice == 'y':
            print("continuing...")
            continue
        elif choice == 'n':
            print("program ended.")
            break
        elif choice == 'p':
            print_anime()
            continue
        elif choice == 's':
            key = input("enter anime code to search: ")
            if key in empty_dict:
                pangsearch()
            else:
                print("anime code not found in database.")
            continue
        else:
            print("invalid input.")
            continue
def code_challenge15():
    print("Hello! Welcome to Anime entry program. \nPlease provide the title of an anime to continue and type 'exit' to terminate.")

    anime = True
    anime_titles = []
    while anime == True:
        title = input("Enter anime title: ")
        if title.lower() == 'exit':
            print("Program terminated. Goodbye!")
            break
        else:
            anime_titles.append(title)
            print(f"'{title}' has been added to your anime list.")
    print("The anime titles you have entered are:")
    for anime in anime_titles:
        print(f"- {anime}")      
        