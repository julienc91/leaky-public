class DBEngine:
    def connect(self, host: str, port: int, login: str, password: str, db_name: str):
        raise NotImplementedError()


class SlackEngine:
    def send_message(self, api_key: str, message: str):
        raise NotImplementedError()


engine = DBEngine()
