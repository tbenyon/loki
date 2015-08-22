import web

urls = ("/door", "door")

class door:
    def GET(self):
        return "Door status: Locked"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
