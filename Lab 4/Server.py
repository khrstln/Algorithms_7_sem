import time
import asyncio

class Server:
    def __init__(self):
        self.clients = {}
        self.load = 0

    def register_client(self, client, processing_time):
        self.load = 25
        if client.id in self.clients:
            print(f"Client {client.id} is already registered on the portal")
        else:
            self.clients[client.id] = client
            print(f"Client {client.id} has been successfully registered on the portal")
            time.sleep(processing_time)

    async def async_register_client(self, client, processing_time):
        self.load = 25
        if client.id in self.clients:
            print(f"Client {client.id} is already registered on the portal")
        else:
            self.clients[client.id] = client
            print(f"Client {client.id} has been successfully registered on the portal")
            await asyncio.sleep(processing_time)

    def register_clients(self, clients, processing_time):
        for client in clients:
            self.register_client(client, processing_time)


    def get_main_page(self, client, processing_time):
        self.load = 15
        print(f"Client {client.id} has successfully gotten the main page")
        time.sleep(processing_time)

    async def async_get_main_page(self, client, processing_time):
        self.load = 15
        print(f"Client {client.id} has successfully gotten the main page")
        await asyncio.sleep(processing_time)

    def get_main_pages(self, clients, processing_time):
        for client in clients:
            self.get_main_page(client, processing_time)

    def check_reg_list(self, client, processing_time):
        self.load = 1
        print(f"Client {client.id} has successfully checked the registration list")
        time.sleep(processing_time)

    async def async_check_reg_list(self, client, processing_time):
        self.load = 1
        print(f"Client {client.id} has successfully checked the registration list")
        await asyncio.sleep(processing_time)

    def check_reg_lists(self, clients, processing_time):
        for client  in clients:
            self.check_reg_list(client, processing_time)
