import media
import fresh_tomatoes

#Instances calling the atributes of the Movie class: movie_title, movie_storyline, poster_image, trailer_youtube
fifty_shades_darker = media.Movie("Fifty Shades Darker", "While Christian wrestles with his inner demons, Anastasia must confront the anger and envy of the women who came before her.", "https://i.ytimg.com/vi/hyEpF8Cd3pY/hqdefault.jpg", "https://youtu.be/OItKvc13gws")

trolls = media.Movie("Trolls", "After the Bergens invade Troll Village, Poppy, the happiest Troll ever born, and the curmudgeonly Branch set off on a journey to rescue her friends.", "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSBo7b0ngMRP3uld-YpTzuImP5NgLusjKKW7ZOPuobRk_XoR4tF", "https://youtu.be/xyjm5VQ11TQ")

silver_linings = media.Movie("Silver Linings",
                            #  "After a stint in a mental institution, former teacher Pat Solitano moves back in with his parents and tries to reconcile with his ex-wife.Things get more challenging when Pat meets Tiffany, a mysterious girl with problems of her own.",
                             "teste teste",
                             "https://upload.wikimedia.org/wikipedia/en/9/9a/Silver_Linings_Playbook_Poster.jpg",
                             "https://youtu.be/Lj5_FhLaaQQ")

the_revenant = media.Movie("The Revenant", "A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear and left for dead by members of his own hunting team.", "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg", "https://youtu.be/LoebZZ8K5N0")

mad_max = media.Movie("Mad Max", "A woman rebels against a tyrannical ruler in postapocalyptic Australia in search for her home-land with the help of a group of female prisoners, a psychotic worshipper, and a drifter named Max.","http://static.metacritic.com/images/products/movies/1/75341fb373e410eb339784e65a09f140.jpg", "https://youtu.be/hEJnMQG9ev8")

hunger_games = media.Movie("Hunger Games", "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://youtu.be/4S9a5V9ODuY")

#Array with the instances
movies = [fifty_shades_darker, trolls, silver_linings, the_revenant, mad_max, hunger_games]

#reveive a list of movies and transforme to a html file and stores in the folder as your code
fresh_tomatoes.open_movies_page(movies)
