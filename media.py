import webbrowser

class Entertainment():
    """ Base class for the entertainment web page
    CLASSIFICATION is class variable"""
	
    CLASSIFICATION = ["Film", "Documentary", "TV Series", "Play", "Musical"]
	
    def __init__(self, title, storyline, poster_image,
			trailer_youtube, director, star, premiere,
			runtime, awards, classification):
        """Base class constructor attributes:
	movie_title: title of the movie
	movie_storyline: storyline of the movie
	poster_image: link of the poster image of the movie
	trailer_youtube: link of the youtube trailer of the movie"""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.star = star
        self.premiere = premiere
        self.runtime = runtime
        self.awards = awards
        self.classification = classification
	    
    def __str__(self):
        """__str__ () returns sumarry info of the object"""
        return ("this is {0} of {1} class".format(self.title, self.__class__))

class Movie(Entertainment):
    """ class for feature films and documentaries.
    it inherits from the Entertainment base class
    with VALID_RATINGS and GENRE as class variables"""
        
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    GENRE = ["COMEDY", "DRAMA", "THRILLER", "SCiFi","FAMILY"]
	
    def __init__(self, title, storyline, poster_image,
    	    trailer_youtube, director, star, premiere, runtime, awards,
		classification, genre, rating, budget, boxoffice):
    	"""Movie class own attributes:
    	GENRE, RATING, budget, boxoffice"""
	    
        Entertainment.__init__(self, title, storyline, poster_image,
	    trailer_youtube, director, star, premiere, runtime, awards,
	    classification)
        self.genre = genre
	self.rating = rating
	self.budget = budget
	self.boxoffice = boxoffice
	

    def show_trailer(self):
	"""Method that plays the youtube trailer of the movie"""
        webbrowser.open(self.trailer_youtube_url)
            
    def __str__(self):
        """ Return object info """
        return ("This is {0} of {1} class".format(self.title, self.__class__))
            
class TvSeries(Entertainment):
    """ class definition for Tv Series
    inherits from Entertainment base class"""
    
    TV_STATIONS = ["ABC", "AL_JAZEERA", "BBC", "CBS", "FOX",
    			"FRANCE24", "NBC", "HBO"]
    def __init__(self, title, storyline, poster_image,
    	    trailer_youtube, director, star, premiere, runtime, awards,
    	    classification, created_by,
    	    episodes, series_type, tv_station):
    	"""TvSeries class own attributes:
    	created_by, episodes,series_type, tv_station"""
    
    	Entertainment.__init__(self, title, storyline, poster_image,
    	    trailer_youtube, director, star, premiere, runtime, awards,
    	    classification)
    	self.created_by = created_by
    	self.episodes = episodes
    	#self.run_time = run_time
    	self.series_type = series_type
    	self. tv_station = tv_station
    
    def __str__(self):
    	""" Return object info """
    	return ("This is {0} of {1} class".format(self.title, self.__class__))
    	#pass
    

class OnStage(Entertainment):
    """ class definition for musicals and plays
    inherits from Entertainment base class"""
    def __init__(self, title, storyline, poster_image,
    	    trailer_youtube, director, star, premiere, runtime, awards,
    	    classification, music, lyrics, book, productions):
    	"""Movie class own attributes:
    	music, lyrics, book, productions"""
    	
	Entertainment.__init__(self, title, storyline, poster_image,
		trailer_youtube, director, star, premiere, runtime, awards,
		classification)
	#self.stage_type = stage_type
	self.music = music
	self.lyrics = lyrics
	self.book = book
	self.productions = productions
	
    def __str__(self):
        """ Return object info """
	return ("this is {0} of {1} class".format(self.title, self.__class__))
        
