from fastapi import FastAPI
import psycopg2

app = FastAPI()


# -----------------------------------
# HOME / BACKEND TEST
# -----------------------------------

@app.get("/")
def home():
    return {
        "message": "Cybersecurity Backend is Running!"
    }


# -----------------------------------
# DATABASE CONNECTION TEST
# -----------------------------------

@app.get("/db-test")
def db_test():

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="cybersecurity_db",
            user="postgres",
            password="Pshetty06@"
        )

        conn.close()

        return {
            "status": "success",
            "message": "PostgreSQL connection is working!"
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


# -----------------------------------
# GET USERS FROM DATABASE
# -----------------------------------

@app.get("/users")
def get_users():

    try:

        conn = psycopg2.connect(
            host="localhost",
            database="cybersecurity_db",
            user="postgres",
            password="Pshetty06@"
        )

        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, username, email, created_at
            FROM users
            ORDER BY id;
        """)

        users = cursor.fetchall()

        cursor.close()
        conn.close()

        return {
            "users": [
                {
                    "id": user[0],
                    "username": user[1],
                    "email": user[2],
                    "created_at": user[3]
                }
                for user in users
            ]
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }