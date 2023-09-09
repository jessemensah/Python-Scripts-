import pymysql

drop_vinyldb = "DROP DATABASE IF EXISTS vinylrecordshop;"

create_vinyldb = "CREATE DATABASE vinylrecordshop;"


drop_artist = "DROP TABLE IF EXISTS artist;"

create_artist  = """
            CREATE TABLE artist (
              artist_id int(11) NOT NULL AUTO_INCREMENT,
              fname varchar(40) NOT NULL,
              lname varchar(40) NOT NULL,
              isHallOfFame tinyint(1) NOT NULL,
              PRIMARY KEY (artist_id)
            )           
            ENGINE=InnoDB DEFAULT CHARSET=latin1;
         """

insert_data = """INSERT INTO artist (artist_id, fname, lname, isHallOfFame) 
                VALUES
                    (1, 'John', 'Lennon', 0),
                    (2, 'Paul', 'McCartney', 0),
                    (3, 'George', 'Harrison', 0),
                    (4, 'Ringo', 'Starr', 0),
                    (5, 'Denny', 'Zager', 0),
                    (6, 'Rick', 'Evans', 0),
                    (10, 'Van', 'Morrison', 0),
                    (11, 'Judy', 'Collins', 0),
                    (12, 'Paul', 'Simon', 0),
                    (13, 'Art', 'Garfunkel', 0),
                    (14, 'Brian', 'Wilson', 0),
                    (15, 'Dennis', 'Wilson', 0),
                    (16, 'Carl', 'Wilson', 0),
                    (17, 'Ricky', 'Fataar', 0),
                    (18, 'Blondie', 'Chaplin', 0),
                    (19, 'Jimmy', 'Page', 0),
                    (20, 'Robert', 'Plant', 0),
                    (21, 'John Paul', 'Jones', 0),
                    (22, 'John', 'Bonham', 0),
                    (23, 'Mike ', 'Love', 0),
                    (24, 'Al ', 'Jardine', 0),
                    (25, 'David', 'Marks', 0),
                    (26, 'Bruce ', 'Johnston', 0);"""

#update connection data as required for the local MySQL setup
con = pymysql.connect(host='localhost', user='root', password='admin')
with con:
    cur = con.cursor() #create a cursor object that will use to execute MySQL queries.
    cur.execute(drop_vinyldb)
    cur.execute(create_vinyldb)
    cur.execute("USE vinylrecordshop;")
    cur.execute(drop_artist)
    cur.execute(create_artist)
    cur.execute(insert_data) #execute insert query