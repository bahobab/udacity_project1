
# coding=utf-8
import fresh_tomatoes
import media

# instanciate class items

renoir = media.Movie("Renoir",
                    "The story of the Jeann Renoir's last model...",
                    "http://en.wikipedia.org/wiki/Renoir_%28film%29#/media/File:Renoir_%28film%29.jpg",
                    "https://www.youtube.com/watch?v=3Cv9KxLIHAE",
                    "Giles Bourdos",
                    "Michel Bouquet, Christa Theret, Vincent Rottiers, Thomas Doret",
                    "25 May 2012, Cannes",
                    "120 min",
                    "Palm d'Or?",
                    "Film",
                    "Comedy, Drama",
                    "PG-13",
                    "$6 M",
                    "$5.8 M")

seinfeld = media.TvSeries("Seinfeld",
                    "Misadventures of neurotic standup comedien Seinfeld and friends, in a New York City settings",
                    "http://images.moviepostershop.com/seinfeld-movie-poster-1990-1020469924.jpg",
                    "https://www.youtube.com/watch?v=ydHBwdgvhZo",
                    "Art Wolf",
                    "Jerry Seinfeld, Julia Louis-Dreyfus, Michael Richards, Jason Alexander",
                    "1989",
                    "22 min",
                    "Emmy, Golden Globe...",
                    "TvSeries",
                    "Jerry Seinfeld, Larry David",
                    "180",
                    "Sitcom",
                    "NBC")

fela = media.OnStage("Fela",
                    "Life and music of Fela Anikulapo Kuti, an advocate of social justice and political critique",
                    "http://www.brooklynvegan.com/img/music2/fela_discount.jpg",
                    "https://www.youtube.com/watch?v=IkJfdqoKcYg",
                    "Bill T. JonesJim",
                    "Sahr Ngaujah",
                    "4 Sept. 2008",
                    "120 min",
                    "Tony-2010",
                    "Musical",
                    "Fela Kuti",
                    "Fela Kuti",
                    "Bill T. Jones, Jim Lewis",
                    "Broadway, Chicago, London...")

verite = media.Movie("La verite",
                    "A young woman comes to try her luck in Paris. She is accused of killing her lover and faces death",
                    "http://upload.wikimedia.org/wikipedia/en/4/41/Verite.jpg",
                    "https://www.youtube.com/watch?v=CejcRKSwaq0",
                    "Henri-Georges Clouzot",
                    "Brigitte Bardot, Paul Meurisse...",
                    "2 Nov 1960",
                    "127 min",
                    "Academy-Nom",
                    "Film",
                    "Drama",
                    "n/a",
                    "n/a",
                    "n/a")

germinal = media.Movie("Germinal",
                    "Exploited minors go on strike and are repressed by mine owner",
                    "http://en.wikipedia.org/wiki/Germinal_(1993_film)#/media/File:Germinal93.jpg",
                       #"http://upload.wikimedia.org/wikipedia/en/9/9b/Germinal93.jpg",
                    "https://www.youtube.com/watch?v=chCnbs7UMSk",
                    "Claude Berri",
                    "Gerard Depardieu, Miou Miou...",
                    "29 Sept 1993",
                    "160 min",
                    "",
                    "Film",
                    "Drama",
                    "R",
                    "$27 M",
                    "$37 M")
                       
les_400_coups = media.Movie("Les 400 coups",
                    "A young boy misunderstood by his mother and mistreated by his stepfather runs away from home...",
                    "http://upload.wikimedia.org/wikipedia/en/f/f9/Quatre_coups2.jpg",
                    "https://www.youtube.com/watch?v=2cFdnN8d1j8",
                    "Francois Truffaut",
                    "Jean-Pierre Leaud, Albert Remy, Claire Maurier",
                    "4 May 1959",
                    "99 min",
                    "Cannes-Best Dir",
                    "Film",
                    "Drama",
                    "n/a",
                    "n/a","n/a")
                    
