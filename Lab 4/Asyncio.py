import time
import asyncio
from Server import Server
from Client import Client

U1 = 10
U2 = 15
U3 = 5

T1 = 2
T2 = 1
T3 = 0.5

clients_for_reg = []
clients_main_page = []
clients_reg_list = []

for i in range(1, U1 + 1):
    clients_for_reg.append(Client(i))
for j in range(U1 + 1, U1 + U2 + 1):
    clients_main_page.append(Client(j))
for k in range(U1 + U2 + 1, U1 + U2 + U3 + 1):
    clients_reg_list.append(Client(k))

srvr = Server()
tasks = []
event_loop = asyncio.get_event_loop()
start_time = time.time()

for i in range(U1):
    client = clients_for_reg[i]
    task = srvr.async_register_client(client, T1)
    tasks.append(task)

for j in range(U2):
    client = clients_main_page[j]
    task = srvr.async_get_main_page(client, T2)
    tasks.append(task)

for i in range(U3):
    client = clients_reg_list[i]
    task = srvr.async_register_client(client, T3)
    tasks.append(task)

event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()

end_time = time.time()

print()
print(f"Elapsed time using asyncio is {end_time - start_time}")
