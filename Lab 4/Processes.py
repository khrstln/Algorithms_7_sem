from Client import Client
from Server import Server
import multiprocessing
import time

if __name__ == "__main__":

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
    processes = []

    start_time = time.time()

    for i in range(U1):
        client = clients_for_reg[i]
        thread = multiprocessing.Process(target=srvr.register_client, args=(client, T1))
        processes.append(thread)
        thread.start()

    for j in range(U2):
        client = clients_main_page[j]
        thread = multiprocessing.Process(target=srvr.get_main_page, args=(client, T2))
        processes.append(thread)
        thread.start()

    for k in range(U3):
        client = clients_reg_list[k]
        thread = multiprocessing.Process(target=srvr.check_reg_list, args=(client, T3))
        processes.append(thread)
        thread.start()

    for thread in processes:
        thread.join()

    end_time = time.time()

    print()
    print(f"Elapsed time using multiprocessing is {end_time - start_time}")