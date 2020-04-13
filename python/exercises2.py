import constants
import random
import utils

courses = dict(
  spanish = random.randint(1,50)/10,
  math = random.randint(1,50)/10,
  economics = random.randint(1,50)/10,
  prog = random.randint(1,50)/10,
  english = random.randint(1,50)/10
  )

def subjets_aver():
  grades = (courses.values())
  rounded_aver = round(sum(grades) / len(grades),2)
  return rounded_aver

def best_subject():
  best_grade = max(courses.values())
  return utils.find_in_dict_by_value(courses,best_grade, 'key')

def num_list_properties(limit=10):
  num_list = []
  while len(num_list) < limit:
    num_list.append(abs(int(input('enter a whole number: '))))
  properties = dict(
    sum=sum(num_list),
    aver=sum(num_list)/len(num_list),
    max=max(num_list),
    min=min(num_list) # ’;-—:“”
  )
  return properties

def palindrome_sentences():
  sentences_list = utils.user_input('Enter a sentence: ', False)
  palindrome_list = []
  for sentence in sentences_list:
    if sentence==sentence[::-1]:
      palindrome_list.append(sentence)
  return palindrome_list

def most_repeated_word(text=constants.FIRST_CHAPTER_OF_FRANKENSTEN):
  text_char_list = list(text)
  unwanted_chars = '’;-—:“”.,'
  text_words_list = ''.join(utils.delete_from_list(text_char_list,unwanted_chars)).lower().split()
  words_count = {}
  for word in text_words_list:
    if word not in words_count:
      words_count[word] = text_words_list.count(word)
  max_value = max(words_count.values())
  return utils.find_in_dict_by_value(words_count,max_value)

def show_string_as_corelated_numbers():
  sentence = input('Enter a sentence: ')
  chars_as_numbers = []
  for c in sentence:
    for key, value in constants.ENGLISH_ALPHABET:
      if c.lower() == key: chars_as_numbers.append(f'{value}')
  return ''.join(chars_as_numbers)

def count_of_each_vowel():
  sentence = input('Enter a sentence: ')
  vowles = dict(
    a=sentence.count('a'),
    e=sentence.count('e'),
    i=sentence.count('i'),
    o=sentence.count('o'),
    u=sentence.count('u')
  )
  return vowles

def number_of_vowels():
  return sum(count_of_each_vowel().values())

def delete_all_vowels():
  sentence = input('Enter a sentence: ')
  sentence_char_list = list(sentence)
  return ''.join(utils.delete_from_list(sentence_char_list, constants.ENGLISH_VOWELS))

def only_odds(begin=1, end=100):
  if begin % 2 != 0: begin = begin + 1
  if end % 2 == 0: end = end + 1
  odds_list = []
  for num in range(begin,end,2):
    odds_list.append(num)
  return odds_list

print('Average of subjects:',subjets_aver())
# print('Best subject:',best_subject())
# print('Properties of a given 10 numbers list:',num_list_properties())
# print('All palindrome sentences of a given sentences list:',palindrome_sentences())
# print('Most repeated word on first chapter of Frankenstein:',most_repeated_word())
# print('Character-numbered version of a given sentence:',show_string_as_corelated_numbers())
# print('Number of vowles in a given sentence:',number_of_vowels())
# print('Count of each vowel in a given sentence:',count_of_each_vowel())
# print('Deletion of all vowels from a given sentence:',delete_all_vowels())
# print('List of all odds from 0 to 100:',only_odds())
