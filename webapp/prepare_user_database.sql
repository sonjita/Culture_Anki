-- Run this file via $ sqlite3; .read prepare_user_database.sql
-- Caution: This overwrites existing DB with empty one.
-- Drop tables via $ sqlite3; drop table <name of table>

CREATE TABLE users (
   id integer PRIMARY KEY,
   email text NOT NULL,
   unsecure_password text NOT NULL
);

--all languages supported by Vocbulary through Culture (which are all languages supported by Python's NLTK)
--with information which of the for main parts of speech have inflections in that language
CREATE TABLE languages (
   id integer PRIMARY KEY,
   lang text NOT NULL
   nouns integer NOT NULL --bolean
   adjectives integer NOT NULL --boolean
   regular_verbs integer NOT NULL --boolean
   irregular_verbs integer NOT NULL --boolean
);

--table of all words seen in this app. If they come from the corpus, they have a rank; if they were first seen 
-- CREATE TABLE words (
--    id integer PRIMARY KEY,
--    word_rank integer,
--    lang_id integer NOT NULL,
--    FOREIGN KEY(lang_id) REFERENCES languages(id)
-- );
-- CREATE TABLE words (
--    id integer PRIMARY KEY,
--    word_rank integer,
--    lang text NOT NULL,
--    FOREIGN KEY(lang_id) REFERENCES languages(id)
-- );


CREATE TABLE media_types (
   id integer PRIMARY KEY,
   media_type text NOT NULL
);
INSERT INTO media_types (media_type) VALUE ("Book");
INSERT INTO media_types (media_type) VALUE ("Movie");
INSERT INTO media_types (media_type) VALUE ("Series");
INSERT INTO media_types (media_type) VALUE ("Song");

CREATE TABLE sources (
   id integer PRIMARY KEY,
   title text NOT NULL,
   media_type_id integer NOT NULL,
   user_id integer NOT NULL, --foreign key
   date_added text, 
   FOREIGN KEY (media_type_id) REFERENCES media_types(id)
);

-- CREATE TABLE words_users (
--    id integer PRIMARY KEY,
--    word_id integer, 
--    iser_id
--    known_when_media --boolean
--    assume_as_known --boolean
--    date_learned text --date   
--    source_id integer NOT NULL --foreign key

-- );

-- table of all words added into the db for any user: The same word might be added several times for different sources, but only if for the former sources known==False;
-- iff in a row known==True, date_learned is not NULL; known_when_media_added indicates if the user knew the word when they uploaded the source it comes from
CREATE TABLE words_users (
   id integer PRIMARY KEY,
   word text NOT NULL, 
   user_id integer NOT NULL,
   known_when_media_added integer NOT NULL, --boolean
   known integer NOT NULL, --boolean
   date_learned text, --date   
   source_id integer NOT NULL,--foreign key
   FOREIGN KEY (user_id) REFERENCES users(id),
   FOREIGN KEY (source_id) REFERENCES sources(id)
);
/*
CREATE TABLE passwords (
   user_id integer PRIMARY KEY,
   email text NOT NULL,
   password text NOT NULL
);


CREATE TABLE media_items (
    media_id integer PRIMARY KEY,
    email text NOT NULL,
    medium text NOT NULL,
    title text NOT NULL,
    language text NOT NULL,
    seen integer NOT NULL,
    learnt integer NOT NULL,
    date_added text NOT NULL
);

CREATE TABLE known_words (
   email text NOT NULL,
   word text NOT NULL,
   language text NOT NULL,
   title text NOT NULL  
);

CREATE TABLE unknown_words (
   email text NOT NULL,
   word text NOT NULL,
   language text NOT NULL,
   source text NOT NULL,
   sample_sentences text
);
*/

.save user_database.db
