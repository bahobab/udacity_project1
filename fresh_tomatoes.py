import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #CCCC99;
            cursor: pointer;
            border:2px solid;
            border-color:#CC6600;
            border-radius:5px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
            
        }
	.info {
	    background-color: #D3D3D3;
	    line-height: 0.5;
	    marging-top: 1px;
	    margin-bottom: 7px;
	    padding-bottom:2px;
	    border: 2px solid;
	    border-radius: 5px;
	    border-color:#999900;
	   
	}
	.classification{
		background-color: white;
		border-radius:5px;
	}
	.navbar-brand{
		font-color:#ccc666333;
	}
	
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#"><p><font color="red">Konan's Favorite Movie Trailers</font></p></a>
          </div>
        </div>
      </div>
    </div>
    
    <div class="container">
      {movie_tiles}
    </div>
    
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="poster-image"><img src="{poster_image_url}" width="220" height="342"></div>
    <div class = "classification">
    	<h4>{movie_title}</h4>
    </div>
    <div class="info">
    	<h5>{movie_storyline}</h5>
    	<h6>{movie_info}</h6>	
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    info = ''
    story_line = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
	
	if (movie.classification == "Film") or (movie.classification == "Documentary"):
	#if a movie or a documentary
		info = "<strong>Dir: </strong>" + movie.director + \
			"<strong> | Stars: </strong>" + movie.star + \
			"<strong> | Rating: </strong>" + movie.rating + \
			"<strong> | Runtime: </strong>" + movie.runtime + \
			"<strong> | Awards: </strong>" + movie.awards + \
			"<strong> | 1ere'd: </strong>" + movie.premiere + \
			"<strong> | Budget: </strong>" + movie.budget + \
			"<strong> | Boxoffice: </strong>" + movie.boxoffice
			
	elif movie.classification == "TvSeries":
	#if a TvSeries
		info = "<strong>Dir: </strong>" + movie.director + \
			"<strong> | Stars: </strong>" + movie.star + \
			"<strong> | Episodes: </strong>" + movie.episodes + \
			"<strong> | Type: </strong>" + movie.series_type + \
			"<strong> | Runtime: </strong>" + movie.runtime + \
			"<strong> | TV Station: </strong>" + movie.tv_station + \
			"<strong> | Awards: </strong>" + movie.awards + \
			"<strong> | 1ere'd: </strong>" + movie.premiere
			
	elif movie.classification == "Musical" or "Play":
	#if a play or a musical
		info = "<strong> Dir: </strong>" + movie.director + \
			"<strong> | Stars: </strong>" + movie.star + \
			"<strong> | Lyrics: </strong>" + movie.lyrics + \
			"<strong> | Music: </strong>" + movie.music + \
			"<strong> | Book: </strong>" + movie.book + \
			"<strong> | Runtime: </strong>" + movie.runtime + \
			"<strong> | Awards: </strong>" + movie.awards + \
			"<strong> | 1ere'd: </strong>" + movie.premiere
		
	content += movie_tile_content.format(
            movie_title= movie.classification + ": " + movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
	    movie_storyline = movie.storyline,
	    movie_info = info
        )
#movie_director=movie.director,
#movie_premiere=movie.premiere
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
