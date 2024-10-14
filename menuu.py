try:
    book_lst = []
    while True:
        def menu():
            print("1. Добавить книгу \n"
                  "2. Удалить книгу \n"
                  "3. Показать список книг \n"
                  "4. Очистить список книг \n")
        menu()

        def book_plus(book):
            book_lst.append(book)
        def book_minus(book):
            book_lst.remove(book)
        def listt_book():
            print(book_lst)
        menu = int(input())
        if menu == 1:
            book_plus(input("Введите имя книги которую необходимо добавить: "))
        elif menu == 2:
            book_minus(input("Введите имя книги которую необходимо удалить: "))
        elif menu == 3:
            listt_book()
        elif menu == 4:
            book_lst.clear()
except ValueError:
    print("Такой книги не существует")
