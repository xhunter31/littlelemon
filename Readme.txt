When you submit your assignment, other learners in the course will review and grade your work. They will evaluate the following:

Does the web application use Django to serve static HTML content?
>For validation go to http://127.0.0.1:8000/restaurant/

Has the learner committed the project to a Git repository?

Does the application connect the backend to a MySQL database?
>add your mySql details in the databases section in settings.py file

Are the menu and table booking APIs implemented?
Menu
>http://127.0.0.1:8000/restaurant/menu/
Gets all menu items
>http://127.0.0.1:8000/restaurant/menu/<int:pk>/
Get the menu item defined by integer specified in url

Booking
>http://127.0.0.1:8000/restaurant/booking/
The default basic root view for DefaultRouter
>http://127.0.0.1:8000/restaurant/booking/tables/
The booking details can be accessed via the above. It requires the a bearer token for authentication.

Is the application set up with user registration and authentication?
>http://127.0.0.1:8000/auth/
The default basic root view for DefaultRouter
>127.0.0.1:8000/auth/users/
You can use the above for user registration to register username and password.
>http://127.0.0.1:8000/restaurant/api-token-auth/
POST Request : Using Postman/Insomnia client, you can get your bearer token for a registered user from the above endpoint. Specify the username and password in the body with below json format.
{"username":"<your-username>","password":"<your-password"}


Does the application contain unit tests?
Added test_models.py file under tests folder in the root directory. You can run the test by executing ("python manage.py test tests.test_models")

Can the API be tested with the Insomnia REST client?
You can test the API using Insomnia REST client as mentioned above