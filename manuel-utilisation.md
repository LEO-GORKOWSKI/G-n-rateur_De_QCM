# Manuel d'utilisation du Générateur de QCM

Ce document vous guidera dans l'utilisation du Générateur de QCM, un outil permettant de créer des questionnaires à choix multiples personnalisés pour vos élèves.

## Prérequis

Avant d'utiliser le programme, assurez-vous d'avoir installé :
- Python 3.6 ou supérieur
- La bibliothèque python-docx pour la génération de fichiers DOCX

Vous pouvez installer la bibliothèque nécessaire avec la commande :
```bash
pip install python-docx
```

## Format du fichier de questions

Le fichier de questions doit être au format texte (.txt) et respecter la structure suivante :
```
Question
Réponse1
Réponse2
Réponse3
Réponse4
n° solution

(ligne vide)
```

Par exemple :
```
Quelle est la capitale de la France ?
Paris
Londres
Berlin
Madrid
1

Quel est le plus grand océan du monde ?
L'océan Atlantique
L'océan Indien
L'océan Pacifique
L'océan Arctique
3
```

**Note importante :** Le numéro de solution doit être un entier entre 1 et 4, indiquant quelle réponse est correcte.

## Utilisation de l'interface graphique

1. Lancez l'interface graphique en exécutant :
   ```bash
   python interface_qcm.py
   ```

2. Dans l'interface :
   - Cliquez sur "Parcourir..." pour sélectionner votre fichier de questions
   - Définissez le nombre d'élèves (sujets à générer)
   - Choisissez le nombre de questions par sujet (5, 10, 15 ou 20)
   - Entrez une graine aléatoire (pour reproduire les mêmes résultats si nécessaire)
   - Sélectionnez le format de sortie (TXT, DOCX ou les deux)

3. Cliquez sur "Générer QCM" pour créer les fichiers

4. Les fichiers générés seront sauvegardés dans le même répertoire que le programme :
   - `qcm_sujets.txt` ou `qcm_sujets.docx` : Contient les sujets pour les élèves
   - `qcm_corrections.txt` ou `qcm_corrections.docx` : Contient les corrections pour l'enseignant

## Utilisation en ligne de commande

Vous pouvez également utiliser le programme en ligne de commande :

```bash
python generateur_qcm.py fichier_questions [options]
```

Options disponibles :
- `--nb_eleves` : Nombre d'élèves (par défaut : 5)
- `--nb_questions` : Nombre de questions par sujet, doit être 5, 10, 15 ou 20 (par défaut : 10)
- `--graine` : Graine pour la génération aléatoire (par défaut : 42)
- `--format` : Format de sortie, peut être 'txt', 'docx' ou 'both' (par défaut : 'both')

Exemple :
```bash
python generateur_qcm.py QCM_cinema.txt --nb_eleves 10 --nb_questions 15 --graine 123 --format docx
```

## Structure des fichiers générés

### Fichiers de sujets (`qcm_sujets.txt` ou `qcm_sujets.docx`)

Chaque sujet contient :
- Le numéro du sujet
- Un champ pour le nom et prénom de l'élève
- Les consignes
- Un tableau de réponses où l'élève pourra indiquer ses choix
- La liste des questions avec les choix de réponses (mélangées pour chaque sujet)

Dans la version DOCX, les questions sont disposées sur deux colonnes pour optimiser l'espace et faciliter la lecture.

### Fichiers de correction (`qcm_corrections.txt` ou `qcm_corrections.docx`)

Les fichiers de correction contiennent :
- Pour chaque sujet, les réponses correctes sous forme de lettres (a, b, c, d) regroupées par blocs de 5
- Des informations supplémentaires pour l'enseignant :
  - Quelles questions initiales ont été intégrées dans chaque sujet
  - Dans quels sujets apparaît chaque question initiale

## Caractéristiques du Générateur de QCM

Le générateur offre plusieurs fonctionnalités avancées :
- Mélange aléatoire des questions pour chaque sujet
- Mélange aléatoire des réponses pour chaque question
- Génération de fichiers au format TXT et/ou DOCX
- Traçabilité des questions (savoir quel sujet contient quelle question initiale)
- Mise en page optimisée pour l'impression (format paysage, deux colonnes pour les questions)
- Tableau de réponses pour faciliter la correction

## Conseils d'utilisation

- Préparez votre fichier de questions avec soin, en respectant strictement le format indiqué
- Utilisez la même graine aléatoire si vous souhaitez reproduire exactement les mêmes sujets
- Pour des classes nombreuses, il est recommandé de disposer d'un grand nombre de questions initiales pour assurer une bonne variété entre les sujets
- Le format DOCX est recommandé pour une impression de qualité
- Vérifiez les fichiers générés avant l'impression ou la distribution aux élèves

## Résolution des problèmes courants

- **Erreur de lecture du fichier :** Vérifiez que votre fichier de questions respecte bien le format spécifié
- **Pas assez de questions :** Assurez-vous que votre fichier contient au moins autant de questions que le nombre demandé par sujet
- **Erreur lors de la génération du DOCX :** Vérifiez que la bibliothèque python-docx est bien installée
