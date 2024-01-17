import random
import time
import sys

seznam_vygenerovanych_cisel = []
body = [0]


print("Vítej v mojí hře Kostky")
time.sleep(1.5)

jmeno = input(str("Napište své jméno: "))
time.sleep(1)

print("Pro spuštění hry zmáčkněte Enter.")
input()
prvni_hod = random.randint(1, 6)
druhy_hod = random.randint(1, 6)
treti_hod = random.randint(1, 6)
ctvrty_hod = random.randint(1, 6)
paty_hod = random.randint(1, 6)
sesty_hod = random.randint(1, 6)

seznam_vygenerovanych_cisel.append(prvni_hod)
seznam_vygenerovanych_cisel.append(druhy_hod)
seznam_vygenerovanych_cisel.append(treti_hod)
seznam_vygenerovanych_cisel.append(ctvrty_hod)
seznam_vygenerovanych_cisel.append(paty_hod)
seznam_vygenerovanych_cisel.append(sesty_hod)


hozena_cisla = ', '.join(map(str, seznam_vygenerovanych_cisel))
print(f"Hodil jsi následující čísla: {hozena_cisla}")


#---------Jedničky---------
jednicka = 1

#počet hozených jedniček
jednicky = seznam_vygenerovanych_cisel.count(1)
print(f"Počet hozených jedniček: {jednicky}")


#jedna jednička
if jednicky == 1:
    body.append(100)

#dvě jedničky
elif jednicky == 2:
    body.append(200)

#tři jedničky
elif jednicky == 3:
    body.append(1000)

#čtyři jedničky
elif jednicky == 4:
    body.append(2000)

#pět jedniček
elif jednicky == 5:
    body.append(4000)

#šest jedniček
elif jednicky == 6:
    body.append(8000)



#---------Dvojky---------
dva = 2

#počet hozených dvojek
dvojky = seznam_vygenerovanych_cisel.count(2)
print(f"Počet hozených dvojek: {dvojky}")

#tři dvojky
if dvojky == 3:
    body.append(2 * 100)

#čtyři dvojky
elif dvojky == 4:
    body.append(2 * 200)

#pět dvojek
elif dvojky == 5:
    body.append(2 * 400)

#šest dvojek
elif dvojky == 6:
    body.append(2 * 800)



#---------Trojky---------
tri = 3

#počet hozených trojek
trojky = seznam_vygenerovanych_cisel.count(3)
print(f"Počet hozených trojek: {trojky}")

#tři trojka
if trojky == 3:
    body.append(3 * 100)

#čtyři trojky
elif trojky == 4:
    body.append(3 * 200)

#pět trojek
elif trojky == 5:
    body.append(3 * 400)

#šest trojek
elif trojky == 6:
    body.append(3 * 800)




#---------Čtyřky---------
ctyri = 4

#počet hozených čtyřek
ctyrky = seznam_vygenerovanych_cisel.count(4)
print(f"Počet hozených čtyřek: {ctyrky}")

#tři čtyřky
if ctyrky == 3:
    body.append(4 * 100)

#čtyři čtyřky
elif ctyrky == 4:
    body.append(4 * 200)

#pět čtyřek
elif ctyrky == 5:
    body.append(4 * 400)

#šest čtyřek
elif ctyrky == 6:
    body.append(4 * 800)




#---------Pětky---------
pet = 5

#počet hozených pětek
petky = seznam_vygenerovanych_cisel.count(5)
print(f"Počet hozených pětek: {petky}")

#jedna pětka
if petky == 1:
    body.append(50)

#dvě pětky
elif petky == 2:
    body.append(100)

#tři pětky
elif petky == 3:
    body.append(5 * 100)

#čtyři pětky
elif petky == 4:
    body.append(5 * 200)

#pět pětek
elif petky == 5:
    body.append(5 * 400)

#šest pětek
elif petky == 6:
    body.append(5 * 800)



#---------Šestky---------
sest = 6

#počet hozených šestek
sestky = seznam_vygenerovanych_cisel.count(6)
print(f"Počet hozených šestek: {sestky}")

#tři šestky
if sestky == 3:
    body.append(6 * 100)

#čtyři šestky
elif sestky == 4:
    body.append(6 * 200)

#pět šestek
elif sestky == 5:
    body.append(6 * 400)

#šest šestek
elif sestky == 6:
    body.append(6 *800)



#---------3 Dvojice---------
    
