from auth import AuthManager
from checking_card import Check_Card
from transactions import Found_transfer
from found_transaction import Found_transaction
from account import Account
from utils import Utils
from save_new_account import Save
from staf import Staf
from loan import Loan
import json
import sys


class Bank:

    def __init__(self, id):

        self.save_id = id
        self.central_data = []

        with open('./staf.json', 'r') as f:
            self.stafs = json.load(f)

        with open('./save_new_account.json', 'r') as save:

            content = save.read()

            if not content:
                self.save_id = []
            else:
                save.seek(0)
                self.save_id = json.load(save)

    # --- Execution ---

    def check_staf(self):

        check_staf = input('Enter your rolre(staf/user)')
        found = True

        while found:

            if check_staf == 'staf':

                get_user_name_staf = input('Enter your username:')
                get_password_staf = input('Enter your password:')

                for check in self.stafs:

                    if get_user_name_staf == check['user_name'] and get_password_staf == check['password']:

                        print('welcome!')
                        found = False
                        self.staf_account()

                    else:
                        print('your username or password is not found!')

            elif check_staf == 'user':

                self.main()

            else:

                raise('Enter a valid value')

    def get_central_banck_data(self):

        with open('./centeral_bank.json', 'r') as f:
            self.central_data = json.load(f)

    def main(self):

        print('<<< ATM >>>')

        obj_auth = AuthManager()

        user_chois = input('What do you want?(sign_in or sign_up)')

        if user_chois == 'sign_up':

            obj_save = Save('', '', '')
            obj_save.add_new_account()

        elif user_chois == 'sign_in':

            user = obj_auth.login()

            if user:

                print(
                    'Things that can be done\n'
                    '1-Transaction\n'
                    '2-Find_transaction\n'
                    '3-account_balance / changing_password\n'
                    '4-withraw_payment / deposit_payment\n'
                    '5-request loan\n'
                    '6-exit'
                )

                ex = True
                while ex:

                    choice = input('What do you want to do?(enter the number)')

                    if choice == '1':

                        obj_found_transfer = Found_transfer('', '')
                        obj_found_transfer.found_transfer()

                    elif choice == '2':

                        obj_found_transaction = Found_transaction()
                        obj_found_transaction.find_transaction()

                    elif choice == '3':

                        obj_account = Account()

                        user_request_account = input('which one do you want?(account_balance / changing_password) :')

                        if user_request_account == 'account_balance':

                            print(obj_account.account_balance())

                        elif user_request_account == 'changing_password':

                            print(obj_account.changing_password())

                        else:

                            print('amount enter is invalid')

                    elif choice == '4':

                        obj_utils = Utils()

                        user_request_utils = input('which one do you want?(withraw_payment / deposit_payment) :')

                        if user_request_utils == 'withraw_payment':

                            print(obj_utils.withraw_payment())

                        elif user_request_utils == 'deposit_payment':

                            print(obj_utils.deposit_payment())

                        else:

                            print('amount enter is invalid')

                    elif choice == '5':

                        obj_loan = Loan('', '', user['id'])
                        obj_loan.loan_information()

                    elif choice == '6':

                        print('Bye')
                        sys.exit()

                    else:

                        print('the number is invalid')
                        ex = True

    def staf_account(self):

        loop = True

        while loop:

            staf_choise = input(
                'What do you want to do?\n'
                '1-check users account\n'
                '2-reviewing transactions\n'
                '3-create a new account for the user\n'
                '4-exit'
            )

            obj_staf = Staf('', '', '')

            if staf_choise == '1':

                obj_staf.read_user_account()

            elif staf_choise == '2':

                obj_staf.reviewing_transactions()

            elif staf_choise == '3':

                obj_staf.create_a_new_account_for_the_user()

            elif staf_choise == '4':

                loop = False

            else:

                print('the number is invalid')
                loop = True


obj = Bank('')
obj.check_staf()