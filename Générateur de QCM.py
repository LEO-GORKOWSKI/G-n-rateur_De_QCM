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
    
    def generer_sujet(self, num_sujet):
        """
        Génère un sujet pour un élève.
        
        Args:
            num_sujet (int): Numéro du sujet à générer
            
        Returns:
            tuple: (liste de questions pour ce sujet, 
                   liste des réponses correctes sous forme de lettres)
        """
        # Sélectionner aléatoirement les questions pour ce sujet
        indices_questions = random.sample(range(len(self.questions)), self.nb_questions)
        
        # Enregistrer quelles questions apparaissent dans ce sujet
        self.questions_par_sujet[num_sujet] = indices_questions
        
        # Mettre à jour les sujets dans lesquels chaque question apparaît
        for idx in indices_questions:
            self.sujets_par_question[idx].append(num_sujet)
        
        questions_sujet = []
        reponses_correctes = []
        
        for i, idx in enumerate(indices_questions):
            question = self.questions[idx]
            
            # Copier les réponses pour pouvoir les mélanger
            reponses = question['reponses'].copy()
            solution_originale = question['solution'] - 1  # Convertir 1-4 en 0-3
            
            # Mélanger les réponses
            random.shuffle(reponses)
            
            # Trouver la nouvelle position de la bonne réponse
            nouvelle_solution = reponses.index(question['reponses'][solution_originale])
            
            # Convertir l'indice (0-3) en lettre (a-d)
            lettre_solution = chr(97 + nouvelle_solution)  # 'a', 'b', 'c' ou 'd'
            
            # Ajouter la question et les réponses mélangées au sujet
            questions_sujet.append({
                'numero': i + 1,
                'question': question['question'],
                'reponses': reponses,
                'solution': nouvelle_solution + 1  # Reconvertir 0-3 en 1-4
            })
            
            # Ajouter la lettre de la bonne réponse à la liste
            reponses_correctes.append(lettre_solution)
        
        return questions_sujet, reponses_correctes
    
    def generer_sujets(self):
        """
        Génère tous les sujets pour tous les élèves.
        
        Returns:
            dict: Dictionnaire de sujets par numéro de sujet
        """
        sujets = {}
        
        for i in range(self.nb_eleves):
            sujets[i] = self.generer_sujet(i)
        
        return sujets
