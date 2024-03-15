from database import Database

def table():
    menu_table = f"""
        CREATE TABLE menu(
            menu_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            create_table TIMESTAMP DEFAULT now()
        );"""
    category_table = f"""
        CREATE TABLE category(
            category_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            create_table TIMESTAMP DEFAULT now()
        );"""
    
    data = {
        "menu_table": menu_table,
        "category_table": category_table
    }
    for i in data:
        print(f"{i} - {Database.connect(data[i], "create")}")

if __name__ == "__main__":
    table()