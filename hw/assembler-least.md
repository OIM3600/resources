# Assembler

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to oplen the folder in your **VS Code**.
2. In VS Code, create a new folder `assembler-least`. 
3. Under `assembler-least` folder, create a new file, `assembler.py`. Copy the code from [`assembler.py`](./assembler-least/assembler.py) on GitHub, and paste to the `assembler.py` file you create in VS Code.
3. Under `assembler-least` folder, create a new file, `test_assembler.py`. Copy the code from [`test_assembler.py`](./assembler-least/test_assembler.py) on GitHub, and paste to the `test_assembler.py` file you create in VS Code.

## Create an interpreter of assembler

In this task, you will build a straightforward interpreter for a very simplified [assembler](https://en.wikipedia.org/wiki/Assembly_language). Here are the key aspects of this interpreter:

- There is a single [register](https://en.wikipedia.org/wiki/Processor_register) that stores an integer value, which you can think of as a variable of type `int`.
- Initially, the register's content is set to `0`.
- The interpreter will recognize and process the following `program` instructions:
  - `inc` - This instruction increases the register's content by one.
  - `dec` - This instruction decreases the register's content by one.

Your task is to implement the `assembler` function in the `assembler.py` file. This function will take an input list containing a sequence of program instructions and execute them. The program execution continues until there are no more instructions to process, at which point it should return an integer representing the final content of the register.


## Example

```
# input
['dec', 'inc', 'dec', 'dec', 'dec', 'inc']

# visualized:
dec
inc
dec
dec
dec
inc
```
The above code will (remember the initial value of register is `0`):
- decrease its value by 1,
- increase its value by 1,
- decrease its value by 1,
- decrease its value by 1,
- decrease its value by 1,
- increase its value by 1
  
So, the function `assembler` should return the register value:
```
-2
```

## How to Test Your Code

- Simply run `assembler_test.py` in the same folder.

# How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.

---
_This problem is based on this [kata on Codewar](https://www.codewars.com/kata/58e24788e24ddee28e000053) which was based on the [Advent of Code 2016 - day 12](https://adventofcode.com/2016/day/12)._