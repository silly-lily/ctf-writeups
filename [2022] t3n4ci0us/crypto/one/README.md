# Challenge
The challenge asks us to find the solution to:
````
26s + 8t = 2( == gcd(26,8))
    + 12345 for the correct answer
````

# Solution
Using the extended euclidean algorthim, I noticed that the gcd of `26` and `2` was in fact `2`. So since this was the correct answer, I added `2` to `12345` to get `12347`. The flag was `T3N4CI0UA{123457}`. 