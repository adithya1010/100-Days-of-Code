<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><blockquote>
<p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>
<p><strong>Day-66-11th Dec 2023-Up⬆️ or Down⬇️?</strong></p>
<h2 id="up⬆️-or-down⬇️--a-website-to-check-if-other-websites-are-up⬆️-or-down⬇️">Up⬆️ or Down⬇️?- A website to check if other websites are Up⬆️ or Down⬇️</h2>
<p><img src="https://i.imgur.com/LDzUqWk.png" alt="Up or Down site"><br>
A Mini-Project done by Adithya S.T. as part of Intern-Hiring Process by Kalvium</p>
<p>I’m attaching this within my 100 Days of Code repo as this Project/Task can be dealt with Python</p>
<p><strong>Technologies used:</strong></p>
<ul>
<li>PyCharm</li>
<li>Firefox</li>
<li>Python</li>
<li>Flask</li>
<li>Jinga</li>
<li>BootStrap</li>
<li>SQLite</li>
<li>WTForms</li>
<li>SQLAlchemy</li>
</ul>
<h2 id="📝problem-statement">📝Problem Statement</h2>
<p>Build a service uptime app. The user can enter URLs. The backend checks these endpoints at a specific interval, and reports if the site is UP (status code 2xx) or DOWN (any other status code). Build a simple view that shows the current status of all endpoints entered.</p>
<h2 id="⚒️working">⚒️Working</h2>
<p><strong>Home Page:</strong></p>
<p><img src="https://i.imgur.com/FFuhpPw.gif" alt="Up or Down site"></p>
<p>This is the Home page of the Site<br>
Here the User can enter the URL of the Site that they want to know the Status of</p>
<p><strong>Status Checker:</strong></p>
<p>If the site is up and running and returns a status code of 200 the site will display that the site is Up⬆️</p>
<p><img src="https://i.imgur.com/JW3Kaq8.gif" alt="Site-Up Image"></p>
<p>If the Site is Down or it returns a status code other than 200 then the website will display that the Site is Down⬇️</p>
<p><img src="https://i.imgur.com/FFuhpPw.gif" alt="Site-Down Image"></p>
<p><strong>Status of All Checker:</strong></p>
<p>To Check the Current Status of all sites so far entered the User can click on Check All Sites where it shows the current status of the sites entered so far in a Table Format</p>
<p><img src="https://i.imgur.com/ugzxWy3.png" alt="Status of all entered page"></p>
<h2 id="📺video-explanation">📺Video Explanation</h2>
    <a href="https://1drv.ms/u/s!Am-eVTSjDSr6gtNNBg-oefwWD5v_og?e=ahW4tm">Link to OneDrive Videos</a>

