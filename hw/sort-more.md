# Sort (more comfortable version)

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to open the folder in your **VS Code**.
2. In VS Code, create a new folder `sort-more`. Then, under `sort-more` folder, create a new file, `sort.py`. 
3. Under `sort-more` folder, create a new file, `answers.md`. Copy the code from [`answers.md`](./sort-more/answers.md) on GitHub, and paste to the `answers.md` file you create in VS Code.
4. Download `sort.zip` file from [`sort.zip`](./sort-more/sort.zip) on GitHub. Extract all the files from `sort.zip` into the `data` folder, which should be inside the main `OIM3600` folder. Make sure all the `.txt` files are **directly** inside the **`"data"`** folder (not the `"sort-more"` folder or `"data/sort"` folder).


## Background

Recall from lecture that we saw a few algorithms for sorting a sequence of numbers: selection sort, bubble sort, and merge sort.

- **Selection sort** iterates through the unsorted portions of a list, selecting the smallest element each time and moving it to its correct location.
- **Bubble sort** compares pairs of adjacent values one at a time and swaps them if they are in the incorrect order. This continues until the list is sorted.
- **Merge sort** recursively divides the list into two repeatedly and then merges the smaller lists back into a larger one in the correct order.


## Instructions

1. Create functions in `sort.py` to implement different sorting algorithms (**selection sort**, **bubble sort**, and **merge sort**) on the given different types of data (lists of numbers/integers).
2. You have access to multiple `.txt` files located in the `data` folder. These files contain datasets with `n` lines of values, which may be either **reversed**, **shuffled**, or **sorted**. For example, `reversed10000.txt` contains `10000` lines of numbers in reversed order, while `random10000.txt` contains `10000` lines of numbers in random order.
3. Implement timing functionality in your code to measure the execution time for each sorting algorithm on different datasets. Hint: Import the `time` module and use `time.time()` to record the start and end times.

### Expected Output (Note: the running time will vary):
```shell
> python sort.py
Now sorting random5000.txt
Selction Sorting running time: 0.4596219062805176s
Bubble Sorting running time: 1.0479307174682617s
Merge Sorting running time: 0.008079767227172852s

Now sorting random10000.txt
Selction Sorting running time: 1.5340986251831055s
Bubble Sorting running time: 3.8899996280670166s
Merge Sorting running time: 0.01825714111328125s

Now sorting random50000.txt
Selction Sorting running time: 39.33838772773743s
Bubble Sorting running time: 106.02403545379639s
Merge Sorting running time: 0.10869359970092773s

Now sorting sorted5000.txt
Selction Sorting running time: 0.3858189582824707s
Bubble Sorting running time: 0.0s
Merge Sorting running time: 0.005162715911865234s

Now sorting sorted10000.txt
Selction Sorting running time: 1.5648293495178223s
Bubble Sorting running time: 0.0s
Merge Sorting running time: 0.01197957992553711s

Now sorting sorted50000.txt
Selction Sorting running time: 39.07032632827759s
Bubble Sorting running time: 0.0018961429595947266s
Merge Sorting running time: 0.07236528396606445s

Now sorting reversed5000.txt
Selction Sorting running time: 0.42821192741394043s
Bubble Sorting running time: 1.3187551498413086s
Merge Sorting running time: 0.006318092346191406s

Now sorting reversed10000.txt
Selction Sorting running time: 1.6181821823120117s
Bubble Sorting running time: 5.162095308303833s
Merge Sorting running time: 0.011089801788330078s

Now sorting reversed50000.txt
Selction Sorting running time: 43.05371356010437s
Bubble Sorting running time: 137.666246175766s
Merge Sorting running time: 0.0695810317993164s
```

# How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.