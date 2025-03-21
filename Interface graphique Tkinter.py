import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
from generateur_qcm import GenerateurQCM

class InterfaceQCM(tk.Tk):
    """
    Interface graphique pour le générateur de QCM.
    """
    def __init__(self):
        super().__init__()
        
        self.title("Générateur de QCM")
        self.geometry("600x400")
        
        # Variables
        self.fichier_questions = tk.StringVar()
        self.nb_eleves = tk.IntVar(value=5)
        self.nb_questions = tk.IntVar(value=10)
        self.graine = tk.IntVar(value=42)
        self.format_sortie = tk.StringVar(value="both")
        
        # Création de l'interface
        self._creer_widgets()
    
    def _creer_widgets(self):
        """Crée les widgets de l'interface."""
        # Cadre principal
        main_frame = tk.Frame(self, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sélection du fichier de questions
        tk.Label(main_frame, text="Fichier de questions :").grid(row=0, column=0, sticky=tk.W, pady=5)
        tk.Entry(main_frame, textvariable=self.fichier_questions, width=40).grid(row=0, column=1, sticky=tk.W, pady=5)
        tk.Button(main_frame, text="Parcourir...", command=self._parcourir_fichier).grid(row=0, column=2, padx=5, pady=5)
        
        # Nombre d'élèves
        tk.Label(main_frame, text="Nombre d'élèves :").grid(row=1, column=0, sticky=tk.W, pady=5)
        tk.Spinbox(main_frame, from_=1, to=100, textvariable=self.nb_eleves, width=5).grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Nombre de questions
        tk.Label(main_frame, text="Nombre de questions par élève :").grid(row=2, column=0, sticky=tk.W, pady=5)
        tk.OptionMenu(main_frame, self.nb_questions, 5, 10, 15, 20).grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Graine aléatoire
        tk.Label(main_frame, text="Graine aléatoire :").grid(row=3, column=0, sticky=tk.W, pady=5)
        tk.Entry(main_frame, textvariable=self.graine, width=10).grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Format de sortie
        tk.Label(main_frame, text="Format de sortie :").grid(row=4, column=0, sticky=tk.W, pady=5)
        tk.Radiobutton(main_frame, text="TXT", variable=self.format_sortie, value="txt").grid(row=4, column=1, sticky=tk.W)
        tk.Radiobutton(main_frame, text="DOCX", variable=self.format_sortie, value="docx").grid(row=5, column=1, sticky=tk.W)
        tk.Radiobutton(main_frame, text="Les deux", variable=self.format_sortie, value="both").grid(row=6, column=1, sticky=tk.W)
        
        # Boutons
        boutons_frame = tk.Frame(main_frame)
        boutons_frame.grid(row=7, column=0, columnspan=3, pady=20)
        
        tk.Button(boutons_frame, text="Générer QCM", command=self._generer_qcm, padx=10, pady=5).pack(side=tk.LEFT, padx=10)
        tk.Button(boutons_frame, text="Quitter", command=self.destroy, padx=10, pady=5).pack(side=tk.LEFT)
    
    def _parcourir_fichier(self):
        """Ouvre une boîte de dialogue pour sélectionner le fichier de questions."""
        fichier = filedialog.askopenfilename(
            title="Sélectionner le fichier de questions",
            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        if fichier:
            self.fichier_questions.set(fichier)
    
    def _generer_qcm(self):
        """Génère les QCM avec les paramètres spécifiés."""
        # Vérification des entrées
        if not self.fichier_questions.get():
            messagebox.showerror("Erreur", "Veuillez sélectionner un fichier de questions.")
            return
        
        if not os.path.exists(self.fichier_questions.get()):
            messagebox.showerror("Erreur", "Le fichier de questions n'existe pas.")
            return
        
        try:
            # Créer le générateur
            generateur = GenerateurQCM(
                self.fichier_questions.get(),
                self.nb_eleves.get(),
                self.nb_questions.get(),
                self.graine.get()
            )
            
            # Générer les sujets
            sujets = generateur.generer_sujets()
            
            # Générer les fichiers
            format_sortie = self.format_sortie.get()
            
            if format_sortie in ['txt', 'both']:
                generateur.generer_fichier_txt(sujets)
                generateur.generer_fichier_correction(sujets)
            
            if format_sortie in ['docx', 'both']:
                generateur.generer_fichier_docx(sujets)
                generateur.generer_fichier_correction_docx(sujets)
            
            messagebox.showinfo(
                "Succès",
                f"QCM générés avec succès !\n\n"
                f"Fichiers créés dans le répertoire courant :\n"
                f"- {'qcm_sujets.txt, ' if format_sortie in ['txt', 'both'] else ''}"
                f"{'qcm_corrections.txt' if format_sortie in ['txt', 'both'] else ''}\n"
                f"- {'qcm_sujets.docx, ' if format_sortie in ['docx', 'both'] else ''}"
                f"{'qcm_corrections.docx' if format_sortie in ['docx', 'both'] else ''}"
            )
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

if __name__ == "__main__":
    app = InterfaceQCM()
    app.mainloop()