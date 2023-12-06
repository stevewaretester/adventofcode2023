# adventofcode2023
my advent of code work - if interested feel free to join a leaderboard of mine to see how you did:

3278293-29c0c75c

Difficulty ranking:
(from easiest to hardest)
6,4,2,1,3............5

Retrospectives
#https://adventofcode.com/2023/day/1
Day 1 part 1 was fairly easy, but part 2 I went hard on, coming up with a solution that used objects and their relative positions. This was overkill and there's smarter solutions, but it worked and feels the most "true" - i.e I could throw other variations without word-numbers and get an accurate result.

#https://adventofcode.com/2023/day/2
I can't remember too much of this one, it felt easier than the 1st day, and part 2 is a simple "replace with the bigger number" challenge for multiple different attributes, fairly easy.

#https://adventofcode.com/2023/day/3

Jesus H christ - there's probably easier ways of doing something like this, but I wanted to do it using a 2d-array, the problem with that is checking around a string of characters, which I did by essentially...
Checking the back column, then checking up and down, then checking if whatever right is another number, then stringing them together until the end and checking the fore-column.
A lot of x-1, y-1 and checking I'm not going out of bounds.
There must be an easier solution because this was awful to navigate, I cheated the second part by just limiting my symbols to an asterisk and going again.

#https://adventofcode.com/2023/day/4
Another breeze comparatively. The trick, for the second part, is simply realising that copies of scratchcards have the same score, so if you have 3 of one, and one only has a single winning value, there's 3 of two.
Relatively easy compared to Day 3.#

#https://adventofcode.com/2023/day/5
Oh fuck off - I feel like this is purposefully written to be as obnoxious and ambiguous as possible.
I'll be skipping today until a later point.

#https://adventofcode.com/2023/day/6
Much easier, I realised that you could just go through every number and count as you do, but it's actually easier to loop forwards and then loop backwards - commiting only the max and minimum numbers.
Because numberOfValidInputs = (Max-Min)+1 
