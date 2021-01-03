# Trivia Project

## Introduction
Trivia is amazing full stack web app project developed for udacity Full-Stack Developer Nanodegree Program assinment 
to train on ` API Development and Documentation` concepts.
####Travia App Features :-
1) Display questions and category. 
2) Delete questions.
3) Add questions.
4) Search for questions .
5) Play the quiz game. 


## Getting Started
### Installing Back-end Dependencies

##### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

##### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

##### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

###### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

#### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

#### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 



#### Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
### Installing Front-end Dependencies

##### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```
>_tip_: **npm i** is shorthand for **npm install**



#### Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

nally update this game play to increase the number of questions or whatever other game mechanics you decide. Make sure to specify the new mechanics of the game in the README of the repo you submit so the reviewers are aware that the behavior is correct. 

## API Referance
### Getting Start
- Base URL : At present this app can only be run locally and not hosted as a base URL . The backend app is hosted at the default , `http://127.0.0.1:5000`,The frontend app is hosted at the default , `http://127.0.0.1:3000`
- Authentication : This version of the application does not require authentication or API Keys.
### Error Handling 
Errors are returned as JSON objects in the following format :
```
{
      'success': False,
      'error': 404,
      'message':'resource not found'
}
```
The API will return three error types when requests fail:

- 400: bad request
- 404: resource not found
- 405: method not allowe
- 422: unprocessable
### Endpoint 
#### GET /categories
- General:
    - Returns a list of categories objects, success value.
- Sample:
    - `curl http://127.0.0.1:5000/categories`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```
#### GET /questions
- General:
    - Returns success value , a list of questions objects, total number of questions and a list of categories objects .
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: 
    - `curl http://127.0.0.1:5000/questions`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 22
}
```
####DELETE /questions/{question_id}
- General:
    - Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value.
```
{
  "delete": "22",
  "success": true
}
```
####POST /questions
- General:
    - Creates a new question using the submitted question, answer , category and difficulty. Returns created quistion id  , success value.
- Sample:
    - ` curl -i -X POST -H "Content-Type: application/json" -d "{\"question\":\"test q\",\"answer\":\"test a\",\"category\":1,\"difficulty\":5}" http://127.0.0.1:5000/questions`
```
{
  "create": 21 ,
  "success": true
}
```
####POST /questions/search
- General:
    - search for  questions matches with searchTerm  using searchTerm and current category if null that mean all categories . Returns success value , a list of questions objects, total number of questions .
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

- Sample:
    - ` curl -i -X POST -H "Content-Type: application/json" -d "{\"searchTerm\":\"title\" , \"currentCategory\": null}" http://127.0.0.1:5000/questions/search`
```
                                                                                                                                             
{                                                                                                                                            
  "currentCategory": null,                                                                                                                   
  "questions": [                                                                                                                             
    {                                                                                                                                        
      "answer": "Maya Angelou",                                                                                                              
      "category": 4,                                                                                                                         
      "difficulty": 2,                                                                                                                       
      "id": 5,                                                                                                                               
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"                                                       
    },                                                                                                                                       
    {                                                                                                                                        
      "answer": "Edward Scissorhands",                                                                                                       
      "category": 5,                                                                                                                         
      "difficulty": 3,                                                                                                                       
      "id": 6,                                                                                                                               
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"            
    }                                                                                                                                        
  ],                                                                                                                                         
  "success": true,                                                                                                                           
  "total_questions": 2                                                                                                                       
}                                                                                                                                            
                                                                                                                                             
```
#### GET /categories/<cat_id>/questions
- General:
    - Get questions of category use cat_id,  Returns success value , a list of questions based on category  , total number of questions , current_category .
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: 
    - `curl http://127.0.0.1:5000/categories/1/questions`
```
{                                                                          
  "current_category": "1",                                           
  "questions": [                                                           
    {                                                                      
      "answer": "The Liver",                                               
      "category": 1,                                                       
      "difficulty": 4,                                                     
      "id": 20,                                                            
      "question": "What is the heaviest organ in the human body?"          
    },                                                                     
    {                                                                      
      "answer": "Alexander Fleming",                                       
      "category": 1,                                                       
      "difficulty": 3,                                                     
      "id": 21,                                                            
      "question": "Who discovered penicillin?"                             
    },                                                                     
    {                                                                      
      "answer": "test a",                                                  
      "category": 1,                                                       
      "difficulty": 5,                                                     
      "id": 24,                                                            
      "question": "test q"                                                 
    },                                                                     
    {                                                                      
      "answer": "test2 a",                                                 
      "category": 1,                                                       
      "difficulty": 5,                                                     
      "id": 25,                                                            
      "question": "test2 q"                                                
    },                                                                     
    {                                                                      
      "answer": "test2 a",                                                 
      "category": 1,                                                       
      "difficulty": 5,                                                     
      "id": 33,                                                            
      "question": "test2 q"                                                
    },                                                                     
    {                                                                      
      "answer": "test2 a",                                                 
      "category": 1,                                                       
      "difficulty": 5,                                                     
      "id": 35,                                                            
      "question": "test2 q"                                                
    }                                                                      
  ],                                                                       
  "success": true,                                                         
  "total_questions": 6                                                     
}                                                                          
```
####POST /quizzes
- General:
    -  get questions to play the quiz using category and previous question . Returns success value ,a random questions within the given category, 
  if provided, and that is not one of the previous questions .
- Sample
    - `curl -i -X POST -H "Content-Type: application/json" -d "{\"quiz_category\":{\"type\": \"Science\", \"id\": \"1\"},\"previous_questions\":[1,2]}" http://127.0.0.1:5000/quizzes`
 ```
{
  "question": {
    "answer": "The Liver",
    "category": 1,
    "difficulty": 4,
    "id": 20,
    "question": "What is the heaviest organ in the human body?"
  },
  "success": true
}
``` 
##Authors
Ahmed Hamouda
