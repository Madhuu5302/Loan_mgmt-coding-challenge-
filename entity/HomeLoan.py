from Loan import Loan


class HomeLoan(Loan):
    def __init__(self, loan_id=None, customer=None, principal_amount=None, interest_rate=None,
                 loan_term=None, property_address=None, property_value=None, loan_status="Pending"):
        super().__init__(loan_id, customer, principal_amount, interest_rate,
                         loan_term, "HomeLoan", loan_status)
        self._property_address = property_address
        self._property_value = property_value

    # Getter methods specific to HomeLoan
    def get_property_address(self):
        return self._property_address

    def get_property_value(self):
        return self._property_value

    # Setter methods specific to HomeLoan
    def set_property_address(self, property_address):
        self._property_address = property_address

    def set_property_value(self, property_value):
        self._property_value = property_value

    def display_loan_details(self):
        super().display_loan_details()
        print(f"Property Address: {self._property_address}")
        print(f"Property Value: {self._property_value}")
