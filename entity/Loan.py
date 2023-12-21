class Loan:
    def __init__(self, loan_id=None, customer=None, principal_amount=None,
                 interest_rate=None, loan_term=None, loan_type=None, loan_status="Pending"):
        self._loan_id = loan_id
        self._customer = customer
        self._principal_amount = principal_amount
        self._interest_rate = interest_rate
        self._loan_term = loan_term
        self._loan_type = loan_type
        self._loan_status = loan_status

    # Getter methods
    def get_loan_id(self):
        return self._loan_id

    def get_customer(self):
        return self._customer

    def get_principal_amount(self):
        return self._principal_amount

    def get_interest_rate(self):
        return self._interest_rate

    def get_loan_term(self):
        return self._loan_term

    def get_loan_type(self):
        return self._loan_type

    def get_loan_status(self):
        return self._loan_status

    # Setter methods
    def set_loan_id(self, loan_id):
        self._loan_id = loan_id

    def set_customer(self, customer):
        self._customer = customer

    def set_principal_amount(self, principal_amount):
        self._principal_amount = principal_amount

    def set_interest_rate(self, interest_rate):
        self._interest_rate = interest_rate

    def set_loan_term(self, loan_term):
        self._loan_term = loan_term

    def set_loan_type(self, loan_type):
        self._loan_type = loan_type

    def set_loan_status(self, loan_status):
        self._loan_status = loan_status

    def display_loan_details(self):
        print(f"Loan ID: {self._loan_id}")
        print("Customer Information:")
        self._customer.display_customer_details()
        print(f"Principal Amount: {self._principal_amount}")
        print(f"Interest Rate: {self._interest_rate}")
        print(f"Loan Term: {self._loan_term} months")
        print(f"Loan Type: {self._loan_type}")
        print(f"Loan Status: {self._loan_status}")
