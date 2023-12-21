class Customer:
    def __init__(self, customer_id=None, name=None, email=None, phone_number=None,
                 address=None, credit_score=None):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._address = address
        self._credit_score = credit_score
# using private attributes because of getter and setter methods
    # Getter methods

    def get_customer_id(self):
        return self._customer_id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_phone_number(self):
        return self._phone_number

    def get_address(self):
        return self._address

    def get_credit_score(self):
        return self._credit_score

    # Setter methods
    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_name(self, name):
        self._name = name

    def set_email(self, email):
        self._email = email

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_address(self, address):
        self._address = address

    def set_credit_score(self, credit_score):
        self._credit_score = credit_score

    def display_customer_details(self):
        print(f"Customer ID: {self._customer_id}")
        print(f"Name: {self._name}")
        print(f"Email: {self._email}")
        print(f"Phone Number: {self._phone_number}")
        print(f"Address: {self._address}")
        print(f"Credit Score: {self._credit_score}")
