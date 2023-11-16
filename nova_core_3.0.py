# Nova V1.0

# #1 Programming language designed for humans

# Creating #1 coding language that is 100% light years ahead of all existing languages, that can do all yet very easy to understand,powerful, versatile, safe and secure, highly scalable, supports 32 bits and 64 bits computing, + more.


# Adding comments
=====================

#               # For adding single line comments.

#*  *#     # For adding multi lines comments.

# Data Types
===================

 bit                # A 0 or 1

 number     # A whole number like 5, 60, 39...

 decimal     #  A number with decimal like 5.35, 10.123, 99.9...

 text            #  Letters, words, and characters like "Hi there"

 yn                #  To check value is equal to yes or no  ( boolean ).

 Lists            #  Store ordered collections of data.

 sets             #  Store unordered collections of data.

 Tuple          #  Store ordered collections of data.

 Maps          #  Store unordered collections of key-value pairs data.

 Shape        #  To store shapes data, like circle, square, rectangle, etc.

 # Defining bit data type
=====================

  0  bit     # Example

# Defining number data type
=====================

  0  number     # Example

# Defining decimal data type
=====================

  0.5  decimal     # Example

 # Defining text content ( string )
===========================
# A string data will convert all the content inside the colon into a string or just text.

text:Hello!:  #Single line text content (string)

text::Hello!::  #Mutiline line text content (string)

# Defining yn  data type ( yes or no )
==============================
# Can be yes or no values only.
# Used for conditional logic ( if, else, repeat, while, etc. )
# Work with yn or yn tools (operators)  like AND, OR, NOT etc.

 yes   # yes yn value  (boolean value)

 no    # No yn value  (boolean value)

# Defining list data type
=====================
# A list is an ordered collection of data.
#1: To store user data like name, age, email, etc.
#2: To store product data like name, price, quantity, etc.
# What is the specific purpose of lists over maps data type?
#We can access the data using the index number, so it's easy to access any data using the index number.

list:  # Keywrord to make a single line list.

list::  # Keyword to make a multiline list.

# To create new list: Defining a list with some data.

set fruits = list:apple, banana, orange:    

print fruits   # It will print as a list ( apple, banana, orange ).

# To create a new list: Defining a list with some data in multiline.

set fruits = list::apple, 
banana, 
orange
::

print fruits   # It will print as a list ( apple, banana, orange ).

# Access element using the index number ( index number starts from 0 ).

print(fruits[0])   # It will print (apple )
print(fruits[1], [2],[3] )   # It will print (apple, banana, orange).

# Add item to end of the list ( append ).

add    # Keyword to add item to end of the list.

add fruits, text:mango: 

# List length ( number of items in the list ). 
print(length fruits)  # 3

# Remove item

remove  # Keyword to remove item from list.

remove fruits, 1  # Removes banana

# List of lists
set number_rows = list::
  list:1, 2, 3:, 
  list:4, 5, 6:
::

print number_rows  # It will print as a list ( list:1, 2, 3:, list:4, 5, 6: ).

# repeating (looping) through a list

  set games = list:chess, carrom, ludo:    # Defining a list with some data.

 repeat games as game_name {   # here we are setting a variable named :game_name : to each games in the list to access the games name/data one by one.
    
    print(game)   # It will print 3 times one by one:  chess, carrom, ludo.

  }


# Defining sets data type ( To store unordered collections of data. )
================================================================
set:  # Keyword to make a single line set.

set::  # Keyword to make a multiline set.

# To create new set: Defining a set with some data.

set fruits = set:apple, banana, orange:

print fruits   # It will print as a set ( apple, banana, orange ).

# To create a new set: Defining a set with some data in multiline.

set fruits = set::apple,

banana,

orange::

print fruits   # It will print as a set ( apple, banana, orange ).

# Add item to set

add    # Keyword to add item to set.

add fruits, text:mango:

# Set length ( number of items in the set ).

print(length fruits)  # 4

# Remove item

remove  # Keyword to remove item from set.

remove fruits, banana

# repeating (looping) through a set

  set games = set:chess, carrom, ludo:    # Defining a set with some data.

 repeat games as game_name {   # here we are setting a variable named :game_name : to each games in the set to access the games name/data one by one.
    
    print(game)   # It will print 3 times one by one:  chess, carrom, ludo.

  }

# Check if item exists in set

set  fruits = set:apple, banana, orange:    # Defining a set with some data.
   
  if orange in fruits{   # It will check whether orange is in the set or not.

    print("Orange is in the set")  # It will print ( Orange is in the set ).
  
  else:

  print("Orange is not in the set")  # It will print ( Orange is not in the set ).

  }


# Defining tuple data type ( To store ordered collections of data. )
================================================================
# A tuple is an ordered collection of data.
# What is the specific purpose of tuples over lists?
#We can't change the data in the tuple, so it's safe to use it for storing data that should not be changed.
#1: To store user data like name, age, email, etc.
#2: To store product data like name, price, quantity, etc.

tuple:  # Keyword to make a single line tuple.

tuple::  # Keyword to make a multiline tuple.

# To create new tuple: Defining a tuple with some data.

set fruits = tuple:apple, banana, orange:

print fruits   # It will print as a tuple ( apple, banana, orange ).

# To create a new tuple: Defining a tuple with some data in multiline.

set fruits = tuple::apple,

banana,

orange::

print fruits   # It will print as a tuple ( apple, banana, orange ).

# Access element using the index number ( index number starts from 0 ).

print(fruits[0])   # It will print (apple )

print(fruits[1], [2],[3] )   # It will print (apple, banana, orange).

# Add item to tuple

add    # Keyword to add item to tuple.

add fruits, text:mango:

# Tuple length ( number of items in the tuple ).

print(length fruits)  # 4

# Remove item

remove  # Keyword to remove item from tuple.

remove fruits, banana

# repeating (looping) through a tuple

  set games = tuple:chess, carrom, ludo:    # Defining a tuple with some data.

 repeat games as game_name {   # here we are setting a variable named :game_name : to each games in the tuple to access the games name/data one by one.
    
    print(game)   # It will print 3 times one by one:  chess, carrom, ludo.

  }

# Check if item exists in tuple

set  fruits_set = tuple:apple, banana, orange:    # Defining a tuple with some data.
   
  if orange in fruits_set{   # It will check whether orange is in the tuple or not.

    print("Orange is in the tuple")  # It will print ( Orange is in the tuple ).
  
  else:

  print("Orange is not in the tuple")  # It will print ( Orange is not in the tuple ).

  }


# Defining map data type ( To store any data that has key-value pairs. )
================================================================
# A map is an unordered collection of key-value pairs data.
# What is the specific purpose of maps over list?
#We can access the data using the key name but not the index number, so it's easy to access any using the key name (keyword).
#1: To store data that has : key-value pairs, no order, no index numbers, no duplicates,  no length, no insert option (append), no remove option, no pop, no sort,  no reverse, no count, no index. 
#2: To store user data like name, age, email, etc.
#3: To store product data like name, price, quantity, etc.

map:       # Keyword to make a single line map.

map::     # Keyword to make a multi line map.

#  Create new map: Defining a map with key-value pairs data in single line.

map: key1: value1, key2: value2, key3: value3

set ages = map:bob: 20,alice: 30: john: 40:  #  Defining a map with key-value pairs data in a variable ( In single line ).

print ages  # It will print as a map ( bob: 20, alice: 30, john: 40 ).

#  Create new map :  Defining a map with key-value pairs data in multi line

map:: key1: value1, key2: value2, key3: value3 
key4: value4, key5: value5 
::

set ages = map::bob: 20,
alice: 30,
 john: 40
 :: 

print ages   # It will print as a map ( bob: 20, alice: 30, john: 40 ).

# Access element using the key name ( keyword ).

print(ages[bob])   # It will print (20 )

print(ages[alice])   # It will print (30)

