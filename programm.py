import json

with open("triaaži_reeglid.json", "r", encoding="utf-8") as f:
    reegel = json.load(f)

# Start decision process
kõnnib = input("Kas kannatanu kõnnib? (jah/ei): ").lower()
if kõnnib == "jah":
    print("Kategooria:", reegel["kõnnib"]["jah"]["kategooria"])
else:
    hingab = input("Kas kannatanu hingab? (jah/ei): ").lower()
    if hingab == "ei":
        print(reegel["kõnnib"]["ei"]["hingab"]["ei"]["tegevus"])
        korda = input("Hingab nüüd? (jah/ei): ").lower()
        print(reegel["kõnnib"]["ei"]["hingab"]["ei"]["korda"][korda])
    else:
        verejooks = input("Massiivne verejooks jäsemest? (jah/ei): ").lower()
        if verejooks == "jah":
            print(reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["jah"])
        else:
            hingamissagedus = int(input("Mis on hingamissagedus? "))
            if hingamissagedus < 10:
                print(reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["ei"]["hingamissagedus"]["aeglane"])
            elif hingamissagedus > 30:
                print(reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["ei"]["hingamissagedus"]["kõrge"])
            else:
                pulse = int(input("Mis on pulss? "))
                if pulse == 0:
                    print(reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["ei"]["hingamissagedus"]["normaalne"]["pulse"]["null"])
                elif pulse > 120:
                    print(reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["ei"]["hingamissagedus"]["normaalne"]["pulse"]["kõrge"])
                else:
                    print(reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["ei"]["hingamissagedus"]["normaalne"]["pulse"]["aeglane"])

