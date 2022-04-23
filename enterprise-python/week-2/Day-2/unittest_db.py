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
    def test_user_default_not_active(self):
        db = connection_to_db()
        coding = User(db, 'coding')
        self.assertFalse(coding.active)  # off by default
        db_connection_disconnect(db)
     
    def test_user_is_active(self):
        db = connection_to_db()
        coding = User(db, 'coding')
        coding.set_active()  # activate new user
        self.assertTrue(coding.active)
        db_connection_disconnect(db)
     
if __name__ == '__main__':
    unittest.main()