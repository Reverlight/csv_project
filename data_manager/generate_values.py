# Date
# Full name
# Job
# Phone
# Email
import datetime
from random import choice, randint, randrange

first_names = [
    'Kimberly',
    'Michael',
    'Alexander',
    'Aaron',
    'Mr. Kelly',
    'Heather',
    'Thomas',
    'Jacob',
    'Timothy',
    'Tracey',
    'Bruce',
    'Christine',
    'Colleen',
    'Harold',
    'Brent',
    'Alex',
    'Jennifer',
    'Calvin',
    'Karen',
    'Dawn'
]

last_names = [
    'Nguyen',
    'Wilson',
    'Gillespie',
    'Mcpherson',
    'Duncan',
    'Garcia',
    'Hudson',
    'Barker',
    'Jones',
    'Robertson',
    'Ray',
    'Long',
    'Smith',
    'Adams',
    'Jimenez',
    'Perez',
    'Marquez',
    'Rodgers',
    'Henderson',
    'Kelly',
    'Murphy',
    'Gutierrez'
]

nick_names = [
    'Parthophobia',
    'Overset',
    'Fulvous',
    'Special',
    'Yeuk',
    'Terry',
    'Humpenscrump',
    'Yippee',
    'Naevus',
    'Stilp',
    'Hazel',
    'Stratous',
    'Gasiform',
    'Cathedralwas',
    'Jampan',
    'Periaster',
    'Chorography'
]

email_domains = [
    '@msn.com',
    '@yahoo.com',
    '@gmail.com',
    '@mac.com',
    '@outlook.com',
    '@@msn.com',
]

jobs = [
    'Recreation & Fitness Worker',
    'Software Developer',
    'Medical Secretary',
    'Insurance Agent',
    'Civil Engineer',
    'Telemarketer',
    'Physical Therapist',
    'Housekeeper',
    'Physicist',
    'Human Resources Assistant',
    'Farmer',
    'Librarian',
    'Receptionist',
    'Bus Driver',
    'Compliance Officer',
    'Speech-Language Pathologist',
    'Dentist',
    'Accountant',
    'Automotive mechanic',
    'Police Officer',
    'Coach',
    'Painter',
    'Database administrator',
    'Chef',
    'Loan Officer',
]


def gen_phone():
    phone = f'{randint(100, 999)}-{randint(100, 999)}-{randint(1000, 9999)}'
    return phone


def gen_date():
    start_date = datetime.date(2002, 1, 1)
    end_date = datetime.date(2020, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def gen_job():
    job = choice(jobs)
    return job


def gen_full_name():
    first_name = choice(first_names)
    last_name = choice(last_names)
    return f'{first_name} {last_name}'


def gen_email():
    nick_name = choice(nick_names).lower()
    random_num = randint(3, 999)
    email_domain = choice(email_domains)
    email = f'{nick_name}{random_num}{email_domain}'
    return email


def sort_data(l):
    l.sort(key=lambda i: i['order'])
    return l


def gen_data(type):
    if type == 'Full name':
        return gen_full_name()
    if type == 'Email':
        return gen_email()
    if type == 'Job':
        return gen_job()
    if type == 'Phone':
        return gen_phone()
    if type == 'Date':
        return gen_date().__str__()

    return None


data = [
    {'column_name': 'email', 'type_name': 'Email', 'order': 1},
    {'column_name': 'job', 'type_name': 'Job', 'order': 2},
    {'column_name': 'cellphone', 'type_name': 'Phone', 'order': 0},
    {'column_name': 'date', 'type_name': 'Date', 'order': 3},
]
