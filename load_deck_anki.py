import genanki

L = [('hello', 'hallo', 'hello  world'), ('world', 'die Welt', 'the world is big')]

my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    #{'name': 'Sample sentence from movie'}
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])


for word_information in L:
    my_note = genanki.Note(
    model=my_model,
    fields=word_information[:-1])    