femme_mariee = media.Movie("Une femme mariee",
                    "A maried woman is tormented by a pregnacy she does not know the wether from her husband or from her lover...",
                    "http://upload.wikimedia.org/wikipedia/en/5/55/AMarriedWoman1964Poster.jpg",
                    "https://www.youtube.com/watch?v=g3_Z3vsdjKk",
                    "Jean-Luc Godard",
                    "Bernard Noel, Macha Meril",
                    "4 Dec 1964",
                    "94 min",
                    "n/a",
                    "Film",
                    "Drama",
                    "n/a",
                    "n/a","n/a")

don_camillo = media.Movie("Don Camillo",
                    "Two men, a priest and a communist leader fight in the open but admire each other behind the public eye...",
                    "http://pad.mymovies.it/filmclub/2006/01/327/locandinapg2.jpg",
                    "https://www.youtube.com/watch?v=vIJHU2f4KpU",
                    "Julien Duvivier",
                    "Fernandel, Gino Cervi...",
                    "1952",
                    "107 min",
                    "n/a",
                    "Film",
                    "Comedy",
                    "n/a",
                    "n/a","n/a")

beau_pere = media.Movie("Le beau pere",
                    "After the death of her mother, a fourteen-year-old girl falls in love with her stepfather...",
                    "http://upload.wikimedia.org/wikipedia/en/d/d3/Beau-p%C3%A8re-poster.jpg",
                    "https://www.youtube.com/watch?v=G957jPEHe28",
                    "Bertrand Blier",
                    "Patrick Dewaere, Ariel Besse...",
                    "11 Oct 1981",
                    "123 min", 
                    "n/a",
                    "Film",
                    "Drama",
                    "n/a",
                    "n/a","n/a")

the_artist = media.Movie("The Artist",
                    "The 'Talkies' ends the career of a silent movie actor when he meets a young and beautiful dancer...",
                    "http://upload.wikimedia.org/wikipedia/en/f/f3/The-Artist-poster.png",
                    "https://www.youtube.com/watch?v=H1JsxxlEG-8",
                    "Michel Hazanavicius",
                    "Jean Dujardin, Berenice Bejo...",
                    "15 May 2011",
                    "100 min",
                    "Academy-Oscar",
                    "Film",
                    "Comedy, Drama, Romance",
                    "PG-13",
                    "$15 M",
                    "$133 M")

pauline_ala_plage = media.Movie("Pauline a la plage",
                    "A mother takes some time away from her husband she's about to divorce. She takes her 15-year-old daughter with her...",
                    "http://upload.wikimedia.org/wikipedia/en/d/db/Pauline_at_the_Beach.jpg",
                    "https://www.youtube.com/watch?v=iCjGE43l_2E",
                    "Eric Rohmer",
                    "Amanda Langlet",
                    "23 March 1983",
                    "94 min",
                    "n/a",
                    "Film",
                    "Comedy, Drama, Romance",
                    "R",
                    "n/a","n/a")

black_micmac = media.Movie("Black micmac",
                    "",
                    "http://images.moviepostershop.com/black-mic-mac-movie-poster-1986-1020363561.jpg",
                    "https://www.youtube.com/watch?v=dWPdN-vDc-0",
                    "Thomas Gilou",
                    "Jacques Villeret, Isaac de Bankole, Felicite Wouassi",
                    "23 April 1986",
                    "93 min",
                    "",
                    "Film",
                    "Comedy",
                    "n/a",
                    "n/a","n/a")

diner_de_cons = media.Movie("Le diner de cons",
                    "Each week, Pierre and his friends organize what is called as 'un dîner de cons'.",
                    "http://en.wikipedia.org/wiki/Le_D%C3%AEner_de_Cons_%28film%29#/media/File:Le_d%C3%AEner_de_cons_(Poster).jpg",
                    "https://www.youtube.com/watch?v=4FANGIUNbiA",
                    "Francis Veber",
                    "Thierry Lhermite, Jacques Vileret...",
                    "15 April 1998",
                    "80 min",
                    "",
                    "Film",
                    "Comedy",
                    "PG-13",
                    "$12.5 M",
                    "$78.5 M")

