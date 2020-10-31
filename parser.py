import csv

with open('books.txt', mode = 'r', encoding='utf-8-sig') as books:
    b = [{k: v for k, v in row.items()}
        for row in csv.DictReader(books, skipinitialspace=True, delimiter=';')]

with open('authors.txt', mode = 'r', encoding='utf-8-sig') as authors:
    a = [{k: v for k, v in row.items()}
        for row in csv.DictReader(authors, skipinitialspace=True, delimiter=';')]

with open('magazines.txt', mode = 'r', encoding='utf-8-sig') as magazines:
    m = [{k: v for k, v in row.items()}
        for row in csv.DictReader(magazines, skipinitialspace=True, delimiter=';')]

print("\n \n  BOOKS: {}, \n \n AUTHORS: {}, \n \n MAGAZINES: {},\n \n".format(b, a, m))

books_magazines = b + m
user_input = input("Please enter valid isbn: ")
for check in books_magazines:
    if user_input == check['isbn']:
        print(check['title'])
user_email_search = input("enter email to search : ")
for email in books_magazines:
    if user_email_search == email["authors"]:
        print(email["title"])
input("press enter to sort...")
print("SORTING...", sorted(books_magazines, key=lambda k:books_magazines[0]['title']))
