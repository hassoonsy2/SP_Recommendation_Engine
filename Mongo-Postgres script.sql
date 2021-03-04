DROP TABLE IF EXISTS product CASCADE;
DROP TABLE IF EXISTS prijs CASCADE ;
DROP TABLE IF EXISTS properties CASCADE ;

DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS profiles CASCADE;
DROP TABLE IF EXISTS sessions CASCADE;




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