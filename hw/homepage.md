# Homepage

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to open the folder in your **VS Code**.
2. Inside `hw` folder, create a new folder `homepage`. Within the `homepage` folder, create `.html`, `.css`, `.js` files following the instructions.

## Background

The internet has enabled incredible things: we can use a search engine to research anything imaginable, communicate with friends and family members around the globe, play games, take courses, and so much more. But it turns out that nearly all pages we may visit are built on three core languages, each of which serves a slightly different purpose:

- HTML, or *HyperText Markup Language*, which is used to describe the content of websites;
- CSS, Cascading Style Sheets, which is used to describe the aesthetics of websites; and
- JavaScript, which is used to make websites interactive and dynamic.

Create a simple homepage that introduces yourself, your favorite hobby or extracurricular, or anything else of interest to you.

## Specification

Implement in your homepage directory a website that must:

- Contain at least **two** different `.html` pages, at least one of which is `index.html` (the main page of your website), and it should be possible to get from any page on your website to any other page by following one or more hyperlinks.
- Use at least eight (8) distinct HTML tags besides `<html>`,`<head>`, `<body>`, and `<title>`. Using some tag (e.g., `<p>`) multiple times still counts as just one (1) of those eight!
- Integrate one or more features from Bootstrap into your site. Bootstrap is a popular library (that comes with lots of CSS classes and more) via which you can beautify your site. See Bootstrap’s documentation to get started. In particular, you might find some of Bootstrap’s components of interest. To add Bootstrap to your site, it suffices to include
    ```html
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    ```
    in your pages’ `<head>`, below which you can also include
    ```html
    <link href="styles.css" rel="stylesheet">
    ```
    to link your own CSS.

- Have at least one **stylesheet** file of your own creation, `styles.css`, which uses at least five (5) different CSS selectors (e.g. tag (`example`), class (`.example`), or ID (`#example`)), and within which you use a total of at least five (5) different CSS properties, such as `font-size`, or `margin`; and
- Integrate one or more features of **JavaScript** into your site to make your site more interactive. For example, you can use JavaScript to add alerts, to have an effect at a recurring interval, or to add interactivity to buttons, dropdowns, or forms. Feel free to be creative!
- Ensure that your site looks nice on browsers both on mobile devices as well as laptops and desktops.

## Assessment

Your site’s correctness will be assessed based on whether you meet the requirements of the specification as outlined above, and whether your HTML is well-formed and valid. To ensure that your pages are, you can use this [Markup Validation Service](https://validator.w3.org/#validate_by_input), copying and pasting your HTML directly into the provided text box. Take care to eliminate any warnings or errors suggested by the validator before submitting!

Consider also:

- whether the aesthetics of your site are such that it is intuitive and straightforward for a user to navigate;
- whether your CSS has been factored out into a separate CSS file(s); and
- whether you have avoided repetition and redundancy by “cascading” style properties from parent tags.

## Hints

For fairly comprehensive guides on the languages introduced in this problem, check out these tutorials:

- HTML
  - [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML), [W3S](https://www.w3schools.com/html/)
- CSS
  - [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS), [W3S](https://www.w3schools.com/css/)
- JavaScript
  - [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [W3S](https://www.w3schools.com/js/)

## How to Submit

- Save all the files opened in VS Code. Format your code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.
- (Optional) When you finish, copy and paste all the files to the other repository (`<your-github-id.github.io>`), commit and push to GitHub, and wait one or two minutes. Congratulations, your personal website is now published!
