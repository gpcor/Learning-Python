# Learning Python!

## Objectives:
I will be uploading my code here as I create small projects and learn things of significance. My primary objective is to learn foundational concepts of Python via the following three resources:
1. [ ] Automate The Boring Stuff (free online text)
2. [ ] Invent Your Own Computer Games With Python (I own this book)
3. [ ] Talk Python's #100DaysOfCode lessons *Note: I initially started with this but the lessons were a tad too advanced at the time, so I've dialed it back and will perform their challenges as I gain more confidence*
4. [ ] Pybites and HackerRank, because they have great little code challenges that force me to learn new things to solve problems.

At some point I want to be able to come back to this code and refactor, altering it so it becomes more efficient and uses better Pythonic code.

### Programming Daily Log:
* March 31st, 2020: Spent some time today after work doing some typing practice. Then did sections one thru three of Automate the boring stuff Udemy course (Basics, Flow Control, and Functions). 

* April 1st, 2020: Did some additional typing practice today by spending the entire day making sure I utilized the new typing method. In Python I used the Automate Everything lessons and learned about Try/Except to handle certain explicit errors. I also wrote a complete program (guess the number game) and started working on Lists.

* April 2nd, 2020: I worked more on Lists today and their differen methods and also discovered random.shuffle() by accident. I watched a couple videos about code practices and reviewed a version of my guessing game done by SinfulPhantom, but done in a much more software engineer kind of way (OOP style). It was beautiful and a clear reminder that I have a long way to go but I know where I want to end up.

* April 3rd, 2020: Not much more today. Did some more with Lists and practiced more clean coding techniques. Discovered that Evernote has a Python API. I'd like to make an application that creates a shopping list based on input with item/qty pairs. Once complete, I'd like to be able to push the list to Evernote. Idea is WIP and requires a little more knowledge I think.

* Did not program on 4 April or 5 April, spent the weekend with my wife relaxing and enjoying the nice weather in our backyard during this pandemic. Still hoping to come out of the COVID-19 crisis with more knowledge and programming ability than when it started.

* April 6th, 2020: Finished Lists and started on Dictionaries and Data Structures in my Automate the Boring Stuff Course. I think dictonaries are the way to go for the evernote app. The Key/Value pairs line up nicely with the Item/Qty pairs I mentioned earlier. On the 9th I can start playing video games but I have to make sure it doesn't hinder my programming progress. I need to create a system that makes this easier.

* April 9th, 2020: I finished Dictionaries, Data Structures, and Advanced String Operations in my Automate the Boring Stuff course. I can see where the advanced string operations would be helpful when taking in lots of string data and wanting to make it cleaner, for putting it in a file or database perhaps? I haven't been taking a couple programming breaks as I move to wrap up my final class for the semester. I also do not want to burn myself out by trying to cram too much into too short a period. I forget that I have a little under three years to practice Python before I get out of the Navy and need to worry about becoming employable. I need to take a little more time to enjoy this process.

* April 13th, 2020: I finished the lesson regarding running programs from the command line and started on Regular Expressions on my Automate the Boring Stuff course in Udemy. Last Friday, my primary laptop broke. Fortunately I regular backup this code to my Github repo for learning Python so that wasn't an issue. At the behest of my wife, who does not believe in bandaging a situation with cheap solutions, I was convinced to stop being so meiserly and upgraded to a Macbook. I'm still dialing in the settings for my code environment and some other quality of life items but so far I'm happy to be here. OSX mean less temptation for video games and more code!

* April 16th, 2020: I started working on the REGEX section of Automate the Boring Stuff, and I'm finding it interesting but complex. There are a lot of details that go into search strings or documents as far as disecting matching strings out and getting the match cases correct. It's going to take a little bit of time to get a hang of but I'm sure I will. I can see how the course is teaching us the requisite materials necessary to making webscrapers, read documents, etc. Excited to see what the end of the course looks like.

* April 20th, 2020: I have attempted a few times over the last few days to get some programming in but it's difficult. As the wife and I get more sick (Yay, potential COVID) I find it harder to stay focused and often suffer from brain fog. I managed to use what level of concentration I did have in the successful completion of my last college class for the semester but that's about it. I'll do what I can going forward. I did, however, finish lesson 27 of the Automate the Boring Stuff Udemy course today so I guess some progress is better than none.

