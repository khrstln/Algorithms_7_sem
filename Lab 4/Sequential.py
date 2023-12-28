from Client import Client
from Server import Server
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

start_time = time.time()

srvr.register_clients(clients_for_reg, T1)
srvr.get_main_pages(clients_main_page, T2)
srvr.check_reg_lists(clients_reg_list, T3)

end_time = time.time()

print()
print(f"Elapsed time in sequential case is {end_time - start_time}")