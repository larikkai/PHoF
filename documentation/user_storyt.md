# Padel Hall of Fame user stories

## Main page

### As a visitor, I want to be able to...

  * Read news so that I can sign up for application and participate games or tournaments. [x]

### As a visitor or user, I want to be able to...

  * Read news so that I get information. [x]
  * See news author so I know who wrote the news. [x]

### As an administrator, I want to be able to...

  * Produce content for the home page in the form of news to make the home page interesting. [x]
  * Edit the news so that incorrect information can be removed. [x]

## Sign up

### As a visitor, I want to be able to...

   * Sign up for the application so I participate games or tournaments. [x]

## Games

### As a visitor, I want to be able to...

  * Browse games list so that I can see if games are played. [x]

### As a user, I want to be able to...

  * Choose which game I participate in so I can participate. [x]
  * Browse games to get information about games open to join or games played. [x]
  * Add a new game so that I can play with other users. [x]
  * Remove not yet full game I have organized so that I do not organize unnecessary games. [x]
  * Set result to the game I have participated so that others know how the game ended. [x]
  * View single a game, so I know who played. [x]

### As an administrator, I want to be able to...

  * Change games result so that wrongful results can be corrected. [x]
  * Cancel any game by removing it to ensure high quality games for users. [x]

## Tournaments

### As a visitor, I want to be able to...

  * Browse games list so that I can see if games are played. [x]

### As a user, I want to be able to...

  * Choose which tournament I participate in so I can participate. [x]
  * Browse tournament to get information about tournaments open to join. [x]
  * Add a new tournament so that I can play with other users. [x]
  * Remove not yet full tournament I have organized so that I do not organize unnecessary tournaments. [x]
  * Set results to the tournament game I have participated so that others know how the game ended. [x]
  * View single a tournament game, so I know who played. [x]

### As an administrator, I want to be able to...

  * Change tournament game result so that wrongful results can be corrected. [x]
  * Cancel tournament by removing it to ensure high quality tournaments for users. [x]

## Ranking

### As a visitor, I want to be able to...

  * Browse through ranking so I can see statistics. [x]
  * See players with zero games [x]

### As a user, I want to be able to...

  * I want to see how many games I have played so that I can compare my count to the count of other users. [x]
  * I want to see how many games played I have created so that I can compare my count to the count of other users. [x]
  * See players with zero games [x]

## Only as an administrator, I want to be able to

  * Remove users so that dishonest users don't spoil the experience of others. [x]

# SQL

## Get news
```
SELECT * FROM new
```

## Log in
```
SELECT account.date_created AS account_date_created,
    account.date_modified AS account_date_modified,
    account.id AS account_id,
    account.name AS account_name,
    account.username AS account_username,
    account.password AS account_password
FROM account
WHERE account.username = ? AND account.password = ?
```

## Create account
```
INSERT INTO account (date_created, date_modified, name, username, password)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

## Delete account
```
DELETE FROM account WHERE account.id = ?
```

## Get news
```
SELECT * FROM new
```

## Add news
```
INSERT INTO new (date_created, date_modified, title, content, author)
    VALUES(CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

### Update news
```
UPDATE new SET date_modified=CURRENT_TIMESTAMP, content=?
WHERE new.id = ?
```

### Delete news
```
DELETE FROM new WHERE new.id =?
```


