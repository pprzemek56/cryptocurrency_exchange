import psycopg2

conn = psycopg2.connect(database="cryptocurrency_exchange_db",
                        host="localhost",
                        user="postgres",
                        password="admin",
                        port="5432")

cursor = conn.cursor()

create_transaction_table = '''CREATE TABLE Transaction(
    id SERIAL PRIMARY KEY,
    trading_pair_name VARCHAR(255),
    price NUMERIC,
    value NUMERIC,
    type_of_transaction VARCHAR(255),
    stop_loss NUMERIC,
    take_profit NUMERIC,
    liquidation_price NUMERIC,
    profit NUMERIC,
    status VARCHAR(255),
    is_profitable BOOLEAN DEFAULT FALSE,
    create_date_time TIMESTAMP,
    liquidation_date_time TIMESTAMP
    )
'''

cursor.execute(create_transaction_table)
cursor.close()

conn.commit()
conn.close()
