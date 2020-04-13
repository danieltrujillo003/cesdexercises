import utils
import random

def ages_aver_without_18():
  ages_list = utils.user_input('Enter an age: ')
  list_without_18 = utils.delete_from_list(ages_list,[18])
  return sum(list_without_18) / len(list_without_18)

def sum_with_for(num_of_values=10):
  sum_of_values = 0
  for num in range(10):
    sum_of_values = sum_of_values +random.randint(0,num)
  return sum_of_values

def height_aver():
  height_list = utils.user_input('Enter a height: ')
  return sum(height_list) / len(height_list)

def count_of_negative_and_positive_numbers():
  values_list = utils.user_input('Enter a value: ')
  total_values = dict(
    negative=0,
    positive=0
  )
  for value in values_list:
    if value <= 0: total_values['negative'] = total_values['negative'] + 1
    if value > 0: total_values['positive'] = total_values['positive'] + 1
  return total_values

def even_odds_and_multiplication():
  odds_list = []
  even_list = []
  multiplication = 1
  for num in range(0,101,2):
    odds_list.append(num)
  for num in range(1,100,2):
    even_list.append(num)
  for num in range(1,101):
    multiplication = multiplication * num
  return dict(odds=odds_list, even=even_list, multiplication=multiplication)

def fibbonacci_sequence(series_length):
  prev, beginning= 0, 1
  count = 0
  series = []
  while count < series_length:
    series.append(prev)
    next_num = prev + beginning
    prev = beginning
    beginning = next_num
    count += 1
  return series

# print('Average of ages without 18 years ones:', ages_aver_without_18())
# print('Sum of 10 numbers using for cycle:', sum_with_for())
# print('Average of heights:', height_aver())
# print('Total of negative and positive numbers from a given set of numbers:', count_of_negative_and_positive_numbers())
# print('Odds and even numbers between 0 to 100 and their multiplication:', even_odds_and_multiplication())
# print('Fibonacci sequence:', fibbonacci_sequence(5))