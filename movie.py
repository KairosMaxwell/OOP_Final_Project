
# Movie attribute must be hidden
class Movie:

    genres_overall =["Action","Comedy","Drama","Horror","Sci-Fi","Romance","Thriller","Animation","Documentary","Fantasy"]


    def __init__(self,ids,title,director,genre, available,price,fine_rate,rental_count):
        self.__ids = ids
        self.__title = title
        self.__director = director
        self.__genre = genre
        self.__available = available
        self.__price = 0
        self.__fine_rate = fine_rate
        self.__rental_count = rental_count

    def __str__(self):
        return f"{self.__ids}\t{self.__title}\t{self.__director}\t{self.__genre}\t{self.__available}\t{self.__rental_count}"


    # Getters
    def get_ids(self):
        return self.__ids
    def get_title(self):
        return self.__title
    def get_director(self):
        return self.__director
    def get_genre(self):
        return self.__genre
    def get_available(self):
        return self.__available
    def get_price(self):
        return self.__price
    def get_fine_rate(self):
        return self.__fine_rate
    def get_rental_count(self):
        return self.__rental_count

    def get_availability(self):
        if self.__available is True:
            return "Available"
        else:
            return "Rented"


    def get_genre_name(self):
        genre_name = input("Enter genre name: ")
        if genre_name in Movie.genres_overall:
            return genre_name






#     Setters
    def set_ids(self, ids):
        self.__ids = ids
    def set_title(self, title):
        self.__title = title
    def set_director(self, director):
        self.__director = director
    def set_genre(self, genre):
        self.__genre = genre
    def set_price(self, price):
        self.__price = price
    def set_fine_rate(self, fine_rate):
        self.__fine_rate = fine_rate


    def borrow_movie(self):
        pass


    def return_movie(self):
        pass





