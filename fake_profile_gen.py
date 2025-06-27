#Creates a list of random profiles with names emails usernames and address
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of profiles to generate
num_profiles = int(input('how many files do you want to generate'))

# Generate profiles and save to a text file
for i in range(num_profiles):
    with open(f'employee_profile_{i}.txt', 'w') as file:
        profile = fake.simple_profile()
        file.write(f"Name: {profile['name']}\n")
        file.write(f"Email: {profile['mail']}\n")
        file.write(f"Username: {profile['username']}\n")
        file.write(f"Address: {profile['address']}\n")
        file.write("\n")  # Add a separator between profiles

print(f"{num_profiles} profiles generated and saved ")
