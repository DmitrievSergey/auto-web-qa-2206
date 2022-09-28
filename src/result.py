import pprint
import subprocess
from contextlib import redirect_stdout
from datetime import datetime


def get_processes():
    output = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).stdout.readlines()

    headers = [h for h in ' '.join(output[0].decode('utf-8').strip().split()).split() if h]
    raw_data = map(lambda s: s.decode('utf-8').strip().split(None, len(headers) - 1), output[1:])
    return [dict(zip(headers, r)) for r in raw_data]


list_of_processes = get_processes()


def get_users():
    list_of_users = []
    for line in list_of_processes:
        list_of_users.append(line.get('USER'))
    return set(list_of_users)


def count_processes():
    return len(list_of_processes)


def processes_by_user():
    proc_by_user = {}
    for user in get_users():
        cnt = 0
        for line in list_of_processes:
            if line.get('USER') == user:
                proc_by_user[user] = cnt
                cnt += 1
    return proc_by_user


def all_memory_usage():
    all_mem = 0
    for line in list_of_processes:
        all_mem += float(line.get('%MEM'))
    return all_mem


def all_cpu_usage():
    all_cpu = 0
    for line in list_of_processes:
        all_cpu += float(line.get('%CPU'))
    return all_cpu


def max_memory_usage():
    list_of_memory = []
    proc_max_mem = 0
    for line in list_of_processes:
        if float(line.get('%MEM')) > proc_max_mem:
            list_of_memory.append(line)
            proc_max_mem = float(line.get('%MEM'))
    return list_of_memory[0].get('%MEM'), list_of_memory[0].get('COMMAND')


def max_cpu_usage():
    list_of_cpu = []
    proc_max_cpu = 0
    for line in list_of_processes:
        if float(line.get('%MEM')) > proc_max_cpu:
            list_of_cpu.append(line)
            proc_max_cpu = float(line.get('%CPU'))
    return list_of_cpu[0].get('%CPU'), list_of_cpu[0].get('COMMAND')


def sys_report():
    print('Пользователи системы: ', get_users())
    print('Процессов запущено: ', count_processes())
    print('Пользовательских процессов: ')
    pprint.pprint(processes_by_user())
    print(f'Всего памяти используется: {round(all_memory_usage(), 2)} %')
    print(f'Всего CPU используется: {round(all_cpu_usage(), 2)} %')
    print(f'Больше всего памяти использует: %{max_memory_usage()[0]}, {max_memory_usage()[1]}')
    print(f'Больше всего CPU использует: %{max_cpu_usage()[0]}, {max_cpu_usage()[1]}')


sys_report()

with open('{}-scan.txt'.format(datetime.now().strftime("%d-%m-%Y-%H:%M")), 'w') as f:
    with redirect_stdout(f):
        sys_report()
