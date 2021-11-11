def verhaal_doorslapen():
    print("je dengt er niets van en je slaapt door")
    print("maar dat duurt niet lang een van je ouders maakt je wakker")
    print("ze zegen dat het ontbijt voorbij is en geven je en ze sturen je naar buiten")

def verhaal_pratenmetjeklasgenoten():
    print("terwijl je niet naar de meester hebt geluisterd heb je huiswerk gekregen wat je niet hoorde")
    print("jammer dacht je dit gebeurt wel vaker")
    print("als de les voorbij is en je pauze houdt zie je wat mensen juichen 2 mensen zitten te vechten")

def verhaal_wakkerworden():
    print("je wordt wakker en omdat je dat deed heb je genoeg tijd om naar school te gaan")
    print("dan heb je ontbijt met jouw ouders en doe je daarna jouw dagelijkse ochtends routine")

def verhaal_luisteren():
    print("als de leraar praat kom je nieuwe dingen te weten en krijg je het huiswerk te weten")
    print("als de les voorbij is en je pauze houdt zie je wat mensen juichen 2 mensen zitten te vechten")

def verhaal_snelnaarschoolgaan():
    print("je besluit zo snel mogelijk naar school te gaan")

def verhaal_rustignaarschoolgaan():
    print("je doet rustig om naar school te gaan want je wilt niks vergeten")

def verhaal_kijken():
    print("je vindt dit interesant om te zien en kijk je mee")
    print("maar het gevecht duurt niet lang en een paar meesters onderbreken het gevecht")

def verhaal_nietmeebemoeien():
    print("je wilt niet ook schuldige zijn dus gaat niet erbij staan")
    print("en na een kort momentje is het gevecht al onderbroken")

def verhaal_opstandigmetjeouderszijn():
    print("je wilt niet zo aangesproken zijn dus je praat er tegen in")
    print("maar daarna wordt je naar je kamer gestuurt")

def verhaal_naarjeoudersluisteren():
    print("je vindt dat je ouders gelijk hebben en praat niet tegen")
    print("en daarom is het gesprek heel chil gebleven")

def verhaal_huiswerkmaken():
    print("je gaat je huiswerk maken want dat is belangrijk voor school")
    print("na het maken van je huiswerk is alles af en heb je en rustig weekend")

def verhaal_gamenenanderechilledingendoen():
    print("je vergeet het huiswerk en gaat chillen want huiswerk is moeilijk en saai")
    
print("je bent lekker aan het dromen niet bewust van hoe laat het is")
print("daarna begint je telefoon wekker te luiden")
print("jij bent een jongen van 14 in de middelbare")
inputtxt = input()
if inputtxt == "sta op":
    verhaal_wakkerworden()
elif inputtxt == "doorslapen":
    verhaal_doorslapen()
    inputtxt = input()
    if inputtxt == "luister naar de meester":
        verhaal_luisteren()
    elif inputtxt == "praat met je klasgenoten":
        verhaal_pratenmetjeklasgenoten()
        inputtxt = input()
        if inputtxt == "negeren":
            verhaal_nietmeebemoeien()
        elif inputtxt == "joinen":
            verhaal_kijken()
            inputtxt = input()
            if inputtxt == "huiswerk maken":
                verhaal_huiswerkmaken()
            elif inputtxt == "chillen":
                verhaal_gamenenanderechilledingendoen()
                if inputtxt == "opstandig zijn":
                    verhaal_opstandigmetjeouderszijn()
                elif inputtxt == "luisteren":
                    verhaal_naarjeoudersluisteren()


        
