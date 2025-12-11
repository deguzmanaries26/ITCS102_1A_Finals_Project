from compiler import *
import os

print("Welcome to my finals project!")
name = input("Please enter your name: ")
print(f"Hello, {name}! Let's get started.")
 
while True:
    print("-------------------------------------\n\t    --MENU--")
    print("\tA -- Simple Print\n\tB -- Calculations (activity)\n\tC -- Calculations (code challenge)\n\tD -- for in range Pattern\n\tE -- Username Input\n\tF -- Random (activity)\n\tG -- Random (code challenge)\n\tH -- Listing\n\texit -- to quit")
    choice = input("your choice --> ").lower()
    os.system('cls')
    if choice == 'a':
        print("-------------------------------------")
        print("\t    --simple print--")
        print("\t1 -- activity 01\n\t2 -- activity 02\n\t3 -- activity 03\n\t4 -- activity 04\n\texit -- to main menu")
        print("-------------------------------------")
        choice = input("your choice --> ").lower()
        if choice == '1':
            os.system('cls')
            activity1()
        elif choice == '2':
            os.system('cls')
            activity2()
        elif choice == '3':
            os.system('cls')
            activity3()
        elif choice == '4':
            os.system('cls')
            activity4()
        elif choice == 'exit':
            os.system('cls')
        else: 
            print("invalid choice")
        continue
    elif choice == 'b':
        print("-------------------------------------")
        print("\t    --Calculations (activity)--")
        print("\t1 -- activity 05\n\t2 -- activity 06\n\t3 -- activity 07\n\t4 -- activity 08\n\t5 -- activity 10\n\texit -- to main menu")
        print("-------------------------------------")
        choice = input("your choice --> ").lower()
        if choice == '1':
            os.system('cls')
            activity5()
        elif choice == '2':
            os.system('cls')
            activity6()
        elif choice == '3':
            os.system('cls')
            activity7()
        elif choice == '4':
            os.system('cls')
            activity8()
        elif choice == '5':
            os.system('cls')
            activity10()
        elif choice == 'exit':
            os.system('cls')
        else: 
            print("invalid choice")
        continue
    elif choice == 'c':
        print("-------------------------------------")
        print("\t    --Calculations (code challenge)--")
        print("\t1 -- code challenge 02\n\t2 -- code challenge 04\n\t3 -- code challenge 06\n\t4 -- code challenge 07\n\t5 -- code challenge 08\n\t6 -- code challenge 09\n\t7 -- code challenge 14\n\texit -- to main menu")
        print("-------------------------------------")
        choice = input("your choice --> ").lower()
        if choice == '1':
            os.system('cls')
            code_challenge2()
        elif choice == '2':
            os.system('cls')
            code_challenge4()
        elif choice == '3':
            os.system('cls')
            code_challenge6()
        elif choice == '4':
            os.system('cls')
            code_challenge7()
        elif choice == '5':
            os.system('cls')
            code_challenge8()
        elif choice == '6':
            os.system('cls')
            code_challenge9()
        elif choice == '7':
            os.system('cls')
            code_challenge14()
        elif choice == 'exit':
            os.system('cls')
        else: 
            print("invalid choice")
    elif choice == 'd':
        print("-------------------------------------")
        print("\t    --for in range Pattern--")
        print("\t1 -- activity 12\n\t2 -- activity 13\n\t3 -- activity 14\n\t4 -- activity 15\n\t5 -- activity 16\n\t6 -- activity 17\n\t7 -- activity 18\n\t8 -- activity 19\n\t9 -- activity 20\n\texit -- to main menu")
        print("-------------------------------------")
        choice = input("your choice --> ").lower()
        if choice == '1':
            os.system('cls')
            activity12()
        elif choice == '2':
            os.system('cls')
            activity13()
        elif choice == '3':
            os.system('cls')
            activity14()
        elif choice == '4':
            os.system('cls')
            activity15()
        elif choice == '5':
            os.system('cls')
            activity16()
        elif choice == '6':
            os.system('cls')
            activity17()
        elif choice == '7':
            os.system('cls')
            activity18()
        elif choice == '8':
            os.system('cls')
            activity19()
        elif choice == '9':
            os.system('cls')
            activity20()
        elif choice == 'exit':
            os.system('cls')
        else: 
            print("invalid choice")
        continue
    elif choice == 'e':
        print("-------------------------------------")
        print("\t    --Username Input--")
        print("\t1 -- activity 09\n\t2 -- code challenge 03\n\texit -- to main menu")
        print("-------------------------------------")
        choice = input("your choice --> ").lower()
        if choice == '1':
            os.system('cls')
            print("Please type this.\nusername = ariana grande\npassword = thebestsinger")
            activity9()
        elif choice == '2':
            os.system('cls')
            print("Please type this.\nusername = blackianaisgone\npassword = 123456")
            code_challenge3()
        elif choice == 'exit':
            os.system('cls')
        else: 
            print("invalid choice")
        continue
    elif choice == 'f':
        print("-------------------------------------")
        print("\t    --Random (activity)--")
        print("\t1 -- activity 11\n\t2 -- activity 21\n\t3 -- activity 22\n\t4 -- activity 23\n\t5 -- activity 24\n\texit -- to main menu")
        print("-------------------------------------")
        choice = input("your choice --> ").lower()
        if choice == '1':
            os.system('cls')
            activity11()
        elif choice == '2':
            os.system('cls')
            activity21()
        elif choice == '3':
            os.system('cls')
            activity22()
        elif choice == '4':
            os.system('cls')
            activity23()
        elif choice == '5':
            os.system('cls')
            activity24()
        elif choice == 'exit':
            os.system('cls')
        else: 
            print("invalid choice")
        continue
    elif choice == 'g':
        print("-------------------------------------")
        print("\t    --Random (code challenge)--")
        print("\t1 -- code challenge 01\n\t2 -- code challenge 05\n\t3 -- code challenge 10\n\t4 -- code challenge 11\n\t5 -- code challenge 12\n\t6 -- code challenge 13\n\texit -- to main menu")
        print("-------------------------------------")
        choice = input("your choice --> ").lower()
        if choice == '1':
            os.system('cls')
            code_challenge1()
        elif choice == '2':
            os.system('cls')
            code_challenge5()
        elif choice == '3':
            os.system('cls')
            code_challenge10()
        elif choice == '4':
            os.system('cls')
            code_challenge11()
        elif choice == '5':
            os.system('cls')
            code_challenge12()
        elif choice == '6':
            os.system('cls')
            code_challenge13()
        continue
    elif choice == 'h':
        print("-------------------------------------")
        print("\t    --Random (activity)--")
        print("\t1 -- activity 23\n\t2 -- activity 26\n\t3 -- activity 27\n\t4 -- code challenge 15\n\texit -- to main menu")
        print("-------------------------------------")
        choice = input("your choice --> ").lower()
        if choice == '1':
            os.system('cls')
            activity23()
        elif choice == '2':
            os.system('cls')
            activity26()
        elif choice == '3':
            os.system('cls')
            activity27()
        elif choice == '4':
            os.system('cls')
            code_challenge15()
        elif choice == 'exit':
            os.system('cls')
        else: 
            print("invalid choice")
    elif choice == 'exit':
        print("thank u, next")
        break