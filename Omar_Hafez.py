import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK stopwords
nltk.download('stopwords')

# Load stop words
stop_words = set(stopwords.words('english'))

# Function to process text
def process_text(text):
    # Tokenize the text
    words = nltk.word_tokenize(text)
    # Remove stop words
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.isalpha()]
    return filtered_words

# Function to count word frequency
def count_frequency(words):
    return Counter(words)

# Read contents of the file
with open("paragraphs.txt", "r") as file:
    text = file.read()

# Process the text
processed_text = process_text(text)

# Count word frequency
word_frequency = count_frequency(processed_text)

# Display word frequency count
for word, count in word_frequency.items():
    print(f"{word}: {count}")

  