print(ages[bob], [alice],[john] )   # It will print (20, 30, 40).

# Check if key exists in map ( boolean value  ).

exists  # Keyword to check whether the key exists in the map.

if (exists ages[bob]) {

  print(text: bob exists:)   # It will print ( bob exists ).

  else {

    print(text: bob does not exist:)   # It will print ( bob does not exist ).

  }

}

# Map length ( number of items in the map ).

print(length ages)  #  3

# Add new key-value pair to map

add  # Keyword to add new key-value pair to map.
[ ]      # Square brackets to add new key-value pair to map.

add ages, key: value   # Adds key: value to ages map.
add ages, dave: 40    # Adds dave: 40 to ages map.

# Update key-value pair in map

set  # Keyword to update key-value pair in map.

set ages[dave] = 40  # Adds dave: 40 to ages map, same as above.

print ages   # It will print as a map ( bob: 20, alice: 30, john: 40, dave: 40 ).

# Map of maps

set school = map::

  bob: map: grade: 6, gpa: 3.5 :,  #  Defining a map with key-value pairs data in a variable ( In single line ).
  alice: map: grade: 5, gpa: 3.8:
::

print school  # It will print as a map ( bob: map: grade: 6, gpa: 3.5 :, alice: map: grade: 5, gpa: 3.8: ).

# Access element using the key name ( keyword ).

print(school[bob])   # It will print (map: grade: 6, gpa: 3.5 : )
print(school[bob], [alice] )   # It will print (map: grade: 6, gpa: 3.5 :, map: grade: 5, gpa: 3.8: ). # Access element using the key name ( keyword ).

# Remove key-value pair from map

remove  # Keyword to remove key-value pair from map.

remove ages, bob       # Removes bob: 20
remove ages[alice]    # Removes alice: 30   ( same as above )

print ages  # It will print as a map ( john: 40, dave: 40 ).

# repeating (looping) through a map

  set ages = map:bob: 20,alice: 30: john: 40:  

 repeat ages as age {   # here we are setting a variable name : age : to each age in the map to access the ages data one by one.
    
    print(age)   # It will print 2 times one by one:  bob: 20, alice: 30.

  }

# Defining shape data type ( To store shapes data, like circle, square, rectangle, etc. )
================================================================
# A shape is an unordered collection of key-value pairs data.

shape:       # Keyword to make a single line shape.

shape::     # Keyword to make a multi line shape.

move         # Keyword to update the shape variables data.

#  Create new shape: Defining a shape with key-value pairs data in single line.

shape Circle {
  radius: number,
  color: string,
  x: number,
  y: number
}

shape Rectangle {
  width: number,
  height: number,
  color: string,
  x: number,
  y: number 
}

set c = Circle(10, "red", 20, 30) 

c.radius = 5        # error, radius is immutable

print c.radius   # It will print 10.

c.move(5, 10)   #  Updates ( mutates ) shape varible data (  x and y ).

print c.x, c.y   # It will print 5, 10. 

#  Create new shape :  Defining a shape with key-value pairs data in multi line

shape:: Circle {
  radius: number,
  color: string,
  x: number,
  y: number
}

shape:: Rectangle {
  width: number,
  height: number,
  color: string,
  x: number,
  y: number 
}

set c = Circle(10, "red", 20, 30)

c.radius = 5        # error, radius is immutable

print c.radius   # It will print 10.

c.move(5, 10)   #  Updates ( mutates ) shape varible data (  x and y ).

print c.x, c.y   # It will print 5, 10.

# support pattern matching to extract data from shapes
=========================
#*  Pattern matching is a feature that allows you to check the shape of a value and extract data from it while simultaneously checking its type. *#

match c {
  Circle(radius, color, x, y) => print(radius, color, x, y)   # It will print 10, red, 20, 30.
  Rectangle(width, height, color, x, y) => print(width, height, color, x, y)  # It will not print because it's not a rectangle.
}

 match area(c) {
  match c,  {
    Circle r -> PI * r * r            # It will print 314.1592653589793.
    Rectangle w, h -> w * h  # It will not print because it's not a rectangle.
  }
}



# Generics
===========
# Generics are used to write code that works with any type:
# Generics are useful for writing reusable code.

# Example
task map<T>(list: List<T>, task(T)) -> List<T> {

  #map implementation

}

map([1, 2, 3], task(x) {  

  return x * 2   # 2, 4, 6

})

# This will generate:

task map(list: List<number>, task(number)) -> List<number> {
  
  #map implementation

}

map([1, 2, 3], task(x) {  

  return x * 2  # 2, 4, 6

})

# This will generate:
task map(list: List<text:>, task(text:)) -> List<text:> {

  #map implementation

}

map(["a", "b", "c"], task(x) {  

  return x + "!"  # a!, b!, c!

})

# This will generate:
task map(list: List<Person>, task(Person)) -> List<Person> {
  #map implementation
}


# Actions
=========================

 =   # Put/save, set, update value into a variable.

 +    # To Add  anything ( numbers, text, etc. )

  -    # To Subtract numbers

  *    # To Multiply numbers

  /      # To  Divide numbers

  %   # To get the remainder of dividing numbers ( Modulus ).

# Comparision tools  (operators)
=========================

# Comparing and checking whether both side data are equal.

   == 

 5 == 5   # checks whether 5 equals 5, it will return yes.

# Checks whether both side data are not equal.

    !=             

   5 != 5      # checks whether 5 is not equals to 5, it will return no.

#* Checks  whether the left side data is greater than the  right side data. *#

    >             

    10 > 5     # checks whether 10 is greater than 5, it will return yes.

#* Checks  whether the left side data is lesser than the right side data.  *#

     <            

     10 < 5     # checks whether 10 is lesser than 5, it will return no.

#* checks  whether the left side data is equal or greater than the right side data. *#

    =>          

    6 => 5   # checks whether 6 is equal or greater than 5, it will return yes.

  #* checks  whether the left side data is equal to or lesser than the right side data. *#

     =<          

     6 =< 5    # checks whether 6 is equal or lesser than 5, it will return no.



#  Decision making tools
=========================
#  Decision making tools are used to make decisions based on the conditions that we define.

   if                          # Check & do this if condition is true.

  else                     # Otherwise do this.

  repeat               # Do this multiple times.

  while                 # Keep doing this while condition is true.

  stop                   # Stop repeating or while loop.

  skip                    # Skip to next repeat.


#  if  decision making example
==========================

  return    # Keyword to get the result and stop the task/program.

  print    # Keyword to show/print anything, it can be a result or variable.

   if (10 == 5) {

      print(text: 10 is equal to 5:)   # It will not print because 10 is not equal to 5.

  }

  if (10 == 10) {

  return    # It will return the result and stop the task.
  print(text: 10 is equal to 10:)   # It will print because 10 is equal to 10.

}

#  else  decision making  example
============================
  if (10 == 5) {

      print(text: 10 is equal to 5)   # It will not print because 10 is not equal to 5.

  }

  else {

   return    # It will return the result and stop the task.
   print(text: 10 is not equal to 5)   # It will print because 10 is not equal to 5.

}

#  repeat  decision example (loop)
============================

  repeat (5) {    # Repeat 5 times.

    print(text: Hello:)   # It will print 5 times :  Hello, Hello, Hello, Hello, Hello.

  }

  #  repeat  example (loop) with list

    set  fruits = list:apple, banana, orange:    # Defining a list with some data.

   repeat  fruits as fruit {        # here we are setting a variable name : fruit : to each fruit in the list to access the fruits data one by one.
    
    print(fruit)   # It will print 3 times one by one:  apple, banana, orange.

  }


  #  while  decision example (loop)
==============================
# while  loop will keep doing the task until the condition is true.

   set  mango = 0  number  # Defining a variable with a value.

   while (mango < 5) {    # Keep doing this while count is less than 5.

    print mango   # It will print 5 times ( 0, 1, 2, 3, 4 ).

    mango = mango + 1   # Adding 1 to mango variable.

  }

  #  stop  decision example
