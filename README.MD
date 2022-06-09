It will be a pet project.
Small version of instagram made with Pythons framework FLASK.

It will contain:
- User registration
- User logining
- User authentication
- User can create post with photos
- Followers
- Likes
- And many other


## Setup
To run this project, install Python 3.9 or newest from [Python.org](https://www.python.org/downloads/).

If Python exists:

* Choose directory where you will store this app
* Run
    ```
    $ git clone https://github.com/Viposha/iflask.git
    ```
* For next stage you should create venv (virtual environment):
    ```
    $ python3 -m venv venv
    ```
* And activate venv:

    For Windows:
    ```
    $ venv\Scripts\activate
    ```
    
    For Linux or macOS:
    ```
    $ source venv/bin/activate
    ```
    
To remind you that you have activated a virtual environment, the activation command 
modifies your command prompt to include the name of the environment:

   ```
    (venv) $
   ```  

* Install all packages from requirements.txt with this command:
    ```
    $ pip install -r requirements.txt
    ```
* And finally launch script:
    ```
    $ python iflask.py
    ```
If everything is alright you will see such result:
```
 * Serving Flask app 'iflask' (lazy loading)
 * Environment: production                                                         
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.                                           
 * Debug mode: on                                                                  
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat                                   
 * Debugger is active!
```
Go to your browser and enter this URL
```
http://127.0.0.1:5000 
```
