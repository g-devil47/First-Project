#Basic info
print("Greetings")
users_age = input("What is your Age?\n")
print("What are Your Educational Qualifications?")
users_specific_qualification = input("10th, 12th, Graduation, Post-Graduation, Others\n")

#Employment and Income
users_employement_status = print("Your Employment Status?")
while True:
    user_unlisted_no_1 = input("Y/N?(In Capitals)\n")    
    if user_unlisted_no_1 == "Y":
        users_occupation = input("Occupation\n")
        users_monthly_income = input("Your Monthly Income\n")
        users_annual_income = users_monthly_income / 12
        break     
    elif user_unlisted_no_1 == "N":
        break 
    else:
        print("Invalid input. Please enter Y or N (in capitals).")

#Expenses
users_major_monthly_expenses = input("Your Major Monthly Expenses?\n")
users_outstanding_debit = input("Outstanding Debts\n")
users_spending_habits = input("What are your Spending Habits/Categories\n")

#Additional income
users_additional_source_income = input("Do You Have Any Additional Source of Income?\n")

#Goals
users_short_term__financial_goal = input("What are your Financial Short Term Goals?\n")
users_long_term_financial_goals = input("What are your Long Term Financial Goals?\n")

#Credit History
users_credit_history = input("Do You have a Credit History?(Y/N)\n")
users_possession_of_any_credit_cards = input("Are you in possession of any Credit Cards?\n")
users_credit_score = input("What is Your Credit Score? (As per report generated by CIBIL)\n")

#investements
users_investment = input("Are you investing?(Y/N)\n")

if users_investment == "Y":
    users_investment_type = input("What is your investment type?\n")
    users_amount_invested = input("Amount Invested.\n")
elif users_investment == "N":
    pass

users_emergency_fund = input("Do You have any Emergency Funds?\n")

#savings
users_money_in_saving = input("Do much money do you have in savings?\n")