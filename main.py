from pprint import pprint
import csv

from function import name_normalization, remove_duplicates, updating_phone_numbers

if __name__ == '__main__':


    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        print("Изначальный список")
        pprint(contacts_list)

    correct_name_list = name_normalization(contacts_list)
    no_duplicates_list = remove_duplicates(correct_name_list)
    regular = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})'
    correct_list = updating_phone_numbers(no_duplicates_list, regular, r'+7(\2)\3-\4-\5')
    regular_2 = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s]*[(доб.\s]*(\d+)[)]*'
    correct_phonebook = updating_phone_numbers(correct_list, regular_2, r'+7(\2)\3-\4-\5 доб.\6')
    print("Сортированный список")
    pprint(correct_phonebook)

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(correct_phonebook)