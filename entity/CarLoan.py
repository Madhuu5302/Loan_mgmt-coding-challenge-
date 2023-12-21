from Loan import Loan


class CarLoan(Loan):
    def __init__(self, loan_id=None, customer=None, principal_amount=None, interest_rate=None,
                 loan_term=None, car_model=None, car_value=None, loan_status="Pending"):
        super().__init__(loan_id, customer, principal_amount, interest_rate,
                         loan_term, "CarLoan", loan_status)
        self._car_model = car_model
        self._car_value = car_value

    # Getter methods specific to CarLoan
    def get_car_model(self):
        return self._car_model

    def get_car_value(self):
        return self._car_value

    # Setter methods specific to CarLoan
    def set_car_model(self, car_model):
        self._car_model = car_model

    def set_car_value(self, car_value):
        self._car_value = car_value

    def display_loan_details(self):
        super().display_loan_details()
        print(f"Car Model: {self._car_model}")
        print(f"Car Value: {self._car_value}")
