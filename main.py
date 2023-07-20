from difflib import SequenceMatcher

with open('demo.txt') as one_file, open('demo2.txt') as two_file:
  data_file=one_file.read()
  data1_file=two_file.read()
  matches =SequenceMatcher(None,data_file,data1_file).ratio()
  print(f"The plagiarized content is {matches*100}%")