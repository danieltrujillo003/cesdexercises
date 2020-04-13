import requests # pip install requests -- it's for handling HTTP requests
import math
import datetime
import constants

def triangle_area():
  base = int(input('Enter triangle base: '))
  height = int(input('Enter triangle height: '))
  return (base * height) / 2

def currency_converter(start='USD', end='COP'):
  amount = int(input('Enter currency value: '))
  conversion = f'{start}_{end}'
  params = {'apiKey': constants.CURRENCY_API_KEY, 'compact': "ultra", 'q': conversion}
  res = requests.get(constants.URL, params=params)
  data = res.json()
  result = amount * data[conversion]
  return result

def temperature_converter(begin='celsius',end='fahrenheit'):
  value = int(input('input temperature value: '))
  convert_factor = f'{begin}_to_{end}'
  conversions = {
    'celsius_to_fahrenheit': (value * 9/5) + 32,
    'celsius_to_kelvin': value + 273.15,
    'fahrenheit_to_celsius': (value - 32) * 5/9,
    'fahrenheit_to_kelvin': (value - 32) * 5/9 + 273.15,
    'kelvin_to_celsius': value - 273.15,
    'kelvin_to_fahrenheit': (value - 273.15) * 9/5 + 32
    }
  if convert_factor in conversions:
    return conversions[convert_factor]
  else:
    return f'Cannot convert {begin} to {end}.'

def convert_to_seconds(unit='lustrum'):
  if unit in constants.TIME_VALUES:
    return constants.TIME_VALUES[unit]
  else:
    return f'{unit} unit is not supported.'

def seconds_sun_to_planet(planet='mars'):
  return constants.SUN_DISTANCE_TO[planet] * 1000 / constants.LIGHTSPEED

def num_of_wheel_turns(distance=1,wheel_diameter=50):
  return (distance * 1E5 / wheel_diameter * math.pi)

def compute_shadow_length(object_height=20, sunray_angle=22):
  return (object_height / math.sin(math.radians(sunray_angle)))

def compare_two_ages():
  age1 = input('age 1: ')
  age2 = input('age 2: ')
  if age1 == age2:
    return True
  else:
    return False

def compute_months_since_birthday():
  year_then = int(input('birthday year: '))
  month_then = int(input('birthday month: '))
  year_now = int(datetime.date.today().year)
  month_now = int(datetime.date.today().month)
  return ((year_now - year_then) * 12 + (month_now - month_then))

def subjets_aver(): # Isn't there an aver() function?
  courses = dict(
    spanish = int(input('spanish grade: ')),
    math = int(input('math grade: ')),
    economics = int(input('economics grade: ')),
    prog = int(input('prog grade: ')),
    english = int(input('english grade: '))
    )
  grades = (courses.values())
  rounded_aver = round(sum(grades) / len(grades),2)
  return rounded_aver


print('Triangle area:',triangle_area())
# print('Dollars to colombian peso:',currency_converter())
# print('Celsius to Fahrenheit:',temperature_converter())
# print('Amount of seconds un a lustrum:',convert_to_seconds())
# print('Seconds for light from Sun to Mars:',seconds_sun_to_planet())
# print('Turns of a 50cm diameter wheel in 1km:',num_of_wheel_turns())
# print('Lenght of a 20m building shadow with a 22° sunray:',compute_shadow_length())
# print('Are the ages the same?:',compare_two_ages())
# print('Amount of months since birthday:',compute_months_since_birthday())
# print('Average of subjects:',subjets_aver())
