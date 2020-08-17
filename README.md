# Golden Duck

It crawls the stock data & visualizes them.

### CorpList

```create database test;```
```
create table Company (
  corpCode char(6) not null,
  stockCode char(6),
  name char(64),
  koreanName char(64) not null,
  country char(64) not null,
  province char(64) not null,
  listingDate date not null,
  settlementMonth int(2) not null,
  ceo char(64) not null,
  url char (255),
  sector char (255),
  primary key (corpCode)
);
```
```
+-----------------+-----------+------+-----+---------+-------+
| Field           | Type      | Null | Key | Default | Extra |
+-----------------+-----------+------+-----+---------+-------+
| corpCode        | char(6)   | NO   | PRI | NULL    |       |
| stockCode       | char(6)   | YES  |     | NULL    |       |
| name            | char(64)  | YES  |     | NULL    |       |
| koreanName      | char(64)  | NO   |     | NULL    |       |
| country         | char(64)  | NO   |     | NULL    |       |
| province        | char(64)  | NO   |     | NULL    |       |
| listingDate     | date      | NO   |     | NULL    |       |
| settlementMonth | int(2)    | NO   |     | NULL    |       |
| ceo             | char(64)  | NO   |     | NULL    |       |
| url             | char(255) | YES  |     | NULL    |       |
| sector          | char(255) | YES  |     | NULL    |       |
+-----------------+-----------+------+-----+---------+-------+
```
