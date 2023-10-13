# Nutrition (less comfortable version)

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to open the folder in your **VS Code**.
2. In VS Code, create a new folder `nutrition-less`. Then, under `nutrition-less` folder, create a new file, `nutrition.py`.


## Nutrition Facts

The U.S. Food & Drug Adminstration (FDA) offers [downloadable/printable posters](https://www.fda.gov/food/food-labeling-nutrition/nutrition-information-raw-fruits-vegetables-and-fish) that "show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores."

In a file called `nutrition.py`, implement a program that prompts users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the [FDA’s poster for fruits](https://cs50.harvard.edu/python/2022/psets/2/nutrition/Nutrition-Information-for-Raw-Fruits---small-PDF-Poster.pdf), which is also [available as text](https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version). Actually [this version](../code/data/nutrition_list.txt) might be easier to parse/use. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., `strawberries`, not `strawberry`). Ignore any input that isn’t a fruit.


Here’s how the program might work if the user inputs `apple` when prompted:

```shell
> python nutrition.py
Fruit: apple
Calories: 130
```

<details>
<summary>Hints:</summary>

1. Rather than use a conditional with 20 Boolean expressions, one for each fruit, better to use a `dict` to associate a fruit with its calories!
2. If `k` is a str and `d` is a dict, you can check whether `k` is a key in `d` with code like:
    ```py
    if k in d:
        ...
    ```
3. Take care to output the fruit’s calories, not calories from fat!

  
</details>

## How to Test

Here's how to test your code manually:

- Run your program with python `nutrition.py`. Type `Apple` and press Enter. Your program should output:
    ```py
    Calories: 130
    ```
- Run your program with python `nutrition.py`. Type `Avocado` and press Enter. Your program should output:
    ```py
    Calories: 50
    ```
- Run your program with python `nutrition.py`. Type `Sweet Cherries` and press Enter. Your program should output
    ```py
    Calories: 100
    ```
- Run your program with python `nutrition.py`. Type `Tomato` and press Enter. Your program should output nothing.


Be sure to try other fruits and vary the casing of your input. Your program should behave as expected, case-insensitively.

# How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.