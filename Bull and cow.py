"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Albrecht

email: albrecht1994@seznam.cz

discord: Rikkiti#3029

"""
import random

separator = "-"*47
delka_hadaneho_cisla = 4
# pozdrav
print ("Hi there!")
print (separator)
print("""I've generated a random 4 digit number for you. 
      Let's play a bulls and cows game.""")
print(separator)

program_bezi = True

# generování čísla
def generuj_hledane_cislo (delka) -> list[int]:
    generovane_cislo = [random.randint(1,9)]
    while len(generovane_cislo)!=delka:
        nahodne_cislo = random.randint(0,9)
        if nahodne_cislo not in generovane_cislo:
            generovane_cislo.append(nahodne_cislo)
    return (generovane_cislo)   
# ověření vstupu uživatele
def vstup_uzivatele () ->str:
    spravy_format_vstupu = False
    while not spravy_format_vstupu:
        zadane_cislo = input(f"Enter all guessed {delka_hadaneho_cisla} digit numbers: ")
        # možnost ukončení programu
        if zadane_cislo.lower() == "exit":
            exit()
        #ověření dvojce čísel a číslic v zadání
        opakujici_se_cislice = False
        je_cislo = True
        cislo = []
                 

        for cislice in zadane_cislo:
            if not cislice.isnumeric():
                je_cislo = False
            if cislice not in cislo:
                cislo.append(cislice) 
            else:
                opakujici_se_cislice = True
        # ověření délky zadaného čísla
        if len(zadane_cislo)!=delka_hadaneho_cisla and je_cislo:
            print(f"This is not a {delka_hadaneho_cisla} digit number, try again!")         
        elif not opakujici_se_cislice and je_cislo and cislo[0]=="0":
            print("first number can´t be 0")
        elif not opakujici_se_cislice and je_cislo:
            spravy_format_vstupu = True
        elif opakujici_se_cislice and je_cislo:
            print("You entered a number with repeating values. Try it again")
        else:
            print("This is not a number, try again!")
        
    return cislo   


# hl smička programu
while program_bezi:
        
    # generování čísla
    hledane_cislo = generuj_hledane_cislo(delka_hadaneho_cisla)
    
    hra_bezi = True
    # smička hry
    pocet_kol = 1
    while hra_bezi:
        # Vstup uživatelem
        hadane_cislo = vstup_uzivatele()

        index_hadane = 0
        index_hledane = 0
        bull = 0
        cow = 0
        # analizování vstupu
        for cislo in hadane_cislo:
            index_hadane += 1
            for spravne_cislo in hledane_cislo:
                index_hledane +=1
                if index_hledane==index_hadane and int(cislo) == spravne_cislo:
                    bull +=1
                elif index_hledane!=index_hadane and int(cislo) == spravne_cislo:
                    cow +=1
            index_hledane = 0

        #   vypis bull and cow
        bull_tvar = str("bull")
        cow_tvar = str("cow")
        if bull >= 2:
            bull_tvar = "bulls"
        if cow >=2:
            cow_tvar = "cows"

        print(f"{bull} {bull_tvar}, {cow} {cow_tvar}")
        if bull == delka_hadaneho_cisla:
            if pocet_kol == 1:
                print("Well, you accidentally guessed everything the first time... it wasn't a proper game.")
            elif pocet_kol <=3:
                print(f"Correct, you've guessed the right number in {pocet_kol} guesses!,that is admirable!")
            elif pocet_kol <=7:
                print(f"Correct, you've guessed the right number in {pocet_kol} guesses!,that is good!")
            elif pocet_kol >=7:
                print(f"Correct, you've guessed the right number in {pocet_kol} guesses!,that is poor!")
            hra_bezi = False
        pocet_kol += 1

    # hrát znovu? 
    hrat_znovu = str(input(f"do you wanna play again? (Yes/no)").lower())
    if hrat_znovu == "yes":
        print("Great, let's continue")
    elif hrat_znovu == "no":
        print("Ok, exiting the program...")
        exit()
    elif hrat_znovu == "exit":
        exit()
    else:
        print("invalid input, exiting the program...")
        break    

        
