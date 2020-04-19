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
  
DAY-9
Task 1 - Create a database table
Created columns according to the fields I mentioned in registration.html along with their data types in a python file.
I had fields like username,email,city and password and I made username as primary key.
Later database connection has been established which has the schema I created.

Time elapsed for this task: 30mins

Task 2 - Insert records
After creating the database I have used self which is used to access the attributes of the class.
Later on I used db.session.add() to add the user details to the table in the database.
Since, I have made the username as the primary key. If any user tries to give the same username then it displays a message that the user already exists and doesn’t add the user details to the database.
If the username is unique then it displays “Successfully Registered” and adds the data to the database.

Time elapsed for this task: 40mins

Task 3 - Retrieve data from a database table
Here I created a new html for admin which is used to get the user info to be displayed.
In my python file where I created columns for the table I also added a timestamp so that I get the time and date when the user has registered.
 And also I have a new route for admin.
Here the data will be retrieved from the table.
render_template  for this route which helps to access the html and send it to the browser the user details which I retrieved from the database.

 Time elapsed for this task :40mins



