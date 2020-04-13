def delete_from_list(original_list, list_of_items_to_delete):
  for item in list_of_items_to_delete:
    while item in original_list:
      original_list.remove(item)
  return original_list

def find_in_dict_by_value(original_dict, value_to_find, key_or_tuple='tuple'):
  for key, value in original_dict.items():
    if value == value_to_find:
      if key_or_tuple == 'key':
        return key
      elif key_or_tuple == 'tuple':
        return (key,value)
      else:
        return "Must select between 'key' or 'tuple'"

def user_input(text_to_show, isInt=True):
  values_list=[]
  another='y'
  while another=='y':
    values_list.append(int(input(text_to_show)) if isInt else input(text_to_show))
    another = input('Another value? (y/n) ')
  return values_list