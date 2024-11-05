# Final Project Instructions

## Project Overview

This final project offers an opportunity to apply the knowledge you’ve learned throughout our course "**Computer Science for Business Students**" by building a dynamic web application. Using FastAPI or Flask for the backend and HTML/CSS/JavaScript for the frontend, you’ll create an engaging app that interacts with users through input forms, integrates external APIs, and, for those up to the challenge (*yes, the more comfortable version*), optionally connects to a database for data persistence and more.

Think of this project as a canvas to demonstrate your skills and understanding of course concepts. Explore your creativity while meeting the foundational requirements, and enjoy bringing your ideas to life! Have fun!

---

## Skills and Learning Outcomes

Through this project, you will strengthen both technical and foundational skills that are essential in computer science and business applications:

- **Python Proficiency:** Enhance your Python programming skills, emphasizing data handling, processing, and logical operations.
- **Web Development with Modern Web Framework:** Build a responsive and interactive web application using either FastAPI or Flask.
- **API Integration:** Demonstrate the ability to connect to external APIs, retrieve data, and display it in the application.
- **Database Management (Optional):** Gain experience with database and SQL for storing and retrieving information.
- **Problem-Solving and Computational Thinking:** Apply computational thinking to decompose problems, design solutions, and implement algorithms effectively.
- **Creative Problem-Solving with GenAI:** Utilize GenAI tools such as ChatGPT for innovative problem-solving, exploring new APIs, and enhancing project features.
- **Collaboration:** Develop teamwork and communication skills, especially when working in pairs, to manage project responsibilities and workflows effectively.
- **Git/GitHub Proficiency:** Demonstrate version control skills with well-maintained GitHub repositories, practicing collaborative development and code management.

---

## Teamwork Guidelines

- **You can choose to work individually or in pairs.**
- If you choose to work in pairs:
  - Clearly define and document each member's responsibilities.
  - Collaborate effectively, using tools like GitHub issues and pull requests.
  - Both team members are accountable for the entire project and will receive the same grade unless discrepancies in contribution are evident.

---

## Requirements

### 1. Project Topic

