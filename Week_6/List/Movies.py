Movies_watched_by_me = ["REMO", "SPIDER MAN", "MONEY HIEST", "VIKRAM", "BEAST", "MASTER"]
#asking how many movies does my friend watched recently?
Total_no_of_movies = int(input("How many movies did you watched recently ? : "))
#creating lists for some specifications like
#Movies_watched_by_my_friend 
# Movies_watched_by_me_alone 
# Movies_watched_by_my_friend_alone 
# Movies_watched_by_us_both 
Movies_watched_by_my_friend = []
Movies_watched_by_me_alone = []
Movies_watched_by_my_friend_alone = []
Movies_watched_by_us_both = []
#using for loop for getting the input of the name of the movie he watched
for movie in range(Total_no_of_movies):
    watched = input("Tell me the name of the movie ? : ")
    Movies_watched_by_my_friend.append(watched)
#using another for loop for checking the movies watched by both of us and movies watched by him alone and checking
#  with the if condition and printing it

for his_movie in range(len(Movies_watched_by_my_friend)):
    both_watched = False
    for my_movie in range(0, len(Movies_watched_by_me)):
        if(Movies_watched_by_my_friend[his_movie] == Movies_watched_by_me[my_movie]):
            Movies_watched_by_us_both.append(Movies_watched_by_my_friend[his_movie])
            both_watched = True
    if(both_watched == False):
        Movies_watched_by_my_friend_alone.append(Movies_watched_by_my_friend[his_movie])


for movie in range(len(Movies_watched_by_me)):
    if Movies_watched_by_me[movie] not in Movies_watched_by_my_friend:
        Movies_watched_by_me_alone.append(Movies_watched_by_me[movie])

print("Movies watched by us both\n", Movies_watched_by_us_both)
print("Movies watched by me alone\n", Movies_watched_by_me_alone)
print("Movies watched by my friend alone\n", Movies_watched_by_my_friend_alone)

# Output
# TEST CASE 1
# How many movies did you watched recently ? : 3   
# Tell me the name of the movie ? : REMO
# Tell me the name of the movie ? : MAARA
# Tell me the name of the movie ? : VILLAIN
# Movies watched by us both
#  ['REMO']
# Movies watched by me alone
#  ['SPIDER MAN', 'MONEY HIEST', 'VIKRAM', 'BEAST', 'MASTER']
# Movies watched by my friend alone
#  ['MAARA', 'VILLAIN']
#  TEST CASE 2
#  How many movies did you watched recently ? : 2
# Tell me the name of the movie ? : VIKRAM VETHA 
# Tell me the name of the movie ? : NO WAY HOME
# Movies watched by us both
#  []
# Movies watched by me alone
#  ['REMO', 'SPIDER MAN', 'MONEY HIEST', 'VIKRAM', 'BEAST', 'MASTER']
# Movies watched by my friend alone
#  ['VIKRAM VETHA', 'NO WAY HOME']
#  TEST CASE 3
#  How many movies did you watched recently ? : 3
# Tell me the name of the movie ? : REMO
# Tell me the name of the movie ? : VIKRAM
# Tell me the name of the movie ? : SEETHA RAMAM
# Movies watched by us both
#  ['REMO', 'VIKRAM']
# Movies watched by me alone
#  ['SPIDER MAN', 'MONEY HIEST', 'BEAST', 'MASTER']
# Movies watched by my friend alone
#  ['SEETHA RAMAM']
