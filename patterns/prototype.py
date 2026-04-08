import copy

class Config:
    def __init__(self, host, port, features):
        self.host = host
        self.port = port
        self.features = features

    def clone(self):
        return copy.deepcopy(self)

base_config = Config(
    host="localhost",
    port=8080,
    features=["auth", "logging"]
)

dev_config = base_config.clone()
dev_config.port = 3000

prod_config = base_config.clone()
prod_config.host = "api.prod.com"

print(base_config.__dict__)
print(dev_config.__dict__)
print(prod_config.__dict__)
