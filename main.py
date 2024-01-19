import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import bigrams, trigrams
from collections import Counter
import string

def find_most_common_seo_words(file_path, top_n=10, output_file='job_listing_seo.txt'):
    # Step 1: Read the Text File
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()

    # Step 2: Tokenization
    nltk.download('punkt')  # Download the punkt tokenizer data
    tokens = word_tokenize(text_content)

    # Step 3: Remove Stop Words and Non-Alphabetic Words
    nltk.download('stopwords')  # Download the stopwords data
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]

    # Step 4: Count Word Frequencies
    word_freq = Counter(filtered_tokens)

    # Step 5: Get Top Words
    most_common_words = word_freq.most_common(top_n)

    # Step 6: Print or Use the Results to File
    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(f'Top {top_n} Most Common SEO Words:\n')
        for word, frequency in most_common_words:
            output_file.write(f'{word}: {frequency} times\n')

        # Count Bigrams
        bigram_freq = Counter(list(bigrams(filtered_tokens)))
        most_common_bigrams = bigram_freq.most_common(top_n)
        output_file.write(f'\nTop {top_n} Most Common SEO Bigrams:\n')
        for bigram, frequency in most_common_bigrams:
            output_file.write(f'{bigram}: {frequency} times\n')

        # Count Trigrams
        trigram_freq = Counter(list(trigrams(filtered_tokens)))
        most_common_trigrams = trigram_freq.most_common(top_n)
        output_file.write(f'\nTop {top_n} Most Common SEO Trigrams:\n')
        for trigram, frequency in most_common_trigrams:
            output_file.write(f'{trigram}: {frequency} times\n')

# Example Usage
file_path = 'joblisting.txt'  # Replace with the path to your text file
find_most_common_seo_words(file_path, top_n=10)
