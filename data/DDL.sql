CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(50) NOT NULL ,
	phone_number VARCHAR(20) NOT NULL,
	otp_token CHAR(16) not null,
	is_confirmed BOOLEAN DEFAULT false,
	UNIQUE (email)
);

CREATE TABLE otp (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	user_id INTEGER not null,
	at TIMESTAMP not null,
	expire TIMESTAMP not null,
	FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE user_auths (
	user_id INTEGER PRIMARY KEY,
	face BLOB,
	tmd BLOB,
	voice BLOB,
	FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE email_confirmations (
	user_id INTEGER PRIMARY KEY,
	token VARCHAR(50) NOT NULL,
	expire TIMESTAMP NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users(id)
)