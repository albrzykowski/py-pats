class JobQueue:
    def __init__(self):
        self.jobs = []

    def add_job(self, job):
        self.jobs.append(job)

    def run(self):
        for job in self.jobs:
            job()

def send_email(user):
    print(f"Sending email to {user}")

def generate_report():
    print("Generating report...")


queue = JobQueue()

queue.add_job(lambda: send_email("john@example.com"))
queue.add_job(generate_report)

queue.run()
