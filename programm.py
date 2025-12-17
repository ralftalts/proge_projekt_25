"""
Antud programm kannab nime "Pirogovi abimees".
Programmi autorid on Joosep Jagomägi ja Ralf Talts.
Töö peamiseks allikaks on "Esmase triaaži teostamise kaart. Skeem: Kaitseväe meditsiiniteenistus. 2021."
Programmi käivitamiseks peab olema allalaetud Python (mõningate operatsioonisüsteemiga on see juba eelnevalt allalaetud).
"""

import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

with open("triaaži_reeglid.json", "r", encoding="utf-8") as f: #loeb tiraazi reeglid sisse
    reegel = json.load(f)

def seadista_aken(aken, laius=400, kõrgus=200): #teeb 400*200 akna ekraani keskele
    ekraani_laius = aken.winfo_screenwidth()
    ekraani_kõrgus = aken.winfo_screenheight()
    x = (ekraani_laius - laius) // 2
    y = (ekraani_kõrgus - kõrgus) // 2
    aken.geometry(f"{laius}x{kõrgus}+{x}+{y}")

def seadista_hüpik(root):
    hüpik = Toplevel(root)
    hüpik.title("Tiraaž")
    hüpik.transient(root)
    hüpik.grab_set()
    hüpik.protocol("WM_DELETE_WINDOW", lambda: None)
    return hüpik

def jah_ei(root, küsimus): #teeb antud küsimusega jah/ei vastuse variantidega akna ja tagastab True/False
    """Küsib jah/ei küsimust"""
    vastus = {"võti": None}
    
    aken = seadista_hüpik(root)
    seadista_aken(aken, 400, 150)
    
    def vali(value): #Omistab vastus["võti"] True/False väärtuse
        vastus["võti"] = value
        aken.destroy()
    
    # Küsimus
    Label(aken, text=küsimus, font=("Arial", 12), wraplength=350, pady=20).pack()
    
    # Nupud
    nupu_raam = Frame(aken)
    nupu_raam.pack(pady=10)
    
    Button(nupu_raam, text="Jah", command=lambda: vali(True), 
           font=("Arial", 11), width=12, padx=10, pady=5).pack(side=LEFT, padx=5)
    
    Button(nupu_raam, text="Ei", command=lambda: vali(False),
           font=("Arial", 11), width=12, padx=10, pady=5).pack(side=LEFT, padx=5)
    
    root.wait_window(aken)
    return vastus["võti"]

def teade(root, tekst): #teeb akna, mis kuvab diagnoosi
    aken = seadista_hüpik(root)
    seadista_aken(aken,400,150)
    
    
    # Teade
    Label(aken, text=tekst, font=("Arial", 12), wraplength=350, pady=25).pack()
    
    # OK nupp
    Button(aken, text="OK", command=aken.destroy,
           font=("Arial", 11), width=12, padx=10, pady=5).pack(pady=10)
    
    root.wait_window(aken)

def number(root, küsimus): #teeb antud küsimusega akna ja tagastab sisestatud numbri
    """Küsib numbrit"""
    vastus = {"võti": None}
    
    aken = seadista_hüpik(root)
    seadista_aken(aken,400,150)
    
    def loe(): #omistab vastus["võti"] numbrilise väärtuse
        try:
            vastus["võti"] = int(sisend.get())
            aken.destroy()
        except ValueError:
            error_label.config(text="Palun sisesta number!")
    
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
    
    root.wait_window(aken)
    return vastus["võti"]

def nime_küsimine(root, küsimus): 
    """Küsib nimi"""
    vastus = {"võti": None}
    
    aken = seadista_hüpik(root)
    seadista_aken(aken,400,150)
    
    def loe(): #omistab vastus["võti"] väärtuse, mis ei ole tühi
        sisestus = sisend.get().strip()
        if sisestus != "":
            vastus["võti"] = sisestus
            aken.destroy()
        else:
            error_label.config(text="Väli ei tohi olla tühi!")

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
    
    root.wait_window(aken)
    return vastus["võti"]

def kontrolli_kõnnib(root): #Küsib, kas kannatanu kõnnib ja jätkab/annab tulemuse
    if jah_ei(root, "Kas kannatanu kõnnib?"):
        return reegel["kõnnib"]["jah"]["kategooria"]
    else:
        return kontrolli_hingab(root)


