# During a special pi day of 2015 (March 14th 2015 for 3.1415) pizza hut
# released a challenge. 3 questions. Anyone who got them right would get
# free pizza for 3.14 years thereafter. I saw the questions on the day of
# but was busy. The next day, a brilliant friend of mine answered the first
# question, unfortunately it was too late for him to get the prize. He
# solved it by hand with a friend using the rules for division, such as 
# "if the sum of digits equals 3, the whole number is divisible by 3"
# I think about it often and thought the first question was an easy programming
# challenge. Answers are here:
#
# https://blog.pizzahut.com/national-pi-day-math-problems-solved/

from itertools import permutations


number = '1234567890'
length = len(number)

perms = permutations(number,length)
for p in perms:
  num = ''.join(p)
  # print(num)
  candidate = 1
  n = 1
  while candidate and (n < length+1):
    # print("checking with", n,":   ", (int(num[:n])/n)%1)
    if (int(num[:n])/n)%1 != 0:
      candidate = 0
      break
    n +=1
  if candidate:
    print(f'{num} is a candidate!')
