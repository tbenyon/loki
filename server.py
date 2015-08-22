import web

render = web.template.render('templates/')

urls = ("/door", "door")

class door:
    def GET(self):
        return render.door()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
