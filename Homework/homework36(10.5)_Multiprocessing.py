import multiprocessing as mp

class WarehouseManager:
    def __init__(self, shared_data):
        self.data = shared_data

    def process_request(self, request):
        product, operation, quantity = request
        if operation == 'receipt':
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
            print(f'Добавлено {quantity} в {product}, всего {self.data[product]}')
        elif operation == 'shipment':
            if product in self.data:
                self.data[product] -= quantity
            else:
                self.data[product] = -quantity
            print(f'Убрано {quantity} из {product}, всего {self.data[product]}')

    def run(self, requests):
        with mp.Pool(processes=2) as pool:
            pool.map(self.process_request, requests)


if __name__ == '__main__':
    with mp.Manager() as manager:
        shared_data = manager.dict()
        warehouse_manager = WarehouseManager(shared_data)

        requests = [
            ("product1", "receipt", 100),
            ("product2", "receipt", 150),
            ("product1", "shipment", 30),
            ("product3", "receipt", 200),
            ("product2", "shipment", 50)
        ]
        warehouse_manager.run(requests)
        print(dict(shared_data))
