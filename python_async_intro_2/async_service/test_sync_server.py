import tornado.testing

from async_service import sync_server


class Test(tornado.testing.AsyncHTTPTestCase):
    def get_app(self):
        return sync_server.make_app()

    def test_calculate_square(self):
        response = self.fetch("/calculate_square?num=2")
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b"4.0")
