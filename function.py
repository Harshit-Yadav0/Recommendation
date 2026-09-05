#Imported modules and lib
import sqlite
import random

random.seed(7985763728)

#Main function
def add_sub(x,y,z):
    conn=sqlite3.connect('recommendation.db')
    cursor=conn.cursor()
    
    t=1000000000
    unique_id=0
    for i in range(t):
        unique_id=random.randint(1,9999999999)
        cursor.execute('''
            SELECT id FROM movies
            WHERE id = (?)
            ''',(unique_id,);
        )

        result=cursor.fetchone()
        if result is NONE:
            cursor.execute('''
                INSERT INTO movies (id,name,rating,genre)
                VALUES (?,?,?,?)
                ''',(unique_id,x,y,z))

            cursor.commit()
            break
    conn.close()
