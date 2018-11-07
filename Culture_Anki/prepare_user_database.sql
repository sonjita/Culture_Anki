-- Run this file via $ sqlite3; .read prepare_user_database.sql
-- Caution: This overwrites existing DB with empty one.

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

.save user_database.db
