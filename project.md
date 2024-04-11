# Final Term Project Instructions

## Project Overview

In this final term project, you'll have the chance to reinforce and apply the knowledge learned throughout the course "Computer Science for Business Students." Your task is to craft a dynamic web application using Flask for the back end and HTML/CSS/JavaScript for the front end. This application should engage users through input forms, connect to external APIs, and, for those up to the challenge (yes, the more comfortable version), integrate optional database connectivity to ensure data persistence.

Consider this project as your canvas to exhibit your understanding of course concepts in a practical context. Embrace your creativity and curiosity while ensuring the project fulfills its foundational requirements. Enjoy it!

---

## Skills Emphasized

- **Web Development with Flask**: Focus on building a responsive and interactive web application using Flask.
- **API Integration**: Demonstrate the ability to connect to external APIs, retrieve data, and display it in the application.
- **Python**: Emphasize using Python for efficient data processing and logical operations.
- **Database** (Optional): Showcase skills in database and SQL for storing and retrieving information.
- **Problem Solving with ChatGPT**: Utilize ChatGPT for creative problem-solving, exploring new APIs, and improving project features.
- **Collaboration**: For those working in pairs, emphasize effective collaboration and communication in project development.
- **Git/GitHub Proficiency**: Showcase version control skills through well-maintained GitHub repositories.

---

## Requirements

### 1. Project Topic

- The project can be on any topic of your choice.
- Choose a topic that aligns with your interests and showcases your skills.
- Example Project Ideas:
  - **Weather Web App**: Build a web application that fetches and displays weather information based on user input.
  - **Country Trivia Quizzes**: Create a website that quizzes users on various facts about countries. Include a leaderboard that displays high scores and optionally, store quiz results in a database for later review.
  - **TV Tracker**: Create a TV tracking app that logs and displays users' favorite and watched TV and related information.
  - **E-commerce Platform**: Create a simple e-commerce site with product listings and a shopping cart.
  - **Telegram/Slack/Discord Bot**: Implement functionalities such as natural language processing to understand user queries. Use external APIs to provide dynamic and informative responses. (You don't have to use Flask for this project idea.)

### 2. Flask Web Application

- The project must be implemented as a Flask web application.
- Utilize Flask features such as routing, rendering templates, get and process form data and global variables.
- (Optional) Enable cookies, sessions, and connection with database.
- Flask Quickstart: Read the following sections of [Flask Quickstart documentation](https://flask.palletsprojects.com/en/3.0.x/quickstart/):
  - A Minimal Application
  - Debug Mode
  - Routing
    - Variable Rules
    - Unique URLs / Redirection
    - Behavior
    - URL Building
    - HTTP Methods
  - Static Files
  - Rendering Templates
  - Redirects and Errors
  **Suggestion**: Follow every single step in this tutorial. Replicate all the code. Make the server run!

### 3. Python

Implement Python functions or modules to achieve the following:

- Data Handling:
  - Make sure the user's input or external data is organized and ready for use.
- Make Decisions:
  - Implement logical operations to make dynamic decisions.
- Algorithmic Processing:
  - Apply Python to use algorithms, like sorting or searching, making your app work better.
- Data Transformation:
  - Choose the best data structures for your data to work with external APIs or databases.
- Computational Operations:
  - Solve complex math problems to support features like predictions or analytics.
- Integration with External Libraries:
  - Integrate external Python libraries for specialized functionalities, exploring and incorporating tools that extend the capabilities of your application beyond basic Python.
- Data Validation:
  - Ensure the integrity and correctness of data.

### 4. API Integration

- Incorporate at least one external API to retrieve data dynamically.
- Example APIs:
  - [Rest Countries](https://restcountries.com/)
  - [Yahoo! Finance](https://github.com/ranaroussi/yfinance)
  - [OpenWeather](https://openweathermap.org/api)
  - [JokeAPI](https://v2.jokeapi.dev/)
  - Many more:
    - [GitHub repository - Public APIs](https://github.com/public-apis/public-apis)
    - [RapidAPI - Discover More APIs](https://rapidapi.com/hub)
    - [ApiVault](https://apivault.dev/)
    - [APIs.guru](https://apis.guru/)

### 5. Database (Optional)

- Integrate a database for persistent data storage. SQLite3 is recommended for simplicity.
- Store relevant information in the database and retrieve/display it within the application.
- Examples:
  - Use `shows.db` (or [TMDB API](https://developer.themoviedb.org/reference/intro/getting-started)) for creating "The Office Trivia Game".
  - Use `songs.db` (or [Spotify API](https://developer.spotify.com/documentation/web-api)) for finding user's favorite songs/artists.
  - Create your own database and table(s) for storing user information and other data.

### 6. Collaboration

- You can choose to work individually or in pairs.
- Clearly define individual responsibilities for collaborative projects.

### 7. Git/GitHub

- Each student or team should create a new **public** GitHub repository for the project.
- The repository should be well-organized with clear documentation and a `README.md` file.

### 8. ChatGPT

- As part of the project, you are encouraged to use ChatGPT to explore additional APIs and Python libraries not covered in the course.
- Utilize ChatGPT for debugging purposes, seeking assistance in identifying and resolving issues in your code.
- Leverage ChatGPT to improve your project's README file by generating clear and concise instructions. Use it to articulate complex concepts in a user-friendly manner.

### 9. Deploy on Cloud/Platform (Optional)

- Deploy your Flask web application on a cloud/platform such as [PythonAnywhere](https://www.pythonanywhere.com/details/flask_hosting), [Heroku](https://devcenter.heroku.com/categories/python-support), or [DigitalOcean](https://www.digitalocean.com/community/tutorial-series/how-to-create-web-sites-with-flask).

---

## Project Writeup and Reflection

Write a summary of your project and your reflections on it in [`README.md`](README.md), using [Markdown format](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) (1 per team, not 1 per person). The [`README.md`](README.md) file should include the following sections:

### 1. Project Overview

- Briefly describe the purpose and functionality of your web application.

### 2. Usage Guidelines

- Explain how users can interact with your application, including any input requirements or steps to follow.

### 3. Dependencies

- List any external libraries, APIs, tools and database that your project depends on.

### 4. Project Structure

- Give a high-level overview of your project's structure, outlining key files and directories.

### 5. Collaboration Information (if applicable)

- If you collaborated on the project, specify how collaboration was managed, including roles and responsibilities.

### 6. Acknowledgments

- Credit any external resources, libraries, or APIs that you used in your project.

### 7. Reflection

After you finish the project, reflect on:

- From the **process** point of view, what went well, what challenges that were faced and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped you succeed.

- From a **learning** perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed.

**Note**:

- Begin by including the names of all team members at the top of the document.
- Keep the `README.md` clear and concise.

---

## Evaluation Criteria

Projects will be evaluated based on the following criteria:

- **Functionality**: Does the web application perform as intended, with user input, API integration, and optional database functionality?

- **Code Quality**: Is the code well-structured, readable, and follows best practices?

- **Documentation**: Is the `README` file comprehensive, providing clear instructions for running the application and understanding the codebase? Is your reflection demonstrating your insight into challenges, solutions, and personal growth?

- **Creativity**: Are there unique features or creative elements in the project that go beyond the basic requirements?

Read more about [Code Grading Rubric](https://github.com/OIM3600/resources/blob/main/code_grading_rubric.md).

---

## How to Submit

1. Push your completed code, including updated `README.md`, to GitHub repository. Make sure it is public.
2. Submit project's GitHub repository URL to Canvas. In the comment area on Canvas, specify names of all team members. **Note: Everyone in the team needs to submit on Canvas and add comment.**
