from flask import Flask, render_template, request
import giphypop


def get_gif(gifname):
	g = giphypop.Giphy()
	results = g.search('cats') # returns a list of objects
	for result in results:
		print(result.media_url)
		print(result.url)
	return g