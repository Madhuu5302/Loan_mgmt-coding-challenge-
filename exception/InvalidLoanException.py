class InvalidLoanException(Exception):
    def __init__(self, message="Invalid loan"):
        self.message = message
        super().__init__(self.message)
