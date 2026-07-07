# Email Analyzer System

# Take email from user to analyze
email = input("Please enter your email : ")

print("="*60)
print("               EMAIL ANALYZER REPORT")
print("="*60)

# Now we will analysis on the user_email
print("Email : "+email) 
userName = email.split("@")[0]
print("User name's length",len(userName))

# Check user name 
if userName.isalnum() and userName.islower() and not userName.isalpha() and not userName.isdigit():
    print("Your user name is valid : "+userName)
else:
    print("This is not valid user name!! please rewrite valid user name : "+userName)

# Check domain name 
domain = email[email.find("@"):]
print("Domain's name : ",domain)
if domain=="@gmail.com":
    print("This is valid domain name...")
else:
    print("This is not valid domain name!")

print("Extension's name : ",domain[-4:])
print("Position of '@' : ",email.find("@"))

# Reverse email
print("Reverse email : ",email[::-1])