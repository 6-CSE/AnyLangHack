from validate_email_address import validate_email
# install dependencies from requirements.txt

# user input
email = input("Enter the email address: ")

 #checks if the email given is valid
if validate_email(email, verify=True):
    print(f"The email {email} is valid ✅")
else :
    print(f"The email {email} is invalid ❌")

