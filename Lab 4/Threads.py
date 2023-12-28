from Client import Client
from Server import Server
import threading
import time

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
threads = []

start_time = time.time()

for i in range(U1):
    client = clients_for_reg[i]
    thread = threading.Thread(target=srvr.register_client, args=(client, T1))
    threads.append(thread)
    thread.start()

for j in range(U2):
    client = clients_main_page[j]
    thread = threading.Thread(target=srvr.get_main_page, args=(client, T2))
    threads.append(thread)
    thread.start()

for k in range(U3):
    client = clients_reg_list[k]
    thread = threading.Thread(target=srvr.check_reg_list, args=(client, T3))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print()
print(f"Elapsed time using threads is {end_time - start_time}")