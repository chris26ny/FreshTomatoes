import webbrowser

class Movie():
	def __init__(self, title, plot, poster_url, trailer_url):
		self.title = title
		self.plot = plot
		self.poster_url = poster_url
		self.trailer_url = trailer_url
	
	def show_trailer(self):
   		webbrowser.open(self.trailer_url)