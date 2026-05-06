# Title  
The Steppe's Last Wall

## Earf

## Domain  
OSINT

## Difficulty  
Medium

### Question Description  

Provided:
`https://www.tumblr.com/steppewall/795945261633503232/the-steppes-last-wall`


### Intended Solution  
1. **The Blog Post and Initial Cipher**    
   The blog post begins with a poetic riddle describing the player's deliberate style on "a dark square".
   The key given is a cryptic string:  
   `H2E49nGlav6*IAF:3:t` 
   Running rot-47 on this gives `watch?v=2GeYxpuibiE`, which leads to the highlights page of the grand finals of the austin major
   
2. **Pastebin**  
   The blog links to a password protected pastebin ``https://pastebin.com/jZtLByqc`

   The password is the three-letter abbreviation of the city hosting the finals `AUS`, as mentioned in the blogpost in `its code whispered by those who know the city where the brightest lights shone that day`.


3. **Unlocking the zip**  
   the pastebin links to a mediafire link which gives a .zip file called `mong0lia.zip`, the password to this is `///spending.flight.soda`, every "e" in the pastebin is replaced with a "3" and the line `This is no ordinary k3y but a location, a cod3 craft3d by a cl3v3r mind th3y call it` alludes that the password is the what3words of the arena where the major was held.

4. **Analyzing the Extracted Image**  
   the zip file gives an image named `mong0lia.png` which has the flag of mongolia and a thunder logo on it, along with this the original blogpost has a comment which says `a blue and white horse might fit the puzzle`, which is referencing liquipedia, where if you visit the match of the finals and look through the profile of each player on the profile of "bL1tz" in the trivia section it is mentioned that he is a fide master in chess.

5. **Getting the flag**
   in the pastebin 
   "With thos3 words s3t right you will unlock th3 ch3st, s3al3d and waiting, th3 guards staring at th3 rating.Th3 path forward li3s hidd3n b3yond th3 door, qui3t and pati3nt as th3 first mov3 on a dark squar3", clearly mentions that the answer will be his {rating,blackopening}. 




### Flag  
> `ctf{2369,french_defence}kernel (can also accept ctf{2369, french_defense}kernel})`
