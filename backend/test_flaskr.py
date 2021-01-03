import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('postgres:root@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question={
            'question':'test question',
            'answer': 'test answer',
            'category': 1,
            'difficulty': 1
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # test get all categories
    def test_get_categories(self):
        # get response and data
        res = self.client().get('/categories')
        data = json.loads(res.data)
        # check state and sucsses
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        # check that categories return data
        self.assertTrue(data['categories'])
        self.assertEqual(len(data['categories']),6)

    # test get questions
    def test_get_questions(self):
        # get response and data
        res = self.client().get('/questions')
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        # check that questions return data of pagination of QUESTIONS_PER_PAGE
        self.assertTrue(data['questions'])
        self.assertEqual(len(data['questions']),10)
        # check that categories return data
        self.assertTrue(data['categories'])
        self.assertEqual(len(data['categories']), 6)
        # check that total question  return data
        # get all questions to check the respond total question
        totalQuestions = Question.query.all()
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['total_questions'],len(totalQuestions))

    # test error if page request is over than questions pages
    def test_error_questions_page_not_valid(self):
        # get response and data
        res = self.client().get('/questions?page=50')
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)
        # check error message data
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')


    # test delete questions
    def test_delete_question(self):
        # create new question to delete it
        question = Question(question=self.new_question['question'], answer=self.new_question['answer'], category=1, difficulty = 1 )
        question.insert()
        # get inserted question id
        q_id = question.id
        res = self.client().delete('/questions/{}'.format(q_id))
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check that  return data
        self.assertTrue(data['delete'])
        self.assertEqual(data['delete'], str(q_id))

    # test error delete questions
    def test_error_delete_questions_id_not_valid(self):
        # get response and data
        res = self.client().delete('/questions/50')
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'],False)
        # check error message data
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'unprocessable')

    # test add questions
    def test_add_questions(self):
        res = self.client().post('/questions',json=self.new_question)
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check that  return data
        self.assertTrue(data['create'])

     # test error add  questions empty data

    def test_error_add_questions_empty(self):
        empty_new_question = {
            'question': '',
            'answer': '',
            'difficulty': 1,
            'category': 1,
        }
        # get response and data
        res = self.client().post('/questions',json=empty_new_question)
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        # check error message data
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'unprocessable')

    # test search_question
    def test_search_question(self):
        search_question = {
            'searchTerm':'What',
            'currentCategory': 1
        }
        res = self.client().post('/questions/search',json=search_question)
        data = json.loads(res.data)
        # check state and sucsses true
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check that questions  return data
        self.assertTrue(data['questions'])
        self.assertEqual(len(data['questions']), 1)
        # check that total_questions return data
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['total_questions'], 1)
        self.assertTrue(data['currentCategory'])

    # test  error if there isnot question get from search
    def test_error_search_no_question_exist(self):
        search_question = {
            'searchTerm': 'qweasdzxc',
            'currentCategory': 1
        }
        res = self.client().post('/questions/search', json=search_question)
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        # check error message data
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

    # test get questions by category id
    def test_get_questions_by_cat(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        # check state and sucsses
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check that current categories return data
        self.assertTrue(data['current_category'])
        self.assertEqual(data['current_category'], '1')

        # check that question  return data
        self.assertTrue(data['questions'])
        self.assertNotEqual(len(data['questions']),0 )
        # check that total_questions  return data
        self.assertTrue(data['total_questions'])
        self.assertNotEqual(data['total_questions'], 0)

    # test error if category isnot exist
    def test_error_No_cat_exist(self):
        res = self.client().get('/categories/100/questions')
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        # check error message data
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

    # test quizze
    def test_quizze(self):
        quizze_data = {
            'quiz_category':  {'type': 'Science', 'id': '1'},
            'previous_questions': [1,2]
        }
        res = self.client().post('quizzes', json=quizze_data)
        data = json.loads(res.data)
        # check state and sucsses
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # check that question  return data
        self.assertTrue(data['question'])
        self.assertNotEqual(len(data['question']), 0)
        # check that question not  return previous_questions
        self.assertNotEqual(data['question']['id'],1)
        self.assertNotEqual(data['question']['id'],2)

    # test error delete questions
    def test_error_quiz_category_id_not_valid(self):
        quizze_data = {
            'quiz_category': {'type': 'Science', 'id': '50'},
            'previous_questions': [1, 2]
        }
        res = self.client().post('quizzes', json=quizze_data)
        data = json.loads(res.data)
        # check error state and sucsses false
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'],False)
        # check error message data
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'unprocessable')






# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()