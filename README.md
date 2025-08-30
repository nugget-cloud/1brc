# 1 Billion Rows Challenge

## Restrictions
I cannot use any library except the Python standard library, just to make this fun. I will do this challenge again in Go as well, to extend my knowledge, since I am very weak in Go. But here we are.

### Approach 1  
Day 1: This was the most naive approach, using async. Sadly, the code does not run with a billion rows altogether—I get no output. I need to figure this out.

Day 2: Well, the initial enthusiasm has worn off and I have no clue how this all works. It turns out Python does not support multithreading; I don’t even know what that means in depth, but sure. From what I know, I need to use multiprocessing rather than asyncio. I went ahead and started reading code from people smarter than me to understand how this works, as in my 1 month of experience, reading code makes you a better developer rather