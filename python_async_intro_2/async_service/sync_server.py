import asyncio

import tornado.web

import async_service.sync_backend

class CalculateSquareHandler(tornado.web.RequestHandler):
    def get(self):
        num_str = self.get_argument('num')
        num = float(num_str)
        squared_num = async_service.sync_backend.calculate_square(num)
        self.write(str(squared_num))

def make_app():
    return tornado.web.Application([
        (r"/calculate_square", CalculateSquareHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
