"""
Created on Thu Oct 26 16:59:18 2023
@author: marccrampe
"""

# Import necessary libraries
from bs4 import BeautifulSoup
from transformers import pipeline
from summa import keywords
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
import spacy
from keybert import KeyBERT

lemmatizer = WordNetLemmatizer()

# Load Named Entity Recognition (NER) model with grouped_entities=True
ner = pipeline("ner", grouped_entities=True)

# Open the HTML file
with open("/home/marc/rapport.html", "r") as file:
    html_content = file.read()

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all <b> elements (bold text)
participants = soup.find_all("b")

# Dictionary to store interventions by participants
interventions_dict = {}

# Load the French spaCy model
spacy.cli.download("fr_core_news_sm")
nlp = spacy.load("fr_core_news_sm")

# Define custom stopwords
custom_stopwords = set(stopwords.words('french'))
custom_stopwords.add("tout")
custom_stopwords.add("fait")
custom_stopwords.add("celle")
custom_stopwords.add("quel")
custom_stopwords.add("lorsqu")

# Iterate through each participant
for participant in participants:
    participant_text = participant.get_text().strip()  # Participant's name
    intervention_text = participant.find_next("p").get_text().strip()  # Text of the intervention

    # Apply NER to the intervention text
    result = ner(intervention_text)
    
    # Extract entities with a score greater than 0.9 or of type "MISC"
    entities = [(entity['word'], entity['entity_group']) for entity in result if entity['score'] > 0.9 or (entity['entity_group'] == 'MISC' and entity['score'] > 0.7)]
    
    # Check if any entities were extracted
    if entities:
        # Check if the participant is already in the dictionary
        if participant_text in interventions_dict:
            interventions_dict[participant_text].append({"entities": entities})
        else:
            interventions_dict[participant_text] = [{"entities": entities}]

    # Extract keywords using TextRank
    extracted_keywords = keywords.keywords(intervention_text, ratio=0.5)
    phrases = extracted_keywords.splitlines()

    # Filter out stopwords from phrases
    filtered_phrases = []
    for phrase in phrases:
        words = phrase.split()
        if len(words) == 1:  # Single word
            word = words[0]
            if len(word) > 1 and word.lower() not in custom_stopwords:
                doc = nlp(word)
                if len(doc) == 1 and doc[0].pos_ == 'NOUN':
                    lemmatized_word = lemmatizer.lemmatize(doc[0].text)
                    if lemmatized_word not in filtered_phrases:
                        filtered_phrases.append(lemmatized_word)
        else:  # Multiple words (phrase)
            filtered_words = [word for word in words if word.lower() not in custom_stopwords]
            filtered_phrase = ' '.join(filtered_words)
            if filtered_phrase:
                filtered_phrases.append(filtered_phrase)
    
    
    # Store the intervention and filtered keywords
    if participant_text in interventions_dict:
        interventions_dict[participant_text].append({"intervention": intervention_text, "keywords": filtered_phrases})
    else:
        interventions_dict[participant_text] = [{"intervention": intervention_text, "keywords": filtered_phrases}]

# Display the results
for participant, interventions in interventions_dict.items():
    print("Participant:", participant)
    for intervention in interventions:
        entities = intervention.get("entities")
        if entities:
            print("Entities:")
            for entity, entity_type in entities:
                print(f"- {entity} ({entity_type})")
        keywords = intervention.get("keywords")
        if keywords:
            print("Keywords:")
            for keyword in keywords:
                print("- ", keyword)
        print()