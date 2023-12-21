from entity.Customer import Customer
from entity.Loan import Loan
from entity.HomeLoan import HomeLoan
from entity.CarLoan import CarLoan
from dao.ILoanRepository import Loan_repo
from exception.InvalidLoanException import InvalidLoanException
from util.DBPropertyConn import dbConnection

class LoanManagement:
    def _init_(self):
        self.db_connection = dbConnection(host='localhost', database='loan_mgmt', user='root', password='Madhu@5302')
        self.db_connection.open()

    def _del_(self):
        self.db_connection.close()

    def apply_loan(self):
        try:
            # Creating instances
            customer1 = Customer()
            customer1.set_customer_id("103")
            customer1.set_name("Madhu")
            customer1.set_email("madhu@gmail.com")
            customer1.set_phone_number("9045619053")
            customer1.set_address("123 Main St, Chennai")
            customer1.set_credit_score(750)

            # Displaying customer details
            customer1.display_customer_details()

            customer2 = Customer()
            customer2.set_customer_id("104")
            customer2.set_name("Kamalesh")
            customer2.set_email("kamalesh@gmail.com")
            customer2.set_phone_number("9245678901")
            customer2.set_address("456 Cross St, Madurai")
            customer2.set_credit_score(800)

            # Displaying customer details
            customer2.display_customer_details()

            # Create instances of HomeLoan and CarLoan
            home_loan1 = HomeLoan()
            home_loan1.set_loan_id("1001")
            home_loan1.set_customer(customer1)
            home_loan1.set_principal_amount(100000)
            home_loan1.set_interest_rate(0.035)
            home_loan1.set_loan_term(36)
            home_loan1.set_property_address("ABC Main St, Pune")
            home_loan1.set_property_value(150000)
            home_loan1.set_loan_status("Approved")

            car_loan1 = CarLoan()
            car_loan1.set_loan_id("1002")
            car_loan1.set_customer(customer2)
            car_loan1.set_principal_amount(20000)
            car_loan1.set_interest_rate(0.05)
            car_loan1.set_loan_term(12)
            car_loan1.set_car_model("Toyota")
            car_loan1.set_car_value(25000)
            car_loan1.set_loan_status("Pending")

            # Displaying details
            home_loan1.display_loan_details()
            car_loan1.display_loan_details()

            confirmation_req = True
            home_loan1.applyLoan(confirmation_req)

            interest_amount_home_loan = home_loan1.calculateInterest()
            interest_amount_car_loan = car_loan1.calculateInterest()

            print(f"Interest amount for Home Loan: {interest_amount_home_loan}")
            print(f"Interest amount for Car Loan: {interest_amount_car_loan}")

            home_loan1.loanStatus()

            emi_amount = car_loan1.calculateEMI()
            print(f"EMI Amount: {emi_amount}")

            # Add the loans to the list
            home_loan1.add_loan()
            car_loan1.add_loan()

        except InvalidLoanException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def get_all_loans(self):
        try:
            all_loans = Loan.get_all_loans()
            if not all_loans:
                print("No loans available.")
            else:
                for loan in all_loans:
                    loan.display_loan_details()
        except Exception as e:
            print(f"Error: {e}")

    def get_loan_details(self, loan_id):
        try:
            loan = Loan.get_loan_by_id(loan_id)
            if loan:
                loan.display_loan_details()
            else:
                print(f"No loan found with ID: {loan_id}")
        except Exception as e:
            print(f"Error: {e}")

    def loan_repayment(self, amount):
        try:
            loan_id = input("Enter Loan ID for Repayment: ")
            loan = Loan.get_loan_by_id(loan_id)

            if not loan:
                print(f"No loan found with ID: {loan_id}")
                return

            loan.loanRepayment(amount)
        except Exception as e:
            print(f"Error: {e}")

    def create_sample_data(self):
        try:
            # Your code to create sample customer and loan data for testing goes here
            pass
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    loan_management = LoanManagement()
    loan_management.create_sample_data()
    loan_management.apply_loan()
    loan_management.get_all_loans()
    loan_management.get_loan_details("1001")
    loan_management.loan_repayment(5000)
