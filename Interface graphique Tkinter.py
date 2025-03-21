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