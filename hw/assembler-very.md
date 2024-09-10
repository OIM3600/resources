# Assembler (very comfortable version)

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to open the folder in your **VS Code**.
2. Inside `hw` folder, create a new folder `assembler-very`.
3. Within the `assembler-very` folder, create a new file, `assembler.py`. Copy the code from [`assembler.py`](./assembler/assembler-very/assembler.py) on GitHub, and paste to the `assembler.py` file you create in VS Code.
4. Within the `assembler-very` folder, create a new file, `test_assembler.py`. Copy the code from [`test_assembler.py`](./assembler/assembler-very/test_assembler.py) on GitHub, and paste to the `test_assembler.py` file you create in VS Code.

## Create an interpreter of assembler

In this task, you will build a simple interpreter for a simplified [assembler](https://en.wikipedia.org/wiki/Assembly_language). Here are the key aspects of this interpreter:

- There are multiple [registers](https://en.wikipedia.org/wiki/Processor_register) that store integer values.
- Note, the contents of all registers are not initilized before executing the program.
- The interpreter will recognize and process the following `program` instructions:
  - `mov x y` - copies `y` (either a constant integer value or the content of a register) into register `x`.
  - `inc x` - increases the content of the register `x` by one
  - `dec x` - increases the content of the register `x` by one
  - `jnz x y` - jumps to an instruction `y` steps away (positive means forward, negative means backward, `y` can be a register or a constant), but only if `x` (a constant or a register) is not zero
- Register names are alphabetical (letters only). Constants are always integers (positive or negative).
- Note: the `jnz` instruction moves relative to itself. For example, an offset of `-1` would continue at the previous instruction, while an offset of `2` would skip over the next instruction.

Your task is to implement the `assembler` function in the `assembler.py` file. This function will take an input list containing a sequence of program instructions and execute them. The program execution continues until there are no more instructions to process, at which point it should return returns a dictionary with the contents of the registers.

## Example

```python
# input
["mov a 5"; "inc a"; "dec a"; "dec a"; "jnz a -1"; "inc a"]

# visualized:

mov a 5
inc a
dec a
dec a
jnz a -1
inc a
```
The above code will:

- set register `a` to `5`,
- increase its value by `1`,
- decrease its value by `2`,
- then decrease its value until it is zero (`jnz a -1` jumps to the previous instruction if `a` is not zero)
- and then increase its value by `1`, leaving register `a` at `1`

So, the function `assembler` should return:
```python
{'a': 1}
```

## How to Test Your Code

- Simply run `assembler_test.py` in the same folder.
- You can also test your function on [Codewar](https://www.codewars.com/kata/58e24788e24ddee28e000053).

## How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.

---
_This problem is based on this [kata on Codewar](https://www.codewars.com/kata/58e24788e24ddee28e000053) which was based on the [Advent of Code 2016 - day 12](https://adventofcode.com/2016/day/12)._
