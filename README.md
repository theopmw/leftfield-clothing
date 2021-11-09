## **Site Goals**

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development Diploma, specifically for the **Full Stack Frameworks** module. The objective of this project is to "build a full-stack site based around business logic used to control a centrally-owned dataset". The site features an authentication mechanism and provides paid access to the site's data based on the dataset, such as the purchase of a product.

## **UX**

### User Stories

#### As a user, I would like to:

**Viewing and Navigation**

- [x] View a list of available products

- [x] View a specific category of products

- [x] View details of an individual product, including name, price, description, rating, image and sizes if applicable

- [x] Identify sale items and special offers

- [x] Easily review the total of my purchases

**Registration and User Accounts**

- [x] Easily register an account

- [x] Easily login/logout

- [x] Easily recover my password if I lose access to my account

- [x] Receive an email confirmation on successful registration of an account

- [x] Have a personal user profile to view my order history and save my personal information

**Sorting and Searching**

- [x] Sort the list of available products by best rated, best priced, or by category

- [x] Sort products within a specific category by name, price or rating

- [x] Sort multiple categories of products simultaneously across broad categories such as clothing or footwear or hats

- [x] Search for a product by name, description or brand

- [x] Easily see what I have searched for and the number of results

**Purchasing and Checkout**

- [x] Easily select the size and quantity of a product when purchasing

- [x] View the items in my bag

- [x] View the total cost of items in my bag

- [x] View the total shipping cost of my order

- [x] Adjust the quantity of individual items in my bag

- [x] Easily enter my payment information

- [x] Know that my personal information and payment details are secure

- [x] View an order confirmation after checkout

- [x] Receive a confirmation email after checkout

#### As an admin, I would like to:

**Admin and Store Management**

- [x] Add a product

- [x] Edit/update a product

- [x] Delete a product

Possible additions:

- [x] See which products are being viewed the most

- [x] See product sales volumes to see which products are selling best

## Technologies Used

### Languages Used

* HTML
* CSS
* JavaScript
* Python

### Frameworks & Libraries and Tools Used

* [Gitpod](https://gitpod.io/) - **Gitpod** was used for the IDE while building the website.
* [Git](https://git-scm.com/) - **Git** was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) - **GitHub** is used to store the projects code after being pushed from Git.
* [Heroku](https://id.heroku.com/login) - **Heroku** was used as the deployment platform for this project.
* [Bootstrap 4](https://getbootstrap.com/) - **Bootstrap** was used to assist with the responsiveness and styling of the website.
* [JQuery](https://jquery.com/) - **JQuery** JavaScript library was used to simplify JavaScript code.
* [Django](https://www.djangoproject.com/) - **Django** high-level Python web framework was used to speed up and simplify the application build.
* [Stripe](https://stripe.com/en-gb) - **Stripe** was used to process online payments and webhooks.
* [AWS](https://aws.amazon.com/?nc2=h_lg) - **AWS** used for storage of static and media files using [S3](https://aws.amazon.com/s3/) and [IAM](https://aws.amazon.com/iam/) services.
* [Autopep8](https://pypi.org/project/autopep8/) - **Autopep8** used to format Python code to be PEP8 compliant.
* [Favicon.io](https://favicon.io/) - **Favicon.io** was used to create the favicon for the website.
* [Font Awesome](https://fontawesome.com/) - **Font Awesome** was used on all pages throughout the website to add icons for aesthetic and UX purposes.
* [Google Fonts](https://fonts.google.com/) - **Google Fonts** were used to import the fonts into the application to style the fonts used on all pages of the project.
* [Balsamiq](https://balsamiq.com/) - **Balsamiq** was used to create the wireframes during the design process.
* [Web Formatter](https://webformatter.com/) - **Web Formatter** was used to beautify code.
* [Am I Responsive](http://ami.responsivedesign.is/) - **Am I Responsive** was used to test page layouts during the build process.
[GMail](https://gmail.com) - **Gmail** was used to provide the SMPT server, allowing the application to handle emails.
* [PostgreSQL](https://www.postgresql.org/) - **PostgreSQL used for the relational database, hosted and deployed via Heroku.

## Testing

Detailed testing information can be found in separate [TESTING.md](https://github.com/theopmw/leftfield-clothing/blob/main/TESTING.md) file.

## Git and Version Control

This project is managed using Git version control system.

For each meaningful change made, Git is used to stage, commit and push the files to the [Recipe Box repository](https://github.com/theopmw/recipe-box) on GitHub.

For each change made, the following process was followed, a description of the different commands used throughout the project and their uses has also been provided:

* Staging:
    * When a file has been modified and it must be marked to go it to your next commit.
    * To check the status of your Git repository, including files that are not staged and files that are staged, the ```git status``` command is used.
    * To stage modified files, the ```add``` command is used, which can be run multiple times before a commit. 
        * You can either specify the specific file with ```add```. For example: "```git add my_file.html```". Or add stage all files in the current directory with "```git add .```".
        * You can also remove files from staging without losing the changes made to the file using ```reset```. For example: "```git reset my_file.html```".
* Committing:
    * Once updates have been staged, you are ready to commit them, which will record the changes made to the repository.
    * Run the ```commit``` command to commit staged files, a meaningful commit message must be included to track commits. For example: "```git commit -m "Meaningful commit message" "```.
    * You can stage and commit all tracked files with a condensed message: "```git commit -am "Meaningful commit message" "```.
    * The commit message can be modified using the ```--amend``` flag. For example: "```git commit --amend -m "New commit message""```.
* Pushing:
    * Once files have been committed and a commit message has been provided, they are pushed to the remote repository using the ```push``` command.
    * "```git push```" will transmit the local commits to the remote repository.

Git branching was also utilised to isolate the production of new features and merge them with the master branch throughout the development cycle of the project.

* Branches
    * New branches were created using ```git branch new-branch```.
    * ```git switch new-branch``` was used to switch to the new branch.
    * A feature was then worked on in the new branch and modifications were staged, committed and pushed.
    * ```git switch master``` was used to switch back to the master branch.
    * The branch was then merged with the master using ```git merge new-branch```
    * When the branch had been merged with the master and was no longer needed, ```git branch -d new-branch``` was used to delete the branch.

Parts of this section used the following article for reference: [How To Use Git: A Reference Guide](https://dev.to/digitalocean/how-to-use-git-a-reference-guide-6b6).