# Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty simple program, so to make it a bit harder, here are some rules to follow.
# RULES
# If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
# Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
# Put a blank line between each verse of the song.
# https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/
def print_lyrics():


	'''
	This function will print the lyrics for 99 bottles of beer on the wall
	'''
	for x in range(99,2,-1):
		#triple quotes for multiline strings
		print("{} bottles of beer on the wall,{} bottles of beer.\n\tTake one down and pass it around,{} bottles of beer on the wall.\n".format(x,x,x-1))
	#printing last four lines as they are different
	print("2 bottles of beer on the wall, 2 bottles of beer.\n\tTake one down and pass it around, 1 bottle of beer on the wall\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
print_lyrics()
