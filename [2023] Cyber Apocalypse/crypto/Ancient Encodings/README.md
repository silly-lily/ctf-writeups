# Challenge
Your initialization sequence requires loading various programs to gain the necessary knowledge and skills for your journey. Your first task is to learn the ancient encodings used by the aliens in their communication.

# Encryption 
I noticed that `FLAG` was first encoded. Then it was written to a file. 
````Python 
def main():
    encoded_flag = encode(FLAG)
    with open("output.txt", "w") as f:
        f.write(encoded_flag)
````

Looking at the declaration of the `FLAG` variable, I realize that the flag is first transformed to bytes from a String. 
````Python
FLAG = b"HTB{??????????}"
````

Then `FLAG` is sent through an econding function. I notice this encoding function transforms `FLAG` to base64. Then it takes the bytes of this base64 `FLAG` and transforms it to hex.
````Python
def encode(message):
    return hex(bytes_to_long(b64encode(message)))
````

# Decryption
First I save the content of `out.py` into a variable `ct`.
````Python
ct = '53465243657a467558336b7764584a66616a4231636d347a655639354d48566664326b786246397a5a544e66644767784e56396c626d4d775a4446755a334e665a58597a636e6c33614756794d33303d'
````

Then I get the bytes from this hex string and decode it from b64 to bytes. Finally, I decode the bytes to a string.
````Python
ct = bytes.fromhex(ct)
ct = b64decode(ct)
pt = ct.decode()
````

Then we have the flag `HTB{1n_y0ur_j0urn3y_y0u_wi1l_se3_th15_enc0d1ngs_ev3rywher3}`.