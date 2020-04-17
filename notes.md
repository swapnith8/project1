DAY-7
Task 1 - Postgresql:
Created an account in Heroku and created a new app named ”project-2019501087”
Selected "Hobby Dev" plan for free access of PostgreSQL database.
In settings there are my credentials and there was a URL through which I accessed my database locally in my system.

Time elapsed for this task : 15-20mins


Task 2 - Python and Flask:
Since I already have python and pip. I directly downloaded project1 from the given link which contained application.py, books.csv, readme.md and requirements.txt files. .   
Through running the command "pip3 install -r requirements.txt" in the command prompt the requirements given in that text files are read.
Then I tried to run flask using command "flask run" then I got a http request link which tried to open in chrome but got an error.
So, I used these commands 
 1. pip3 uninstall werkzeug
 2. pip3 install werkzeug==0.16.0
i.e., I have uninstalled the werkzeug old version and installed the required one.
After this again I tried opening the http link in chrome this time I got it correct
I.e; it displayed "Project 1: TODO"!

Time elapsed for this task : 50-60mins


Task 3 - Goodreads API:

Created an account in GoodReads and I got a key.
By using that API key I have created a sample file with given code in the description.
I tried executing the python file but I got an error “requests not found”.
But after I installed requests by using the command “pip install requests" in the command prompt.
After this  the python file got executed with no errors. The content got printed.

Time elapsed for this task : 30mins

DAY-8
Task 1 - Create Registration Page
Here I have started designing a web page with a registration form.
To create a form I have used tags like form, label, input, button tags.
I have also added a navigation bar using bootstrap.
I have done styling to the page using CSS.

Time elapsed for task1: 40mins

Task 2 - Add the Registration page to Flask app
Created a new route to show the registration web page when it is a GET request.
Here the function render_template( ) is used to render a jinja2 template to an HTML page.
In this I have created two folders one is templates where HTML files are stored.
Static folder to store CSS files and linked these to the html file in templates.

Time elapsed for task2:40mins

Task 3 - Submit Registration form data to the Flask app
  Here, when the user fills the form and submits.
  The details will be displayed on the page.(username,Email,city) 
   I have done this using GET,POST methods.
  In app.route both GET and POST requests can  be used by accessing those methods in the router using If-else condition.

Time elapsed for this task : 40mins
  