=======================
# stop  will stop the while loop when the condition is true.

  set  orange = 5  number  # Defining a variable with a value.

   while (orange < 10) {    # Keep doing this while count is less than 10.

    print orange  # It will print 5 times ( 5, 6, 7, 8  ).

    orange = orange + 1   # Adding 1 to orange variable.

    if ( orange == 8) {

      stop    # It will stop the while loop when count is equal to 8.

    }

  }

  #  skip  decision example
========================
# skip  will skip to next repeat when the condition is true.

  set  jackfruit = 8   number  # Defining a variable with a value.

  repeat (jackfruit) {    # Repeat 10 times.

    print(jackfruit)   # It will print 10 times ( 0, 1, 2, 3, 4, 5, 6, 7, ).

    jackfruit = jackfruit + 1   # Adding 1 to count variable.

    if (jackfruit == 7) {

      skip    # It will skip to next repeat when count is equal to 7.

    }

  }


# yn  - yes or no (  keyword to check  boolean value ) 
============================================

  yn    # Keyword to check yes or no value

#  yn variables ( boolean variables  ) 
==============================

admin?                           # yn variable name

yn admin? = yes         # Saving/setting a value of : yes

yn logged_in? = no   #*  Saving value : no :  to : logged_in? : yn variable.  *#

#  yn -  yes or no ( boolean expressions  ) 
==================================

#* Using  :  if  :  condition to check whether : admin? :  value is  yes or no. * #

if (admin?) {

  # show admin section

}

# Checking whether  : logged_in? :  value is equal to no #

==     # Keyword to check whether both sides are equal.

if (logged_in? == no) {

  # show login form

}

# yn tools  (boolean operators)
===========================

and     #  Both side should be yes.

or         #  Any side can be yes.

not      # To set not equal to.

 #  OR (operator )  Checking whether yes or no on both sides.

 yn boy? = yes

yn girl? = no

 yn baby? = (boy? or girl?)    #  Checking whether yes or no on both sides, it will print yes, because one side is yes. 

 print baby?   #  It will print yes.


# AND  (operator ) 

 yn has_permission? = (admin? and  logged_in?)    #  Checking whether yes or no on both sides, if both sides are yes then it will print yes, otherwise it will print no.

yn milk? = yes

yn tea_leafes? = yes

 yn tea? = (milk? and tea_leafes?)      # Only when both sides are yes we can have tea, otherwise we can't have tea.

print tea?   # It will print yes, because both sides are yes.


# NOT (operator ) 

  !=    #  Keyword for checking with not equal to.

 set  apple = 5
 set mango = 10

yn apple != mango   # Checking whether apple is not equal to mango, we will get yes, because apple is not equal to mango.

yn 7 != 10      #  7 is not equal to 10,  so it will return yes.

print 7 != 10   # ( 7 is not equal to 10 so it will print yes ).

yn logged_in? = yes     # Setting value : yes : to : logged_in? : yn variable.

yn  guest != logged_in?   # Checking whether guest? is not equal to logged_in?

print guest != logged_in?   # It will print no, because guest is equal to logged_in?.


# Variables
===========

#*  Variables value can be changed ( We can read, write and update the value in realtime ). *#
#*  Variables can have any pre defined data type, like number, text, yn, list, map, etc. *#

# By default variable data is unchangeable ( immutable ) in Nova.

Set             # Keyword to save a changeable value for  later use.

mutable    # Keyword to update/change  the variable value in realtime. 

mango       # We are defining a variable name: mango :  to save a changeable value.

Set mango= 0    #  Saving a changeable value  : 0 :

set mango = 1    #  variable value can't be changed (immutable).

 mutable  mango = 1    #  Can be changed the data/vlaue again and again ( realtime ).

 mutable  mango = 2    #  Can be changed the data/vlaue again and again.

 #  Variables can have any pre defined data type, like number, text, yn, list, map, etc.
 # Why we need to define data type for variables ?
  # To avoid confusion between the names of variables and constants.
  # To avoid errors while using the variables.
  
  set apple = 10 number

  set  grapes =  20.5 decimal
  
   set  banana =  20 text

    set  nutts? =    yes yn

   set  fruits = list:apple, banana, orange:  list

    set  fruits = map:apple: 10, banana: 20:  map

#  Accessing variable value.

print mango   # It will print 2, because we have updated the value to 2.


# Constants 
============

# Value can't be changed ( read-only, you can not update in real-time  ). #
# Full CAPS letters to define, save, and use an un-changeable value.
# Using FULL_CAPS letters to avoid confusion between the names of variables and constants.

CONST          # Keyword to save a un-changeable value.

MAX_SIZE    # we are defining a constant name to save a un-changeable value.

CONST MAX_SIZE = 100    #  Saving a un-changeable value  :100:

# Constants can have any pre defined data type. 
  
  CONST STUDENT _NAME text = "John"  #  Saving a un-changeable value  :John:

  print STUDENT_NAME   # It will print John.


# Task ( Function ) 
================

Task       # keyword to define a function.

Do          # keyword to call a function.

return   # keyword to get the task result/return.

print      # keyword to show/print anything, it can be a result or variable.

  # Defining a  task ( function )
=========================

  set apple number

  set banana number

Task add_fruits {

  set c number

  c  =  apple+banana

  return  c  #  Returning the result, 

  print c

}

# Calling a  task ( function )

Do add_fruits (10, 20)   # Calling a task ( function ) with values.


# Ingredients ( Parameters )
========================
#Pass data/values to a task (function) during the call.
#Receive data/values from a task (function) during the call.
#Act like variables, storing values/data within the task.
#Different functions can have different ingredients.
#Same ingredients in different functions save data/values based on the task name.
#Can have pre-defined data types.
#Can have default values.
#Serve new data/values during the call; default values used if not served.


# Defining the input ingredients ( parameters )
=========================================

# 1st way : Defining input ingredients without default values assigned, but defining the values/data while calling the task.

Task add_fruits (apple, mango, banana) {

  set total number

    total  =  apple + mango + banana

  return total  #  Returning the result, it will return 39.
  
  print total    # It will print 39.

}

Do add_fruits (10, 20, 9)

# 2nd way:  Defining input ingredients with default values assigned.

Task add_fruits (apple = 9, mango =10, banana = 15) {

  set total number

  total  =  apple + mango + banana

  return total  #  Returning the result, it will return 39.
  
  print total    # It will print 39.

}

# Serving new values/data while calling the task.

Do add_fruits (10, 20, 9)

#* 3rd way: Defining input ingredients with default values and it's data types assigned ( Safe way error less )  *#

Task add_fruits (apple = 9 number, mango =10 number, banana = 15 number) {

  set total number

   total  =  apple + mango + banana

  return total  #  Returning the result, it will return 39.
  
  print total    # It will print 39.

}

# Serving new values/data while calling the task.

Do add_fruits (10, 20, 9) 

#*  4th way : Defining default values for some ingredients and not defining for some ingredients. * #

# Let's say two ingredients we need for a task, we can set a default value for both or any one of the ingredient, so we can serve any type of data/value for the undefined one. 


 Task add_fruits ( stock_available? yn, mango = 9 number, banana = 6 number) {

  set total number

   total  = stock_available?, mango + banana

  return total  #  Returning the result, it will return yes, 39.
  
  print total    # It will print yes, 39.

}

# We are also using a yn data type

Do add_fruits ( yn stock_available? = yes, 20, 7)


# Wrong way  to define or call a task.
===============================

#*  If you did't set any default value for ingredients, and also if you don't set/serve values while calling a task, it would result in error.  *#

#*  Example: Defining the input ingredients without any values typed (assigned/saved).  *#

Task add_fruits (apple, mango, banana) {

  set total number

  total  =  apple + mango + banana

  return total  #  Returning the result, it will return 39.
  
  print  total    # It will print 39.

}

