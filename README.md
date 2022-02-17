# Demo3
write a program to check if the given number is happy number or print all the happy number between 1 to 100
STEP 1:isHappyNumber() determines whether a given number is happy or not.
If the number is greater than 0, then calculate the remainder rem by dividing the number with 10.
Calculate the square of rem and add it to a variable sum.
Divide number by 10.
Repeat the steps from a to c till the sum of the square of all digits present in number has been calculated.
Finally, return the sum.
STEP 2:Define and initialize variable num.
STEP 3:Define a variable result and initialize it with a value of num.
STEP 4:If the result is neither equal to 1 nor 4 then, make a call to isHappyNumber().
STEP 5:Otherwise, if the result is equal to 1 then, the given number is a happy number.
STEP 6:If the result is equal to 4 then, the given number is not a happy number.

# OOP's Concepts
1. Encapsulation : Encapsulation in Python is the process of wrapping up variables andmethods into a single 
entity. In programming, a class is an example that wraps all the variables and methods defined inside it.
Encapsulate means to hide. Encapsulation is also called data hiding
2. Inheritance: In inheritance, the child class acquires the properties and can access all the data members and functions defined in the 
parent class. A child class can also provide its specific implementation to the functions of the parent class.
The idea of reusability is called the inheritance
3. Polymorphism: It is a word that came from two greek words, poly means many and morphos means forms. If a variable, object or method perform different behavior according to situation, it is called polymorphism.
Class : Python class is a group of attributes and methods
Attributes : Represented by variable that contains data
Methods : Performs an action or task. It is similar to function.
Object :It is class type variable or class instance. To use the class, we should create an object to the class.
By using object we can access the all the properties of that class.
Instance creation represents allocating memory necessary to store the actual data of the variables.
Each time you create an object of a class a copy of each variables defined in the class is created.
In other word we can say that each object of a class has its own copy of data members defined in the class.
self : It is a variable which refers to current class instance or object.
It is the default variable that contains the memory address of the current object.
This variable is used to refer all the instance variable and method
When we create object of a class, the object name contains the memory location of the object.
This memory location is internally passed to self, as self knows the memory address of the object so we can access 
variable and method of object.
Self is the first argument to any object method because the first argument is always the object reference. This is 
automatic, whether you call it self or not.
Constructor: Python support the special type of method called constructor for initializing the instance variable of a 
class. A class constructor, if defined is called whenever a program create an object of that class.
A constructor is called only once at the time of creating an instance.
If two instances are created for a class, the constructor will be called once for each instance.
__init__() : This method is used to initialize the variables. This is the special method. we do not call this method 
explicitly.
TYPES OF VARIABLES:
1. Instance variable:
These are the variables whose separate copy is created in every project.
Instance variables are defined and initialized using a constructor with self parameter.
To access the instance variable, we need instance methods with self as a first parameter then we can access 
instance variable using self.variable_name.
We can access instance variable using obect_name.variable_name
Instance variables are the variables whose separate copy is created in every object.
If we modify the copy of instance variable in an instance, it will not affect all the copies in the other instance.
2. Class Variable / static variable:
These are the variables whose single copy is available to all the instance of the class.
If we modify the copy of class variable in an instance, it will affect all the copies in the other instance.
NAMESPACE : It represents a memory block where names are mapped to objects.
Class Namespace : A class maintains its own namespace known as class namespace. In the namespace, the names are 
mapped to class variables.
Instance Namespace : Every instance have its own namespace known as instance namespace. In the instance
namespace, the names are mapped to instance variable.s
TYPES OF METHODS:
1. Instance Methods : (Normal Methods)
a. Accessor Method:
b. Mutator Methods:
2. Class Methods:
3. Static Methods:
normal method: the current object if automatically passed as an (additional) first argument
classmethod: the class of the current object is automatically passed as an (additional) fist argument
staticmethod: no extra arguments are automatically passed. What you passed to the function is what you get.
Static Methods:
Simple functions with no self argument.
Work on class attributes; not on instance attributes.
Can be called through both class and instance.
The built-in function staticmethod()is used to create them.
Class Methods:
Functions that have first argument as classname.
Can be called through both class and instance.
These are created with classmethod in-built function.
Similarity: Both of them can be called on the Class itself, rather than just the instance of the class. So, both of 
them in a sense are Class's methods.
Difference: A classmethod will receive the class itself as the first argument, while a staticmethod does not.
Concepts of OOP
1. Encapsulation : Encapsulation in Python is the process of wrapping up variables andmethods into a single 
entity. In programming, a class is an example that wraps all the variables and methods defined inside it.
Encapsulate means to hide. Encapsulation is also called data hiding.
Classical object-oriented languages, such as C++ and Java, control the access to class resources by public, private and 
protected keywords. 
Public members are accessible from outside the class. The object of the same class is required to invoke a public 
method. All members in a Python class are public by default.
Private members of a class are denied access from the environment outside the class. They can be handled only from 
within the class.
2. Abstraction
Abstraction means hiding the complexity and only showing the essential features of the object. So in a way, 
Abstraction means hiding the real implementation and we, as a user, knowing only how to use it.
Abstraction is implemented using interface and abstract class while Encapsulation is implemented using private and 
protected access modifier.
Difference:
Abstraction: Suppose you are going to an ATM to withdraw money. You simply insert your card and click some buttons 
and get the money. You don’t know what is happening internally on press of these buttons. Basically you are hiding 
unnecessary information from user. So, abstraction is a method to hide internal functionalities from user.
Encapsulation: Suppose there is a tree. Now a tree can have its components like root, stem, branches, leaves, flowers 
and fruits. It has some functionalities like Photosynthesis. But in a single unit we call it a tree. In same way 
encapsulation is a characteristic to bind data members and functions in single unit.
Inheritance: 
In inheritance, the child class acquires the properties and can access all the data members and functions defined in the 
parent class. A child class can also provide its specific implementation to the functions of the parent class.
The idea of reusability is called the inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class or super class
Child class is the class that inherits from another class, also called derived class or sub class
Constructor overriding: defining constructor in parent and child class
If we write constructor in the both classes, parent class and child class then the parent class constructor is not 
available to the child class.
In this case only child class constructor is accessible which means child class constructor is replacing parent 
class constructor.
Constructor overriding is using when programmer want to modify the existing behaviour of a constructor.
super() : method is used to call parent class constructor or methods from the child class.
b. Multi-Level Inheritance : Multi-level inheritance is archived when a derived class inherits another derived class. 
There is no limit on the number of levels up to which, the multi-level inheritance is archived in python.
c. Hierarchical Inheritance
When more than one derived classes are created from a single base this type of inheritence is called 
hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.
d. Multiple Inheritance : Python provides us the flexibility to inherit multiple base classes in the child class.
When a class can be derived from more than one base classes this type of inheritance is called multiple 
inheritance. In multiple inheritance, all the features of the base classes are inherited into the derived class.
Method Resolution Order (MRO) : In the multiple inheritance scenario members of class are searched first in 
the current class. If not found, the search continue into parent classes in depth – first, left to right manner 
without searching the same class twice. 
Search for the child class before going to its parent class.
When a class is inherited from several classes, it searches in the order from left to right in the parent classes.
It will not visit any class more than once which means a class in the inheritance hierarchy is traversed only once 
exactly.
e. Hybrid Inheritance: Inheritence consisting of multiple types of inheritence is called hybrid inheritence.
Polymorphism:
1. Duck Typing:
In python, we follow a principal – If ‘it walks like a duck and talk like a duck it must be a duck’ which means 
python doesn’t care about which class of object it is, if it is an object and required behaviour is present for 
that object then it will work. The type of object is distinguished only at runtime. This is called as duck 
typing.
Python doesn’t care about which class of object it is, in order to call an existing method on an object. If the 
method is defined on the object, then it will be called.
STRONG TYPING : 
We can check whether the object passed to the member has the method being invoked or not.
hasattr() : It is used to check whether the object has a method or not.
Syntax : hasattr(object, attribute)
Where attribute can be a method or variable. If it is found in the object then this method returns True else 
False.
2. Method Overloading:
When more than one method with the same name is defined in the same class, it is known as method 
overloading. In python, if a method is written such that it can perform more than one task, it is called 
method overloading. 
We achieve method overloading by writing same method with several parameters.
3. Method Overriding:
If we write a method in the both classes, parent class and child class then the parent classes method is not 
available to the child class.
In this case only child class’s method is accessible which means child class’s method is replacing parent 
class’s method.
4. Operator Overloading:
If any operator performs additional actions other than what it is meant for, it is called operator overloading.
