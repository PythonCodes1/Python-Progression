# Slice the email with the user and domain name

email = input("What is your email address?: ").strip()

username = email[:email.index("@")]

domain_name = email[email.index("@")+1:]

output = "Your username is '{}' and your domain name is '{}'".format(username,domain_name)

print(output)