Do add_fruits (apple, mango, banana)   

# There is no default values are set for ingredients so calling without any values will result in error.

#  If already default ingredients values are set calling this way would work, otherwise you will get an error.

Do add_fruits   # Missing ingredients name or vaule.

# Calling without any ingredients name and calling without any values being passed for existing ingredients would result in error.

Do add_fruits ()   # Missing ingredients name or value.


# Static Optional Typing
=======================
#*  Static optional typing is a feature that allows you to specify the type of a variable or function parameter. *#
# It's optional, you can use it or not, it offers more safety and security, better for bug free coding.

# Defining the input ingredients ( parameters ) with data types assigned.
# Also we are defining the return type of the task ( function ). ( This is the difference between static optional typing and dynamic typing ).

# The key aspects:

x=5 number       # declare the variable type 

y=10 number    # declare the ingredient types

-> number         # Declares the return type of the function/task.

Task cool (x= 5 number, y= 10 number ) -> number {
  return x + y # 15
}

print cool(5, 10) # 15


# Math features built in.
=========================

# Addition 
Task add(10, 20) {

  return 10 + 20

}

do add   # This will print 30

print   # This will print 3

# Subtraction
Task subtract(a, b) {
  return a - b  # a = 5, b = 2
}

print subtract(5, 2)   # This will print 3

# Multiplication
Task multiply(a, b) {
  return a * b # a = 2, b = 3

}

 print multiply(2, 3)   # This will print 6

# Division
Task divide(a, b) {
  return a / b  # a = 6, b = 2
}

print divide(6, 2)   # This will print 3

# Exponentiation
Task power(base, exponent) {
  return base ^ exponent  # base = 2, exponent = 3

}

print power(2, 3)   # This will print 8

# Square root
Task sqrt(a) {
  return a ^ 0.5  # a = 9
}

print sqrt(9)   # This will print 3

# Absolute value
# What it does: It calculates the absolute value of a number.
Task abs(a) {
  if a < 0 {
    return -a   #this will return 5
  } else {
    return a  # Ths will return 5
  }
}

print abs(-5)   # This will print 5

# Modulo
Task mod(a, b) {
  return a % b
}

print mod(5, 2)   # This will print 1

# Basic Arithmetic Operations
print(abs(-5))       #  5 
print(max(1, 3))    #  3
print(min(4, 2))    #  2

# Powers 
print(pow(2, 3))    # 8 

# Roots 
print(sqrt(9))    # 3

# Logarithms 
print(log(10))    # 1
print(log2(8))    # 3 

# Trigonometry 
print(sin(45))      # 0.707
print(cos(180))  # -1

# Random 
set num = random(1, 10)   #Random between 1-10

# Rounding 
print(round(3.14159))   #  3 
print(ceil(3.7)) // 4    #  4 

print(floor(3.7))   # 3 

# Statistics 
set nums = list:1.1, 2.2, 3.3: 

print(mean(nums))    # 2.2
print(median(nums))  # 2.2

# Calculate standard deviation, variance, and covariance, and more.
# What it does: It calculates the standard deviation of a sample of data.

print(stdev(nums))    # 1.1

   # example: 
   
   1.1, 2.2, 3.3   # 1.1 is 1.1 away from the mean of 2.2, 2.2 is 0 away from the mean, and 3.3 is 1.1 away from the mean. 

 # Get data histogram, and more.
# What it does: It calculates the histogram of a sample of data.

set hist = histogram(data)    # 1.1

  # example

    1.1, 2.2, 3.3   # 1.1 is 1.1 away from the mean of 2.2, 2.2 is 0 away from the mean, and 3.3 is 1.1 away from the mean.


# Numerical Analysis
=======================
# What it does: It calculates the numerical analysis of a sample of data.
# Calculate the numerical analysis of a sample of data.

set nums = list:1.1, 2.2, 3.3:

# Definite integral
# What it does: It calculates the definite integral of a function.

print(integrate(f(x), 1, 10))  # Definite integral , it will print 385.0

#example: 

set f(x) = x ^ 2

print(integrate(f(x), 1, 10))  # Definite integral , it will print 385.0

# Linear least squares
# What it does: It calculates the linear least squares of a sample of data.

set coeffs = lstsq(A, b)  

# example

set A = matrix:1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10:

set b = vector:1, 2, 3, 4, 5, 6, 7, 8, 9, 10:

set coeffs = lstsq(A, b)

print(coeffs)  # It will print 1.0, 1.0

# Decimal Precision
====================
# What it does: It sets the decimal precision of a number.

set decimal_precision(4) 

print(3.14159)  # 3.1416 rounded to 4 places  

# Math Constants
=================
CONST PI = 3.14159265358979323846
CONST E = 2.71828182845904523536
CONST INF = 1.0 / 0.0      #Infinity
CONST NAN = 0.0 / 0.0   # Not a number

print(PI)    
print(E * E)   # 7.3890560989306495

# Minimum of values
==================
print(min(1, 2, 3))  # 1

# Maximum of values  
===================
print(max(1, 2, 3))  # 3  

# Absolute value
================
print(abs(-5)) # 5

# Power 
=========
print(pow(2, 3))  # 8

# Square root
==============
print(sqrt(9))  # 3

# Round to nearest integer   
===========================
print(round(3.14))  # 3

# Round up
=============
print(ceil(3.7))  # 4

# Round down
===============
print(floor(2.1))  # 2

# Exception Handling
====================

set x = 1 / 0  

     # Triggers divide-by-zero exception

try:
  dangerous_operation() 
catch:

  #Handle exception
  print(text: An error occurred) 

# Bitwise Operators
====================
set bits = 1024 | 64 | 8     # Bitwise OR
print(~0b1100)                   #  Bitwise NOT 

# Utility Functions 
====================

print(clamp(5, 0, 10))     # 5
print(clamp(15, 0, 10))   # 10 

set y = lerp(1, 5, 0.5)   # Linear interpolate  

# Complex Numbers
=================
set c = complex(2, 3)   # 2 + 3i

print(c.real)  # 2
print(c.imag)  # 3 

print(abs(c)) // sqrt(4 + 9) = 3.605551275463989

# Matrices
=================
set A = matrix:1, 2, 3: 4, 5, 6: 7, 8, 9:

set B = matrix:1, 2, 3: 4, 5, 6: 7, 8, 9:

print(A + B)     # Matrix addition

print(A * B)     # Matrix multiplication

print(A ** 2)   # Matrix power

print(A.T)         # Matrix transpose

print(A.I)          # Matrix inverse

print(A.det)    # Matrix determinant

print(A.eig)     # Matrix eigenvalues

print(A.eigv)   # Matrix eigenvectors

# Vectors
=================
set v = vector:1, 2, 3:

print(v + 1)       # Vector addition

print(v * 2)      # Vector multiplication

print(v ** 2)   # Vector power

print(v.T)          # Vector transpose

print(v.I)          # Vector inverse

print(v.det)     # Vector determinant

print(v.eig)      # Vector eigenvalues

print(v.eigv)   #Vector eigenvectors


# Date and time
==============

#*  It can be used to store the current date and time, or a specific date and time.  *#
#    It can be used to format dates and times, and convert between strings and timestamps.


# Keyword to get the current date and time.
# This will return a datetime object, representing the current date and time in UTC.

datetime  # This will return a datetime object, representing the current date and time.

# Date Formatting

print(now.format(text: %Y-%m-%d:))   #2023-02-15 

print(now.format(text: %H:%M:%S:))  # 12:30:45

print(now.format(text: %Y-%m-%d %H:%M:%S:))   # 2023-02-15 12:30:45, representing the current date and time in UTC.

# Date Parsing

parse  # Keyword to parse a date from a string, parase means to convert a string into a date.

set date = datetime.parse(text: 2023-02-15:, text: %Y-%m-%d:)
print(date)   # 2023-02-15T00:00:00.000Z, representing the date in UTC.