def kontrolli_hingab(root): #Küsib, kas kannatanu hingab ja jätkab/annab juhise
    kannatanu = reegel["kõnnib"]["ei"]
    
    if not jah_ei(root, "Kas kannatanu hingab?"):
        return käsitle_ei_hinga(root, kannatanu["hingab"]["ei"])
    else:
        return käsitle_hingab(root, kannatanu["hingab"]["jah"])


def käsitle_ei_hinga(root, reeglid): #Annab juhise ja jätkab/ annab tulemuse
    teade(root, reeglid["tegevus"])
    hingab_nüüd = jah_ei(root, "Hingab nüüd?")
    return reeglid["korda"][str(hingab_nüüd)]


def käsitle_hingab(root, reeglid): #Küsib kas jäsemets on massiivne verejooks ja jätkab/annab tulemuse
    if jah_ei(root, "Massiivne verejooks jäsemest?"):
        return reeglid["verejooks"]["jah"]
    else:
        return kontrolli_parameetreid(root, reeglid["verejooks"]["ei"])


def kontrolli_parameetreid(root, reeglid): #Küsib hingamissagedust ja jätkab/annab tulemuse
    hingamissagedus = number(root, "Mis on hingamissagedus?")
    sagedus_reeglid = reeglid["hingamissagedus"]
    
    if hingamissagedus < 10:
        return sagedus_reeglid["aeglane"]
    elif hingamissagedus > 30:
        return sagedus_reeglid["kõrge"]
    else:
        return kontrolli_pulss(root, sagedus_reeglid["normaalne"]["pulss"])


def kontrolli_pulss(root, pulss_reeglid): # Küsib pulssi ja annab tulemuse
    pulss = number(root, "Mis on pulss?")
    
    if pulss == 0:
        return pulss_reeglid["null"]
    elif pulss > 120:
        return pulss_reeglid["kõrge"]
    else:
        return pulss_reeglid["aeglane"]
    
def loo_tabel():
    root = Tk()
    root.title("Kannatanud")
    seadista_aken(root, 400, 600)
    
    tabel = ttk.Treeview(root, columns= ("nimi", "kategooria"), show="headings")
    tabel.heading("nimi", text= "Nimi/ID")
    tabel.heading("kategooria", text= "Kategooria")
    tabel.pack(padx=10, pady=10, fill=BOTH, expand=True)
    
    tabel.tag_configure("Roheline T3", background="#24f228")
    tabel.tag_configure("Kollane T2", background="#f2ef24")
    tabel.tag_configure("Punane T1", background="#e81410")
    tabel.tag_configure("Must, surnud", background="black", foreground="white") # Black
    
    def lisa_uus_kannatanu():
        nimi = nime_küsimine(root, "Sisesta kannatanu nimi/ID")
        if not nimi: return
        
        kategooria = kontrolli_kõnnib(root)
        if kategooria:
            tabel.insert("", "end", values=(nimi, kategooria), tags=(kategooria,))
    
    def hinda_uuesti():
        valitud = tabel.selection()
        
        if not valitud:
            messagebox.showwarning("Hoiatus", "Vali tabelist kannatanu, keda uuesti hinnata!")
            return
        
        item_id = valitud[0]
        nimi = tabel.item(item_id, "values")[0]
        
        uus_kategooria = kontrolli_kõnnib(root)
        tabel.item(item_id, values=(nimi, uus_kategooria), tags=(uus_kategooria,))
        tabel.selection_remove(item_id)
        
    def sulgemine():
        if messagebox.askokcancel("Välju", "Kas soovid programmi sulgeda? Kõik sisestatud andmed kaovad."):
            root.destroy()
            root.quit()
        
    nupud = Frame(root)
    nupud.pack(pady=10)
    
    Button(nupud, text="Lisa uus patsient",
            font=("Arial", 11, "bold"), padx= 15, pady= 5,
            command= lisa_uus_kannatanu).pack(side=LEFT, padx= 10)
    
    Button(nupud, text="Hinda uuesti",
            font=("Arial", 11, "bold"), padx= 15, pady= 5,
            command= hinda_uuesti).pack(side=LEFT, padx= 10)
    root.protocol("WM_DELETE_WINDOW", sulgemine)
    
    root.mainloop()
    
    
    
if __name__ == "__main__":
    loo_tabel()
