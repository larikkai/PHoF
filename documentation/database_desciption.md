# Database desciption

## Database diagram

Fully normalized and corrent diagram

[Tietokantakaavio](https://github.com/larikkai/PHoF/blob/master/documentation/database_diagram.jpg "Tietokantakaavio")

## Create table statements

```
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
);

CREATE TABLE game (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL,
        playerCount INTEGER NOT NULL, 
        done BOOLEAN NOT NULL,
        score1 INTEGER,
        score2 INTEGER,
        PRIMARY KEY (id),
        FOREIGN_KEY(account_id) REFERENCES account (id)
        FOREIGN_KEY(tournament_id) REFERENCES tournament (id)
);

CREATE TABLE new (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        title VARCHAR(144) NOT NULL,
        content VARCHAR(144) NOT NULL, 
        author VARCHAR(144) NOT NULL, 
        account_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN_KEY(account_id) REFERENCES account (id)
);

CREATE TABLE role (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN_KEY(account_id) REFERENCES account (id)
);

CREATE TABLE tournament (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL,
        playerCount INTEGER NOT NULL, 
        done BOOLEAN NOT NULL,
        account_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN_KEY(account_id) REFERENCES account (id)
);
```

## SQL querys