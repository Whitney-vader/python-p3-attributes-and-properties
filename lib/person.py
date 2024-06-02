class Person:
    APPROVED_JOBS = ["ITC", "Sales", "Engineer"]

    def __init__(self, name="John Doe", job=None):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            self.name = "John Doe"
        else:
            self.name = name.title()

        if job is not None and job not in Person.APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self.job = None
        elif job is not None:
            self.job = job
        else:
            self.job = "Unemployed"