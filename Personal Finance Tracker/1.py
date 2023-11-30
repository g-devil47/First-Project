print("Greetings")
print("Please Enter your following Financial details")
users_annual_income = input("Annual Income: \n")
users_annual_income = float(users_annual_income)
users_monthly_income = users_annual_income / 12
print("Your Monthly Income:", str(users_monthly_income))
input("Is this Your Monthly Income? {}".format(users_monthly_income))
