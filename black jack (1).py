import random
import time

dealer = 0
jatekos = 0
huzas = 0
megy = 1

def huz(ki):
    global huzas
    global jatekos
    global dealer
    huzas = random.randint(1, 11)
    if ki == "jatekos":
        jatekos += huzas
    elif ki == "dealer":
        dealer += huzas

def dontes():
    global megy
    global jatekos
    valasz = input("Szeretnél kártyát felhúzni, vagy megállsz? [húzz/megáll]: ")
    print("\n" * 7)
    if valasz == "húzz":
        huz("jatekos")
        if jatekos > 21:
            megy = 0
        else:
            print(f"Dealer🤖: {dealer} \nJátékos🤠: {jatekos}\n")
    elif valasz == "megáll":
        megy = 0
    else:
        print("Érvénytelen válasz, kérlek írd be: húzás vagy megállás.")

# Játék kezdete
print("Üdvözöllek, ez itt egy BlackJack játék!")
print("A dealer és a játékos is húz kettő-kettő lapot. \n")

for _ in range(2):
    huz("dealer")
    huz("jatekos")

print(f"Dealer🤖: {dealer} \nJátékos🤠: {jatekos}\n")

while megy == 1:
    dontes()

# Eredmény
print(f"Dealer🤖: {dealer} \nJátékos🤠: {jatekos}\n")
time.sleep(1)

if jatekos <= 21:
    while dealer <= 16:
        huz("dealer")
        print("Húz a dealer...")
        time.sleep(1)
        print("\n" * 7)
        print(f"Dealer🤖: {dealer} \nJátékos🤠: {jatekos}\n")

    if dealer > 21 or dealer < jatekos:
        print("💲Nyertél!💲")
    elif dealer > jatekos:
        print("❌Vesztettél!❌")
    else:
        print("🤝Döntetlen!")
else:
    print("❌Vesztettél, mivel átlépted a 21-et!❌")
