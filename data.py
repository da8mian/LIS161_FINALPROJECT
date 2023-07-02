import sqlite3

db_path = "pa.db"


def connect_to_db(path):
    conn = sqlite3.connect(path)
    # Converting tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())


def read_cafes_by_cafe_area(cafe_area):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM cafes WHERE area = ?'
    value = cafe_area
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results


def read_cafe_by_cafe_id(cafe_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM cafes WHERE id = ?'
    value = cafe_id
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result


def insert_cafe(cafe_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO cafes (area, name, desc, url, address, time, outlet, parking, number, email, website, fb, ig) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)' 
    values = (cafe_data['cafe_area'], cafe_data['name'],
              cafe_data['desc'], cafe_data['url'],
              cafe_data['address'], cafe_data['time'],
              cafe_data['outlet'],
              cafe_data['parking'], cafe_data['number'],
              cafe_data['email'], cafe_data['website'],
              cafe_data['fb'], cafe_data['ig'],
            )
    cur.execute(query,values)
    conn.commit()
    conn.close()


def update_cafe(cafe_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE cafes SET area=?, name=?, desc=?, url=?, address=?, time=?, outlet=?, parking=?, number=?, email=?, website=?, fb=?, ig=? WHERE id=?" 
    values = (cafe_data['cafe_area'], 
              cafe_data['name'],
              cafe_data['desc'],
              cafe_data['url'],
              cafe_data['address'],
              cafe_data['time'],
              cafe_data['outlet'],
              cafe_data['parking'],
              cafe_data['number'],
              cafe_data['email'],
              cafe_data['website'],
              cafe_data['fb'],
              cafe_data['ig'],
              cafe_data['cafe_id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_cafe(cafe_id):
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM cafes WHERE id = ?"
    values = (cafe_id,)
    cur.execute(query, values)
    conn.commit()
    conn.close()