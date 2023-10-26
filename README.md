
Rapport Analyzer
Rapport Analyzer est un script Python conçu pour analyser des rapports au format HTML. Le script effectue plusieurs tâches, notamment l'extraction d'entités nommées, l'extraction de mots-clés pertinents, et la lemmatisation des mots. Il est utile pour l'analyse de documents textuels dans le contexte de rapports ou de discours.

Prérequis
Assurez-vous que vous disposez des bibliothèques Python requises avant d'exécuter le script. Vous pouvez les installer en utilisant pip :

```bash
 pip install transformers beautifulsoup4 summa nltk spacy keybert
```
Le script utilise les bibliothèques suivantes :

transformers: Utilisé pour charger un modèle de traitement automatique du langage naturel (TALN) pour l'extraction d'entités nommées.
beautifulsoup4: Utilisé pour analyser le contenu HTML des rapports.
summa: Utilisé pour extraire des mots-clés pertinents à partir du texte.
nltk: Utilisé pour le traitement du langage naturel, y compris la suppression de mots vides.
spacy: Utilisé pour la lemmatisation des mots dans le texte.
keybert: Utilisé pour extraire des mots-clés basés sur le modèle BERT.
Utilisation
Clonez ce dépôt ou téléchargez le fichier rapport_analyzer.py sur votre système.

Assurez-vous que vous avez un fichier de rapport au format HTML à analyser. Vous pouvez spécifier le chemin du fichier dans le script.

Exécutez le script en utilisant la commande suivante :
```bash
python rapport_analyzer.py
```


Le script analysera le rapport, extraira les entités nommées, les mots-clés pertinents, et effectuera d'autres tâches d'analyse.

Les résultats seront affichés dans la console, indiquant les entités nommées identifiées, ainsi que les mots-clés extraits du texte.

Personnalisation
Vous pouvez personnaliser le script en fonction de vos besoins. Voici quelques points à considérer :

Assurez-vous que le chemin du fichier HTML du rapport est correctement spécifié dans le script.
Vous pouvez ajuster les seuils de score pour l'extraction d'entités nommées et de mots-clés pertinents en modifiant les valeurs dans le script.
Les mots vides (stopwords) peuvent être personnalisés en modifiant la liste custom_stopwords.
Contributions
Les contributions sont les bienvenues. Si vous souhaitez apporter des améliorations au script ou résoudre des problèmes, n'hésitez pas à ouvrir une demande d'extraction (Pull Request) ou un problème (Issue) dans ce dépôt.