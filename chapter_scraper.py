"""
Program:               chapter_scraper.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-09-15

Scrapes a chapter of two books.
"""

# This example assumes you have the Moby_Dick_Chapter_1.txt file in the same directory as your program
import re


if __name__ == '__main__':
    print('Moby Dick:', end='\n\n')
    with open('Moby_Dick_Chapter_1.txt', 'r') as input_file:
        # Word counts
        moby_old_count = 0
        moby_water_count = 0

        for line in input_file:
            # First lowercase all characters in the line
            line = line.lower()
            # Next clean the line of any punctuation
            line_clean = re.sub(r'[^\w\s]', '', line)
            # Now split the line into words
            line_split = line_clean.split()
            # Now we can add the words to our dictionary
            for word in line_split:
                if word == 'old':
                    moby_old_count += 1
                elif re.search('water', word) is not None:
                    moby_water_count += 1

        print(f'Old count: {str(moby_old_count)}')
        print(f'Water count: {str(moby_water_count)}')

    with open('Moby_Dick_Chapter_1.txt', 'r') as input_file:
        # Average sentence length
        moby_average_sentence_length = 0

        for line in input_file:
            sentence_split = re.split(r'[\.]', line)
            for sentence in sentence_split:
                moby_average_sentence_length += len(sentence)
            moby_average_sentence_length = int(moby_average_sentence_length / len(sentence_split))

        print(f'Average sentence length: {str(moby_average_sentence_length)}')

    print('\n')
    print('Sense and Sensibility:', end='\n\n')
    with open('Sense_and_Sensibility_Chapter_1.txt', 'r') as input_file:
        # Word counts
        sas_old_count = 0
        sas_water_count = 0

        for line in input_file:
            # First lowercase all characters in the line
            line = line.lower()
            # Next clean the line of any punctuation
            line_clean = re.sub(r'[^\w\s]', '', line)
            # Now split the line into words
            line_split = line_clean.split()
            # Now we can add the words to our dictionary
            for word in line_split:
                if word == 'old':
                    sas_old_count += 1
                elif re.search('water', word) is not None:
                    sas_water_count += 1

        print(f'Old count: {str(sas_old_count)}')
        print(f'Water count: {str(sas_water_count)}')

    with open('Sense_and_Sensibility_Chapter_1.txt', 'r') as input_file:
        # Average sentence length
        sas_average_sentence_length = 0

        for line in input_file:
            sentence_split = re.split(r'[\.]', line)
            for sentence in sentence_split:
                sas_average_sentence_length += len(sentence)
            sas_average_sentence_length = int(sas_average_sentence_length / len(sentence_split))

        print(f'Average sentence length: {str(sas_average_sentence_length)}')
