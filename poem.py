# Python 3.5

def make2gram_probability (seq_of_word):
  # Make Sliding window of 2
  two_words = zip(seq_of_word[:-1],seq_of_word[1:])
  probability_table= {}
  for first,second in two_words:
    # If key doesn't exist, create
    if (probability_table.get(first,0) == 0):
      probability_table[first] = {}
    probability_table[first][second] = probability_table[first].get(second,0) + 1
  for first in probability_table:
    total = sum(probability_table[first].values())
    for word,count in probability_table[first].items():
      prob = float(count)/total
      probability_table[first][word] = prob
    probability_table[first] = (float(total)/(len(seq_of_word)-1),probability_table[first])
  return probability_table

def generate_poem (probability_table,n):
  from random import random
  # pick first word
  r = random()
  picked = ''
  for word,(prob,_) in probability_table.items():
    r = r - prob
    picked = word
    if (r <= 0):
      break
  poem = [picked]
  for i in range(0,n):
    r = random()
    first = poem[-1]
    picked = ''
    try:
      prob,second_table = probability_table[first]
      for word,prob in second_table.items():
        r = r - prob
        picked = word
        if (r <= 0):
          break
      poem.append(picked)
    except Exception as E:
      r = random()
      picked = ''
      for word,(prob,_) in probability_table.items():
        r = r - prob
        picked = word
        if (r <= 0):
          break
        poem.append(picked)
  return poem

def load_words_from_file(filename):
  return None

def main():
  seq_of_word = load_words_from_file(filename)
  prob_table = make2gram_probability(seq_of_word)
  print(generate_poem(prob_table,8))
  return prob_table

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1 # use start += 1 to find overlapping matches

def cut_and_paste_poem (base_poem, seeder, length, cut_length, find_length):
  import random
  poem = seeder
  while len(poem) < length :
    if len(seeder) == 0:
      index = random.randint(0,len(base_poem) - cut_length)
      sentence = base_poem[index:index+cut_length]
      poem += '\n\n' + sentence
      seeder = sentence[-find_length:]
    else:
      all_occurence = list(find_all(base_poem,seeder))
      # Not found anything
      if len(all_occurence) == 0:
        seeder = seeder[1:]
      else:
        index = random.choice(all_occurence) + len(seeder)
        sentence = base_poem[index:index+cut_length]
        poem += sentence
        seeder = sentence[-find_length:]
  return poem


if __name__ == '__main__':
    with open("beowulf.txt",'r') as beowulf:
      poem = beowulf.read()
      print(cut_and_paste_poem(poem,"sun",500,50,1))
    with open("byron-don-juan.txt",'r') as beowulf:
      flatten = lambda l: [item for sublist in l for item in sublist]
      words = flatten([line.strip().split() for line in beowulf])
      prob_table = make2gram_probability(words)
      seq_of_word = generate_poem(prob_table,900)
      continuous_poem = " ".join(seq_of_word)
      formatted_poem = continuous_poem.replace('.','.\n').replace('--','--\n').replace(',',',\n')
      print(formatted_poem)