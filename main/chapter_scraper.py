"""
Program:               chapter_scraper.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-09-18

Scrapes a chapter of two books.
"""

from re import search, split, sub

from constants import READ_ONLY, FILE_LOCATION_MOBY_DICK_CHAPTER_1, FILE_LOCATION_SENSE_AND_SENSIBILITY_CHAPTER_1, WORD_OLD, WORD_WATER


def get_lines(text):
    """
    Gets all of the lines from a text file.

    :param text: Text file location
    :return: list of lines from text file
    """
    # Initialize list of lines.
    lines = []

    # Open text file.
    with open(text, READ_ONLY) as input_file:
        # Loop through each line in text file.
        for line in input_file:
            # Append line to list of lines.
            lines.append(line)

    # Return list of lines.
    return lines


def get_words(lines_list):
    """
    Gets all of the words from a list of lines.

    :param lines_list: list of lines
    :return: list of words from list of lines
    """
    # Initialize list of words.
    words = []

    # Loop through each line in list of lines.
    for line in lines_list:
        # Lowercase all characters in the line.
        line = line.lower()
        # Remove punctuation from the line.
        line_no_punctuation = sub(r'[^\w\s]', '', line)
        # Split the line into words.
        words_in_line = line_no_punctuation.split()
        # Loop through each word in the line.
        for word_in_line in words_in_line:
            # Append word to list of words.
            words.append(word_in_line)

    # Return list of words.
    return words


def get_sentences(lines):
    """
    Gets all sentences from a list of lines.

    :param lines: list of lines
    :return: list of sentences from list of lines
    """
    # Initialize list of lines without single newlines.
    lines_without_single_newlines = []

    # Initialize list of lines without newlines.
    lines_without_newlines = []

    # Initialize chapter string.
    chapter = ''

    # Loop through each line in lines list.
    for line in lines:
        # Determine if line only contains a newline.
        if line != '\n':
            # Append line to lines without single newlines list.
            lines_without_single_newlines.append(line)

    # Loop through each line without single newlines list.
    for line in lines_without_single_newlines:
        # Remove newlines from line.
        line_without_newlines = sub(r'[\n]', '', line)
        # Append line without newlines to lines without newlines list.
        lines_without_newlines.append(line_without_newlines)

    # Loop through each line without newlines list until the last.
    for line in lines_without_newlines[:-1]:
        # Append each line with a space at the end to the chapter string.
        chapter += line + ' '
    # Append the last line without a space at the end to the chapter string.
    chapter += lines_without_newlines[-1]

    # Split sentences (imperfectly) from chapter string.
    sentences = split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<![A-Z][a-z][a-z]\.)(?<=[.?!_”])\s', chapter)

    # Return list of sentences.
    return sentences


def get_word_count_of_exact_word(words_list, word_to_search):
    """
    Gets word count of exact word match in a list of words.

    :param words_list: list of words
    :param word_to_search:  word to search exact match
    :return: word count of exact matches of a word in a list of words
    """
    # Initialize word count.
    word_count = 0

    # Loop through each word in list of words.
    for word_in_list in words_list:
        # Determine if the word is an exact match of a given word.
        if word_in_list == word_to_search:
            # Increment word count upon found match.
            word_count += 1

    # Return word count.
    return word_count


def get_word_count_of_partial_word_match(words_list, word_to_search):
    """
    Gets word count of partial word match in a list of words.

    :param words_list: list of words
    :param word_to_search: word to search partial match
    :return: word count of partial matches of a word in a list of words
    """
    # Initialize word count.
    word_count = 0

    # Loop through each word in list of words.
    for word_in_list in words_list:
        # Determine if the word contains a given word.
        if search(word_to_search, word_in_list) is not None:
            # Increment word count upon found match.
            word_count += 1

    # Return word count.
    return word_count


def get_average_sentence_length(sentences_list):
    """
    Calculates average sentence length from list of sentences.

    :param sentences_list: list of sentences
    :return: average sentence length
    """
    # Initialize total characters.
    total_characters = 0

    # Loop through each sentence in sentences list.
    for sentence in sentences_list:
        # Add length of sentence to total characters.
        total_characters += len(sentence)

    # Calculate average sentence length.
    average_sentence_length = int(total_characters / len(sentences_list))

    # Return average sentence length.
    return average_sentence_length


def print_text_information(text):
    """
    Prints information from a text file.

    :param text: Text file location
    :return: N/A
    """
    # Get list of lines.
    lines_list = get_lines(text)

    # Get list of words.
    words_list = get_words(lines_list)

    # Get list of sentences.
    sentences_list = get_sentences(lines_list)

    # Get word counts.
    old_count = get_word_count_of_exact_word(words_list, WORD_OLD)
    water_count = get_word_count_of_partial_word_match(words_list, WORD_WATER)

    # Get average sentence length.
    average_sentence_length = get_average_sentence_length(sentences_list)

    # Print information.
    print(f'Old count: {str(old_count)}')
    print(f'Water count: {str(water_count)}')
    print(f'Average sentence length: {str(average_sentence_length)}')


if __name__ == '__main__':
    # Moby Dick
    print('Moby Dick:', end='\n\n')
    # Moby Dick Chapter 1
    print_text_information(FILE_LOCATION_MOBY_DICK_CHAPTER_1)

    # Print newline
    print('\n')

    # Sense and Sensibility
    print('Sense and Sensibility:', end='\n\n')
    # Sense and Sensibility Chapter 1
    print_text_information(FILE_LOCATION_SENSE_AND_SENSIBILITY_CHAPTER_1)