# Timezones

set local = now(timezone = text: Asia/Kolkata:)
set utc = now(timezone = text: UTC:)

print(local)  # It will print : 2023-02-15T12:30:45.123+05:30, representing the current date and time in IST.
print(utc)    # It will print : 2023-02-15T07:00:45.123Z, representing the current date and time in UTC.

# Timestamps
# A timestamp is a number representing the number of milliseconds since the Unix epoch (January 1, 1970 00:00:00 UTC).

set ts = now().timestamp()  # This is will return a timestamp in milliseconds, representing the current time.
set dt = datetime(timestamp = ts)   # This is will return a datetime object, representing the current time.

print(ts)     # It will print : 1673896245123, representing the current time in milliseconds.
print(dt)    # It will print : 2023-02-15T12:30:45.123Z, representing the current date and  time in UTC.

# Date Ranges 

set week = datetimerange(
  start = today() - timedelta(days = 7),
  end = today() 
)

print(week)   # It will print : 2023-02-08T00:00:00.000Z,2023-02-15T00:00:00.000Z, representing the date range in UTC.

# Repeat (Loop) over range
repeat week as day:{
  print(day)    # It will print : 2023-02-08T00:00:00.000Z,2023-02-09T00:00:00.000Z,2023-02-10T00:00:00.000Z,2023-02-11T00:00:00.000Z,2023-02-12T00:00:00.000Z,2023-02-13T00:00:00.000Z,2023-02-14T00:00:00.000Z, representing the date range in UTC.
}
  

#Repeat task ( Recursive Functions )
================================
#*  A repeat task is a function that calls itself.  *#
#There must be a terminating condition to stop the recursion.
#Useful for problems that can be reduced to subproblems.
#Repeat task is a powerful technique that allows elegant solutions to complex problems by reducing them down to simpler cases repeatedly.
# You can call a repeat_task from inside the task itself, any number of times, from any where in the repeat task.
# Cons: Can lead to exponential time/space complexity if not written carefully.

repeat_task  # Keyword to repeat a task.

do task_name   #  Calling a repeat task.

# Example

 set students = 8

  repeat_task count_down(students) {

  if students == 0 {

  print(text: Shool closed!:)

}

  else {

  print(students)  # Printing the students count, 8, 7, 6, 5, 4, 3, 2, 1, Shool closed!

  do count_down(students - 1)    # Calling the task  again and again until the condition is true.

  }

  return students  # Returning the result, it will return 0.

}

  do count_down(students)   #Returns  8, 7, 6, 5, 4, 3, 2, 1, Shool closed!


#* Free Task ( Pure functions )  without side effects  *#
=========================================
# Free task characteristics:
# No side effects, does not modify external state or variables.
# No I/O operations.
# Does not call functions with side effects.

#  Advantages of free task ( functions) :
# Easier to understand, test, parallelize, and optimize.
# Isolated, reusable, cacheable, and thread-safe.

# Key Features of free task ( functions) :
# Always return the same output for a given input.
# Self-contained with no external state.
# Immutable, where the output depends only on the input.

# Benefits of free task ( Functions ) :
# Reusable, can be safely called from anywhere.
# Testable with no external dependencies.
# Thread-safe, can run in parallel.
# Cacheable, allowing for output caching.
# Optimizable, can be optimized by the compiler.

# Example 1

free_task add_books(harry_potter, lord_of_the_rings) {

return  harry_potter +  lord_of_the_rings  # Only depends on input, it will return 11, because we are serving new value 8 and 3 to the task.

}

do  add_books (8, 3)  # 11

print add_books           # 11

# Examples 2

free_task  products_count ( 10 number) {

  set product_available = 10 * 2  # Only depends on input

  return           # It will return 20

}

Do products_count ( 20 number)   # It will return 40, because we are serving new value 20 to the task.

print products_count  # It will print 40.


# Unfree Task ( Impure functions ) ( Functions with side effects )
=======================================================
#Characteristics of Unfree Tasks:

#Have side effects, modify global state, or perform I/O operations.
#Depend on external factors outside themselves.

#When to Use Unfree Tasks:

# Modifying global state.
# Performing I/O operations.
# Calling other functions with side effects.

#Cons: Difficult to understand, test, parallelize, and optimize, not thread-safe, reusable, testable, or cacheable.
#Unfree tasks have side effects and depend on external factors, making them challenging to work with and limiting their functionality.

# Example

set     # Set  is the global state to define a variable in Nova language, but here we are using a different keyword to define a variable, so it is an unfree task .

unfree_task add_one_apple {

var  total_apples  =  10  + 1    # Uses outside variable : var :  instead of :  set :, it breaks the standard rule of Nova to assign a value to a variable, uses diffent variable keyword, so it is an unfree task.

return  total_apples              # Returns outside variable, it will return 11

}

print add_one_apple    # It will print  11


# What is the difference between a normal task ( Normal function ) and  free task ( Pure function )?
=====================================================================================
 # A normal function: Can modify external state, can have side effects, output depends on more than just inputs.
 # Normal tasks are more flexible, but free tasks are  easier to understand.
 # Example:

 update_global  # Keyword to update a global variable.

 task normal_add( orange, ) {
  set  sum = x + y
  update_global(sum)   # Here we will have side effect, means modifying external state/variable ( global variable ).
  
  return sum  
 }

  do normal_add(1, 2)   # 3

  print normal_add  # 3

# A free task ( Pure function ): Can not modify external state, can not have side effects, output depends only on inputs.

# Example: 

   set fruits_count = 0   # Using :  set  : it is the global state/or follows rules to define a variable as per Nova language.

   free_task fruits_count( apple = 10  number, banana= 30 number) {

   set fruits_count = apple + banana    # Follows the standard rule to assign a value to a variable, uses only the  variable which is defined inside the task.

   return fruits_count        # Only depends on input

}

  do fruits_count (30, 40)    # It will return 70, because we are serving new value 30 and 40 to the task.

  print fruits_count  # It will print 70.

# What is the difference between a normal task ( Normal function ) and  unfree task ( Impure function )?
==========================================================================================
# A normal function: Can modify external state, can have side effects, output depends on more than just inputs.

# Example:

    set fruits_count =  10  # Global variable/global state/or follows rules to define a variable as per Nova language.

  task fruits_count_total(  papaya, jackfruit) {

  set  fruits_count = papaya + jackfruit

  update_global(fruits_count)   # Side effect means modifying external state/variable ( global state ).
  
  return fruits_count     # It will return 70, because we are serving new value 30 and 40 to the task.
 }

  do fruits_count_total (30, 40)    

  print fruits_count_total  # It will print 70.

# An unfree task ( Impure function ): Can modify external state, can have side effects, output depends on more than just inputs.

# Example:

  unfree_task fruits_count( apple = 10  number, banana= 30 number) {

  var fruits_count = apple + banana   # uses: var : keyword instead of:  set :, it breaks the standard rule to assign a value to a variable, uses outside variable.

  return fruits_count        # It will return 70.

  }

  do fruits_count (30, 40)    # It will return 70, because we are serving new value 30 and 40 to the task.

  print fruits_count  # It will print 70.


# Lambdas/Closures
====================
# Lambdas are anonymous functions that can be stored in variables and passed around.
#Lambdas are closures, meaning they can access variables from the enclosing scope.
# The key aspects are:
# Anonymous functions
# Stored in variables, Passed around, Closures, can access variables from the enclosing scope.
# Closures, can access variables from the enclosing scope.
# Can be passed as arguments to other functions.

 lambda    #keyword to denote this is a lambda function definition.
(x, y)           #  parameters similar to regular Nova tasks
{ }                 #  function body enclosed in braces

# Can be assigned to a variable like multiply
# Called like a normal function
# Some benefits of lambdas

# Define simple one-off functions without naming them
# Pass functions as arguments to other functions
# Use functions as return values

