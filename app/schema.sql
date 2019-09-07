DROP TABLE IF EXISTS segments;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS votes;
DROP TABLE IF EXISTS snippets;

CREATE TABLE segments (
  id INTEGER NOT NULL,
  label TEXT NOT NULL,
  tape TEXT NOT NULL,
  url TEXT NOT NULL,
  start_tc TEXT  NOT NULL,
  end_tc TEXT  NOT NULL
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE votes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  voter_id INTEGER NOT NULL,
  snippet_id INTEGER NOT NULL,
  vote INTEGER NOT NULL,
  FOREIGN KEY (voter_id) REFERENCES users (id),
  FOREIGN KEY (snippet_id) REFERENCES snippets (id)
);

CREATE TABLE snippets (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  snippetname TEXT NOT NULL
);

INSERT INTO segments (id, label, tape, url, start_tc, end_tc)
VALUES 
   (1, 'Overture', 'Tape 18', 'https://operatinder.s3.amazonaws.com/Honeycomb.mp3', '00:02:07', '00:04:07'),
   (2, 'Overture', 'Tape 19', 'https://operatinder.s3.amazonaws.com/Honeycomb.mp3', '00:12:03', '00:20:10'),
   (3, 'Overture', 'Tape 20', 'https://operatinder.s3.amazonaws.com/Honeycomb.mp3', '00:08:10', '00:10:30'),
   (4, 'Overture', 'Tape 56', 'https://operatinder.s3.amazonaws.com/Honeycomb.mp3', '00:21:01', '00:25:07');


INSERT INTO snippets (snippetname)
VALUES 
   ('snippet1'),
   ('snippet2'),
   ('snippet3'),
   ('snippet4');
