from functools import reduce
 
# Find highest the frequency of a character in a string 
text = "khanjan is Great python programmer goooddd"

freq = lambda s: max(set(s)-{" "},key=lambda ch: s.count(ch))

print(freq(text))

# Find a factorial of 5 to 10
fact = lambda x: x*fact(x-1) if x != 0 else 1

for i in range(5,11,1):
    print(fact(i))

# Check Palindrome from string 
ispalin = lambda s: s == s[::-1]

print(ispalin("level"))

# List answer  will be second highest
lst1 = [10,20,320,10,430,102,43,500]

second_high = lambda lst: sorted(lst,reverse=True)[1]

print(second_high(lst1))

## Find the LCM of 2 numbers
# first find GCD
gcd = lambda a,b: a if b == 0 else gcd(b,a%b)

lcm = lambda a,b : (a*b) // gcd(a,b)

print("GCD : ",gcd(135,225))
print("LCM : ",lcm(135,225))

# Count a number of vowels in strings  
s = "khanjan is a AI ML engineer"
s2 = "AaEeIiOoUu"

vow = lambda s:sum(map(lambda ch:1 if ch.lower() in "aeiou" else 0,s))

print(vow(s2))

# Find the student with the highest result.(using dictonary)

students = {"Ramu" : 100,"Shamu" : 90,"Tamu" : 25,"Mamu" : 78, "Aura_man" : 100}

find_keys = lambda d,val: [k for k,v in  d.items() if v == val]

find_highest_marks = lambda d: find_keys(d,max(list(d.values())))

print(find_highest_marks(students))


        