* April 22nd, 2020: I worked on some more of the Automate the Boring Stuff course today and I was able to get through the last of the Regex lesson. I hand copied the regex email and phone number scraper. It used the regex library to make expressions and the pyperclip library to pull date out of the clipboard, run the regex across the text, join it all together, then send the results back to the clipboard so it could be pasted back onto a document if I wanted to. It was pretty neat, although I wonder if it could be done better. I think there should be away to put the name, email, and phone number into a list together so that you could see the number and email that corresponds to a specific person. I'm sure there is, it just might be a more advanced topic that is outside of my current scope of knowledge.

* April 25th, 2020: I started the file section of the Automate the boring stuff lessons on Udemy. So far I have figured out how to get the current working directory of the file I'm working on and I was able to join that in a variable with the name of a different file that I wanted to open. However, if I use the open command to attempt to open the file, the code runs successfully but the file itself doesn't open. I don't know if that is a Mac related issue or not, so that'll require some research. I also discovered today that my future, sometime after I've gain a better level of proficiency with Python, will be to move to Godot and GDScript. The game dev dream isn't dead. 

* April 26th, 2020: I finished the file section of Automate the boring stuff lesson on udemy. I was able to make a practice directory on my desktop and have a program walk the directory and delete files with the extension that I designated. For some reason it was a little more complicated than simply telling it to unlink the file when I asked. I kept throwing an error that a specific file didn't exist. The top level for loop was already working in the directory I wanted to delete stuff in but I think os.unlink was more concerned with the relative path. I solved this with a mild work around of concatenating a string that contained the file path and file name that I wanted gone. The next lesson is in regards to debugging which I feel will be helpful going forward when I want to understand my errors in my programming.

* April 28th, 2020: Today I finished the Debugging section of the Automate the boring stuff course on Udemy. I learned some valuable bits and pieces about making errr logs that can tell me about what my program is doing and when. I learned about the debugger tool in IDLE which is pretty useful. I need to spend some time with the buitlin debugger in VSCODE so I can operate it more smoothly but all in all I get the gist. It'll be nice to get to implement my own error logs in a larger program some day. I then began the web browser section briefly before stopping for the day. I now have a mapit command that I can use in the terminal that will open a google maps page and take me to the location I give it or the one in my clipboard. It took a little bit of troubleshooting to get the script to accept command line arguments but I got it figured out. Pretty neat little trick! May need to use it later to make some automation tools for me on my Mac. It makes me want to try out some automation projects. Maybe I can go back to that pomodoro timer idea and make it a command line tool that I can use a script for rather than have a dedicated app off the app store for. It could even count how many sessions I do and send it to a csv maybe? What an idea!

* May 1-3, 2020: I'm having a hard time remembering which days I programmed over the weeked as I was kind of busy with a lot of different things. I am still on the Web scraping section of the ATBS Udemy course. I took some time to work on my mapit command script. It now takes some commmand line arguments that are comma delimited, splits them into the start and end point addresses, and then opens the browser to the directions page on google maps and gives you the directions you want. I reviewed it with a friend of mine (Github @SinfulPhantom) and he made some recommendations. We got rid of the floating function call and he helped me to understand the "If __name__ = "__main__" concept. He also recommended trying to accomplish the script with the print() module rather than sys.argv so that is something I want to try and alter later on. 

* May 4th, 2020: Happy Star Wars Day 2020! Unfortunately today was not a great day for programming. I am pretty tired today and spent a lot of time doing some administrative work for my actual job. When I tried to sit down and work on my ATBS course I discovered some difficulties with my virtualenv in that it didn't recognize the modules I was installing. I still need to figure out how all that stuff works but for now I'm okay with adding my modules to the global framework folder. After spending time with that and finishing my work for the day, I attempted to work on the lesson and didn't really feel the motivation so I decided to call it a day. Hopefully I feel better about it tomorrow because I would like to learn more about web scraping.

* May 5th, 2020: I attempted some more progress on the programming front today but I couldn't stay focused on it. I did a little bit of the ATBS course and attempted to work with selenium but there is a known issue with this thing called "geckodriver" and firefox in their download and MACOS after version 10.15 Catalina (which is what I'm using now). Not a big deal but It'll make forward progress a bit difficult if I can't find a way to work around it. I will attempt to program more tomorrow. I think I'll try to make a script that strips a price for an item off of bestbuy and puts the item date, item price, and item name in a text document or something. That'll be cool right? Anywho, I'll figure out something to motivate me. Just not tonight. Tonight I am going to relax and maybe play a video game.