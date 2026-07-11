# cube root
value = lambda x: x**(1/3)

print(value(27))

#min of 2 
min = lambda a,b: a if a<b else b

print(min(5,9))

# longest word
Statement = "Today i am attending advance python lecture using lambda function"
large = lambda x: max(x.split(),key=len)
print(large(Statement))

# Write a lambda function to remainder of 2 number
x = lambda a,b: a%b
print(x(10,6)) 

