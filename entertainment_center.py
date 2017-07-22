import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that came to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar","A marine on an alien planet",
		"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
		"https://www.youtube.com/watch?v=5PSNL1qE6VY")

spiderman = media.Movie("Spider-man Home Coming",
	"Spider-Man: Homecoming is a 2017 American superhero film based on the Marvel Comics character Spider-Man",
	"https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
	"https://www.youtube.com/watch?v=39udgGPyYMg")
	

khaidi = media.Movie("Khaidi no 150",
	"Megastar's 150 movie..Boss is back",
	"https://upload.wikimedia.org/wikipedia/en/0/0e/Chiranjeevi%27s_Khaidi_No.150_poster.jpg",
	"https://www.youtube.com/watch?v=UwYfxVlwy64")


#print (avatar.storyline)
#avatar.show_trailer()

#print (khaidi.storyline)
#khaidi.show_trailer()

movies = [toy_story,avatar,spiderman,khaidi]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)