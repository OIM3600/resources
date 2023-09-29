# Nutrition (more comfortable version)

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to oplen the folder in your **VS Code**.
2. In VS Code, create a new folder `nutrition-more`. Then, under `nutrition-more` folder, create a new file, `nutrition.py`.


## Nutrition Facts

The U.S. Food & Drug Adminstration (FDA) offers [downloadable/printable posters](https://www.fda.gov/food/food-labeling-nutrition/nutrition-information-raw-fruits-vegetables-and-fish) that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.” 

You can find the number of calories in one portion of each fruit, per the [FDA’s poster for fruits](https://cs50.harvard.edu/python/2022/psets/2/nutrition/Nutrition-Information-for-Raw-Fruits---small-PDF-Poster.pdf), which is also [available as text](https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version). Actually [this version](../code/data/nutrition_list.txt) might be easier to parse/use. 


## Total Calories

In a file called `nutrition.py`, implement a program that prompts the user for fruits, one per line, until the user enters "`done`". Then output the user’s fruit list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. And last line shows the total calories. No need to pluralize the items. Treat the user’s input case-insensitively.

Here’s how the program might work:

```shell
> python nutrition.py
banana
apple
banana
avocado
done

1 APPLE
1 AVOCADO
2 BANANA
TOTAL CALORIES: 400
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

- Run your program with python `nutrition.py`. Type `peach` and press Enter, then type `strawberries` and press Enter, then type `done` and press Enter. Your program should output:
    ```py
    1 PEACH
    1 STRAWBERRIES
    TOTAL CALORIES: 110
    ```
- Run your program with python `nutrition.py`. Type `Avocado` and press Enter, then type `Avocado` again and press Enter, then type `done` and press Enter. Your program should output:
    ```py
    2 AVOCADO
    Calories: 100
    ```

# How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.