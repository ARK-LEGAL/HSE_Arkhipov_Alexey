import json
import re
import csv

# Step 1: Извлекаем ИНН из traders.txt
with open('traders.txt', 'r', encoding='utf-8') as file:
    inn_list = file.read().splitlines()

# Step 2: Find information in traders.json
with open('traders.json', 'r', encoding='utf-8') as file:
    traders_data = json.load(file)

# Извлекаем данные для CSV
traders_info = []
for inn in inn_list:
    for trader in traders_data:
        if trader.get('ИНН') == inn:
            traders_info.append({
                'ИНН': inn,
                'ОГРН': trader.get('ОГРН', 'N/A'),
                'Адрес': trader.get('Адрес', 'N/A')
            })
            break

# Сохраняем в traders.scv
csv_file_path = 'traders.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ИНН', 'ОГРН', 'Адрес']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(traders_info)

#csv_file_path


def find_emails(text):
    # Regular expression for finding email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)


# Загружаем датасет
with open('1000_efrsb_messages.json', 'r', encoding='utf-8') as file:
    messages_data = json.load(file)

# Collect emails by publisher_inn
emails_dict = {}
for message in messages_data:
    publisher_inn = message.get('publisher_inn')
    msg_text = message.get('msg_text', '')

    if publisher_inn:
        emails = find_emails(msg_text)
        if emails:
            if publisher_inn not in emails_dict:
                emails_dict[publisher_inn] = set()
            emails_dict[publisher_inn].update(emails)

# Преобразуем сеты для JSON
emails_dict_serializable = {k: list(v) for k, v in emails_dict.items()}

# Сохраняем в emails.json
emails_file_path = 'emails.json'
with open(emails_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(emails_dict_serializable, jsonfile, ensure_ascii=False, indent=4)

# emails_file_path
