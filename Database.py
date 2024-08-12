from sqlalchemy import create_engine, text
import os

engine = create_engine(os.environ['DB_CONNECTION'])

# Function to get all the items info from the database
def load_items_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('select * from handicraft'))
    
        items_info = []
        for row in result.fetchall():
            new_dict = {"Item_id": row.Item_id, "Item_name": row.Item_name, "Metal_name": row.Metal_name,
                        "Weight":row.Weight, "Polish":row.Polish, "Price":row.Price}
            items_info.append(new_dict)
        return items_info
