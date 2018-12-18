# asking name and age
name = input ( "what is your name ")
age = int (input( "what is your age "))
print ("Hello " + name + " you are " + str(age))

# asking if want to know when 100

when_100 = ((2018-age)+100)


question = input ("would you like to know when you become 100?: ")
if question =="yes":
    print ("you become 100 in the year " + str (when_100))
else:
    print ("what a shame")
