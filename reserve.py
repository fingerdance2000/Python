import os
import time
import random

state = "exit"
task = 'reserve'

("\n\t\tWellcome to Reserve interface", random.randint(1, 10), '%')
time.sleep(.2)
print("\n\t\tWellcome to Reserve interface", random.randint(10, 20), '%')
time.sleep(random.randint(0, 1))
print("\n\t\tWellcome to Reserve interface", random.randint(20, 30), '%')
time.sleep(random.randint(0, 1))
print("\n\t\tWellcome to Reserve interface", random.randint(30, 40), '%')
time.sleep(random.randint(0, 1))
print("\n\t\tWellcome to Reserve interface", random.randint(40, 50), '%')
time.sleep(random.randint(0, 1))
print("\n\t\tWellcome to Reserve interface", random.randint(50, 60), '%')
time.sleep(random.randint(0, 1))
print("\n\t\tWellcome to Reserve interface", random.randint(60, 70), '%')
time.sleep(random.randint(0, 1))
print("\n\t\tWellcome to Reserve interface", random.randint(70, 80), '%')
time.sleep(random.randint(0, 1))
print("\n\t\tWellcome to Reserve interface", random.randint(80, 90), '%')
time.sleep(random.randint(0, 1))
print("\n\t\tWellcome to Reserve interface", '100 %')
time.sleep(random.randint(0, 2))

def admin():

    global task

    while task != state :

        time.sleep(.4)
        print("\tCoRrEct.\n\nnOw wE HaVe thEse tHinGs foR You:\n\t[game, photo, music, exit]")
        print('\nWhaT yOu ganNa Do?')
        task = input('> ')
        task = task.lower()

        if task == "game" :
            print("so yOu WaNna PlaY GaMe; lEt's gO.")
            os.startfile("game.py")
            time.sleep(3)
            
        elif task == "photo" :
            print("GoOd cHoIse")
            time.sleep(.2)
            os.startfile("sa.png")
            time.sleep(2)

        elif task == "music" :
            print("lET's DaNCe!")
            time.sleep(.3)
            os.startfile("TONES AND I - Dance Monkey ( cover by J.Fla ).mp4")
            time.sleep(2)

        elif task == "exit" :
            print("\n\tGooD dAy")
            time.sleep(2)

        else :
            print("New fEaturEs On near FutuRe!")
            time.sleep(4)

def newnuser(user, poassword) :
    passwort = password
    username = user

    

print("\n\n\tDo you have an account?\n")
answe = input('> ')
answer = answe.lower()

if answer == 'yes' :
    print('tYpe uOur UsernaMe hEre> ' , end = "")
    existingusername = input()

    print("TypE yOur passWord heRe> " , end = "")
    existingpassword = input()
    
    passwort = "420"
    username = "aDmIn"
    
    if existingpassword == passwort and existingusername == username :
        admin()

    else :
        print('Wrong password or username!')
        time.sleep(3)


elif answer == 'no' :
    print("We are happy to have you on side of us.\nPleas help us to remember you as well.")
    
    print("Name> " , end = '')
    name = input()
    
    print("Surname> " , end = '')
    surname = input()

    print('Now peakup a username> ')
    newusername = input('> ')
    time.sleep(.3)
    print('Secure you account by a password.\n\n!The password must have alphabet and number!')
    newpassword = input('> ')
    time.sleep(.2)

    print('Retype your password')
    confirmpassword = input('> ')
    time.sleep(.2)

    if newpassword == confirmpassword :
        userna = newusername
        userpass = newpassword
        print("We will call you soon")
        time.sleep(5)
#        newuser(userna, userpass)

    else :
        print("Password does not mach!")
        time.sleep(3)
