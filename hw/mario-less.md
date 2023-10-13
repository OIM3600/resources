# Mario (less comfortable version)

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to open the folder in your **VS Code**.
2. In VS Code, create a new folder `mario-less`. Then, under `mario-less` folder, create a new file, `mario.py`.


## World 1-1

Toward the end of World 1-1 in Nintendo’s Super Mario Brothers, Mario must ascend right-aligned pyramid of blocks, a la the below.

<img src="images/mario-pyramid-less.png" height="200" alt="Mario (less)" />

Let’s recreate that pyramid in Python, albeit in text, using hashes (#) for bricks, a la the below. Each hash is a bit taller than it is wide, so the pyramid itself will also be taller than it is wide.

```shell
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

The program we’ll write will be called `mario`. And let’s allow the user to decide just how tall the pyramid should be by first prompting them for a positive integer between, say, 1 and 8, inclusive.

Here’s how the program might work if the user inputs `8` when prompted:

```shell
> python mario.py
Height: 8
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

Here’s how the program might work if the user inputs `4` when prompted:

```shell
> python mario.py
Height: 4
   #
  ##
 ###
####
```

And here’s how the program might work if the user inputs `1` when prompted:

```shell
> python mario.py
Height: 1
#
```

If the user doesn’t, in fact, input a positive integer between `1` and `8`, inclusive, when prompted, the program should re-prompt the user until they cooperate:

```shell
> python mario.py
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #
  ##
 ###
####
```
# Very Detailed Step-by-Step Instructions

## Pseudocode

Create a new file, `pseudocode.txt` inside folder `mario-less`. Write in `pseudocode.txt` some pseudocode that implements this program, even if not (yet!) sure how to write it in code. There’s no one right way to write pseudocode, but short English sentences suffice. Odds are your pseudocode will use (or imply using!) one or more functions, conditionals, Boolean expressions, loops, and/or variables.

<details>
<summary>(Spoiler Warning!) Hints:</summary>
  
There’s more than one way to do this, so here’s just one!

1. Prompt user for height
2. If height is less than 1 or greater than 8 (or not an integer at all), go back one step
3. Iterate from 1 through height:
   1. On iteration i, print i hashes and then a newline

It’s okay to edit your own after seeing this pseudocode here, but don’t simply copy/paste ours into your own (because this pseudocode actually is **NOT** made for Python.)
  
</details>


## Prompting for Input

Whatever your pseudocode is, let’s first write only the Python code that prompts (and re-prompts, as needed) the user for input. 

Now, modify `mario.py` in such a way that it prompts the user for the pyramid’s height, storing their input in a variable, re-prompting the user again and again as needed if their input is not a positive integer between `1` and `8`, inclusive. Then, simply print the value of that variable, thereby confirming (for yourself) that you’ve indeed stored the user’s input successfully, a la the below.

```shell
> python mario.py
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
Stored: 4
```

## Building the Opposite

Now that your program is (hopefully!) accepting input as prescribed, it’s time for another step.

It turns out it’s a bit easier to build a left-aligned pyramid than right-, a la the below.

```shell
#
##
###
####
#####
######
#######
########
```

So let’s build a left-aligned pyramid first and then, once that’s working, right-align it instead!

Modify `mario.py` at right such that it no longer simply prints the user’s input but instead prints a left-aligned pyramid of that height.


<details>
<summary>(Spoiler Warning!) Hints:</summary>

- Keep in mind that a hash (`#`) is just a character like any other, so you can print it with `print`.
Just as Scratch has a `repeat` block, so does Python have a `for` loop, via which you can iterate some number times. Perhaps on each iteration, you could print that many hashes?

You can actually “nest” loops, iterating with one variable (e.g., `i`) in the “outer” loop and another (e.g., `j`) in the “inner” loop. For instance, here’s how you might print a square of height and width `n`, below. Of course, it’s not a square that you want to print!

```python
for i in range(n):
    for j in range(n):
        print('#', end='')
    print('\n')
```

</details>

## Right-Aligning with Dots

Let’s now right-align that pyramid by pushing its hashes to the right by prefixing them with dots (i.e., periods, `.`), a la the below.

```shell
.......#
......##
.....###
....####
...#####
..######
.#######
########
```

Modify `mario.py` in such a way that it does exactly that!

<details>

<summary>(Spoiler Warning!) Hints:</summary>

Notice how the number of dots needed on each line is the “opposite” of the number of that line’s hashes. For a pyramid of height 8, like the above, the first line has but 1 hash and thus 7 dots. The bottom line, meanwhile, has 8 hashes and thus 0 dots. Via what formula (or arithmetic, really) could you print that many dots?

</details>


## How to Test Your Code

Does your code work as prescribed when you input

- `-1` (or other negative numbers)?
- `0`?
- `1` through `8`?
- `9` or other positive numbers?
- letters or words?
- no input at all, when you only hit Enter?

## Removing the Dots

All that remains now is a finishing flourish! Modify `mario.py` in such a way that it prints spaces instead of those dots!

## Easy? Let's try something else

- Search how to use f-string, which could make your code shorter and easier to understand.
- Try [Mario (more comfortable version)](mario-more.md).

# How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.