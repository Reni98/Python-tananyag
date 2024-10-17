import random
# 1.Feladat
# Ha egy szabályos pénzérmét feldobunk, akkor egyenlő eséllyel lehet fej (F) vagy írás (I)
#  az eredmény. 
# Szimulálj öt pénzfeldobást, ahol azonos esélye van a fejnek és az írásnak is! 
# Az eredményt írasd ki txt fájlba.
# Kérj be a felhasználótól egy tippet, majd szimulálj egy pénzfeldobást és írasd ki, 
# hogy eltalálta-e vagy sem!

# F I I F I
# Kérek egy tippet (F/I): F
# A tipp F, a dobás eredménye I volt.
# Ön nem találta el!

dobas=["F","I"]
dobasok=[]
for i in range(5):
    dob = random.choice(dobas)
    dobasok.append(dob)
print(" ".join(dobasok))
feldobas= random.choice(dobasok)
tipp = input("Kérek egy tippet (F/I):")
with open("penzdobas.txt", "a") as file:
    file.write(f"A tipp {tipp},a dobás eredménye {feldobas} volt.")
    if tipp == feldobas:
        file.write("Eltaláltad!")
        print("Eltaláltad!")
    else:
        file.write("Nem találtad el!")
        print("Nem találtad el!")