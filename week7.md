# Week 7 Outline

## Reading
- It will be increasingly important to keep up with reading from Practical Computing and other supplementary sources.
- For this week, take a look at Chapters 7 and 8.

## Final Project
- We'll talk about these in more detail after Fall Break, but now is an important time to start thinking about what you want to work on.
- As we develop our skills in Python, you should start thinking about how to use your new skills to meet the goals of your project
- Here are some broad questions to start answering:
  - What area of biology would you like to explore?
  - What types of data might be collected and analyzed for studies in this area?
  - Do you want to write code that would analyze data? Or provide new visualizations? Or simulate data?
  - Try looking through the primary literature for ideas. Google Scholar or the Web of Science are good tools for exploring.


## Introduction to Python

- [ ] What is Python?
  - Interpreted, high-level language
  - Very popular among computational biologists
  - Perhaps the most "human readable" programming language
  - One of the few languages where line indentation is actually interpreted as part of the code
  - Python is _much_ less picky than bash about spacing within lines, though
  - Dynamically typed (we'll get to this later)


- [ ] Getting Python Up and Running
  - Your VM comes with Python natively as part of its Ubuntu Linux distribution
  - However, by default the name `python` is associated with version 2. In this class, we'll be using version 3.
  - To update where the name `python` points, run this command: `sudo ln -sf /usr/bin/python3.6 /usr/bin/python`
  - Now when you type `python` on the command line, you should see a line at the top indicating that you're running Python 3.6.5.
  - You are now running Python interactively!


- [ ] Basic Python Data Types
  - Numbers
    - Note that, unlike bash, Python can handle _both_ integers and floating point (decimal) numbers.
    - Integers - `myInt = 10`
    - Floating point numbers (decimals) - `myFloat = 3.21312`
    - Define myInt and myFloat as above. Now calculate `myInt / myFloat`. What type of number is the result?
    - Now try `float(myInt)` and `int(myFloat)`. What are the results? Look back at the values of `myInt` and `myFloat`. Have they changed?
    - Changing numbers from one type to another is one form of "type casting".
  - Strings - `myStr = "This is a string."`
    - Strings can be of any length, but are always defined with quotes.
    - Individual characters, or subsets of characters, can be accessed using square brackets - []
      - String indices (and all indices in Python) start at 0
      - `myStr = "biology"`
      - `myStr[0]`
      - A range of indices can be defined with a colon
      - `myStr[2:5]`
    - Strings can be concatenated together with the `+` operator.
      - `myStr = "biology"`
      - `newString = myStr + "_is_super_interesting"`
      - `newString`
  - Booleans - `True` or `False`
    - These variables can take the values `True` or `False` only.
      - `myBool = True`
    - These are the data types used in things like `if...else` statements and `while` loops.
    - Logical statements, like `myNum > 3` or `myStr == "test"`, return a boolean variable indicating the result of the comparison
    - In Python, the value of a Boolean can be reversed by preceding it with `not`.


- [ ] String Formatting
  - Python has a special way to format strings so that the values of variables can be included
  - The operator `%` is used to indicate that the values of certain variables should be used to fill in a string
  - The parts of the string where the values should go is indicated with placeholders (kinda like wildcards)
  - The three most basic placeholders are:
    - `%d` - An integer
    - `%f` - A floating point number (i.e., a decimal)
    - `%s` - A string
  - Try this:
    - `faveInt = 7`
    - `faveFloat = 3.14`
    - `faveString = phyleaux`
    - print("Favorite integer is %d, favorite float is %f, and favorite string is %s." % (faveInt,faveFloat,faveString))
  - Note how the variables holding the values are provided in the same order inside parentheses after the `%`.


- [ ] Functions
  - Functions are the verbs of a programming language
  - Functions take some variables or objects as input (arguments) and either do something with them or return a new variable/object.
  - Functions are always written like this - `myFunction(object1,object2,...)`
  - They _always_ have parentheses, even if they don't need any arguments to be passed to them
    - For example, `myFunction()`
  - The number and type of arguments needed is specific to each function
  - Perhaps the simples function to use is `print()`. `print()` can take an arbitrary number of variables as arguments and will print them to the screen.
  - Here are a few other really useful functions and what they do:
    - `len(string)` - Takes one argument (a string) and returns its length
    - `abs(number)` - Takes one argument (either an integer or a float) and returns its absolute value
    - `round(float)` - Takes one floating point number as an argument and rounds it to the nearest integer
    - `type(variable)` - Takes one variable as an argument and returns its type


- [ ] Methods
  - Methods are functions (sort of like actions or verbs) that belong to a variable
  - Methods are accessed and used by appending them to the name of a variable, separated by a `.`
  - For instance, let's say we define a string - `myStr = "biOLogy  "`. Here are some really useful methods that can be used with that string:
    - `myStr.upper()` - Converts all characters in the string to uppercase
    - `myStr.lower()` - Converts all characters in the string to lowercase
    - `myStr.strip()` - Removes whitespace from the beginning or ending of the string
    - Methods can also be chained! - `myStr.strip().lower()`
    - `myStr.replace("y","ical")` - This method functions like find and replace, where the first argument is the text to find and the second argument is the text to use when replacing.
    - `myStr.split("O")` - Breaks up the string, using the character provided as an argument as the delimiter. This method then returns a list of new strings. We'll talk more about lists later.


- [ ] Creating a Python Script
  - Python scripts can be created in a similar way to bash scripts
  - Open a blank text file and add a "shebang" line at the top
    - `#!/usr/bin/env python`
  - Add some Python code to the file
  - Print something to the screen using the `print()` command.
  - Add execute permissions to the file with `chmod`
  - Execute the script in Terminal


- [ ] Comments in Python
  - Especially now that we will be writing more complicated code, comments are essential
  - Comments are included in Python by putting a `#` at the beginning of a line.
  - Many text editors have a shortcut keystroke to toggle lines between being commented and uncommented. For instance, check the Edit menu in Atom.
  - `# This is an example of a comment`


- [ ] User Input
  - Python has a special function, `input("Message:" )`, to accept input from a user.
  - This function reads the user input and returns it. But be sure to store it in a variable!
    - `userStr = input("Input some string: ")`
  - You can use the string methods outlined above to standardize user input - like stripping out excess whitespace, changing character case, etc.


## Additional Resources
- [Python](https://www.python.org)
- [Software Carpentry - Intro. to Python](http://swcarpentry.github.io/python-novice-inflammation/)


## Week 7 Assignment (due Tuesday, Oct. 9th)
- Fork this repository, then clone it to your computer
- In the Assignments folder, add the following script.
- Remember the bash script we wrote to count the frequencies of different bases in a DNA sequence? Write a version of this program in Python that prompts the user to provide a DNA sequence and then calculates and prints the relevant values.
- Commit this script to your branch, push it to your fork, and submit a pull request.
