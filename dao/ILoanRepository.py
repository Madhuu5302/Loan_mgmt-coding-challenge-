from exception.InvalidLoanException import InvalidLoanException
# from entity.Customer import Customer
from entity.Loan import Loan
# from entity.HomeLoan import HomeLoan
# from entity.CarLoan import CarLoan
# from util.DBPropertyUtil import PropertyUtil
from util.DBPropertyConn import dbConnection

class Loan_repo():
    def applyLoan(self, confirmation_req=True):
        try:
            if confirmation_req:
                user_input = input("Do you want to apply for this loan? (Yes/No): ")
                if user_input.lower() != "yes":
                    raise InvalidLoanException("Loan application cancelled.")
            self._loan_status = "Approved"
            print("Loan applied successfully!")

        except InvalidLoanException as e:
            print(f"Error: {e}")

        def calculateInterest(self):
            try:
                if not self._loan_id or not self._principal_amount or not self._interest_rate or not self._loan_term:
                    raise InvalidLoanException("Invalid loan details for interest calculation.")

                # Calculate interest based on loan details
                interest = (self._principal_amount * self._interest_rate * self._loan_term) / 12
                return round(interest, 2)
            except InvalidLoanException as e:
                print(f"Error: {e}")

        def loanStatus(self):
            try:
                if not self._customer or not self._customer.get_credit_score():
                    raise InvalidLoanException("Invalid customer details for loan status check.")

                credit_score = self._customer.get_credit_score()

                if credit_score > 650:
                    self._loan_status = "Approved"
                    print("Loan is approved!")
                else:
                    self._loan_status = "Rejected"
                    print("Loan is rejected.")

            except InvalidLoanException as e:
                print(f"An error occurred: {e}")

        def calculateEMI(self):
            try:
                if not self._loan_id or not self._principal_amount or not self._interest_rate or not self._loan_term:
                    raise InvalidLoanException("Invalid loan details for EMI calculation.")

                # Converting annual interest rate to monthly interest rate
                monthly_interest_rate = self._interest_rate / 12 / 100

                # Calculate EMI using the formula
                emi = (self._principal_amount * monthly_interest_rate * (
                    pow(1 + monthly_interest_rate, self._loan_term))) / (
                              pow(1 + monthly_interest_rate, self._loan_term) - 1)
                return round(emi, 2)

            except InvalidLoanException as e:
                print(f"An error occurred: {e}")

        def get_all_loans(self):
            try:
                connection = dbConnection.get_connection()
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM loan")
                    result = cursor.fetchall()
                    loans = []
                    for row in result:
                        loan = Loan(
                            loan_id=row[0],
                            customer_id=row[1],
                            loan_amount=row[2],
                            loan_duration=row[3],
                            interest_rate=row[4],
                            loan_type=row[5],
                            loan_status=row[6]
                        )
                        loans.append(loan)
                    return loans
            except Exception as e:
                print(f"Error:{e}")
            finally:
                connection.close()

        def get_loan_details(self, loan_id):
            try:
                connection = dbConnection.get_connection()
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM loan WHERE loan_id=%s", (loan_id,))
                    result = cursor.fetchone()
                    if result:
                        loan = Loan(
                            loan_id=result[0],
                            customer_id=result[1],
                            loan_amount=result[2],
                            loan_duration=result[3],
                            interest_rate=result[4],
                            loan_type=result[5],
                            loan_status=result[6]
                        )
                        return loan
                    else:
                        raise InvalidLoanException("Loan not found with ID: {}".format(loan_id))
            except Exception as e:
                print(f"Error fetching loan details: {e}")
            finally:
                connection.close()

        def loan_repayment(self, loan_id, amount):
            try:
                connection = dbConnection.get_connection()
                with connection.cursor() as cursor:
                    cursor.execute("SELECT loan_amount, loan_duration FROM loan WHERE loan_id=%s", (loan_id,))
                    result = cursor.fetchone()
                    if result:
                        loan_amount = result[0]
                        loan_duration = result[1]

                        emi_amount = loan_amount / loan_duration

                        if amount < emi_amount:
                            raise InvalidLoanException("Payment rejected. Amount is less than a single EMI.")

                        no_of_emi_paid = int(amount / emi_amount)

                        cursor.execute("UPDATE loan SET loan_duration = loan_duration - %s WHERE loan_id=%s",
                                       (no_of_emi_paid, loan_id))

                        print(f"Payment successful. {no_of_emi_paid} EMIs paid.")
                        print(f"Remaining loan term: {loan_duration - no_of_emi_paid} months")
                    else:
                        raise InvalidLoanException("Loan not found with ID: {}".format(loan_id))

                connection.commit()
            except Exception as e:
                print(f"Error:{e}")
            finally:
                connection.close()
