# Madness-tryhackme-room-
madness tryhackme room somewhat challenging for me and still need root flag 
# madness
 
 ![](madness_image.jpg)

## nmap:
two ports are open
22 ssh
80 http



### gobuster shows no hidden directry

![](modifying_png_to_jpeg.png)

### but find a hidden directry by converting corrupted png file to jpeg file
/th1s_1s_h1dd3n
![](thm.jpeg)
source code of this directry
<html>
<head>
  <title>Hidden Directory</title>
  <link href="stylesheet.css" rel="stylesheet" type="text/css">
</head>
<body>
  <div class="main">
<h2>Welcome! I have been expecting you!</h2>
<p>To obtain my identity you need to guess my secret! </p>
<!-- It's between 0-99 but I don't think anyone will look here-->

<p>Secret Entered: </p>

<p>That is wrong! Get outta here!</p>

</div>
</body>
</html>





then is used python to brute forcing the requests
import requests
for i in range(100):
    r=requests.get(f"http://10.10.150.152/th1s_1s_h1dd3n/?secret={i}")
    if b"wrong" not in r.content:
        print("Secret is",i)

Secret is 73     






after home page shows

Welcome! I have been expecting you!

To obtain my identity you need to guess my secret!

Secret Entered: 73

Urgh, you got it right! But I won't tell you who I am! y2RPJ4QaPF!B



this shit is password for steghide
root@kali:~/ctf/tryhackme/Madness# cat hidden.txt                                                                                                                                                            
Fine you found the password!                                                                                                                                                                                 

Here's a username 

wbxre
cipher used to encrypt is ROT110
I didn't say I would make it easy for you!
decoding the username




wbxre:joker




I didn't think you'd find me! Congratulations!

Here take my password

*axA&GF8dP






