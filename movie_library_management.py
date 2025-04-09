"""
 The application should allow users to add, update, remove, search for, rent, and
return a movie. The application also allows the user to list movies by genre, list the top rented
movies, check the movies availability by genre, and display a summary of the movies’ library

"""

def load_movie(file_name):
    with open(file_name,'r') as f:
        for data in f.readlines():
            return data

def save_movies(file_name,movies):
    with open(file_name,'w') as f:
        for data in movies:
            f.write(data)

def print_menu():
    pass














def main():
    if __name__ == "__main__":
        main()
