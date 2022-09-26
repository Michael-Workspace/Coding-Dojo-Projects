#1. print "Hello wolrd"
print("Hello World")

#2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print ("Hello",name)
print ("Hello "+ name)

# 3. print "Hello 42!" with the number in a variable
name = 42
print ("Hello",name)
print ("Hello "+str(name)) #print print ("Hello "+name) will output an error

# 4. print "I love to eat suhi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print ("I love to eat {food_one} and {food_two}".format(food_one="sushi",food_two="pizza"))
print ("i love to eat %s and %s" %(fave_food1,fave_food2))
