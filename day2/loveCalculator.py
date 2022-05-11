

print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n").lower()
name2 = input("What is your name?\n").lower()
together_name = name1 +name2
result = 0
t = together_name.count("t")
r = together_name.count("r")
u = together_name.count("u")
e = together_name.count("e")    

l = together_name.count("l")
o = together_name.count("o")
v = together_name.count("v")
e = together_name.count("e")

result =int(str(t+r+u+e)+ str(l+o+v+e))

if (result <10 or result >90):
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result>40 and result <50:
    print(f"Your score is {result}, you are alright together.")
else :
    print(f"Ypur score is {result}")