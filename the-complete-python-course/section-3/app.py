"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and
    'q' to quit.

- Add movies
- See movies
- Find a movie
- Stop running the progrm

"""

movies = []

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see the collection, \
'f' to find a movie, or 'q' to quit: ")

    while user_input != "q":
        if user_input == "a":
            add_movie()
        elif user_input == "l":
            list_movies()
        elif user_input == "f":
            find_by = input("Which search item? (movie/year/director): ")
            search_term = input("What do you want to search for? ")
            if find_by not in ["movie", "year", "director"]:
                print("Key to search is invalid")
            else:
                movie = find_movie(search_term, lambda x: x[find_by])
                print(movie or 'No movies found.')
        else:
            print("Wrong option.")
        user_input = input("Enter 'a' to add a movie, 'l' to see the collection, \
'f' to find a movie, or 'q' to quit: ")

    print("Thanks, and have a good day!")

def add_movie():
    movie = input("Enter the name of the movie: ")
    year = input("Enter the year of the movie: ")
    director = input("Enter the director of the movie: ")
    movies.append({
        'movie': movie,
        'year': year,
        'director': director}
    )
    print(f"{movie} has been added.")

def list_movie_info(movie):
    print(f"Title: {movie['movie']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")

def list_movies():
    for movie in movies:
        list_movie_info(movie)

def find_movie(search_term, search_func):
    result = []
    for movie in movies:
        if search_func(movie) == search_term:
            result.append(movie)
    return result

menu()