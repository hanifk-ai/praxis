import unittest
     
def connection_to_db():
    print('[connect to db]')
def db_connection_disconnect(db):
    print('[not connected to db {}]'.format(db))

class User:
    username = ''
    active = False
    def __init__(self, db, username):  # using db sample
        self.username = username
    def set_active(self):
        self.active = True

class TestUser(unittest.TestCase):
    def setUp(self):
        self.db = connection_to_db()
        self.coding = User(self.db, 'coding')
     
    def tearDown(self):
        db_connection_disconnect(self.db)
        
    def test_user_default_not_active(self):
        self.assertFalse(self.coding.active)  # off by default
     
    def test_user_is_active(self):
        self.coding.set_active()  # activate new user
        self.assertTrue(self.coding.active)

if __name__ == '__main__':
    unittest.main()