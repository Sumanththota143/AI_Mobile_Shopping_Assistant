
import sqlite3

conn = sqlite3.connect("mobiles.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mobiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    model TEXT UNIQUE,
    price INTEGER,
    rating REAL,
    ram_gb INTEGER,
    storage_gb INTEGER,
    battery_mah INTEGER
)
""")

# 50 mobiles: 10 brands x 5 models
mobiles = [
    # Samsung
    ("Samsung", "Galaxy S25", 75000, 4.6, 12, 256, 4000),
    ("Samsung", "Galaxy S25 Ultra", 130000, 4.8, 12, 512, 5000),
    ("Samsung", "Galaxy A56", 42000, 4.4, 8, 256, 5000),
    ("Samsung", "Galaxy A36", 33000, 4.3, 8, 128, 5000),
    ("Samsung", "Galaxy M35", 20000, 4.2, 8, 128, 6000),

    # Apple
    ("Apple", "iPhone 16", 70000, 4.6, 8, 128, 3561),
    ("Apple", "iPhone 16 Plus", 80000, 4.5, 8, 128, 4674),
    ("Apple", "iPhone 16 Pro", 110000, 4.8, 8, 256, 3582),
    ("Apple", "iPhone 16 Pro Max", 145000, 4.9, 8, 512, 4685),
    ("Apple", "iPhone 15", 60000, 4.5, 6, 128, 3349),

    # Xiaomi
    ("Xiaomi", "Xiaomi 15", 65000, 4.6, 12, 256, 5240),
    ("Xiaomi", "Xiaomi 15 Ultra", 110000, 4.8, 16, 512, 5410),
    ("Xiaomi", "Redmi Note 14 Pro+", 31000, 4.4, 8, 256, 6200),
    ("Xiaomi", "Redmi Note 14", 19000, 4.2, 8, 128, 5110),
    ("Xiaomi", "Redmi 14C", 10000, 4.0, 4, 128, 5160),

    # OnePlus
    ("OnePlus", "OnePlus 13", 70000, 4.8, 12, 256, 6000),
    ("OnePlus", "OnePlus 13R", 43000, 4.6, 12, 256, 6000),
    ("OnePlus", "Nord 4", 30000, 4.4, 8, 128, 5500),
    ("OnePlus", "Nord CE4", 25000, 4.3, 8, 128, 5500),
    ("OnePlus", "OnePlus 12", 65000, 4.7, 12, 256, 5400),

    # Vivo
    ("Vivo", "X200 Pro", 95000, 4.7, 16, 512, 6000),
    ("Vivo", "V50", 35000, 4.4, 8, 256, 6000),
    ("Vivo", "V40", 35000, 4.3, 8, 256, 5500),
    ("Vivo", "T3 Pro", 25000, 4.2, 8, 128, 5500),
    ("Vivo", "Y200", 22000, 4.1, 8, 128, 4800),

    # Oppo
    ("Oppo", "Find X8 Pro", 100000, 4.7, 16, 512, 5910),
    ("Oppo", "Reno13 Pro", 50000, 4.5, 12, 256, 5800),
    ("Oppo", "Reno12", 33000, 4.3, 8, 256, 5000),
    ("Oppo", "F27 Pro+", 28000, 4.2, 8, 128, 5000),
    ("Oppo", "A3 Pro", 18000, 4.0, 8, 128, 5100),

    # Realme
    ("Realme", "GT 7 Pro", 60000, 4.7, 12, 256, 5800),
    ("Realme", "GT 6", 41000, 4.5, 12, 256, 5500),
    ("Realme", "14 Pro+", 33000, 4.4, 8, 256, 6000),
    ("Realme", "Narzo 70 Pro", 20000, 4.2, 8, 128, 5000),
    ("Realme", "C75", 15000, 4.1, 8, 128, 6000),

    # Motorola
    ("Motorola", "Edge 50 Ultra", 55000, 4.5, 12, 512, 4500),
    ("Motorola", "Edge 50 Pro", 32000, 4.4, 8, 256, 4500),
    ("Motorola", "Edge 50 Fusion", 23000, 4.3, 8, 128, 5000),
    ("Motorola", "Moto G85", 18000, 4.2, 8, 128, 5000),
    ("Motorola", "Moto G64", 15000, 4.1, 8, 128, 6000),

    # Google
    ("Google", "Pixel 9", 80000, 4.6, 12, 256, 4700),
    ("Google", "Pixel 9 Pro", 110000, 4.8, 16, 256, 4700),
    ("Google", "Pixel 9 Pro XL", 125000, 4.8, 16, 512, 5060),
    ("Google", "Pixel 8a", 53000, 4.4, 8, 128, 4492),
    ("Google", "Pixel 8", 76000, 4.5, 8, 128, 4575),

    # Nothing
    ("Nothing", "Phone 3", 80000, 4.5, 12, 256, 5500),
    ("Nothing", "Phone 3a Pro", 33000, 4.4, 8, 256, 5000),
    ("Nothing", "Phone 3a", 25000, 4.3, 8, 128, 5000),
    ("Nothing", "Phone 2a Plus", 28000, 4.2, 12, 256, 5000),
    ("Nothing", "Phone 2a", 24000, 4.3, 8, 128, 5000)
]

# Insert data
cursor.executemany("""
INSERT OR IGNORE INTO mobiles
(brand, model, price, rating, ram_gb, storage_gb, battery_mah)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", mobiles)

conn.commit()

# Display total records
cursor.execute("SELECT COUNT(*) FROM mobiles")
print("Total mobiles:", cursor.fetchone()[0])

conn.close()
print("Database created successfully!")
