URL = "https://free.currconv.com/api/v7/convert"

currency_api_key = "1eee96803fea247c8118" # https://free.currencyconverterapi.com/

time_values = {'second': 1}
time_values['minute'] = time_values['second'] * 60
time_values['hour'] = time_values['minute'] * 60
time_values['day'] = time_values['hour'] * 24
time_values['week'] = time_values['day'] * 7
time_values['year'] = (time_values['day'] * 365) + (time_values['hour'] * 6)
time_values['lustrum'] = time_values['year'] * 5
time_values['decade'] = time_values['year'] * 10
time_values['century'] = time_values['year'] * 100

lightspeed = 299792458 # m/s

sun = { #km
  'mercury': 57.91E6,
  'venus': 108.2E6,
  'earth': 149.6E6,
  'mars': 227.9E6,
  'jupiter': 778.5E9,
  'saturn': 1.434E9,
  'uranus': 2.871E9,
  'neptune': 4.495E9,
}
