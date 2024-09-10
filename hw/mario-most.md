# Mario (most comfortable version)

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to open the folder in your **VS Code**.
2. In VS Code, check if there is already a folder named `hw`. If it doesn't exist, create one. Otherwise, move to the next step.
3. Inside the `hw` folder, create a new folder `mario-most`. Within the `mario-most` folder, create a new file, `mario.py`.

## World ✕

In a twist on Mario’s adventures, imagine Mario encountering a mysterious grid filled with blocks. To navigate through, Mario needs to draw an "✕" on the grid, marking his path from corner to corner.

Let's recreate this "✕" in Python, using `■` (solid block) and `□` (empty block) for the grid. The program we’ll write will be called `mario`, and it will allow the user to input an odd integer `n` (where n >= 3) to determine the size of the grid.

Here's how the program might work if the user inputs `5` when prompted:

```shell
> python mario.py
Size: 5
■□□□■
□■□■□
□□■□□
□■□■□
■□□□■
```

Here’s how the program might work if the user inputs `3` when prompted:

```shell
> python mario.py
Size: 3
■□■
□■□
■□■
```

If the user doesn’t input an odd integer greater than or equal to 3, the program should re-prompt the user until they provide a valid input:

```shell
> python mario.py
Size: 4
Size: 8
Size: 5
■□□□■
□■□■□
□□■□□
□■□■□
■□□□■
```

Notice that the diagonal lines of the "✕" are made up of `■`, while the spaces in between are filled with `□`.

Open your `mario.py` file to implement this problem as described!

## How to Test Your Code

Does your code work as prescribed when you input

- An even number like `4`?
- A number less than `3`?
- An odd number like `5`, `7`, or larger?
- Letters or words?
- No input at all, when you only hit Enter?

## Easy? Let's try something else

- Search how to use f-string, which could make your code shorter and easier to understand.
- Try to create functions to wrap up some logical code blocks.
- Try to create different shapes or patterns.

## How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.

---
_This problem is based on this [kata on Codewar](https://www.codewars.com/kata/5906436806d25f846400009b)._