<h2 id="🧑‍💻code-explanation">🧑‍💻Code Explanation</h2>
<p><strong>Imports:</strong></p>
<p><img src="https://i.imgur.com/g8KgwW1.png" alt="Import"></p>
<p>Importing the required packages such as Flask, Flask-BootStrap, Flask-SQLAlchemy, Flask-WTF, requests module to implement in the Project</p>
<p><strong>Initializing the app:</strong></p>
<p><img src="https://i.imgur.com/BejAvlB.png" alt="Init"></p>
<p>Initializing the app for Flask and also applying BootStrap to the same. Also initializing the database-websites-collection.db under the instance folder of the project using SQLAlchemy</p>
<p><img src="https://i.imgur.com/xyuDKok.png" alt="instance"></p>
<p><strong>Creating a New Table within the DB:</strong></p>
<p>Creating a new table within the DB using SQLAlchemy</p>
<p><img src="https://i.imgur.com/dhFUd3P.png" alt="create table"></p>
<p>Creating a new Form to be used in Home page of the app using Flask-WTForms</p>
<p><img src="https://i.imgur.com/ADvPoFG.png" alt="Form"></p>
<p><strong>Home Page:</strong></p>
<p>At home page the index.html is rendered as well as the form which asks the user to enter the URL</p>
<p><img src="https://i.imgur.com/I6jy2i9.png" alt="Home Page code"></p>
<p><strong>index.html:</strong></p>
<p>At the index.html the home page and it’s content are displayed as well as the form that has passed on over using Flask-WTForms and Jinga</p>
<p><img src="https://i.imgur.com/OgyhDvM.png" alt="index.html"></p>
<p><strong>Home Page-POST:</strong></p>
<p><img src="https://i.imgur.com/62i9PTQ.png" alt="post-home"></p>
<p>When the user clicks on the submit buttin the form’s data is stored in a variable and the url entered is then obtained from it</p>
<p>The site then makes a GET Request to the site and gets the status code</p>
<p>If the status code is obtained then it is printed in the console as well as the site status is updated as Up</p>
<p>If the status code is not obtained then the site status is updated as Down</p>
<p>The DB is updated with the url and it’s current status code and is reflected on the DB</p>
<p><strong>Data on the DB viewed using DB Browser:</strong></p>
<p><img src="https://i.imgur.com/ErDzfRb.png" alt="DB view here"></p>
<p>The site status is then passed on to the status.html file to be displayed there</p>
<p><strong>status.html file:</strong></p>
<p>The passed on status is displayed here in a if clause using Jinga<br>
If the site status is Up then the corresponding status , message and GIF are displayed</p>
<p>Same goes for Down<br>
<img src="https://i.imgur.com/OLKSU9j.png" alt="status.html"></p>
<p><strong>Up:</strong></p>
<p><img src="https://i.imgur.com/SPHLJtR.png" alt="Site-Up Image"></p>
<p><strong>Down:</strong></p>
<p><img src="https://i.imgur.com/XW4eykQ.png" alt="Site-Down Image"></p>
<p>The user can then check the status of all sites entered so far by clicking on the Check All Sites Button</p>
<p><strong>Check Page:</strong></p>
<p><img src="https://i.imgur.com/YTdqN5E.png" alt="Check function"></p>
<p>In the check function the data entered so far in the DB is fetched using a query and also the urls and the ids entered</p>
<p>For every url and id the URL entered is checked everytime the check url is called and the new status is then reflected in the DB using the update function of SQLAlchemy</p>
<p>The data in the DB is then passed on to the check.html file</p>
<p><strong>check.html:</strong></p>
<p><img src="https://i.imgur.com/wk69pam.png" alt="check.html"></p>
<p>In the check.html file the contents of the DB that was passed on is then displayed in a table format for the user</p>
<p>The user has the option to click on Go back to Home to start the process all over again</p>
<h2 id="🔍proof-of-work">🔍Proof of Work</h2>
<p>My Proof of Work is the very Repo in which this Project resides</p>
<p>Currently I’m doing the 100 Days of Code Challenge where I try my best to do a Project every day by learning new tech/implementations in Python</p>
<p>I have extensively used memes as part of the Project also as a proof as my previous projects also contain similar memes which I personally like and not someone else’s</p>
<p>I also used my <a href="https://adithya1010.notion.site/100-Days-of-Code-504b2b4887434c2c802e5c6a97002d62">Notion file</a> where I have stored all the code that I have done for this challenge to use as reference point to complete this Project</p>
<p>You can also check my Twitter profile for the latest projects/updates that I do:</p>
<p><img src="https://gtce.itsvg.in/api?username=adithya_st" alt="">](<a href="https://github.com/VishwaGauravIn/github-twitter-card-embed">https://github.com/VishwaGauravIn/github-twitter-card-embed</a>)</p>
<p>Thanks for giving me this opportunity to showcase my Skills. This is my very first Project that I’m submitting as part of a selection process and the experience has taught me many invaluable lessons. Once again Thanking anyone and everyone for this opportunity🙏.</p>
</div>
</body>

</html>
