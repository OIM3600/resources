# Vanity Plates (less comfortable version)

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to oplen the folder in your **VS Code**.
2. Inside `hw` folder, create a new folder `plates-less`. Within the `plates-less` folder, create a new file, `plates.py`.

## Vanity Plates

In Massachusetts, it's possible to [request a vanity license plate](https://www.mass.gov/how-to/request-a-vanity-license-plate) for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

- All vanity plates must start with at least two letters.
- … vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
- Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable Passenger vanity plate; AAA22A would not be acceptable. The first number used cannot be a "0".
- No periods, spaces, or punctuation marks are allowed.

In `plates.py`, implement a program that prompts the user for a vanity plate and then output `Valid` if meets all of the requirements or `Invalid` if it does not. Assume that any letters in the user's input will be uppercase. Structure your program per the below, wherein `is_valid` returns `True` if `s` meets all requirements and `False` if it does not. Assume that `s` will be a `str`. You're welcome to implement additional functions for `is_valid` to call (e.g., one function per requirement).

```py
def is_valid(s):
    """"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()
```

<details>
<summary>Hints:</summary>

1. Recall that a `str` comes with quite a few [methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
2. Much like a `list`, a str is a “sequence” (of characters), which means it can be [sliced](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) into shorter strings with syntax like `s[i:j]`. For instance, if `s` is `"OIM3600"`, then `s[0:3]` would be `"OIM"`.
  
</details>

## How to Test

Here's how to test your code manually:

- Type `BABSON` and press Enter. Your program should output:
    ```python
    Valid
    ```
- Type `OIM360` and press Enter. Your program should output:
    ```python
    Valid
    ```

- Type `OIM036` and press Enter. Your program should output:
    ```python
    Invalid
    ```

- Type `OIM36X` and press Enter. Your program should output
    ```python
    Invalid
    ```

- Type `OIM.36` and press Enter. Your program should output
    ```python
    Invalid
    ```

- Type `BAB ON` and press Enter. Your program should output
    ```python
    Invalid
    ```

- Type `BABSONCOLLEGE` and press Enter. Your program should output
    ```python
    Invalid
    ```

## How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.
