import json
import random

class Loan:

    def __init__(self, creat_request, salary, user_id):
        self.creat_request = creat_request
        self.salary = salary
        self.user_id = user_id

        self.dump_informations = {
            'loan_id':None,
            'user_id':None,
            'installments':None,
            'amount':None,
            'interest_rate':None,
            'total_repayment':None
        }

        with open('./loan.json', 'r') as loan:
            content = loan.read()

            if not content:
                self.creat_request = []
            else:
                loan.seek(0)
                self.creat_request = json.load(loan)

        with open('./save_new_account.json', 'r') as sal:
            self.salary = json.load(sal)

    def loan_information(self):
        installments = input('in how many installments do you want to pay?(12/24/36)')

        offers = []

        money = [
            20_000_000,
            50_000_000,
            70_000_000,
            100_000_000,
            120_000_000,
            150_000_000,
            200_000_000,
            250_000_000,
            300_000_000,
            350_000_000,
            400_000_000,
            450_000_000,
            500_000_000
        ]

        # print("User ID:", self.user_id)
        # print("Users:", self.salary)

        for user in self.salary:
            if user["id"] == self.user_id:
                user_salary = user["salary"]
                break

        for i in money:
            if i // int(installments) + 10_000_000 < user_salary:
                offers.append(str(i))

        print(f'your amount can be {offers}')
        amount = input('wich one do you want?')

        interest_rate = [4,10,15,20,24,25]
        interest_rate = random.choice(interest_rate)

        print(f'You are required to pay the bank an additional {interest_rate} as interest rate.')

        total_repayment = ((interest_rate // 100) * amount) + amount

        self.dump_informations['loan_id'] = 1
        self.dump_informations['user_id'] = self.user_id
        self.dump_informations['installments'] = installments
        self.dump_informations['amount'] = amount
        self.dump_informations['intrest_rate'] = interest_rate
        self.dump_informations['total_repayment'] = total_repayment
