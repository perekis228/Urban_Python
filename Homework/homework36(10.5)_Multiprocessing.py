import multiprocessing as mp

class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        if request[1] == 'receipt':
            if request[0] in self.data.keys():
                self.data[request[0]] += request[2]
            else:
                self.data[request[0]] = request[2]
            print(f'Добавлено {request[2]} в {self.data[request[0]]}')
        elif request[1] == 'shipment':
            if request[0] in self.data.keys():
                self.data[request[0]] -= request[2]
            else:
                self.data[request[0]] = -request[2]
            print(f'Убрано {request[2]} из {self.data[request[0]]}')

    def run(self, requests):
        with mp.Pool(processes=2) as pool:
            pool.map(self.process_request, requests)
        # for request in requests:
        #     self.process_request(request)

if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)
