import sys
from loan_management import LoanManagement

class MainModule:
    @staticmethod
    def main():
        loan_management = LoanManagement()

        while True:
            print("\n===== Loan Management System =====")
            print("1. Apply Loan")
            print("2. Get All Loans")
            print("3. Get Loan Details")
            print("4. Loan Repayment")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                loan_management.apply_loan()
            elif choice == '2':
                loan_management.get_all_loans()
            elif choice == '3':
                loan_id = input("Enter Loan ID: ")
                loan_management.get_loan_details(loan_id)
            elif choice == '4':
                amount = float(input("Enter Repayment Amount: "))
                loan_management.loan_repayment(amount)
            elif choice == '5':
                print("Exiting Loan Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

print(sys.path)

if __name__ == "__main__":
    MainModule.main()