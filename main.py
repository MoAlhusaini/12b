name =input("what is your name?")
print("hello", name.capitalize(),"i will solve your quadratic")
a = float(input("what is your a in your quadratic ax^2+bx+c=0"))
b = float(input("what is your b in your quadratic ax^2+bx+c=0"))
c = float(input("what is your c in your quadratic ax^2+bx+c=0 "))
formula = b**2 - 4*a*c
ex1 =  (((-b) - (formula**0.5)) / (2 * a))
ex2 = (((-b) + (formula**0.5) )/ (2 * a))
print("thank you", name.capitalize(),"the roots are", ex1,"and", ex2)
quit()