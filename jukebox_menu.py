albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

for name, artist, year, songs in albums:
    print(f"Album: {name} | Artist: {artist} | Year: {year} | Songs: {songs}")
print()
print("Just enter 0 whenever you want to terminate (quit) the program.")

option = None

while True:
    if option is None:
        print("Please choose the album you want to look at: ")
        for index, (title, artist, year, songs) in enumerate(albums):
            print(f"{index + 1}: {title} | {artist} | {year}")
        option = int(input())

    if 1 <= option <= len(albums):
        print(f"You chose album {option}")
        songs_list = albums[option - 1][SONGS_LIST_INDEX]
    elif option == 0 or option == -0:
        print("You have chosen to quit the program.")
        break
    else:
        print("Sorry, you have to choose a number respective \nto the album you want to look at.")
        option = None
        continue

    print("Please choose the song you want to hear: ")
    for index, (track_number, song) in enumerate(songs_list):
        print(f"{index + 1}: {song}")

    song_option = int(input())
    if 1 <= song_option <= len(songs_list):
        print(f"You chose song {song_option}")
        title = songs_list[song_option - 1][SONG_TITLE_INDEX]
    elif song_option == 0 or song_option == -0:
        print("You have chosen to quit the program.")
        break
    else:
        print("Sorry, you have to choose a number respective \nto the song you want to hear.")
        continue
    option = None
    print(f"Playing: {title}")
    print("=" * 50)
    print("Thank you for choosing your album and your song using IntelliJ IDEA!")










