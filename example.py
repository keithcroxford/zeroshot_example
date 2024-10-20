import pandas as pd
from transformers import pipeline

# define a classifier for zero shot. 
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Sample ticket Data 
ticket_data = 'example_tickets.csv'
df = pd.read_csv(ticket_data)

#Define Candidate Labels
candidate_labels = ["Routing", "Maintenance Notices", "Password Resets", "Spam", "Web Portal Issues"]

#Iterate over the Dataframe and classify
for index, row in df.iterrows():
    
    # Run the classifier against the description and candidate labels
    result = classifier(row['Description'], candidate_labels)
    
    # Convert result into a dictionary of labels and scores
    r = dict(zip(result['labels'], result['scores']))
    max_key = max(r, key=r.get)
    max_value = r[max_key]
    
    # Print the results 
    print(f"Ticket #: {row['Ticket ID']} | Known Category: {row['Category']} | Zero Shot Category: {max_key} | Zero Shot Probability: {max_value}")
