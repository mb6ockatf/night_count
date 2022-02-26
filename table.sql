use night_count;
CREATE TABLE nightcount
( id  INT(11) NOT NULL AUTO_INCREMENT,
  date_column DATE,
  time_column time,
  CONSTRAINT nightcount_pk PRIMARY KEY (id)
);
