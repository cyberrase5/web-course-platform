CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	firstname TEXT,
 	lastname TEXT,
	password TEXT,
	isteacher BOOLEAN,
	username TEXT
);

CREATE TABLE courses (
	id SERIAL PRIMARY KEY,
	coursename TEXT,
	teacher_id INTEGER REFERENCES users,
	taskcount INTEGER 
);

CREATE TABLE participants (
	id SERIAL PRIMARY KEY,
	course_id INTEGER REFERENCES courses,
	user_id INTEGER REFERENCES users	
);

CREATE TABLE tasks (
	id SERIAL PRIMARY KEY,
	course_id INTEGER REFERENCES courses,
	question TEXT,
	maxpoints INTEGER,
	correctanswer TEXT
);

CREATE TABLE submissions (
	id SERIAL PRIMARY KEY,
	course_id INTEGER REFERENCES courses,
	user_id INTEGER REFERENCES users,
	points INTEGER
);

CREATE TABLE texts (
	id SERIAL PRIMARY KEY,
	course_id INTEGER REFERENCES courses,
	content TEXT
);

CREATE TABLE choices (
	id SERIAL PRIMARY KEY,
	task_id INTEGER REFERENCES tasks,
	choice TEXT,
	course_id INTEGER REFERENCES courses
);
