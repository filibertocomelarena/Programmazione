import tkinter
import Produttore
import Consumatore
import rubrica


class GUI():
    def __init__(self):
        # creo una finestra
        self.window = tkinter.Tk()
        self.window.title("GUI")
        self.window.configure(width=500, height=300, bg='#F0FFFF')
        #creo una label
        self.label = tkinter.Label(self.window, text="RUBRICA",font=("Times", 12),bg='#F0F8FF',fg='#000000')
        self.label.grid()
        self.label.place(in_=self.window, anchor="c", relx=.5, rely=.03)
        # creo due bottoni
        self.button1 = tkinter.Button(self.window, text="SIMPLE TEST")
        self.button1.configure(bg= '#98FB98' , font=("Helvetica", 15), relief='ridge', fg='white', padx= 140)
        self.button1.grid()
        self.button1.place(in_=self.label, anchor="c", relx=.5, rely=3)
        self.button2 = tkinter.Button(self.window, text="MULTITEST", relief='ridge')
        self.button2.configure(bg='#B8860B', font=("Helvetica", 15), relief='ridge', fg='white', padx=150)
        self.button2.grid()
        self.button2.place(in_=self.label, anchor="c", relx=.5, rely=6)
        # creo un evento click per i bottoni
        self.button1.bind("<Button-1>", self.button1_click)
        self.button2.bind("<Button-1>", self.button2_click)

        # creo una casella di testo
        self.textbox = tkinter.Entry(self.window)
        self.textbox.grid()
        self.textbox.place(in_=self.label, anchor="c", relx=.5, rely=11)
        self.status = tkinter.Label(self.window, text="Nessun Test In Corso", font='Times',bg='#F0FFFF')
        self.status.grid()
        self.status.place(in_=self.label, anchor="c", relx=.5, rely=12.50)


    # creo una funzione evento per il bottone
    def button1_click(self, event):
        if self.test_running: #togliere l'if
            self.status['text'] = "Un test è già in esecuzione"
            return

        self.status['text'] = "Simple test in esecuzione"
        self.status.update()
        self.test_running = True #togliere questa

        #creo rubrica, produttore e consumatore
        r = rubrica.Rubrica()
        p = Produttore.Produttore(r, 1)
        c = Consumatore.Consumatore(r, 1)

        p.start()
        c.start()

        p.join()
        c.join()


        self.status['text'] = "Simple test terminato"
        self.test_running = False #posso togliere questa

    # creo un evento click per il bottone
    def button2_click(self, event):
        if self.test_running: #togliere
            self.status['text'] = "Un test è già in esecuzione"
            return

        self.test_running = True #togliere
        # prendo il numero di thread che si scrivono in txt box
        numero_threads = self.textbox.get()
        if not numero_threads.isdigit():
            self.status['text'] = "Input non numerico"
            self.test_running = False
            return

        numero_threads = int(numero_threads)
        if numero_threads < 2 or numero_threads > 100: #vedo se rientra nel range
            self.status['text'] = "Numero di thread non valido"
            self.test_running = False #tolgo
            return

        r = rubrica.Rubrica()
        #lista di thread prod e consumatori(alternati)
        lista_threads = []
        for i in range(numero_threads):
            p = Produttore.Produttore(r, i)
            lista_threads.append(p)
            c = Consumatore.Consumatore(r, i)
            lista_threads.append(c)

        for t in lista_threads: #partono
            t.start()
        #aggiorno la label
        self.status['text'] = "Multi test avviato (" + str(numero_threads) + " threads)"
        self.status.update()

        for t in lista_threads:
            t.join()

        self.status['text'] = "Multi test terminato"
        self.test_running = False #tolgo


gui = GUI()   #creo un oggetto interfaccia in GUI
gui.window.mainloop() #avviamo la finestra( l'interfaccia )