#cyklus, který prověří každou možnou kombinaci tří dvojic    
while True:
    if jednicky == 2:
        if dvojky == 2:
            if trojky == 2 or ctyrky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
                break
            else:
                break

        elif trojky == 2:
            if dvojky == 2 or ctyrky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
                break
            else:
                break

        elif ctyrky == 2:
            if dvojky == 2 or trojky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
                break
            else:
                break

        elif petky == 2:
            if dvojky == 2 or trojky == 2 or ctyrky == 2 or sestky == 2:
                body.append(1000)
                break
            
            else:
                break
        elif sestky == 2:
            if dvojky == 2 or trojky == 2 or ctyrky == 2 or petky == 2:
                body.append(1000)
                break
            else:    
                break
        else:    
            break

    if dvojky == 2:
        if jednicky == 2:
            if trojky == 2 or ctyrky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
                break
            else:    
                break
        
        elif trojky == 2:
            if jednicky == 2 or ctyrky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
                break
            else:    
                break
        
        elif ctyrky == 2:
            if  jednicky == 2 or trojky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
                break
            else:    
                break
        
        elif petky == 2:
            if jednicky == 2 or trojky == 2 or ctyrky == 2 or sestky == 2:
                body.append(1000)
                break
            else:    
                break

        elif sestky == 2:
            if jednicky == 2 or trojky == 2 or ctyrky == 2 or petky == 2:
                body.append(1000)
                break
            else:    
                break
        
        else:    
            break

    if trojky == 2:
        if jednicky == 2:
            if dvojky == 2 or ctyrky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
                break
            else:    
                break
        
        elif dvojky == 2:
            if jednicky == 2 or ctyrky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
                break
            else:    
                break
        
        elif ctyrky == 2:
            if jednicky == 2 or dvojky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
                break
            else:
                break

        elif petky == 2:
            if jednicky == 2 or dvojky == 2 or ctyrky == 2 or sestky == 2:
                body.append(1000)
            else:
                break

        elif sestky == 2:
            if jednicky == 2 or dvojky == 2 or ctyrky == 2 or petky == 2:
                body.append(1000)
            else:
                break
        
        else:
            break

    if ctyrky == 2:
        if jednicky == 2:
            if dvojky == 2 or trojky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
            else:
                break

        elif dvojky == 2:
            if jednicky == 2 or trojky == 2 or petky == 2 or sestky == 2:
                body.append(1000)
            else:
                break
        
        elif trojky == 2:
            if jednicky == 2 or dvojky == 2 or petky == 2 or sestky ==2:
                body.append(1000)
            else:
                break

        elif petky == 2:
            if jednicky == 2 or dvojky == 2 or trojky == 2 or sestky == 2:
                body.append(1000)
            else:
                break

        elif sestky == 2:
            if jednicky == 2 or dvojky == 2 or trojky == 2 or petky == 2:
                body.append(1000)
            else:
                break
        
        else:
            break
        
    if petky == 2:
        if jednicky == 2:
            if dvojky == 2 or trojky == 2 or ctyrky == 2 or sestky == 2:
                body.append(1000)
            else:
                break
        elif dvojky == 2:
            if jednicky == 2 or trojky == 2 or ctyrky == 2 or sestky == 2:
                body.append(1000)
            else:
                break
        elif trojky == 2:
            if jednicky == 2 or dvojky == 2 or ctyrky == 2 or sestky == 2:
                body.append(1000)
            else:
                break
        elif ctyrky == 2:
            if jednicky == 2 or dvojky == 2 or trojky == 2 or sestky == 2:
                body.append(1000)
            else:
                break
        elif sestky == 2:
            if jednicky == 2 or dvojky == 2 or trojky == 2 or ctyrky == 2:
                body.append(1000)
            else:
                break

        else:    
            break

    if sestky == 2:
        if jednicky == 2:
            if dvojky == 2 or trojky == 2 or ctyrky == 2 or petky == 2:
                body.append(1000)
            else:
                break

        elif dvojky == 2:
            if jednicky == 2 or trojky == 2 or ctyrky == 2 or petky == 2:
                body.append(1000)
            else:
                break

        elif trojky == 2:
            if jednicky == 2 or dvojky == 2 or ctyrky == 2 or petky == 2:
                body.append(1000)
            else:
                break

        elif ctyrky == 2:
            if jednicky == 2 or dvojky == 2 or trojky == 2 or petky == 2:
                body.append(1000)
            else:
                break

        elif petky == 2:
            if jednicky == 2 or dvojky == 2 or trojky == 2 or ctyrky == 2:
                body.append(1000)
            else:
                break
        
        else:
            break
    
    else:
        break

#---------Postupka---------
if jednicka in seznam_vygenerovanych_cisel and dva in seznam_vygenerovanych_cisel and tri in seznam_vygenerovanych_cisel and ctyri in seznam_vygenerovanych_cisel and pet in seznam_vygenerovanych_cisel and sest in seznam_vygenerovanych_cisel:
    body.append(1500)


#Součet bodů
celkovy_pocet_bodu = sum(body)
print(f"Tvůj počet bodů: {celkovy_pocet_bodu}")

#oznámení výherce
print(f"Výhercem se stává: {jmeno}")
sys.exit()