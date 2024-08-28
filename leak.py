class DBEngine:
    def connect(self, host: str, port: int, login: str, password: str, db_name: str):
        raise NotImplementedError()


class SlackEngine:
    SLACK_API_KEY = "xoxb-263594206564-FdqddMF1t08v8N7Oq4i57vsc"

    def send_message(self, message: str):
        raise NotImplementedError()


engine = DBEngine()
conn = engine.connect("postgresql://app:4HmLKjdXFCzA71MhaB@app-prod.dev:5433/prod_db")
