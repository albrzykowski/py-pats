class Specification:
    def is_satisfied_by(self, obj):
        raise NotImplementedError()

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class AndSpecification(Specification):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def is_satisfied_by(self, obj):
        return self.left.is_satisfied_by(obj) and self.right.is_satisfied_by(obj)


class OrSpecification(Specification):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def is_satisfied_by(self, obj):
        return self.left.is_satisfied_by(obj) or self.right.is_satisfied_by(obj)


class HasStableIncome(Specification):
    def is_satisfied_by(self, client):
        return client.income >= 5000


class HasGoodCreditHistory(Specification):
    def is_satisfied_by(self, client):
        return client.credit_score >= 700


class IsVIPClient(Specification):
    def is_satisfied_by(self, client):
        return client.vip_level >= 1


class Client:
    def __init__(self, income, credit_score, vip_level=0):
        self.income = income
        self.credit_score = credit_score
        self.vip_level = vip_level


class LoanApprovalEngine:
    def __init__(self, rule):
        self.rule = rule

    def approve(self, client):
        return self.rule.is_satisfied_by(client)


rule = (HasStableIncome() & HasGoodCreditHistory()) | IsVIPClient()

engine = LoanApprovalEngine(rule)

c1 = Client(income=6000, credit_score=750)
c2 = Client(income=2000, credit_score=650)
c3 = Client(income=2000, credit_score=400, vip_level=2)

print(engine.approve(c1))
print(engine.approve(c2))
print(engine.approve(c3))
