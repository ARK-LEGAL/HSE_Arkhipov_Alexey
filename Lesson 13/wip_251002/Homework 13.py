import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import tempfile

class ParserCBRF:
    def __init__(self, url: str, output_dir: str = None):
        """
        Инициализация парсера.
        :param url: Ссылка на страницу или файл для парсинга.
        :param output_dir: Директория для сохранения файлов. Если не указана, используется временная директория.
        """
        self.url = url
        self.output_dir = output_dir if output_dir else tempfile.gettempdir()
        self.data = {}

    def start(self) -> dict:
        """
        Публичный метод для запуска парсинга.
        :return: Словарь с данными.
        """
        if self.url.endswith(('.xlsx', '.xls', '.csv', '.pdf')):
            self.__download_file()
            self.__parse_file()
        else:
            self.__parse_web_page()
        return self.data

    def __download_file(self) -> None:
        """Приватный метод для загрузки файла."""
        try:
            response = requests.get(self.url, stream=True)
            response.raise_for_status()
            file_name = os.path.join(self.output_dir, os.path.basename(self.url))
            with open(file_name, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Файл успешно загружен: {file_name}")
        except Exception as e:
            print(f"Ошибка при загрузке файла: {e}")

    def __parse_file(self) -> None:
        """Приватный метод для парсинга файла."""
        file_name = os.path.join(self.output_dir, os.path.basename(self.url))
        try:
            if self.url.endswith('.xlsx') or self.url.endswith('.xls'):
                df = pd.read_excel(file_name)
            elif self.url.endswith('.csv'):
                df = pd.read_csv(file_name)
            else:
                print("Формат файла не поддерживается для парсинга.")
                return

            # Пример парсинга для ключевой ставки ЦБ РФ
            for _, row in df.iterrows():
                date = row.get('Дата', None)
                value = row.get('Значение', None)
                if date and value:
                    self.data[date] = value
        except Exception as e:
            print(f"Ошибка при парсинге файла: {e}")

    def __parse_web_page(self) -> None:
        """Приватный метод для парсинга веб-страницы."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Пример парсинга ключевой ставки ЦБ РФ
            # Логика зависит от структуры страницы
            # Например, если данные в таблице:
            table = soup.find('table')
            if table:
                for row in table.find_all('tr')[1:]:  # Пропускаем заголовок
                    columns = row.find_all('td')
                    if len(columns) >= 2:
                        date = columns[0].text.strip()
                        value = columns[1].text.strip()
                        self.data[date] = value
        except Exception as e:
            print(f"Ошибка при парсинге веб-страницы: {e}")

# Пример использования
if __name__ == "__main__":
    # Пример для парсинга веб-страницы
    url = "https://www.cbr.ru/hd_base/KeyRate/"
    parser = ParserCBRF(url)
    result = parser.start()
    print(result)

    # Пример для парсинга файла
    # file_url = "https://www.cbr.ru/s/key-rate?file=key-rate.xlsx"
    # parser = ParserCBRF(file_url)
    # result = parser.start()
    # print(result)
