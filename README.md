# Vocabulary Through Culture (WIP)

## Installation
Prerequisites: Python 3.7, Pipenv, SQLite

Clone repository
`pipenv install`
`pipenv run start_app.py`
Follow the CLI instructions (got to port 7000)

## Description

Configure the app: which languages do you want to use the app for? What's your proficiency level in those languages? Additionally to your proficiency level self-evaluation, the app will further evaluate your vocabulary knowledge a bit.

Now, upload a media item (subtitle, ebook or song lyrics file) in one of those languages. The app will give you all the vocabulary you probably don't know -evaluated based on your proficiency level configuration as well as discarding all the words you've already marked as known in previous media items. Go through that list and mark the words you do in fact know. That's less of a hassle than it seems: you'll be presented that list in several chunks. The chunks will be ordered. The words in the first chunk are the most frequent ones in that language. So you might just want to skim through that chunk and hit "know them all" and then possibly uncheck the ones you know. Only in the last chunks you probably really have to select the known vocabulary word by word.

Let me also tell you why in the language configuration you are asked about both your vocabulary and your grammar knowledge. It's because your grammar knowledge is used to decide if different inflections of the same word will be treated as the same word - and therefore won't be repeated in the list of unknown words- or not . With inflections, for example, I refer to plural forms like "house" - "houses" or "man" - "men" and to verb inflections like "eat" - "eats" - "ate" - "eaten" etc. 

Now, what do you do with that list of all unknown words in your media item? Are you lazy about looking for a translation for all of them by yourself and learn them some old-school way? Well, you don't need to: there's also the option to automatically load those words into Anki. You can choose if the back side of the Anki flashcards should be the translation of the correspondent word in your mother tongue or a description of its meaning in the language it's in.

And voilà, there you have your Anki deck of words you might want to learn before watching the movie/reading the book. Once you've watched the movie/read the book, don't forget to mark it as watched/read. That way, one to two sample sentences from the movie/book, in which that word appeared in, get added to the correspondent Anki flash card. Also, if you're confident you're going to learn all those words, mark that option, too. That way they'll already be taken into account as known words by the app for the next media item.

Have fun learning and not missing out on parts of your movie/book/song due to missing vocabulary!

