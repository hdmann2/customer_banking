# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance_input = input("Enter current savings account balance: ")
    savings_interest_input = input("Enter savings account interest rate: ")
    savings_maturity_input = input("How long will the balance remain in the savings account (in months): ")

    savings_balance = float(savings_balance_input)
    savings_interest = float(savings_interest_input)
    savings_maturity = int(savings_maturity_input)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(float(savings_balance), float(savings_interest), savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nAfter {savings_maturity} month, this savings account will earn ${:.2f, format(savings_interest)}.format")
    print(f"\n Your updated blance will be ${savings_balance} ")
          
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = input("Enter current cd account balance: ")
    cd_interest = input("Enter cd accont interest rate: ")
    cd_maturity = input("How long will the balance remain in the cd account (in months): ")


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"\n After {cd_maturity} month, this cd account will earn ${cd_interest}.")
    print(f"\n Your updated blance will be ${cd_balance} ")

if __name__ == "__main__":
    # Call the main function.
    main()