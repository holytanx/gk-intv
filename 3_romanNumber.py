'''
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Exceptional condition:
- Substraction principle
4 = IV 
9 = IX
XL = 40
XC = 90
CD = 400
CM = 900

'''

roman_map_number = {
  'I': 1, # should not found 5 times
  'V': 5, # should not found twice
  'X': 10, # should not found 5 times
  'L': 50, # should not found twice
  'C': 100, # should not found 5 times
  'D': 500, # should not found twice
  'M': 1000
}
subtract_roman_exception = {
  'IV': 4,
  'IX': 9,
  'XL': 40,
  'XC': 90,
  'CD': 400,
  'CM': 900
}

def get_roman_map_count(input_lst):
  romap_map_count = {}
  for item in set(input_lst):
    if input_lst.count(item) > 1:
      romap_map_count[item] = input_lst.count(item) 
  return romap_map_count

def validate_duplicate(roman_map_count):
  for item in roman_map_count:
    actual_value = roman_map_number[item]
    actual_sum = actual_value * roman_map_count[item]
    if actual_sum in subtract_roman_exception.values() or actual_sum in roman_map_number.values():
      print("Exception: Roman number is wrong format at ", item * roman_map_count[item])
      return False
  return True

def validate_error(sum_lst, input_lst):
  if sorted(sum_lst, reverse=True) != sum_lst:
    print("Exception: Roman number should sort as most value number to least number ", sum_lst)
    return False

  roman_map_count = get_roman_map_count(input_lst)
  if not validate_duplicate(roman_map_count):
    return False
  
  return True

def calculate(input):
  input_lst = [*input]
  sum = []
  prev_char = ''
  prev_index = 0
  for index in range(len(input_lst)):
    char = input_lst[index]
    if char in roman_map_number:
      concat = prev_char + char
      if index > 0:
        if concat in subtract_roman_exception:
          sum[prev_index] = subtract_roman_exception[concat]
        else:
          sum.append(roman_map_number[char])
      else:
        sum = [roman_map_number[char]]
      prev_char = char
      prev_index = len(sum)-1
    else:
      print("Exception: Some character not match to Roman number", input)
      return [0]
  if validate_error(sum, input_lst):
    return sum
  return [0]

if __name__ == "__main__":
  input_roman = input("Roman number: ")
  result = calculate(input_roman.upper())
  print("Result: ", sum(result))



