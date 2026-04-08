def get_data(user):
    print(f"Fetching data for {user}")

def require_auth(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied")
            return
        return func(user)
    return wrapper

def log(func):
    def wrapper(user):
        print(f"[LOG] User: {user}")
        return func(user)
    return wrapper


@log
@require_auth
def secure_get_data(user):
    print(f"Secure data for {user}")

secure_get_data("admin")
secure_get_data("guest")