- The project can be on any topic of your choice.
- Choose a topic that aligns with your interests and showcases your skills.
- Example Project Ideas:
  - **Weather Web App**: Build a web application that fetches and displays weather information based on user input.
  - **Country Trivia Quizzes**: Create a website that quizzes users on various facts about countries. Include a leader board that displays high scores and optionally, store quiz results in a database for later review.
  - **TV Tracker**: Create a TV tracking app that logs and displays users' favorite and watched TV and related information.
  - **E-commerce Platform**: Create a simple e-commerce site with product listings and a shopping cart.
  - **Telegram/Slack/Discord Bot**: Implement functionalities such as natural language processing to understand user queries. Use external APIs to provide dynamic and informative responses. (You don't have to use FastAPI/Flask for this project idea.)

### 2. FastAPI/Flask Web Application

- The project must be implemented as a web application using either FastAPI or Flask.
- Utilize FastAPI/Flask features such as routing, rendering templates, get and process form data and global variables.
- (Optional) Enable cookies, sessions, and connection with database.
- Quickstart tutorials:
  - [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
  - [Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
  - **Suggestion**: Follow every single step in this tutorial. Replicate all the code. Make the server run!

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
- Documentation:
  - Write docstrings for all functions and classes, following the [PEP 257](https://peps.python.org/pep-0257/) conventions.
  - Include comments to explain complex logic or important decisions in your code.
- Error Handling (Optional):
  - Implement robust error handling to manage unexpected inputs, API failures, or exceptions gracefully.
  - Provide informative feedback to users when errors occur.

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
- **Note**: Do not commit API keys or any sensitive credentials to your GitHub repository. Use environment variables or configuration files (e.g, `.env` file) that are excluded from version control (e.g., using a .gitignore file). Include instructions in your `README.md` on how to set up these variables.

### 4. Frontend (HTML/CSS/JavaScript)

Your application should include a user-friendly interface developed with HTML, CSS, and JavaScript. It should be responsive and accessible, providing a seamless user experience.

Suggestions for the frontend in FastAPI/Flask:

- Organize your static files (CSS, JavaScript, images) in a dedicated `static` directory.
- Use your framework's method for serving static files.
  - [FastAPI Static Files](https://fastapi.tiangolo.com/tutorial/static-files/)
  - [Flask Static Files](https://flask.palletsprojects.com/en/3.0.x/quickstart/#static-files)

### 5. Database (Optional)

- Integrate a database for persistent data storage. SQLite3 is recommended for simplicity.
- Store relevant information in the database and retrieve/display it within the application.
- Examples:
  - Use `shows.db` (or [TMDB API](https://developer.themoviedb.org/reference/intro/getting-started)) for creating "The Office Trivia Game".
  - Use `songs.db` (or [Spotify API](https://developer.spotify.com/documentation/web-api)) for finding user's favorite songs/artists.
  - Create your own database and table(s) for storing user information and other data.

### 6. Git/GitHub

- Each student or team should create a new **public** GitHub repository for the project.
- The repository should be well-organized with clear documentation and a `README.md` file.- Use a `.gitignore` file to exclude unnecessary or sensitive files from your repository (e.g., virtual environment directories, `.env` files, compiled files).
- Ensure only essential files are committed to keep your repository clean.

### 7. GenAI

You are encouraged to use GenAI tools like ChatGPT to assist with your project:

- Brainstorm ideas for your project, refine your project scope, and explore creative features.
- Explore additional APIs and Python libraries that are not covered in the course.
- Help for debugging purposes, seeking assistance in identifying and resolving issues in your code.
- Improve your project's `README.md` file by generating clear and concise instructions, and articulate complex concepts in a user-friendly manner.

**Note**: When using GenAI tools such as ChatGPT:

- Do not submit AI-generated code as your own without understanding and testing it.
- Properly cite any significant assistance received from AI tools in your `README.md` file.
- Ensure that all submitted work reflects your own understanding and effort.

### 8. Testing and Quality Assurance (Optional)

- Implement testing strategies (e.g., unit tests, integration tests) to ensure your application functions correctly.
- Include any test cases or instructions for running tests in your `README.md`.
- Demonstrating testing practices can enhance your project's evaluation.

### 9. Deploy on Cloud/Platform (Optional)

- Deploy your FastAPI/Flask web application on a cloud/platform such as [PythonAnywhere](https://www.pythonanywhere.com/details/flask_hosting), [Heroku](https://devcenter.heroku.com/categories/python-support), or [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-app-using-gunicorn-to-app-platform).

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

Reflect on the project experience, focusing on both the **process** and **learning** perspectives. Consider what went well, challenges faced, and how this experience can benefit you in future projects. While the reflection can cover any aspects meaningful to you, feel free to draw insights from areas such as project planning, problem-solving, or using GenAI tools like ChatGPT.

**Note**:

- Begin by including the names of all team members at the top of the document.
- Keep the `README.md` clear and concise.

---

## Evaluation Criteria

Projects will be evaluated based on the following criteria:

- **Functionality**: Does the web application perform as intended, with user input, API integration, and optional database functionality?
- **Documentation**: Do all the functions and classes have docstrings? Does your code provide commented where necessary? Is the `README.md` file comprehensive, providing clear instructions for running the application and understanding your code? Is your reflection demonstrating your insight into challenges, solutions, and personal growth?
- **Code Styles**: Is your code formatted, well-structured and readable? Does it adhere to PEP 8 styling guidelines? Does it follow best practices? Do functions and variables have meaningful names?
- **Creativity**: Are there unique features or creative elements in the project that go beyond the basic requirements?

Read more about [Code Grading Rubric](https://github.com/OIM3600/resources/blob/main/code_grading_rubric.md).

---

## How to Submit

- Push your completed code, including the updated `README.md`, to your **public** GitHub repository.
- Each team member must submit the project's GitHub repository URL on Canvas.
- In the submission comments on Canvas, specify the names of all team members.
- **Note:** All team members must individually submit and include the same information.

## Submission Deadline

Please refer to Canvas for the due date.

---

*Updated:* *2024/11/05*
