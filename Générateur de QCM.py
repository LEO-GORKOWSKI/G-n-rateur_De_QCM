import random
import os
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.shared import Cm

class GenerateurQCM:
    """
    Classe principale pour générer des QCM à partir d'un fichier de questions.
    """
    def __init__(self, fichier_questions, nb_eleves, nb_questions, graine):
        """
        Initialise le générateur de QCM.
        
        Args:
            fichier_questions (str): Chemin vers le fichier contenant les questions
            nb_eleves (int): Nombre d'élèves (donc de sujets à créer)
            nb_questions (int): Nombre de questions par sujet (5, 10, 15 ou 20)
            graine (int): Graine pour la génération aléatoire
        """
        self.fichier_questions = fichier_questions
        self.nb_eleves = nb_eleves
        self.nb_questions = nb_questions
        self.graine = graine
        
        # Fixer la graine aléatoire
        random.seed(graine)
        
        # Charger les questions
        self.questions = self.charger_questions()
        
        # Vérifier qu'il y a assez de questions
        if len(self.questions) < nb_questions:
            raise ValueError(f"Le fichier ne contient que {len(self.questions)} questions, mais {nb_questions} sont demandées.")
        
        # Pour suivre quelles questions apparaissent dans quels sujets
        self.questions_par_sujet = {}
        self.sujets_par_question = {i: [] for i in range(len(self.questions))}
        
    def charger_questions(self):
        """
        Charge les questions depuis le fichier.
        
        Returns:
            list: Liste de dictionnaires contenant les questions, réponses et solution
        """
        questions = []
        
        with open(self.fichier_questions, 'r', encoding='utf-8') as f:
            lignes = f.readlines()
            
            i = 0
            while i < len(lignes):
                # Si on est à la fin du fichier ou devant une ligne vide, passer
                if i >= len(lignes) or not lignes[i].strip():
                    i += 1
                    continue
                
                # Récupérer la question
                question = lignes[i].strip()
                
                # Récupérer les 4 réponses
                reponses = []
                for j in range(1, 5):
                    if i + j < len(lignes) and lignes[i + j].strip():
                        reponses.append(lignes[i + j].strip())
                    else:
                        # Si pas assez de réponses, passer cette question
                        break
                
                # Récupérer la solution
                if i + 5 < len(lignes) and lignes[i + 5].strip():
                    try:
                        solution = int(lignes[i + 5].strip())
                        
                        # Vérifier que la solution est valide (entre 1 et 4)
                        if 1 <= solution <= 4:
                            # Ajouter la question
                            questions.append({
                                'question': question,
                                'reponses': reponses,
                                'solution': solution
                            })
                    except ValueError:
                        # Si la solution n'est pas un entier, passer cette question
                        pass
                
                # Passer à la question suivante (question + 4 réponses + solution + ligne vide)
                i += 7
        
        return questions