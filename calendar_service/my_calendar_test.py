import unittest

from my_calendar import *


class MyCalendarTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_get_time(self):
        response = self.app.get('/time', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_date(self):
        response = self.app.get('/date', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_time_2(self):
        r = get_time()
        self.assertEqual(3, r['id'])

    def test_get_date_2(self):
        r = get_date()
        self.assertEqual(1, r['id'])


if __name__ == "__main__":
    unittest.main()
