# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:55:11 2024

@author: user
"""



#%%
a = 874 
b = 861

print(f"{a**2} + {b**2} =  {a**2 + b**2}")

#%%

string = "nAcUFXTCKXTZeeiuQTnCTJR5fs1bHKNido5hlAWCeratophrysDT90Q4gMkTFBjnHCzIjfX8qEeiboGyvEEFBzbdOp3hbhSkJIZhEdW0WMRRuvXdbrBxF6Kuea8p7BKlvvcWOYKUKn9MxKz6fqo7R2VIDaD4x7T2LPduRaH3KApaganusrd"

start1 = 39 
end1 = 49 

start2 = 170 
end2 = 176

print(f"{string[start1: end1 + 1]} {string[start2 : end2 + 1]}")

#%%
a  = 4893 
b = 9316
result = sum([x for x in range(a,b+1) if x % 2 != 0])
print(result)
#%%
outputfile = []

with open("Python Village\input.txt", "r") as f :
    outputfile = [line for pos, line in enumerate(f.readlines())
                  if pos % 2 == 0]

with open("Python Village\output", "w") as f:
    f.write("".join(line for line in outputfile))

#%%
from collections import Counter
string = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
diction = Counter(string.split(" "))
for k, v in diction.items():
    print(k, v)

    