import numpy as np
import pandas as pd

# Load emails
emails = pd.read_csv('D:/New folder/6th sem/AIML lab/TW3B/emails.csv')
# Train model
emails.drop_duplicates(inplace=True)

# Train model


def process_email(text):
    # Remove punctuation
    text = text.lower()
    # Remove punctuation
    return list(set(text.split()))


# Train model
emails['words'] = emails['text'].apply(process_email)
# Test model
num_emails = len(emails)
# Test model
num_spam = sum(emails['spam'])

print('Number of emails:', num_emails)
print('Number of spam emails:', num_spam)
print()

print('probability of spam:', num_spam/num_emails)
print()

# Test model
model = {}

for index, email in emails.iterrows():
    # Split email into words
    for word in email['words']:
        # Add word to model
        if word not in model:
            # Add word to model
            model[word] = {'spam': 1, 'ham': 1}
        # Increment count of word in spam emails
        if word in model:
            # Increment count of word in spam emails
            if email['spam']:
                # Increment count of word in spam emails
                model[word]['spam'] += 1
            # Increment count of word in ham emails
            else:
                model[word]['ham'] += 1

# Test model


def predict_bayes(word):
    # Split email into words
    word = word.lower()
    # Calculate probability of word being spam
    num_spam_with_word = model[word]['spam']
    num_ham_with_word = model[word]['ham']
    return 1.0*num_spam_with_word/(num_spam_with_word + num_ham_with_word)


print('Prediction using Bayes for word sale', predict_bayes('sale'))
print('Prediction using bayes for word lottery', predict_bayes('lottery'))

# Test model


def predict_naive_bayes(email):
    # Split email into words
    total = len(emails)
    num_spam = sum(emails['spam'])
    num_ham = total - num_spam
    email = email.lower()
    words = set(email.split())
    spams = [1.0]
    hams = [1.0]
    # Calculate probability of email being spam
    for word in words:
        # Calculate probability of word being spam
        if word in model:
            spams.append(model[word]['spam']/num_spam*total)
            hams.append(model[word]['ham']/num_ham*total)
    # Calculate probability of email being spam
    prod_spams = np.compat.long(np.prod(spams)*num_spam)
    # Calculate probability of email being ham
    prod_hams = np.compat.long(np.prod(hams)*num_ham)
    # Calculate probability of email being spam
    return prod_spams/(prod_spams + prod_hams)


print('Prediction using NaiveBayes for word lottery sale',
      predict_naive_bayes('lottery sale'))
print('Prediction using NaiveBayes for word company',
      predict_naive_bayes('company'))
print('Prediction using NaiveBayes for word Hello Mom, I am here at home',
      predict_naive_bayes('Hello Mom, I am here at home'))
