# Exploring World Countries with Countries API

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to open the folder in your **VS Code**.
2. Inside `hw` folder, create a new folder `countries`. Within the `countries` folder, create a new file, `countries.py`.

## Exploring World Countries with Countries API

### **Objective:**

In this assignment, you will explore the REST Countries API to retrieve information about various countries and perform creative tasks using Python and data structures.

### Instructions:

1. API Setup

    - Go to the Countries API documentation: [REST Countries API](https://restcountries.com/). Read the documentation to understand how to make API requests and what data you can retrieve.

2. Required Python Functions:

   - `get_country_info(country_name)`: This function should take a country name as input, make an API request to retrieve information about that country, parse the JSON response, and return a dictionary containing relevant information such as the country's name, capital, population, area, and list of languages spoken.
   - `display_country_info(country_info)`: This function should take the dictionary returned by `get_country_info` and display the information in a creative and visually appealing way. You can simply pretty-print the dictionary using `pprint` module, or generate ASCII art representing the country's flag or create a simple graphical representation of its data.

3. Select one of the following functions or unleash your creativity to create any function by utilizing the information retrieved from this API. Make sure that you include a docstring explaining the function's purpose and usage.

   - `quiz_random_country()`: This function should randomly select a country, retrieve its information using `get_country_info`, and then ask the user a quiz question about that country's facts (e.g., capital, population, or language spoken). Provide feedback on the user's answers.
   - `get_neighboring_countries(country_name)`: This function should take a country name as input, retrieve the list of neighboring countries using the API, and return a list of neighboring country names.
   - `how_many_countries_between(start_country_name, end_country_name)`: This function should calculate the number of countries that lie between the two given countries. Note: this one may be challenging, primarily because it involves finding a path or route through a potentially complex network of countries.
   - `suggest_travel_destination()`: This function should suggest a random travel destination based on the country's data (e.g., suggest a country with a small population for a quiet getaway or a country with a rich history for a historical trip).

## How to Submit

- Before submitting, please read Code [Grading Rubric](https://github.com/OIM3600/resources/blob/main/code_grading_rubric.md).
- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.
