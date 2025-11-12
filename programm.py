import json
from tkinter import *
from tkinter import messagebox

with open("triaaži_reeglid.json", "r", encoding="utf-8") as f:
    reegel = json.load(f)

def jah_ei(küsimus):
    return messagebox.askyesno(title="Triaaš", message=küsimus)

def teade(tekst):
    messagebox.showinfo(title="Triaaš", message=tekst)

def number(küsimus):
    vastus = {"võti": None}
    
    def loe():
        vastus["võti"] = int(sisend.get())
        aken.destroy()
        
            
    aken = Tk()
    aken.title("Tiraaš")
    Label(aken, text=küsimus).pack(pady=10)
    
    sisend = Entry()
    sisend.pack(pady=5)
    
    Button(aken, text="OK", command=loe).pack(pady=10)
    aken.mainloop()
    return vastus["võti"]
    

#kõnnib = input("Kas kannatanu kõnnib? (jah/ei): ").lower()
if jah_ei("Kas kannatanu kõnnib?"):
    #print("Kategooria:", reegel["kõnnib"]["jah"]["kategooria"])
    teade(("Kategooria:", reegel["kõnnib"]["jah"]["kategooria"]))
else:
    #hingab = input("Kas kannatanu hingab? (jah/ei): ").lower()
    if not jah_ei("Kas kannatanu hingab?"):
        #print(reegel["kõnnib"]["ei"]["hingab"]["ei"]["tegevus"])
        teade((reegel["kõnnib"]["ei"]["hingab"]["ei"]["tegevus"]))
        korda = str(jah_ei("Hingab nüüd?")) #input("Hingab nüüd? (jah/ei): ").lower()
        #print(reegel["kõnnib"]["ei"]["hingab"]["ei"]["korda"][korda])
        teade((reegel["kõnnib"]["ei"]["hingab"]["ei"]["korda"][korda]))
    else:
        #verejooks = input("Massiivne verejooks jäsemest? (jah/ei): ").lower()
        if jah_ei("Massiivne verejooks jäsemest?"):
            #print(reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["jah"])
            teade(("Kategooria:",reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["jah"]))
        else:
            #hingamissagedus = int(input("Mis on hingamissagedus? "))
            hingamissagedus = number("Mis on hingamissagedus?")
            if hingamissagedus < 10:
                teade((reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["ei"]["hingamissagedus"]["aeglane"]))
            elif hingamissagedus > 30:
                teade((reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["ei"]["hingamissagedus"]["kõrge"]))
            else:
                pulss = number("Mis on pulss?")
                if pulss == 0:
                    teade((reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["ei"]["hingamissagedus"]["normaalne"]["pulss"]["null"]))
                elif pulss > 120:
                    teade((reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["ei"]["hingamissagedus"]["normaalne"]["pulss"]["kõrge"]))
                else:
                    teade((reegel["kõnnib"]["ei"]["hingab"]["jah"]["verejooks"]["ei"]["hingamissagedus"]["normaalne"]["pulss"]["aeglane"]))
