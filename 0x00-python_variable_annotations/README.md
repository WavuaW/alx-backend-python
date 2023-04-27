Python Variable Annotations
Python 3.5 introduced support for variable annotations, which allow you to add type hints to your code. This feature is useful for providing documentation to your code, making it easier for other developers to understand how your code works. This guide will provide an overview of how to use variable annotations in Python.

Basic Syntax
To add a variable annotation, you can use the colon (:) followed by the type of the variable. For example:

python
Copy code
name: str = 'John Doe'
age: int = 30
In this example, we've declared two variables, name and age, with the types str and int, respectively.

Using Annotations with Functions
Variable annotations can also be used with function parameters and return values. For example:

python
Copy code
def greet(name: str) -> str:
    return f'Hello, {name}!'
In this example, the greet function takes a name parameter of type str and returns a string.

Optional and Union Types
You can also use optional types and union types with variable annotations. Optional types are denoted by adding a question mark (?) after the type, while union types are denoted by using the | operator to separate multiple types. For example:

python
Copy code
email: str | None = None
In this example, the email variable can be either a string or None.

Conclusion
Variable annotations are a useful feature in Python for providing documentation and improving the readability of your code. By using variable annotations, you can make it easier for other developers to understand how your code works and reduce the likelihood of bugs and errors.