from faker import Faker
fake = Faker(locale='en_US')
for _ in range(100000):
    print(fake.ssn())


