import threading
from threading import Thread
import time

class BankAccount(Thread):

    def __init__(self, lock, balance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__balance = balance
        self.lock = lock

    def deposit(self, amount):
        with self.lock:
            self.__balance += amount
            print(f'Deposited {amount}, new balance is {self.__balance}')
            time.sleep(0.1)

    def withdraw(self, amount):
        with self.lock:
            self.__balance -= amount
            print(f'Withdraw {amount}, new balance is {self.__balance}')
            time.sleep(0.1)


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


lock = threading.Lock()
account = BankAccount(lock, 1000)

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()