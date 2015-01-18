import random
guesses_made = 0;
name=raw_input("hello! what is your name?\n")
#using raw_input method will prompt the following sentence and then 
#exit until receive an input

number =random.randint(1,20)
print "well,{0}, I am thinking of a number between 1 and 20.".format(name);
#we could also use tag id instead: i.e. {id_tag}.format(id_tag=variable)

while guesses_made < 6:
	guess = int(raw_input("Take a guess:"));
	guesses_made = guesses_made+1;

	if guess<number:
		print "Too LOW!"

	if guess>number:
		print "Too HIGH"

	if guess==number:
		break;

if guess==number:
	print "good job, {0}! you guessed my number in {1} rounds".format(name, guesses_made);
else:
	print "Nope. The number I was thinking of was {0}".format(number);