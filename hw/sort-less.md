# Sort (less comfortable version)

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to open the folder in your **VS Code**.
2. Inside `hw` folder, create a new folder `sort-less`. Within the `sort-less` folder, create a new file, `sort.py`. Copy the code from [`sort.py`](./sort-less/sort.py) on GitHub, and paste to the `sort.py` file you create in VS Code.
3. Within the `sort-less` folder, create a new file, `answers.md`. Copy the code from [`answers.md`](./sort-less/answers.md) on GitHub, and paste to the `answers.md` file you create in VS Code.
4. Download `sort.zip` file from [`sort.zip`](./sort-less/sort.zip) on GitHub. Extract all the files from `sort.zip` into the `data` folder, which should be inside the main `OIM3600` folder. Make sure all the `.txt` files are **directly** inside the **`"data"`** folder (not the `"sort-less"` folder or `"data/sort"` folder).

## Background

Recall from lecture that we saw a few algorithms for sorting a sequence of numbers: selection sort, bubble sort, and merge sort.

- **Selection sort** iterates through the unsorted portions of a list, selecting the smallest element each time and moving it to its correct location.
- **Bubble sort** compares pairs of adjacent values one at a time and swaps them if they are in the incorrect order. This continues until the list is sorted.
- **Merge sort** recursively divides the list into two repeatedly and then merges the smaller lists back into a larger one in the correct order.

## Instructions (Very simple!)

1. Read `sort.py` and run the file. Make sure no other applications are running during its execution. Note: Some algorithms may take very long time (more than 1 minute) to complete.
2. Paste the terminal output into `answers.md` inside the "Output" section.
3. Explain the differences in running times for different datasets and sorting algorithms in the "Result Analysis" section of `answers.md`.

## How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.
