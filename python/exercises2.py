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
  sentences_list=[]
  palindrome_list=[]
  another='y'
  while another=='y':
    sentences_list.append(input('Enter a sentence: '))
    another = input('Another sentence? (y/n) ')
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



# print('Average of subjects:',subjets_aver())
# print('Best subject:',best_subject())
# print('Properties of a given 10 number list:',num_list_properties())
# print('All palindrome sentences of a given sentences list:',palindrome_sentences())
# print('Most repeated word on first chapter of Frankenstein:',most_repeated_word())