# Lambda function definition
set multiply = lambda(x, y) {
  return x * y
}

# Calling lambda function
set result = multiply(2, 3) 

print(result)  # Prints 6

# Passing lambda function as argument

set result = map(list:1, 2, 3:, lambda(x) {
  return x * 2   # 2, 4, 6
})

print(result)  # Prints list:2, 4, 6:

# Returning lambda function from another function
=============================
task makeMultiplier(m) {
  return lambda(x) {
    return x * m
  }
}

set triple = makeMultiplier(3)
print(triple(5))     # Prints 15

# Currying
# Currying is the process of transforming a function that takes multiple arguments into a function that takes a single argument.

set multiply_by = lambda(x) {

  return lambda(y) {
  
    return x * y  # 2 * 3 = 6
  
  }
}

set multiply_by_2 = multiply_by(2)   # 2 * y

set result = multiply_by_2(3)  # 6

print(result)  # Prints 6


# Higher Order Functions
=========================
# Higher order functions are functions that take other functions as arguments or return functions as their result.
# Higher order functions are like special helpers that either take other functions as helpers or give back functions as results. They make your code more flexible and powerful.

set nums = list:1, 2, 3:

task map(list, task) {
  set result = [list:]  # Create empty list  

  each(list as item) {

    add(result, func(item))   
  }

  return result     # Returns list of results 
}

# Simple function to multiply by 2
task double(n) {
  return n * 2
}

set nums = [1, 2, 3]

set doubled = map(nums, double)

print(doubled)   # [2, 4, 6]

# Filter using predicate function
set evens = filter(nums, task(n) {
  return n % 2 == 0  # Returns true if n is even
})

print(evens) # [2]  

# Reduce using accumulator function 

set nums = [List: 1, 2, 3: ]  # List of numbers

accumulator = 0  # Initial value of accumulator

n  = 0  # Current value

set sum = reduce(nums,
 task( accumulator, n) {
  return accumulator + n
}, accumulator)

print(sum)  # 6


#*  Pattern matching  *#  
==========================
#  Why use pattern matching? #
#*  Pattern matching is a way to check a value against any values, and extract data from the patterns of values.  *#

  check_ mach    # Keyword to check a value against a pattern of values.

  @     #  Keyword to check a value against a pattern of values, we add it at the end of the pattern to check the value.

 # simple example

  check_match 5 {

    5@  print(text: 5 is a number:)   # It will print 5 is a number.

    6@  print(text: 6 is a number:)   # It will not print because it is not matching the pattern.

  }

# Variable binding to check pattern matching 
=================================
#*  We can bind variables to perform multiple variables values at the same time.  *#


 set food = text:pizza: 

  set   calories = 100 number

  check_match food {

   case pizza@

    print(text: Yummy pizza!)

   case salad and calories < 100@     #here we are using two variables (salad,  calories ) at the same time to check the condition.
    
    print(text: Healthy salad!)     # It will not print because it is not matching the pattern.

}


 # Example 2  ( Variable binding )
  
  set  fruits = list:apple, banana, orange:  list

  set eat = 3 number

  set  vegetables = list:carrot, potato, tomato:  list

  set  food = list:fruits, vegetables:  list

  check_ match  fruits_vegetables {
      
    case fruits and vegetables@   # here we are using two variables (fruits, vegetables ) at the same time to check the condition.

    print(text: I like fruits and vegetables:)   # It will print I like fruits and vegetables.

    case fruits@ if eat < 3 number   

    print(text: buy more fruits:)   # It will not print because it is not matching the pattern.

    case vegetables@ if vegetables = 3 number

    print(text: buy more vegetables:)   # It will print buy more vegetables.

  }


# Powerful Concurrency Support (  Nova  can execute multiple tasks at the same time. )
===========================================================================
#  concurrent processes, enabling efficient and scalable applications.
#*  Nova  can execute multiple tasks at the same time.  *#

# Goroutines
================
#*  Goroutines are lightweight threads managed by the Nova runtime.  *#
# Goroutines are lightweight threads managed by the Nova runtime. They allow massive concurrency on a single OS thread.
# To create a goroutine, use the go keyword before calling a function. The goroutine will execute concurrently with the calling function.
# To create a goroutine, use the go_routine keyword to define a function that will run concurrently. Then call it using go to spawn it as a goroutine.

# Some key behaviors of goroutines:

# They run concurrently with other goroutines and the main program.
# The Nova runtime handles scheduling goroutines on threads.
# Goroutines pause when waiting for I/O or synchronization.
# Lightweight and cheap to create in high numbers.



# Defining a goroutine 
go_routine download_file(url) {
  # ... function body ...
}

