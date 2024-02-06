0. Basic Flask app
mandatory
First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).
1. Basic Babel setup
mandatory
Install the Babel Flask extension:
$ pip3 install flask_babel==2.0.0
Then instantiate the Babel object in your app. Store it in a module-level variable named babel.
In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].
Use Config to set Babel’s default locale ("en") and timezone ("UTC").
Use that class as config for your Flask app.
2. Get locale from request
mandatory
Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.
3. Parametrize templates
mandatory
Use the _ or gettext function to parametrize your templates. Use the message IDs home_title and home_header.
4. Force locale with URL parameter
mandatory
In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.
In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.
Now you should be able to test different translations by visiting http://127.0.0.1:5000?locale=[fr|en].
5. Mock logging in
mandatory
Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.
6. Use user locale
mandatory
Change your get_locale function to use a user’s preferred local if it is supported.
The order of priority should be
Locale from URL parameters
Locale from user settings
Locale from request header
Default locale
Test by logging in as different users
7. Infer appropriate time zone
mandatory
Define a get_timezone function and use the babel.timezoneselector decorator.
The logic should be the same as get_locale:
Find timezone parameter in URL parameters
Find time zone from user settings
Default to UTC
Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use pytz.timezone and catch the pytz.exceptions.UnknownTimeZoneError exception.
8. Display the current time
#advanced
Based on the inferred time zone, display the current time on the home page in the default format. For example:
Jan 21, 2020, 5:55:39 AM or 21 janv. 2020 à 05:56:28
