#treat file as list
file = open('sonnet_xviii.txt') #relative path

for line in file:
    print(line)



#count lines
file = open('words_small.txt')

count = 0
for line in file:
   count = count + 1

print(count, "lines") 



#count words
file = open('sonnet_xviii.txt')

count = 0
for line in file:
    words = line.split(' ') #space delimiter
    for word in words: #nested loop
        count = count + 1

print(count, "words")



#splitting so we can find all spaces/punctuation
#import regex
import re #for regex
file = open('sonnet_xviii.txt')

count = 0
for line in file:
    # split on regex (not word or ' chars)
    words = re.split("[^\w']+", line)
    for word in words:
      if word != '':
        #print(word)
        count = count + 1

print(count, "words")



#count average line length
file = open('words.txt')

total_ltr = 0
count = 0
for line in file:
    total_ltr = total_ltr + len(line)
    count = count + 1

avg_len = total_letters/count

print("Average word length:", avg_len)



#find a line
file = open('words_huge.txt')

target = input("Word to find: ")

found = False
for line in file:
    if line.strip() == target:
        found = True
    # NO ELSE

if found:
    print(target + " is in the list!")



#don't do this to find lines
file = open('words_small.txt')

target = input("Word to find: ")

found = False
for line in file:
    print("looking at", line)
    if line.strip() == target:
        found = True
    else: #this will keep looking and not print the result
        found = False

if found: #only if found is CURRENTLY TRUE
    print(target + " is in the list!")



#look for a word within a line
file = open('book.txt')
target = input("Word to find: ")

found = False
for line in file:
    if target in line:
        found = True

if found:
    print(target + " is in the list!")



#longest line
file = open('words_huge.txt')

largest = '' #initialize king
for line in file:
    if len(line) > len(largest): #compare to the king
        largest = line

print(largest + " is the largest!")




#all words shorter than n
file = open('words_huge.txt')
max_length = int(input("Max word length? "))

all_short = True
for line in file:
    if len(line) > max_length:
        all_short = False
        break #can leave early

if all_short:
    print("All words short")
else:
    print("A word was long")