truman_show = media.Movie("The Truman Show",
                    "The life of a salesman who discovers his entire life is actually tv reality show",
                    "http://www.impawards.com/1998/posters/truman_show_ver2.jpg",
                    "https://www.youtube.com/watch?v=c3gI9ms8Fdc",
                    "Peter Weir",
                    "Jim Carrey, Laura Linney...",
                    "5 June 1998",
                    "103 min",
                    "Golden Globe",
                    "Film",
                    "Drama",
                    "PG",
                    "$60 M",
                    "$264 M")

hugo = media.Movie("Hugo",
                    "An orphan who lives in the walls of a train station is wrapped up in a mystery involving his late father and an automaton.",
                    "http://http://www.imdb.com/media/rm2425270784/tt0970179?ref_=tt_ov_ihttp://www.blogcdn.com/blog.moviefone.com/media/2011/10/hugo-poster-big.jpg",
                    "https://www.youtube.com/watch?v=hR-kP-olcpM",
                    "Martin Scorsese",
                    "Asa Butterfield, Chloe Grace Moretz...",
                    "23 Nov 2011",
                    "126 min",
                    "",
                    "Film",
                    "Adventure, Drama, Family",
                    "PG",
                    "$170 M",
                    "$73 M")


#sin_city = media.Movie("Sin City",
#            "A film that explores the dark and miserable town, Basin City, and tells the story of these...",
#            "http://oyster.ignimgs.com/wordpress/stg.ign.com/2014/05/Sin-City2-ALBA-poster-610x903.jpg",
#            "https://www.youtube.com/watch?v=nqRRF5y94uE")
#sin_city = media.Movie("Sin City",
#                         "A film that explores the dark and miserable town, Basin City, and tells the story of three different people, all caught up in violent corruption.",
#                         "http://oyster.ignimgs.com/wordpress/stg.ign.com/2014/05/Sin-City2-ALBA-poster-610x903.jpg",
#                          "https://www.youtube.com/watch?v=nqRRF5y94uE")
#hitch = media.Movie("Hitch",
#                      "While helping his latest client woo the fine lady of his dreams, a professional 'date doctor' finds that his game doesn't quite work on the gossip columnist with whom he's smitten.",
#                       "http://www.impawards.com/2005/posters/hitch.jpg",
#                        "https://www.youtube.com/watch?v=lp--Un6fNro")

#dark_knight = media.Movie("Dark Knight",
#                                   "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
#                                   "http://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
#                                   "https://www.youtube.com/watch?v=EXeTwQWrcwY")

#the_artist = media.Movie("The Artist",
#                                   "A silent movie star meets a young dancer, but the arrival of talking pictures sends their careers in opposite directions.",
#                                   "http://http://www.imdb.com/media/rm3029383424/tt1655442?ref_=tt_ov_ihttp://www.circlecinema.com/wp-content/uploads/2012/01/The-Artist-Poster.jpeg",
#                                   "https://www.youtube.com/watch?v=O8K9AZcSQJE")

#les_jeux_sont_faits = media.Movie("Les jeux sont faits",
#                                  "Two people discover they love each other in the afterlife and get a second chance...",
#                                  "",
#                                  "http://")
#la_vie_dun_honete_homme media.Movie("La vie d'un honete homme",
#                                    "",
#                                    "http://",
#                                    "http://")
#marius = media.Movie("Marius",
#                     "",
#                     "http://",
#                     "http://")
#cesar = media.Movie("Cesar",
#                    "",
#                    "http://",
#                    "http://")
#gribouille = media.movie("Gribouille",
#                         "",
#                         "http:",
#                         "http://")
#la_femme_du_boulager = media.Movie("La Femme du boulanger",
#                                   "",
#                                   "http://",
#                                   "http://")

# add movies to list
movies = [the_artist,
          verite,
          les_400_coups,
          truman_show,
          seinfeld,
          fela]
#          hugo,
#          renoir,
#          germinal,
#          diner_de_cons,
#          femme_mariee,
#          don_camillo,
#          beau_pere,
#          pauline_ala_plage,
#          black_micmac]

# call fresh_tomatoes with the list
fresh_tomatoes.open_movies_page(movies)

