class HttpRequest:
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = {}
        self.body = None

    def send(self):
        print(f"{self.method} {self.url}")
        print(f"Headers: {self.headers}")
        print(f"Body: {self.body}")


class HttpRequestBuilder:
    def __init__(self):
        self.request = HttpRequest()

    def set_method(self, method):
        self.request.method = method
        return self

    def set_url(self, url):
        self.request.url = url
        return self

    def add_header(self, key, value):
        self.request.headers[key] = value
        return self

    def set_body(self, body):
        self.request.body = body
        return self

    def build(self):
        return self.request


request = (
    HttpRequestBuilder()
    .set_method("POST")
    .set_url("https://api.example.com/users")
    .add_header("Authorization", "Bearer TOKEN")
    .set_body({"name": "John"})
    .build()
)

request.send()
