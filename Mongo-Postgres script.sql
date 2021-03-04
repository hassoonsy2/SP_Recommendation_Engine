DROP TABLE IF EXISTS product CASCADE;
DROP TABLE IF EXISTS prijs CASCADE ;
DROP TABLE IF EXISTS properties CASCADE ;
DROP TABLE IF EXISTS profiels CASCADE;
DROP TABLE IF EXISTS  orders CASCADE;
DROP TABLE IF EXISTS sessions CASCADE;
DROP TABLE IF EXISTS profiel_recommndations CASCADE;



CREATE TABLE product(
id_product varchar(300) NOT NULL,
naam varchar(300) ,
category varchar(300),
sub_category varchar(300) ,
sub_sub_category varchar(300),
gender varchar(300),
brand varchar(300),
PRIMARY KEY(id_product)
);



CREATE TABLE prijs(
id_prijs varchar(300) NOT NULL,
discount varchar(300),
selling_price varchar(300),
FOREIGN KEY(id_prijs) REFERENCES product(id_product)on delete cascade on update cascade ,
PRIMARY KEY(id_prijs)
);



CREATE TABLE properties(
id_properties varchar(300) NOT NULL,
variant varchar(300),
FOREIGN KEY(id_properties) REFERENCES product(id_product) on delete cascade on update cascade ,
PRIMARY KEY(id_properties)
);


CREATE TABLE profiels(
	id_profiel varchar(300) NOT NULL,
	browsersid TEXT [] unique ,
	segment varchar(300),
	first_date timestamp  , 
	last_date timestamp ,
	PRIMARY KEY(id_profiel)

);

CREATE TABLE profiel_recommndations(
	id_profiel varchar(300) NOT NULL,
	viewed_before_id varchar array,
	similars_id varchar array,
	previously_recommended varchar array,
	FOREIGN KEY(id_profiel) REFERENCES profiels(id_profiel) on delete cascade on update cascade
	
);	

CREATE TABLE sessions(
	session_id varchar(300)NOT NULL,
	profile_id varchar (300), 
	session_start timestamp,
	session_end timestamp,
	has_sale boolean ,
	user_agent_browser varchar(300),
	user_agent_device varchar(300),
	segment_sessions varchar(300),
	utm_source varchar(300),
	event_source varchar(300),
	event_action varchar(300),
	PRIMARY KEY(session_id),
	FOREIGN KEY(profile_id) REFERENCES profiels(id_profiel) on delete cascade on update cascade 

	

);	

CREATE TABLE orders(
	id_product varchar(300)NOT NULL,
	id_profiel_o varchar(300) NOT NULL,
	PRIMARY KEY(id_product),
	FOREIGN KEY(id_profiel_o) REFERENCES profiels(id_profiel) on delete cascade on update cascade 
);




	
	