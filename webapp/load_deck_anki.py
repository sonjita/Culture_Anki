import genanki

L1 = [('hello', 'hallo', 'hello  world'), ('world', 'die Welt', 'the world is big')]
L2 = [('wall', 'vand', 'the wall is white'), ('cable', 'cable', 'the cable is also white')]

SEEN_MOVIE = True

model_with_sentence = genanki.Model(
  1996392842,
  'Model With Sentence',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'Sample sentence from movie'}
  ],
  templates=[
    {
      'name': 'With sentence',
      'qfmt': '{{Question}}<br>{{Sample sentence from movie}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

model_without_sentence = genanki.Model(
  1996392843,
  'Model Without Sentence',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'Sample sentence from movie'}
  ],
  templates=[
    {
      'name': 'With sentence',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

if SEEN_MOVIE:
    model = model_with_sentence
else:
    model = model_without_sentence


my_deck = genanki.Deck(
        1577318423,
        'Culture'
        )

for word_information in L2:
    my_note = genanki.Note(
    model=model,
    fields=word_information)    
    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file('output.apkg')
