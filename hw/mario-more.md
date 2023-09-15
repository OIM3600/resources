# Mario (more comfortable version)

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to oplen the folder in your **VS Code**.
2. In VS Code, create a new folder `mario-more`. Then, under `mario-more` folder, create a new file, `mario.py`.


## World 1-1

Toward the beginning of World 1-1 in Nintendo’s Super Mario Brothers, Mario must hop over adjacent pyramids of blocks, per the below.

<img src="images/mario-pyramid-more.png" height="200" alt="Mario (more)" />

Let’s recreate those pyramids in Python, albeit in text, using hashes (`#`) for bricks, a la the below. Each hash is a bit taller than it is wide, so the pyramids themselves will also be taller than they are wide.

```shell
   #  #
  ##  ##
 ###  ###
####  ####
```

The program we’ll write will be called `mario`. And let’s allow the user to decide just how tall the pyramids should be by first prompting them for a positive integer between, say, `1` and `8`, inclusive.

Here’s how the program might work if the user inputs `8` when prompted:

```shell
> python mario.py
Height: 8
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
  ######  ######
 #######  #######
########  ########
```

Here’s how the program might work if the user inputs `4` when prompted:

```shell
> python mario.py
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

Here’s how the program might work if the user inputs `2` when prompted:


```shell
> python mario.py
Height: 2
 #  #
##  ##
```

And here’s how the program might work if the user inputs `1` when prompted:


```shell
> python mario.py
Height: 1
#  #
```

If the user doesn’t, in fact, input a positive integer between `1` and `8`, inclusive, when prompted, the program should re-prompt the user until they cooperate:

```shell
> python mario.py
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

Notice that width of the “gap” between adjacent pyramids is equal to the width of two hashes, irrespective of the pyramids’ heights.

Open your `mario.py` file to implement this problem as described!



## How to Test Your Code

Does your code work as prescribed when you input

- `-1` (or other negative numbers)?
- `0`?
- `1` through `8`?
- `9` or other positive numbers?
- letters or words?
- no input at all, when you only hit Enter?


## Easy? Let's try something else

- Search how to use f-string, which could make your code shorter and easier to understand.
- Try to create functions to wrap up some logical code blocks.
- Try to create other shapes in Mario.

# How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.