import json
from tkinter import *
from tkinter import messagebox

with open("triaaži_reeglid.json", "r", encoding="utf-8") as f:
    reegel = json.load(f)

def seadista_aken(aken, laius=400, kõrgus=200):
    ekraani_laius = aken.winfo_screenwidth()
    ekraani_kõrgus = aken.winfo_screenheight()
    x = (ekraani_laius - laius) // 2
    y = (ekraani_kõrgus - kõrgus) // 2
    aken.geometry(f"{laius}x{kõrgus}+{x}+{y}")

def jah_ei(küsimus):
    """Küsib jah/ei küsimust"""
    vastus = {"võti": None}
    
    def vali(value):
        vastus["võti"] = value
        aken.destroy()
    
    aken = Tk()
    aken.title("Triaaž")
    seadista_aken(aken, 400, 150)
    
    # Küsimus
    Label(aken, text=küsimus, font=("Arial", 12), wraplength=350, pady=20).pack()
    
    # Nupud
    nupu_raam = Frame(aken)
    nupu_raam.pack(pady=10)
    
    Button(nupu_raam, text="Jah", command=lambda: vali(True), 
           font=("Arial", 11), width=12, padx=10, pady=5).pack(side=LEFT, padx=5)
    
    Button(nupu_raam, text="Ei", command=lambda: vali(False),
           font=("Arial", 11), width=12, padx=10, pady=5).pack(side=LEFT, padx=5)
    
    aken.mainloop()
    return vastus["võti"]

def teade(tekst):
    aken = Tk()
    aken.title("Triaaž")
    seadista_aken(aken, 400, 150)
    
    # Teade
    Label(aken, text=tekst, font=("Arial", 12), wraplength=350, pady=25).pack()
    
    # OK nupp
    Button(aken, text="OK", command=aken.destroy,
           font=("Arial", 11), width=12, padx=10, pady=5).pack(pady=10)
    
    aken.mainloop()

def number(küsimus):
    """Küsib numbrit"""
    vastus = {"võti": None}
    
    def loe():
        try:
            vastus["võti"] = int(sisend.get())
            aken.destroy()
        except ValueError:
            error_label.config(text="Palun sisesta number!")
        
    aken = Tk()
    aken.title("Triaaž")
    seadista_aken(aken, 400, 180)
    
    # Küsimus
    Label(aken, text=küsimus, font=("Arial", 12), pady=15).pack()
    
    # Sisend
    sisend = Entry(aken, font=("Arial", 12), width=25)
    sisend.pack(pady=5)
    sisend.focus()
    
    # Veateade
    error_label = Label(aken, text="", font=("Arial", 9), fg="red")
    error_label.pack()
    
    # OK nupp
    Button(aken, text="OK", command=loe,
           font=("Arial", 11), width=12, padx=10, pady=5).pack(pady=10)
    
    # Enter klahv töötab ka
    aken.bind('<Return>', lambda e: loe())
    
    aken.mainloop()
    return vastus["võti"]


def kontrolli_kõnnib():
    if jah_ei("Kas kannatanu kõnnib?"):
        return reegel["kõnnib"]["jah"]["kategooria"]
    else:
        return kontrolli_hingab()


def kontrolli_hingab():
    kannatanu = reegel["kõnnib"]["ei"]
    
    if not jah_ei("Kas kannatanu hingab?"):
        return käsitle_ei_hinga(kannatanu["hingab"]["ei"])
    else:
        return käsitle_hingab(kannatanu["hingab"]["jah"])


def käsitle_ei_hinga(reeglid):
    teade(reeglid["tegevus"])
    hingab_nüüd = jah_ei("Hingab nüüd?")
    return reeglid["korda"][str(hingab_nüüd)]


def käsitle_hingab(reeglid):
    if jah_ei("Massiivne verejooks jäsemest?"):
        return reeglid["verejooks"]["jah"]
    else:
        return kontrolli_parameetreid(reeglid["verejooks"]["ei"])


def kontrolli_parameetreid(reeglid):
    hingamissagedus = number("Mis on hingamissagedus?")
    sagedus_reeglid = reeglid["hingamissagedus"]
    
    if hingamissagedus < 10:
        return sagedus_reeglid["aeglane"]
    elif hingamissagedus > 30:
        return sagedus_reeglid["kõrge"]
    else:
        return kontrolli_pulss(sagedus_reeglid["normaalne"]["pulss"])


def kontrolli_pulss(pulss_reeglid):
    pulss = number("Mis on pulss?")
    
    if pulss == 0:
        return pulss_reeglid["null"]
    elif pulss > 120:
        return pulss_reeglid["kõrge"]
    else:
        return pulss_reeglid["aeglane"]

if __name__ == "__main__":
    kategooria = kontrolli_kõnnib()
    teade(f"Kategooria: {kategooria}")
