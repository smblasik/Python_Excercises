title_bar = "="*30
print(title_bar)
print('    Email Slicer')
print(title_bar)

# Get User Email Address
email = input('What is your email address? ').strip()

# Slice out username
user = email[:email.index("@")]

# slice out domain name
domain = email[email.index("@")+1:]

# Format message
output = 'Your username is {} and your domain is {}'.format(user, domain)

# Display output message
print(output)

### Reverse strings by using string[::-1] "-1" represents the step
print('Reverse String looks like')
print(email[::-1])
