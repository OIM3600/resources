# Credit

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to oplen the folder in your **VS Code**.
2. In VS Code, create a new folder `credit`. Then, under `mario-less` folder, create a new file, `credit.py`.

## Credit Cards

A credit (or debit) card, of course, is a plastic card with which you can pay for goods and services. Printed on that card is a number that’s also stored in a database somewhere, so that when your card is used to buy something, the creditor knows whom to bill. There are a lot of people with credit cards in this world, so those numbers are pretty long: American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. And those are decimal numbers (0 through 9), not binary, which means, for instance, that American Express could print as many as 10^15 = 1,000,000,000,000,000 unique cards! (That’s, um, a quadrillion.)

Actually, that’s a bit of an exaggeration, because credit card numbers actually have some structure to them:

- All American Express numbers start with 34 or 37; 
- Most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we won’t concern ourselves with for this problem);  
- All Visa numbers start with 4. 


But credit card numbers also have a **“checksum”** built into them, a mathematical relationship between at least one number and others. That checksum enables computers (or humans who like math) to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a database, which can be slow. Of course, a dishonest mathematician could certainly craft a fake number that nonetheless respects the mathematical constraint, so a database lookup is still necessary for more rigorous checks.
Luhn’s Algorithm

So what’s the secret formula? Well, most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:

- Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
- Add the sum to the sum of the digits that weren’t multiplied by 2.
- If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!

That’s kind of confusing, so let’s try an example with a Visa card: 4003600000000014.

1. For the sake of discussion, let’s first underline every other digit, starting with the number’s second-to-last digit:
   
    <u>4</u>0<u>0</u>3<u>6</u>0<u>0</u>0<u>0</u>0<u>0</u>0<u>0</u>0<u>1</u>4

    Okay, let’s multiply each of the underlined digits by 2:

    1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

    That gives us:

    2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

    Now let’s add those products’ digits (i.e., not the products themselves) together:

    2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

2. Now let’s add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting from the end):

    13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

    Yup, the last digit in that sum (20) is a 0, so this card is legit!

So, validating credit card numbers isn’t hard, but it does get a bit tedious by hand. Let’s write a program.

## Implementation Details

In the file called `credit.py` in the `credit` directory, write a program that prompts the user for a credit card number and then reports whether it is a valid American Express, MasterCard, or Visa card number, per the definitions of each’s format herein. So that we can automate some tests of your code, we ask that your program’s last line of output be `AMEX` or `MASTERCARD` or `VISA` or `INVALID`, nothing more, nothing less.

Consider the below representative of how your own program should behave when passed a valid credit card number (sans hyphens).

```shell
> python credit.py
Number: 4003600000000014
VISA
```

It needs to reject hyphens (and more):

```shell
> python credit.py
Number: 4003-6000-0000-0014
Number: foo
Number: 4003600000000014
VISA
```

It’s up to you to catch inputs that are not credit card numbers (e.g., a phone number), even if numeric:

```shell
> python credit.py
Number: 6176292929
INVALID
```

Test out your program with a whole bunch of inputs, both valid and invalid. (We certainly will!) Here are a few card numbers that PayPal recommends for testing.

If your program behaves incorrectly on some inputs (or doesn’t compile at all), time to debug!


# How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.