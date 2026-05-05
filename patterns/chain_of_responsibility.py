class Request:
    def __init__(self, user=None, data=None, ip=None):
        self.user = user
        self.data = data or {}
        self.ip = ip


class Middleware:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

    def set_next(self, handler):
        self.next_handler = handler
        return handler


class AuthMiddleware(Middleware):
    def handle(self, request):
        if not request.user:
            return {"status": 401, "message": "Unauthorized"}
        return super().handle(request)


class ValidationMiddleware(Middleware):
    def handle(self, request):
        if "email" not in request.data:
            return {"status": 400, "message": "Missing email"}
        return super().handle(request)


class RateLimitMiddleware(Middleware):
    def __init__(self, limit=2, next_handler=None):
        super().__init__(next_handler)
        self.limit = limit
        self.requests = {}

    def handle(self, request):
        count = self.requests.get(request.ip, 0)
        if count >= self.limit:
            return {"status": 429, "message": "Too many requests"}
        self.requests[request.ip] = count + 1
        return super().handle(request)


class CreateUserHandler:
    def handle(self, request):
        user = {
            "email": request.data["email"],
            "name": request.data.get("name")
        }
        return {"status": 201, "user": user}


auth = AuthMiddleware()
validation = ValidationMiddleware()
rate_limit = RateLimitMiddleware(limit=2)
endpoint = CreateUserHandler()

auth.set_next(validation).set_next(rate_limit).set_next(endpoint)

request = Request(user="john", data={"email": "john@example.com", "name": "John Doe"}, ip="127.0.0.1")

response = auth.handle(request)
print(response)
