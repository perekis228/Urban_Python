import threading
import queue
import time

class Table:
    def __init__(self, number, is_busy=False):
        self.number = number
        self.is_busy = is_busy

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range(1, 21):
            self.queue.put(i)
            print(f'Посетитель номер {i} прибыл.', flush=True)
            if self.tables[0].is_busy and self.tables[1].is_busy and self.tables[2].is_busy:
                print(f'Посетитель номер {i} ожидает свободный стол.')
            time.sleep(1)

    def serve_customer(self):
        threads = []
        while True:
            try:
                for table in self.tables:
                    if not table.is_busy:
                        cus = Customer(self.queue.get(timeout=1), table)
                        table.is_busy = True
                        cus.start()
                        threads.append(cus)

                for thread in threads:
                    thread.join()

            except queue.Empty:
                break
                        
class Customer(threading.Thread):
    def __init__(self, customer, table, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.customer = customer
        self.table = table

    def run(self):
        print(f'Посетитель номер {self.customer} сел за стол {self.table.number}.', flush=True)
        time.sleep(5)
        print(f'Посетитель номер {self.customer} покушал и ушёл.', flush=True)
        self.table.is_busy = False


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем потоки
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_serve_thread = threading.Thread(target=cafe.serve_customer)

customer_arrival_thread.start()
customer_serve_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
customer_serve_thread.join()
