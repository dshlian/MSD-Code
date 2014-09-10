import random
import math
from sys import argv
script, j = argv
j = int(j)

#counters
in_circle = 0.0
in_square = 0.0
i = 0

#function for random dart in square
def dart(in_circle, in_square):
	dart_x = random.random()
	dart_y = random.random()
	in_square += 1
	if dart_y <= math.sqrt(1 - math.pow(dart_x, 2)):
		in_circle += 1
	return (in_circle, in_square)
	
	
#loop the dartboard
while i!=j:
	i += 1
	in_circle, in_square = dart(in_circle, in_square)
	
est_pi = 4 * (in_circle / in_square)
print "%d of %d darts landed in the circle, yielding a pi estimate of %f." % (in_circle, in_square, est_pi)
	