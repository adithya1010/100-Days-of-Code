


> Written with [StackEdit](https://stackedit.io/).
> 
**Day-66-11th Dec 2022-Up⬆️ or Down⬇️?**

## Up⬆️ or Down⬇️?- A website to check if other websites are Up⬆️ or Down⬇️

![Up or Down site](https://i.imgur.com/LDzUqWk.png)
A Mini-Project done by Adithya S.T. as part of Intern-Hiring Process by Kalvium

I'm attaching this within my 100 Days of Code repo as this Project/Task can be dealt with Python

**Technologies used:**

 - PyCharm
 - Firefox
 - Python
 - Flask
 - Jinga
 - BootStrap
 - SQLite
 - WTForms
 - SQLAlchemy

## 📝Problem Statement
Build a service uptime app. The user can enter URLs. The backend checks these endpoints at a specific interval, and reports if the site is UP (status code 2xx) or DOWN (any other status code). Build a simple view that shows the current status of all endpoints entered.

## ⚒️Working

**Home Page:**

![Up or Down site](https://i.imgur.com/FFuhpPw.gif)

This is the Home page of the Site
Here the User can enter the URL of the Site that they want to know the Status of

**Status Checker:**

If the site is up and running and returns a status code of 200 the site will display that the site is Up⬆️

![Site-Up Image](https://i.imgur.com/JW3Kaq8.gif)

If the Site is Down or it returns a status code other than 200 then the website will display that the Site is Down⬇️

![Site-Down Image](https://i.imgur.com/FFuhpPw.gif)

**Status of All Checker:**

To Check the Current Status of all sites so far entered the User can click on Check All Sites where it shows the current status of the sites entered so far in a Table Format

![Status of all entered page](https://i.imgur.com/ugzxWy3.png)

## 📺Video Explanation
**Video-1:**
<iframe src="https://onedrive.live.com/embed?cid=FA2A0DA334559E6F&resid=FA2A0DA334559E6F%2143467&authkey=AN8jN-CEvALIz_8" width="320" height="180" frameborder="0" scrolling="no" allowfullscreen></iframe>
<br>

**Video-2:**
<iframe src="https://onedrive.live.com/embed?cid=FA2A0DA334559E6F&resid=FA2A0DA334559E6F%2143466&authkey=AGvBnXex0eaUBpk" width="320" height="180" frameborder="0" scrolling="no" allowfullscreen></iframe>

## 🧑‍💻Code Explanation

**Imports:**

![Import](https://i.imgur.com/g8KgwW1.png)

Importing the required packages such as Flask, Flask-BootStrap, Flask-SQLAlchemy, Flask-WTF, requests module to implement in the Project

**Initializing the app:**

![Init](https://i.imgur.com/BejAvlB.png)

Initializing the app for Flask and also applying BootStrap to the same. Also initializing the database-websites-collection.db under the instance folder of the project using SQLAlchemy

![instance](https://i.imgur.com/xyuDKok.png)

**Creating a New Table within the DB:**

Creating a new table within the DB using SQLAlchemy 

![create table](https://i.imgur.com/dhFUd3P.png)

Creating a new Form to be used in Home page of the app using Flask-WTForms

![Form](https://i.imgur.com/ADvPoFG.png)

**Home Page:**

At home page the index.html is rendered as well as the form which asks the user to enter the URL

![Home Page code](https://i.imgur.com/I6jy2i9.png)

**index.html:**

At the index.html the home page and it's content are displayed as well as the form that has passed on over using Flask-WTForms and Jinga

![index.html](https://i.imgur.com/OgyhDvM.png)

**Home Page-POST:**

![post-home](https://i.imgur.com/62i9PTQ.png)

When the user clicks on the submit buttin the form's data is stored in a variable and the url entered is then obtained from it

The site then makes a GET Request to the site and gets the status code

If the status code is obtained then it is printed in the console as well as the site status is updated as Up

If the status code is not obtained then the site status is updated as Down

The DB is updated with the url and it's current status code and is reflected on the DB

**Data on the DB viewed using DB Browser:**

![DB view here](https://i.imgur.com/ErDzfRb.png)

The site status is then passed on to the status.html file to be displayed there

**status.html file:**

The passed on status is displayed here in a if clause using Jinga
If the site status is Up then the corresponding status , message and GIF are displayed

Same goes for Down
![status.html](https://i.imgur.com/OLKSU9j.png)

**Up:**

![Site-Up Image](https://i.imgur.com/SPHLJtR.png)

**Down:**

![Site-Down Image](https://i.imgur.com/XW4eykQ.png)

The user can then check the status of all sites entered so far by clicking on the Check All Sites Button

**Check Page:**

![Check function](https://i.imgur.com/YTdqN5E.png)

In the check function the data entered so far in the DB is fetched using a query and also the urls and the ids entered

For every url and id the URL entered is checked everytime the check url is called and the new status is then reflected in the DB using the update function of SQLAlchemy

The data in the DB is then passed on to the check.html file

**check.html:**

![check.html](https://i.imgur.com/wk69pam.png)

In the check.html file the contents of the DB that was passed on is then displayed in a table format for the user

The user has the option to click on Go back to Home to start the process all over again

## 🔍Proof of Work

My Proof of Work is the very Repo in which this Project resides

Currently I'm doing the 100 Days of Code Challenge where I try my best to do a Project every day by learning new tech/implementations in Python

I have extensively used memes as part of the Project also as a proof as my previous projects also contain similar memes which I personally like and not someone else's

I also used my [Notion file](https://adithya1010.notion.site/100-Days-of-Code-504b2b4887434c2c802e5c6a97002d62) where I have stored all the code that I have done for this challenge to use as reference point to complete this Project

You can also check my Twitter profile for the latest projects/updates that I do:

![](https://gtce.itsvg.in/api?username=adithya_st)](https://github.com/VishwaGauravIn/github-twitter-card-embed)

Thanks for giving me this opportunity to showcase my Skills. This is my very first Project that I'm submitting as part of a selection process and the experience has taught me many invaluable lessons. Once again Thanking anyone and everyone for this opportunity🙏.


