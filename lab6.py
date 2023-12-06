class Book:
    def __init__(self, page_num, page_time, pict_num):
        self.page_num = page_num
        self.page_time = page_time
        self.pict_num = pict_num

    def get_read_time(self):
        print(self.page_num * self.page_time)

    @staticmethod
    def read_book(reader):
        print(f'Книгу читает {reader}')


class Encyclopedia(Book):
    def __init__(self, page_num, page_time, pict_num, total_info):
        super().__init__(page_num, page_time, pict_num)
        self.total_info = total_info

    def count_info_on_page(self):
        print(self.total_info // self.page_num)


class PhoneBook(Encyclopedia):
    def __init__(self, page_num, page_time, pict_num, total_info):
        super().__init__(page_num, page_time, pict_num, total_info)
        self.base = {'Я': '8(999)123-45-67'}

    def create_new_rec(self, name, num):
        self.base[name] = num
        print('Номер добавлен!')

    def delete_rec(self, name):
        del self.base[name]

    def show_base(self):
        print(self.base)


class BookShelf:
    def __init__(self):
        self.books = []

    def add_book(self, book_data):
        book_data = book_data.split(', ')
        self.books.append(book_data)

    def show_books_on_shelf(self):
        print(*self.books)

    def search_type(self, type):
        for data in self.books:
            if data[1] == type:
                print(' '.join(data))

'''
book1 = Book(100, 15, 20)
book1.get_read_time()
book2 = Encyclopedia(200, 30, 100, 500)
book2.get_read_time()
book2.count_info_on_page()
book3 = PhoneBook(20, 3, 0, 400)
book3.get_read_time()
book3.count_info_on_page()
book3.read_book('Anne')
book3.create_new_rec('Nastya', '8(888)324-98-00')
book3.show_base()
book3.delete_rec('Nastya')
book3.show_base()
shelf = BookShelf()
shelf.add_book('my phones, phonebook')
shelf.add_book('animals, encyclopedia')
shelf.show_books_on_shelf()
shelf.search_type('encyclopedia')
'''