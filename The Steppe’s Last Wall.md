# The Steppe’s Last Wall

## Earf

## OSINT

## Medium

### Question Description

Players read a cryptic blog post written by someone who has played chess with the in‑game leader known publicly as “bl1tz.” The post hints at opening a door which requires:

- the city from the last branch of the bracket (city where final was held)

- the tag of the leader from the roster card (ign of bl1tz)

- the highest number from the long board (his highest elo)

- the name of the dark-square gate most often chosen (his most played opening as black)

### Intended Solution

1) Read the blog carefully and identify the four items required for the flag
- City from the final branch of the bracket (event city).
- IGN (the exact in-game tag) from the roster card.
- Highest FIDE standard/classical rating (peak/visible highest figure on the official rating card).
- The most-played Black opening name (French Defence/Defense) from a chess database profile.
- The blog explicitly says all four must be combined in order for the final gate.

2) Extract the hidden video identifier to anchor the correct final
- At the end of the blog, note the string that looks like a video id but in rot13 : jngpu?i=2TrLkchvovR.
- Use this identifier to find the grand final highlights/discussion
- This gives the city : Austin

3) Go to the community tournament wiki implied by “blue and white horse with tabs"
- Blue and White horse is the logo of liquipedia.net
- Search for the event’s main page.
- Open the event page. Navigate to the brackets.

4) Find the grand final page and look for both team's pages
- In the team pages, look for both the in game leaders.
- Go through both of their pages, on the page of bL1tz it is mentioned under "Trivia" that he is still holding the title of FIDE Master (going through the page of apEX reveals no such facts).
- This gives name of the leader : bL1tz.

5) Identify the real name from the team/player page to pivot to chess
- On the player’s page in the same wiki, note the full romanized name.
- This name is the key to searching the official chess rating card.

6) Open the official chess rating profile and capture highest standard/classical rating
- Search the official rating site using the romanized name.
- Open the player’s card and review the rating history table for standard/classical.
- Identify the highest listed standard rating visible on the website (the blog emphasizes “the highest mark that was earned and kept on the long board, not the quick ones”).
- Record that highest standard rating. This is item 3 for the flag: 2369

8) Find the chess database player page and extract the most played Black opening
- Using the same romanized name, open chessbase.
- Scrolling down, it shows both openings played as white as well as black.
- Confirm the most played Black opening is the French Defence. Record the opening name.
- Acceptable spellings: “FrenchDefence” or “FrenchDefense.”
- This is item 4 for the flag.

9) Assemble the flag in the required order
- As specified by the blog: set them in order.
- Required order:
  1) Austin (from the final’s bracket/infobox)
  2) bL1tz (from the roster card)
  3) 2369 (from the official rating card)
  4) FrenchDefence/Defense (from the database opening stats)

Following these steps ensures minimal guesswork and a deterministic path from the blog to forum/VOD context, to the tournament wiki, to the team/player identity, to the official chess profile, and finally to the opening statistics needed for the flag.

### Flag

> ctf{Austin,bL1tz,2369,FrenchDefence}kernel
