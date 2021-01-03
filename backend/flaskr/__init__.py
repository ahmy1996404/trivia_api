import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  '''
    Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app, resources={r"/api/*": {"origins": "*"}})
  '''
  Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response
  '''
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_categories():
    # get all categories
    categories = Category.query.all()
    # format category {'id':'type'}
    formatted_categories = {category.id: category.type for category in categories}
    # return a Response with the JSON representation 'sucsses' and 'categrories
    return jsonify({
      'success':True,
      'categories': formatted_categories
    })


  '''
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def get_questions():
    # make the pagination for every 10 questions) the number of question variable 'QUESTIONS_PER_PAGE'
    page = request.args.get('page', 1, type=int)
    start = (page-1)*QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    # get all questions
    questions = Question.query.all()
    # format the question
    formated_questions = [question.format() for question in questions]
    # if page request  is over than  questions pages
    if (len(formated_questions[start:end]) == 0):
      abort(404)
    # get all categories
    categories = Category.query.all()
    # format categories
    formated_categories = {category.id: category.type for category in categories}
    # return a Response with the JSON representation 'sucsses' , 'questions' , 'total_questions' , 'categories'
    # and 'current_category'
    return jsonify({
      'success': True,
      'questions': formated_questions[start:end],
      'total_questions': len(formated_questions),
      'categories': formated_categories,
      'current_category': None
    })
  '''
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<question_id>', methods=['DELETE'])
  def delete_question(question_id):
    # get question that matches with question_id
    question = Question.query.get(question_id)
    # if there isnot such id with this id
    if question is None:
      abort(422)
    # if exist
    else:
      # delete this question
      question.delete()
      # return a Response with the JSON representation 'sucsses' , 'delete'
      return jsonify({
        'success': True,
        'delete': question_id
      })



  '''
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  @app.route('/questions', methods=['POST'])
  def add_question():
    # get the post request data  'question' , 'answer' , 'category' , 'difficulty'
    body = request.get_json()
    # if request missing any data
    if(not(('question' in body) or ('answer' in body) or ('category' in body) or ('difficulty' in body))):
      abort(400)
      # if empty
    if ((body.get('question') == "") or (body.get('answer') == "") or (body.get('category') == "") or (body.get('difficulty') == "")):
      abort(422)
    try:
      # create question
      question = Question(question = body.get('question', None), answer = body.get('answer', None), category = body.get('category', None),difficulty = body.get('difficulty', None))
      question.insert()
      # return a Response with the JSON representation 'sucsses' , 'create'
      return jsonify({
        'success': True,
        'create': question.id
      })
    except:
      abort(422)

  ''' 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  @app.route('/questions/search', methods=['POST'])
  def search_question():
    # get the post request data  'searchTerm'
    body = request.get_json()
    if (not (('searchTerm' in body)or('currentCategory' in body))):
      abort(400)
    search_term = body.get('searchTerm', None)
    currentCategory = body.get('currentCategory', None)
    # if empty
    if (search_term == ""):
      abort(422)
    try:
      # if currentCategory is all
      if currentCategory == None :
        search_question = Question.query.filter(Question.question.like('%'+search_term+'%')).all()
      else:
        # get questions that question contain the  search_term strings or like it and filter by currentCategory
        search_question = Question.query.filter_by(category=currentCategory).filter(Question.question.like('%'+search_term+'%')).all()
      # if there isnot question get from search
      if len(search_question) == 0:
        abort(404)
      # make the pagination for every 10 questions) the value of 'QUESTIONS_PER_PAGE' variable
      page = request.args.get('page', 1, type=int)
      start = (page - 1) * QUESTIONS_PER_PAGE
      end = start + QUESTIONS_PER_PAGE
      # format the question
      formated_questions = [question.format() for question in search_question]
      # return a Response with the JSON representation 'sucsses' , 'questions' , 'total_questions' , 'currentCategory'
      return jsonify({
        'success': True,
        'questions': formated_questions[start:end],
        'total_questions': len(search_question),
        'currentCategory':currentCategory
      })
    except:
      abort(404)

  '''
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<cat_id>/questions')
  def get_questions_by_cat(cat_id):

    # get the  questions filtered by category
    questions = Question.query.filter_by(category=cat_id).all()
    if len(questions) == 0:
      abort(404)
    # make the pagination for every 10 questions) the value of 'QUESTIONS_PER_PAGE' variable
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    # format the questions
    formated_questions = [question.format() for question in questions]
    # return a Response with the JSON representation 'sucsses' , 'questions' , 'total_questions' , 'currentCategory'
    return jsonify({
      'success': True,
      'questions': formated_questions[start:end],
      'total_questions': len(questions),
      'current_category': cat_id
    })
  ''' 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  @app.route('/quizzes', methods=['POST'])
  def quizze():
    try:
      body = request.get_json()
      quez_cat = body.get('quiz_category')
      previous_ques = body.get('previous_questions')

      if (quez_cat['id'] == 0):
        questions = Question.query.all()
      else:
        questions = Question.query.filter_by(category=quez_cat['id']).all()
      if len(questions) == 0 :
        abort(422)
      if len(previous_ques) == len(questions):
        next_ques = None
        return jsonify({
          'success': True,
          'question': next_ques
        })
      else:
        next_ques = questions[random.randint(0, len(questions) - 1)]

        found = True

        while found:
          if  (next_ques.id  in previous_ques):
            next_ques = questions[random.randint(0, len(questions) - 1)]
            print(next_ques.id)
            print(previous_ques)
          else:
            found = False

      return jsonify({
        'success':True,
        'question':next_ques.format()
      })
    except:
      abort(422)

  '''
 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message':'resource not found'
    }),404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message':'unprocessable'
    }),422
  @app.errorhandler(400)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message':'bad request'
    }),400

  @app.errorhandler(405)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': 'method not allowed'
    }), 405
  return app

    