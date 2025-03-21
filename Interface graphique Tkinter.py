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
    
    