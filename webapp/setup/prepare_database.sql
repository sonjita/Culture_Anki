-- Try via $ sqlite3; .read prepare_database.sql
-- Create database via ~/Dropbox/RC/Vocabulary project/vocabulary_through_culture/webapp/model$ sqlite3 webapp/model/database.db < prepare_database.sql
-- Drop tables via $ sqlite3; drop table <name of table>

CREATE TABLE users (
   id integer PRIMARY KEY,
   email text NOT NULL,
   encrypted_password text NOT NULL,
   salt text NOT NULL,
   proficiencies text NOT NULL -- JSON OBJECT
);
CREATE INDEX user_email ON users (email);

CREATE TABLE sources (
   id integer PRIMARY KEY,
   title text NOT NULL,
   media_type text NOT NULL,
   user_id integer NOT NULL,
   date_added text, 
   consumed integer NOT NULL, --boolean
   -- FOREIGN KEY (media_type_id) REFERENCES media_types(id),
   FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE INDEX source_user_id ON sources(user_id);

CREATE TABLE words_users (
   id integer PRIMARY KEY,
   word text NOT NULL, 
   user_id integer NOT NULL,
   learning_status text NOT NULL, -- enum: "not_known", "previously_known", "learning"
   date_learned text, --date   

   known_when_media_added integer NOT NULL, --boolean
   -- known integer NOT NULL, --boolean

   source_id integer NOT NULL,--foreign key
   FOREIGN KEY (user_id) REFERENCES users(id),
   FOREIGN KEY (source_id) REFERENCES sources(id)
);
CREATE INDEX words_users_user_id_learning_status ON words_users(user_id, learning_status);
CREATE INDEX words_users_source_id ON words_users(source_id);

-- .save database.db


-- CREATE TABLE user_languages (
--    id integer PRIMARY KEY,
--    user_id integer NOT NULL,
--    lang text NOT NULL,
--    vocab_proficiency int NOT NULL,
--    grammar_proficiencies text NOT NULL -- JSON OBJECT
-- )

-- CREATE INDEX tag_titles ON tags (title);

--all languages supported by Vocbulary through Culture (which are all languages supported by Python's NLTK)
--with information which of the for main parts of speech have inflections in that language
-- CREATE TABLE languages (
--    id integer PRIMARY KEY,
--    lang text NOT NULL,
--    nouns integer NOT NULL --bolean
--    adjectives integer NOT NULL --boolean
--    regular_verbs integer NOT NULL --boolean
--    irregular_verbs integer NOT NULL --boolean
-- );

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
-- known==True iff date_learned is not NULL; known_when_media_added indicates if the user knew the word when they uploaded the source it comes from


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


