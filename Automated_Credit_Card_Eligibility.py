# Automated Credit Card Eligibility

# Uer details -
name = input("Enter full name : ")
age = int(input("Enter your age : "))
employment_status = input("Enter your employment status : ")
monthly_net_income = int(input("Enter your monthly income : "))
cibil_score = int(input("Enter your cibil score : "))
prev_loan = input("Enter your existing/previous active loan : ")

# Calculate credit card eligibility
print("="*60)
print(f"        RISK ASSESSMENT REPORT FOR : {name}   ")
print("="*60)

# Check age & employment status
if age>=18 and age<=65:
    print("Age status : Pass")
    if employment_status.lower() == "unemployed":
        print("Employment status : Fail")
    else:
        print("Status : Pass")
else:
    print("STATUS: REJECTED")
    print("REASON: Age Limit Exceeded")

# Check cibil score
if cibil_score<650: print("Rejected : Low CIBIL Score. High financial risk detected.")
elif 650<=cibil_score<=750 and prev_loan.lower()=="no" and monthly_net_income>50000: 
    print("""STATUS: CONDITIONALLY APPROVED (Silver Card)
        CREDIT LIMIT: ₹25,000""")
else:
    if monthly_net_income>75000:
     print("""STATUS: APPROVED (Platinum Premium Card)
        CREDIT LIMIT: ₹2,25,000
        BENEFITS: 0% Fuel Surcharge & International Lounge Access Included.""")
    else:
        print("Rejected: Monthly income is too low.")