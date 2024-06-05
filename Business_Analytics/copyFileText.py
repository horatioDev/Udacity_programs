# Get correct input type --------------------------------------------------
# Get Integer Input
def get_integer_input(prompt):
  while True:
    try:
      value = int(input(prompt))
      return value
    except ValueError:
      print("Invalid input. Please enter a valid integer.")

# Get Positive Integer Input
def get_positive_integer_input(prompt):
  while True:
    try:
      value = int(input(prompt))
      if value <= 0:
        print("Please enter a positive integer.")
      else:
        return value
    except ValueError:
      print("Invalid input. Please enter a valid positive integer.")

# Get Float Input
def get_float_input(prompt):
  while True:
    try:
      value = float(input(prompt))
      return value
    except ValueError:
      print("Invalid input. Please enter a valid float.")

# Get Positive Float Input
def get_positive_float_input(prompt):
  while True:
    try:
      value = float(input(prompt))
      if value <= 0:
        print("Please enter a positive float.")
      else:
        return value
    except ValueError:
      print("Invalid input. Please enter a valid positive float.")

# Get String Input
def get_string_input(prompt):
  while True:
    try:
      value = str(input(prompt))
      if value == '':
        value = None
      return value
    except ValueError:
      print("Invalid input. Please enter a valid string.")

# Copy contents of one file to another
# source_file = get_string_input('Enter source file: ')
# destination_file = get_string_input('Enter destination file: ')
source_file = './s.txt'
destination_file = './delete.txt'
print(f'Source File: {source_file}')
print(f'Destination File: {destination_file}')
print('-'*30)

# Sentence-ize functions
def sentence_maker(txt):
  # Hold sentences in array
  sentences = []
  start = 0

  # Find all periods etc, then split on those indices into an array
  for i in range(len(txt)):
    end = i
    if txt[end] in ('.', '!', '?') and (end == len(txt) - 1 or txt[end+1] == ' '):
      sentence = txt[start:end+1].strip()
      sentences.append(sentence)
      # Skip the space after punctuation
      start = end + 2

      # return sentence # 1st sentence  
  # return sentence # last sentence
  return sentences # All sentences

# Open and read source from file
with open(source_file, 'r') as source:
  text = source.read()
  # Wite to destination file
  with open(destination_file,'w') as destination:
   word_count =  len(text.split())
   sentences = sentence_maker(text)
   print('File copied successfully!')
   print(f'Word count: {word_count}')
   
   count = 0
   for sentence in sentences:
     count += 1
     destination.write(sentence)
     print(f'Sentence {count}: {sentence}')