# Calling a goroutine
go download_file(text:http://example.com/file.zip:)


# Channels 
================
#*  Channels are used to communicate between goroutines.  *#
# Channels provide synchronized communication between goroutines.

# Use make_chan to create a new channel of a given type
# Send values on a channel using the <- operator
# Receive values using the <- channel syntax
# Channels are synchronized, only one goroutine can send/receive at a time. This prevents data races.

make_chan    # creates a new channel of a specific type
<- operator   #sends a value on the channel
<-chan             # syntax receives from the channel

# Creating a channel 

set chan messages = make_chan(string)

# Sending on a channel  
messages <- text:Hello!:

# Receiving from a channel
set msg = <- messages

print(msg)   # It will print Hello!

# Buffered Channels
====================
#Channels enable communication between goroutines:
# Channels can be buffered for asynchronous communication: 
#  Buffered channels allow asynchronous send/receive:
 
set chan jobs = make_chan(int, 100)

go func() {
  repeat(100) {
    jobs <- num
  } 
}

repeat(100) {
  job <- jobs
  print(job)
}


# Channel Range Loop
====================
# Range over a channel to receive values until it is closed:

chan jobs = make_chan() 

go func() {
  jobs <- 1
  jobs <- 2
  close(jobs)
}()

for j := range jobs {
  print(j) 
}

# Select Across Channels
====================
# Select across multiple channels to receive values from the first ready channel:

chan1 := make(chan int)
chan2 := make(chan int)

select {
case v := <- chan1:
   print("received ", v)
case v := <- chan2:
   print("received ", v)  
}


# Closing Channels
====================
# Closing a channel indicates that no more values will be sent on it. This can be useful to communicate completion to the receiver.

# Closing a channel

close(chan)

# Checking if a channel is closed

closed(chan)

# Example

set chan jobs = make_chan(int, 100)

go func() {
  repeat(100) {
    jobs <- num
  } 
  close(jobs)
}

repeat(100) {
  job <- jobs
  print(job)
}


# Select 
=========
#*  Select is used to wait on multiple channel operations.  *#
#*  Select blocks until one of its cases can run, then it executes that case.  *#
#*  It chooses one at random if multiple are ready.  *#
#Select picks the first channel that is ready and executes that case. Useful for multiplexing channels.

select {
  case msg = <-ch1:
     print(msg)
     
  case <-ch2:
     print(text:Received from ch2:)
     
  default:
     print(text:No channels ready:)  
}


# Waitgroups
================
# Waitgroups allow synchronizing goroutines:
#Waitgroups are useful to wait for a set of goroutines to complete.
# Add goroutines to the waitgroup using add.
# Wait for goroutines to finish using wait.
# Call done when a goroutine finishes.
# Call wait to block until all goroutines finish.

add # Adds a goroutine to the waitgroup
done  # Marks a goroutine as finished
wait  # Blocks until all goroutines finish

# Creating a waitgroup

set wg = make_waitgroup()

go func() {
  # do work
  
  wg.done()
}

wg.wait() # Blocks until all goroutines finish

# Mutexes
================
# Mutexes allow synchronizing goroutines:
# Mutexes are used to synchronize access to shared state.
# Lock a mutex before accessing shared state.
# Unlock a mutex after accessing shared state.
# Only one goroutine can hold a mutex at a time.
# Other goroutines will block until the mutex is unlocked.
# Mutexes prevent concurrent access to shared memory. Only one goroutine can hold the lock at a time.

set m = new_mutex()

m.lock()
# critical section 
m.unlock()



# Worker Pools
================
#*  Worker pools are used to limit the number of goroutines running at the same time.  *#
#*  They are often used to limit concurrency when accessing shared resources.  *#

set pool = new_workerpool(10) 

repeat(100) {
  pool.submit(process) 
} 

pool.shutdown()
pool.await() # Wait for completion

# The pool limits the maximum workers to 10 at a time, preventing overload.

# Channels - Ping Pong
# A simple ping pong example using channels:
# This asynchronously ping-pongs a value between two goroutines.

chan ping = make_chan()
chan pong = make_chan()

go func() {
  repeat {
    <-ping
    pong<-
  }
}

repeat { 
  ping<-
  <-pong
}

# Select - Timeout
================
# Using select to implement a timeout:
# This uses select to implement a timeout on a channel.
# Select can wait on both a channel and a timer, executing the first ready case.

select {
  case <-ch:
     # received value
  
  case <-time.after(5 * time.seconds):
     # timeout expired
}


# Pipeline - Fan Out / Fan In
==============================
 # A concurrent pipeline exemplifying fan-out and fan-in:
# This uses multiple goroutines to concurrently compute squares and cubes of numbers, then merges the results.
# Jobs are fanned out to workers, results fanned back in.

chan jobs = make_chan()
chan results = make_chan()

go func() {
  repeat {
    jobs <- job
  }
}

// Start 10 goroutine workers
repeat 10 {
  go func() {
     repeat {
        j := <- jobs
        r := process(j)
        results <- r
     }
  }
} 

// Collect results
repeat {
  r := <- results
}


# Sync Pool
================
# Sync.Pool is used to cache and reuse objects:
# Sync.Pool is used to cache and reuse objects.
# Get an object from the pool using get.
# Put an object back into the pool using put.
# The pool will cache objects for reuse, reducing allocations.
# The pool provides synchronized access to a pool of resources.

set pool = new_syncpool(NewResource)

func GetResource() Resource {
  return pool.get() 
}

func PutResource(r Resource) {
  pool.put(r)
}

# Async/Await
================
# Async/await allows writing asynchronous code in a synchronous style:
# Use async to define an asynchronous function.
# Use await to wait for an asynchronous function to complete.
# Async functions return a promise, which can be used to wait for completion.


async  # Keyword to define an asynchronous function.

await  # Keyword to wait for an asynchronous function to complete.

# The await keyword pauses execution until a goroutine completes.

# Example

async download_file(url) {

  set response = await web.get(url)
  
  set file = await save_file(response) 
  
  return file

}

set file = await download_file(text:http://example.com/file.zip:)
print(file) # Prints the file path


# Work Stealing
================
# Work stealing is used to efficiently schedule goroutines:
# The work stealing queue allows goroutines to steal work from other goroutines, improving efficiency.

set queue = new_workstealingqueue()

go func() {
  repeat {
    task := queue.take() // may steal from others
    do(task)
  }
}

repeat {
  queue.put(task)
}

# Futures/Promises
================
# Futures represent the result of an asynchronous operation:
# Promises are similar and avoid callback hell.

set future = web.get_async(url)

// do other work 

set response = await future

# Data Parallelism
================
# Data parallelism performs an operation across slices concurrently:

set data = []int{1,2,3,4}

set result = parallel.map(data, square) 

func square(num int) int {
  return num * num
}

print(result) # [1,4,9,16]


# Actors
================
# Actors are isolated processes that communicate via messages:
# Actors provide concurrency, isolation and synchronization.
# Actors are isolated from each other, and communicate via messages.
# Actors can be used to model real-world entities, such as people, cars, etc.

actor  # Keyword to define an actor.

send  # Keyword to send a message to an actor.

receive  # Keyword to receive a message from an actor.

actor Counter {
  var count = 0
  
  receive(msg Message) {
    case IncMessage:
      count++
      
    case GetMessage:
      sender <- count
  }
}

set c = spawn_actor(Counter)
c <- IncMessage() 
set result = await c <- GetMessage()

print(result) # 1

#Reactive Extensions
================
# Reactive extensions are used to compose asynchronous and event-based programs:
# Reactive pipelines handle backpressure and propagation of errors.

set result = 
  web.get(url)
    .select(parse_json)
    .map(normalize)
    .filter(validate)
    .subscribe(save_db)

# Dataflow
===========
# Coordinate pipelines using dataflow variables:
# Dataflow variables connect asynchronous stages.
# Dataflow variables are used to coordinate asynchronous stages.
# Dataflow variables can be used to pause/resume asynchronous stages.

set url := new_dataflow()
set data := web.get(url) // pauses

url <- text:example.com: // resumes get

save(data)

# CSP Channels
================
# Channels with input and output ends for communication:
# Used heavily in Go for synchronization and message passing.

chan c = new_chan()
set inp, out = c.ends()

go func() {
  out <- data
}

data = <- inp


# Atomic Operations
================
# Atomic operations are used to perform atomic operations on shared memory:

set x = 0

go func() {
  atomic.add(&x, 1)
}

atomic.compare_and_swap(&x, 1, 2)


# Atomic Counter
================
# Atomic counters are used to perform atomic operations on shared memory:
#Where new_atomic_uint64 and the add and load methods would be built into the Nova standard library.

#The key ideas are:
# atomic.Uint64 provides an atomic 64-bit unsigned integer
# add atomically adds to the value
# load atomically loads the current value
# This allows thread-safe modification and access to the counter variable from multiple goroutines without locks.

set counter = new_atomic_uint64(0)

func increment() {
  counter.add(1)
} 

func getCount() {
  return counter.load() 
}


# Task Cancellation
================
# Tasks can be cancelled using a cancellation token:
# Cancellation tokens can be used to cancel tasks.
# Cancellation tokens are passed to tasks, which can check if they are cancelled.
# Cancellation tokens are useful to cancel long-running tasks.

 cancellation_token  # Keyword to create a cancellation token, which can be used to cancel a task.

# Start a cancelable task
set cts = new_cancellation_token_source()
go do_work(cts.token)

# Cancel task after some time
after(5.seconds) {
  cts.cancel() 
}

# Task checks for cancellation
func do_work(token) {
  repeat {
    if token.cancelled() {
      print("Cancelling task")
      return
    }
    
    do_step()
  }
}

#Graceful Shutdown
================
# Graceful shutdown allows tasks to be cancelled:
# Graceful shutdown is useful to cancel long-running tasks.
# The running variable allows goroutines to stop themselves when the program is shutting down.
#This allows unfinished work to be aborted cleanly to avoid getting stuck.

set running = true

# Start goroutines
go do_work() 

# On signal, start shutdown
on_signal(SIGINT) {
  running = false
}

# Goroutines check for shutdown
func do_work() {
  repeat {
    if !running {
      print("Stopping gracefully") 
      return   
    }
    
    do_step()
  }
}

 
# Macros and Metaprogramming
============================
# Macros are used to generate code at compile-time.

macro  # Keyword to define a macro.

struct Person {
  name: string
  age: int
}

macro generate_getters(struct_name, fields) {
  repeat_task field as fields {
    print(f"
    task {struct_name}get{field}() {field_type} {{
      return self.{field}
    }}
    ")
  }
}

generate_getters(Person, [name, age])

# This will generate:
task Person_get_name() text {
return self.name

}

task Person_get_age() number {
return self.age
}



macro generate_setters(struct_name, fields) {

  # generate setters
  repeat_task field as fields {
    print(f"
    task {struct_name}set{field}(value {field_type}) {{
      self.{field} = value
    }}
    ")
  }
}

macro generate_struct(struct_name, fields) {

  # generate struct
  print(f"
  struct {struct_name} {{
    repeat_task field as fields {
      {field} {field_type}
    }
  }}
  ")

  generate_getters(struct_name, fields)
  generate_setters(struct_name, fields)
}

generate_struct(Person, [name: string, age: int])

# This will generate:
struct Person {
  name: string
  age: int
}

task Person_get_name() text {
  return self.name
}

task Person_get_age() number {
  return self.age
}

task Person_set_name(value text) {
  self.name = value
}

task Person_set_age(value number) {
  self.age = value
}




# Robust Module and Package System
==================================

# Modules
=========
#*  Modules are used to organize code into namespaces.  *#

File: utils.nova

module Utils {

Task public greet() {

print(text: Hello World!:)

}

}

File: main.nova
import Utils from 'utils'

Utils.greet()

# Packages
==========
#*  Packages are used to organize code into reusable libraries.  *#

File: utils/greet.nova
package Utils {

Task public greet() {

print(text: Hello World!:)
}

}

File: main.nova
import Utils from 'utils'

Utils.greet()

# Namespaces
============
#*  Namespaces are used to organize code into namespaces.  *#

module App {

Task greet() {

print(text: Hello!:)
}

}

import App

App.greet()

# Importing specific functions

from Utils import greet

greet()

# Importing all functions

from Utils import *

greet()

# Importing with alias

from Utils import greet as hello

hello()  

# Smart & wise error Handling
==========================
#*  Error handling is used to handle errors in a program.  *#
#*  When an error occurs in a program, it will stop the program execution and display an error message.  *#
#*  Error handling is used to handle errors in a program, so that the program can continue to run without stopping.  *#
# Error Handling
================

enum Error {
  NotFound
  AlreadyExists
  IOError
}

try {
  process_file(path)
} 
catch (NotFound) {
  print("File not found")
} 
catch (IOError e) {
  print("IO Error: " + e.message)
}

# Error Handling with Result
#Exceptions
================
enum Exception {
  NotFound,
  ParseError
}

try {
  # Code that can throw
} 
catch (e Exception) {
  match e {
    NotFound => {
      #handle not found
    },
    ParseError => {
      # Handle parse error
    }
  }
}

# Stack traces
================
try {
  #code
} 
catch (e) {
  print(e.stacktrace())
}

# Resources
set file = open("filename")
try {
  #use file
} 
finally {
  file.close() // clean up resource
}

# User-defined exceptions
================
exception NotFoundError() extends Exception {
  #custom exception
}

throw NotFoundError()

# Error Handling with Result
enum Result {
  Ok,
  Err
}

set result = process_file(path)

if result == Ok {
  print("File processed successfully")
} 
else if result == Err {
  print("Error processing file")
}

# Error Handling with Option
enum Option {
  Some,
  None
}

set result = process_file(path)

if result == Some {
  print("File processed successfully")
} 
else if result == None {
  print("Error processing file")
}

# Error Handling with Panic
panic  # Keyword to panic the program.

set result = process_file(path)

if result == None {
  panic("Error processing file")
}

# Error Handling with Try
try  # Keyword to try a task.
set result = try process_file(path)

if result == None {
  panic("Error processing file")
}

# Error Handling with Assert
assert  # Keyword to assert a condition.

set result = process_file(path)

assert(result == Some)

# Error Handling with Expect
expect  # Keyword to expect a condition.

set result = process_file(path)

expect(result == Some)

# Error Handling with Unwrap
unwrap  # Keyword to unwrap a value.

set result = process_file(path)

set file = unwrap(result)

# Error Handling with UnwrapOr
unwrap_or  # Keyword to unwrap a value or return a default value.

set result = process_file(path)

set file = unwrap_or(result, default_file)

# Error Handling with UnwrapOrElse
unwrap_or_else  # Keyword to unwrap a value or return a default value from a function.

set result = process_file(path)

set file = unwrap_or_else(result, default_file)

# Error Handling with UnwrapErr
unwrap_err  # Keyword to unwrap an error value.

set result = process_file(path)

set file = unwrap_err(result)

# Error Handling with UnwrapErrOr
unwrap_err_or  # Keyword to unwrap an error value or return a default value.

set result = process_file(path)

set file = unwrap_err_or(result, default_file)

# Error Handling with UnwrapErrOrElse
unwrap_err_or_else  # Keyword to unwrap an error value or return a default value from a function.

set result = process_file(path)

set file = unwrap_err_or_else(result, default_file)

# Error Handling with UnwrapPanic
unwrap_panic  # Keyword to unwrap a value or panic.

set result = process_file(path) 

set file = unwrap_panic(result)

# Error Handling with UnwrapPanicOr
unwrap_panic_or  # Keyword to unwrap a value or panic with a custom message.

set result = process_file(path)

set file = unwrap_panic_or(result, "File not found")

# Error Handling with UnwrapPanicOrElse
unwrap_panic_or_else  # Keyword to unwrap a value or panic with a custom message from a function.

set result = process_file(path)

set file = unwrap_panic_or_else(result, "File not found")

# Error Handling with UnwrapPanicErr
unwrap_panic_err  # Keyword to unwrap an error value or panic.

set result = process_file(path)

set file = unwrap_panic_err(result)

# Error Handling with UnwrapPanicErrOr
unwrap_panic_err_or  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_panic_err_or(result, "File not found")

# Error Handling with UnwrapPanicErrOrElse
unwrap_panic_err_or_else  # Keyword to unwrap an error value or panic with a custom message from a function.

set result = process_file(path)

set file = unwrap_panic_err_or_else(result, "File not found")

# Error Handling with UnwrapExpect
unwrap_expect  # Keyword to unwrap a value or panic with a custom message.

set result = process_file(path)

set file = unwrap_expect(result, "File not found")

# Error Handling with UnwrapExpectErr
unwrap_expect_err  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_expect_err(result, "File not found")

# Error Handling with UnwrapErrExpect
unwrap_err_expect  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_err_expect(result, "File not found")

# Error Handling with UnwrapErrExpectErr
unwrap_err_expect_err  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_err_expect_err(result, "File not found")

# Error Handling with UnwrapErrPanic
unwrap_err_panic  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_err_panic(result, "File not found")

# Error Handling with UnwrapErrPanicErr
unwrap_err_panic_err  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_err_panic_err(result, "File not found")

# Error Handling with UnwrapPanicExpect
unwrap_panic_expect  # Keyword to unwrap a value or panic with a custom message.

set result = process_file(path)

set file = unwrap_panic_expect(result, "File not found")

# Error Handling with UnwrapPanicExpectErr
unwrap_panic_expect_err  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_panic_expect_err(result, "File not found")

# Error Handling with UnwrapPanicErrExpect

unwrap_panic_err_expect  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_panic_err_expect(result, "File not found")

# Error Handling with UnwrapPanicErrExpectErr

unwrap_panic_err_expect_err  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_panic_err_expect_err(result, "File not found")

# Error Handling with UnwrapErrPanicExpect

unwrap_err_panic_expect  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_err_panic_expect(result, "File not found")

# Error Handling with UnwrapErrPanicExpectErr

unwrap_err_panic_expect_err  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_err_panic_expect_err(result, "File not found")

# Error Handling with UnwrapErrPanicErrExpect

unwrap_err_panic_err_expect  # Keyword to unwrap an error value or panic with a custom message. 

set result = process_file(path)

set file = unwrap_err_panic_err_expect(result, "File not found")

# Error Handling with UnwrapErrPanicErrExpectErr

unwrap_err_panic_err_expect_err  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_err_panic_err_expect_err(result, "File not found")

# Error Handling with UnwrapPanicErrPanicExpect

unwrap_panic_err_panic_expect  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_panic_err_panic_expect(result, "File not found")

# Error Handling with UnwrapPanicErrPanicExpectErr

unwrap_panic_err_panic_expect_err  # Keyword to unwrap an error value or panic with a custom message.

set result = process_file(path)

set file = unwrap_panic_err_panic_expect_err(result, "File not found")

