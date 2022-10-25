# Challenge 
We want to find the RSA decryption key with the corresponding RSA encryption key `e = 777887` and the corresponding primes `p = 1049` and `q = 2063`. 

````Python
p = 1049
q = 2063

e = 777887
````

# Finding phi
We want to let `phi = (p-1)*(q-1) = 2160976`.
````Python
phi = (p-1)*(q-1)
````

# Finding d
We want to let `d*e = 1 (mod phi)`. We get that `d = 1457215`, so our flag is `flag{d=1457215}`.
````Python
for d in range(0,phi):

    if (d*e)%phi == 1:
        print(d)
````