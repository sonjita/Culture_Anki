-- Run this file via $ sqlite3; .read prepare_user_database.sql
-- Caution: This overwrites existing DB with empty one.
-- Drop tables via $ sqlite3; drop table bla

CREATE TABLE users (
   id integer PRIMARY KEY,
   mail text NOT NULL,
   unsecure_password text NOT NULL
);

--all languages supported by Vocbulary through Culture (which are all languages supported by Python's NLTK using the Gutenberg project)
CREATE TABLE languages (
   id integer PRIMARY KEY,
   supp_language text NOT NULL
);

--table of words in 
CREATE TABLE words (
   id integer PRIMARY KEY,
   word_rank integer,
   lang_id,
   FOREIGN KEY(lang_id) REFERENCES languages(id)
);

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
