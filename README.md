# Искусственная симуляция блокчейн системы, разработанная для эмуляции DDOS-атак и дальнейшего анализа их
Сам блокчейн запускается как веб-сервис на flask (python blockchain.py)\n
Для взаимодействия с блокчейном используются http запросы (примеры ddos атаки на систему в emulate_blockchain_ddos.py)\n
В дальнейшем мы просто выкачиваем c сервера всю инфу по блокам(get_data.py)
И анализируем ее в ipynb\n
TODO:\n
Создать, обучить и встроить в блокчейн модель, позволяющую определять вредные транзакции 
