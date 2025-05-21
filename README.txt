README.txt – How to Use MyLang (Stages 1–4)

Module: 6CC509 – Language Design and Implementation
Author: 100344248

MyLang is a custom interpreter supporting arithmetic expressions, boolean logic, string operations, and global variables (Stages 1 to 4).


STAGE 1: Arithmetic Expressions

• Supports +, -, *, / operators
• Parentheses and unary negation

Example:
>>> 1 - 2
>>> 2.5 + 2.5 - 1.25
>>> (10 * 2) / 6
>>> 8.5 / (2 * 9) - -3


STAGE 2: Boolean Logic

• true / false literals
• ==, !=, <, >, and, or, not

Example:
>>> true == false
>>> true != false
>>> (5 < 10)
>>> !(5 - 4 > 3 * 2 == !false)
>>> true and true
>>> false and true
>>> (0 < 1) or false
>>> false or false


STAGE 3: String Values

• Double-quoted text: "..."
• Concatenation using +
• Comparison using == and !=

Example:
>>> "hello" + " " + "world"
>>> "foo" + "bar" == "foobar"
>>> "10 corgis" != "10" + "corgis"


STAGE 4: Global Variables

• Variable assignment and reuse
• Expressions with variables
• print statements

Example:
>>> quickMaths = 10
>>> quickMaths = quickMaths + 2
>>> print quickMaths

>>> stringCatTest = "10 corgis"
>>> stringCatTest = stringCatTest + 5 + " more corgis"
>>> print stringCatTest

>>> errorTest = 5
>>> errorTest = errorTest + "string"
>>> print errorTest

To exit the interpreter:
>>> exit
or
>>> quit
