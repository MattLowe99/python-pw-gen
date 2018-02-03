# python-pw-gen
A increasingly developed version of a random password generator based off the XKCD method

## Febuarary 1, 2018 -- Version 0.1
This project originally started as an assignment for Northeastern University's CS2550 class, Foundations of Cybersecurity. The original idea was to replicate the ['xkcd password generator' comic](http://preshing.com/20110811/xkcd-password-generator/). However, with development it has morphed into a project with personal long-term goals and ideas.

While I've by no means used Python recently, it was easy to pick back up and scrap something together that worked as intended. However; a new element I had never dealt with before that needed to be implemented was the program had to function on the Linux command line. In the case of Python, this meant using the *sys* module to access the *sys.argv* variable.

The base program works as follows:
```
> $ ./xkcdpwgen.py
> midnightengineeringfortunecheek
```
Generates a random 4-word password from the wordlist.

There is other arguements available that capitalize words, add numbers and/or symbols before, in-between, or after words, along with the ability to control how many words are generated.

For example:
```
> $ ./xkcdpwgen.py -c 2 -n 4
> memberChest7Proposal058committee
```
Generates a random 4-word long password with 2 words randomly capitalized and 4 numbers randomly interwoven in.

Some more examples:
```
> $ ./xkcdpwgen.py -s 3 -n 4 -w 1
> 58.@!introduction23

> $ ./xkcdpwgen.py --words 3 --numbers 1 --caps 2
> Tension2outcomeEntertainment

> $ ./xkcdpwgen.py --words 5 --numbers 6 --symbols 5 --caps 3 
> Safetyinformation@!statement558.4^Loss2&0Debt
```
You get the idea.

### Current Task List
- [x] ~~Add more words to word list (likely to be replaced by a 1 million+ list)~~
- [ ] Add option for other languages (currently Spanish, French, Italian to be added)
- [ ] Add option for user uploaded wordlist
- [ ] Add option for user decided number range
- [ ] Add option for user picked symbols
- [ ] Add GUI/support for non-command line running
