CREATE TABLE IF NOT EXISTS geo{
    id INTEGER AUTO_INCREMENT,
    lat VARCHAR(20) NOT NULL,
    lng VARCHAR(20) NOT NULL,

    CONSTRAINT pk_geo PRIMARY KEY (id)
};

CREATE TABLE IF NOT EXISTS addresses{
    id INTEGER AUTO_INCREMENT,
    street VARCHAR(50) NOT NULL,
    suite VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    zipcode VARCHAR(15) NOT NULL,

    geoID INTEGER NOT NULL,

    CONSTRAINT pk_addresses PRIMARY KEY (id)
    CONSTRAINT fk_addresses_geo FOREIGN KEY (geoID) REFERENCES geo(id)
};

CREATE TABLE IF NOT EXISTS companies{
    id INTEGER AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    catchPhrase VARCHAR(255) NOT NULL,
    bs VARCHAR(255) NOT NULL,

    CONSTRAINT pk_companies PRIMARY KEY (id)
};

CREATE TABLE IF NOT EXISTS users{
    id INTEGER AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(25) NOT NULL,
    website VARCHAR(255) NOT NULL,

    adreesID INTEGER NOT NULL,
    companyID INTEGER NOT NULL,

    CONSTRAINT pk_users PRIMARY KEY (id),
    CONSTRAINT fk_users_companies FOREIGN KEY (companyID) REFERENCES companys(id)
};

CREATE TABLE IF NOT EXISTS posts{
    id INTEGER AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    body VARCHAR(500) NOT NULL,
    user_id INTEGER NOT NULL,

    CONSTRAINT pk_posts PRIMARY KEY (id),
    CONSTRAINT fk_posts_users FOREIGN KEY (user_id) REFERENCES users(id)
};