class student:
    def __init__(self, name, email, password):
        self.name = name
        self .email = email
        self.password = password

    def register(self):
        print("i can register using", self.email)

    def login(self):
        print("i can login using", self.email)

class lecturer(student):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

        def submit_results(self):
            print("i can submit results")

class HOD(lecturer):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

        def standerdize_results(self):
            print("i can standerdize results")
