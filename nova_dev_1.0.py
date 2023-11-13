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

 Maps           #  Store unordered collections of key-value pairs data.

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
=============

#*  Variables value can be changed ( We can read, write and update the value in realtime ). *#

Set             # Keyword to save a changeable value for  later use.

mango       # We are defining a variable name: mango :  to save a changeable value.

Set mango= 0    #  Saving a changeable value  : 0 :

mango = 1

mango = 2                   #  Can be changed the data/vlaue again and again.

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

datetime()    

# Keyword to get the current date and time.
# This will return a datetime object, representing the current date and time in UTC.

datetime.parse()                # Keyword to parse a date from a string.

datetime.format()               # Keyword to format a date to a string.

datetime.timestamp()        # Keyword to get the timestamp of a date.

datetime.timedelta()        # Keyword to get the difference between two dates.

datetime.datetimerange()  # Keyword to get a range of dates.

datetime.now()                  # Keyword to get the current date and time in a specific timezone.

datetime.today()                # Keyword to get the current date in a specific timezone.

datetime.timezone()           # Keyword to get the timezone of a date.

datetime.timezoneoffset()  # Keyword to get the timezone offset of a date.

datetime.timezoneinfo()      # Keyword to get the timezone info of a date.

set now = datetime()     # This will return a datetime object, representing the current date and time.

print(now)                           # 2023-02-15T12:30:45.123Z, representing the current date and time in UTC.

print(now.year)                 # 2023, representing the current year.

print(now.month)            #2,  representing the current month.


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

  do count_down(students - 1)    # Calling the task  again

  return students

}

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

do  add_books (8, 3) # 11

print add_books  #  11

# Examples 2

free_task  products_count ( 10 number) {

  set product_available = 10 * 2  # Only depends on input

  return product_available            # It will return 20

}

Do products_count ( 20 number)   # It will return 40, because we are serving new value 20 to the task.

print products_count  # It will print 40.


# Unfree Task ( Impure functions ) ( Functions with side effects )
================================================================
#Characteristics of Unfree Tasks:

#Have side effects, modify global state, or perform I/O operations.
#Depend on external factors outside themselves.

#When to Use Unfree Tasks:

# Modifying global state.
# Performing I/O operations.
# Calling other functions with side effects.
# Challenges and Limitations:

#Cons: Difficult to understand, test, parallelize, and optimize, not thread-safe, reusable, testable, or cacheable.

# Guiding Principle:
#Use unfree tasks only when necessary, such as when modifying global state, performing I/O operations, or calling functions with side effects.
#Key Idea: Unfree Tasks:
#Unfree tasks have side effects and depend on external factors, making them challenging to work with and limiting their functionality.

# Example

set     # Set  is the global state to define a variable in Nova language, but here we are using a different keyword to define a variable, so it is an unfree task .

unfree_task add_one_apple {

var  total_apples  =  10  + 1    # Uses outside variable : var :  instead of :  set :, it breaks the standard rule of Nova to assign a value to a variable, uses diffent variable keyword, so it is an unfree task.

return  total_apples              # Returns outside variable, it will return 11

}

print add_one_apple    # It will print  11


# What is the difference between a normal task ( Normal function ) and  free task ( Pure function )?
================================================================================================
 # A normal function: Can modify external state, can have side effects, output depends on more than just inputs.
# Normal tasks are more flexible, but free tasks are  easier to understand.
# Example:

task normal_add( orange, ) {
  set  sum = x + y
  update_global(sum)   # Here we will have side effect, means modifying external state/variable ( global variable ).
  
  return sum  
}

  do normal_add(1, 2)   # 3

print normal_add  # 3

# A free task ( Pure function ): Can not modify external state, can not have side effects, output depends only on inputs.

# Example:

   set fruits count = 0   # Using :  set  : it is the global state/or follows rules to define a variable as per Nova language.

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

task normal_add(x, y) {
  var sum = x + y
  update_global(sum)   # Side effect means modifying external state/variable ( global state ).
  
  return sum  
}

# An unfree task ( Impure function ): Can modify external state, can have side effects, output depends on more than just inputs.

# Example:

unfree_task fruits_count( apple = 10  number, banana= 30 number) {

  var fruits_count = apple + banana   # uses: var : keyword instead of:  set :, it breaks the standard rule to assign a value to a variable, uses outside variable.

  return fruits_count        

}

 do fruits_count (30, 40)    # It will return 70, because we are serving new value 30 and 40 to the task.

 print fruits_count  # It will print 70.


#*  Higher order functions  *#
===============================
#*  A higher order function is a function that takes another function as an argument or returns a function as a result.  *#
#Why use higher order functions?
#Higher order functions are useful for creating, reusable code, abstractions, such as map, filter, and reduce.



#*  pattern matching  *#
===============================
#*  Pattern matching is a way to match values against patterns and extract data from the patterns.  *#
#*  It is used to match values against patterns and extract data from the patterns.  *#
#  why use pattern matching? It is useful for matching values against patterns and extracting data from the patterns.

# Example 1

set  fruits = list:apple, banana, orange:  list

match fruits {
  list:apple, banana, orange:  print(text: I like fruits:)   # It will print I like fruits.
  list:apple, banana:  print(text: I like apple and banana:)   # It will not print because it is not matching the pattern.
  list:apple, banana, orange, grapes:  print(text: I like fruits:)   # It will not print because it is not matching the pattern.
}



#*  closures  *#
===============================
#*  A closure is a function that captures the state of its surrounding environment.  *#
#*  It is used to capture the state of its surrounding environment.  *#
#  why use closures? It is useful for capturing the state of its surrounding environment.



# Modules
================
#*  Modules are used to organize the code into multiple files.  *#
#*   When we have a large code base, it's hard to manage all the code in a single file, so we can split the code into multiple files and organize them into modules.  *#
#*  Modules are also used to reuse the code in multiple projects.  *#

# Importing modules

import   # Keyword to import modules from outside this file.

from        # Keyword to import modules from outside this file, but only imports specific tasks from the module that we need.

import module_name

from module_name import  task task_name

# Example 1

import  images  # Importing the images module

from images.resize()   # Calling the resize task from the images module

# Example 2

import  videos  # Importing the videos module

from videos.play()   # Calling the play task from the videos module


# Packages
================
#*  Packages are used to organize the modules into multiple folders.  *#

# Importing packages

import   # Keyword to import packages from outside this file.

from        # Keyword to import packages from outside this file, but only imports specific modules from the package that we need.

import package_name

from package_name import  module module_name

# Example 1

import  image_editor  # Importing the image_editor package.

from image_editor.resize()   # Calling the resize task from the image_editor package.

# Example 2

import  video_editor  # Importing the video_editor package.

from video_editor.play()   # Calling the play task from the video_editor package.


