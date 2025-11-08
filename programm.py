seisund = input("Kas kannatanu kõnnib? (jah/ei): ").lower()

if seisund == "jah":
    kategooria = "ROHELINE T3"
    print("Kategooria:", kategooria)
else:
    hingab = input("Kas kannatanu hingab? (jah/ei): ").lower()
    if hingab == "ei":
        print("Ava hingamisteed")
        hingab = input("Hingab nüüd? (jah/ei): ").lower()
        if hingab == "ei":
            print("Must, surnud")
        else:
            print("Püsiv külili asend")
            print("Punane T1")
    elif hingab == "jah":
        verejooks = input("Massiivne verejooks jäsemest? (jah/ei): ").lower()
        if verejooks == "jah":
            print("Žgutt")
            print("Punane T1")
        elif verejooks == "ei":
            try:
                hingamissagedus = int(input("Mis on kannatanu hingamissagedus? (täisarv): "))
                if hingamissagedus < 10 or hingamissagedus > 30:
                    print("Punane T1")
                else:
                    pulss = int(input("Mis on kannatanu pulss? (täisarv): "))
                    if pulss == 0 or pulss > 120:
                        print("Punane T1")
                    elif 0 < pulss <= 120:
                        print("Kollane T2")
            except ValueError:
                print("Palun sisesta hingamissagedus ja pulss täisarvuna.")

