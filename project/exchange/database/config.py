import psycopg2

conn = psycopg2.connect(database="cryptocurrency_exchange_db",
                        host="localhost",
                        user="postgres",
                        password="admin",
                        port="5432")


def main():
    pass


if __name__ == "__main__":
    main()
