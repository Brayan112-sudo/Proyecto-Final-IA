# Nombres: Brayan Obed Solano Febles
# Matrícula: 23-SISN-2-005


import re

Q = "?w=400&h=400&fit=crop&auto=format"
U = "https://images.unsplash.com/photo-"

# ZAPATILLAS — IDs verificados (título de foto confirma contenido)

# "red Nike shoe lateral"
IMG_Z_NIKE_RED     = U + "1542291026-7eec264c27ff" + Q
# "pair of white Nike shoes"
IMG_Z_NIKE_WHITE   = U + "1606107557195-0e29a4b5b4aa" + Q
# "white Adidas shoe"
IMG_Z_ADIDAS_WHITE = U + "1608231387042-66d1773070a5" + Q
# "black Nike running shoe"
IMG_Z_NIKE_BLACK   = U + "1595950653106-6c9ebd614d3a" + Q
# "pair of running shoes on ground"
IMG_Z_RUNNING_PAIR = U + "1539185441755-769473a23570" + Q
# "Nike shoe side view"
IMG_Z_NIKE_SIDE    = U + "1600185365926-3a2ce3cdb9eb" + Q
# "white-and-red Nike shoe"
IMG_Z_NIKE_WR      = U + "1515955656352-a1fa3ffcd111" + Q
# "pair of orange Nike shoes"
IMG_Z_NIKE_ORANGE  = U + "1565814329452-e1efa11c5b89" + Q
# "Nike Air Max shoe"
IMG_Z_AIRMAX       = U + "1556906781-9a412961a28c" + Q
# "running shoe lateral on track"
IMG_Z_RUN_LAT      = U + "1584735175315-9d5df23be2e4" + Q
# "pink and gray Nike running shoe"
IMG_Z_NIKE_PINK    = U + "1491553895911-0055eca6402d" + Q
# "sport/track shoe"
IMG_Z_TRACK_SHOE   = U + "1562183241-b937e95585b6" + Q


# SPIKES  — zapatillas de pista ligeras / atletismo
IMG_S_1 = U + "1513593771513-93d5eef654db" + Q
# "running shoes on athletic track"
IMG_S_2 = U + "1476480862126-209bfaa8edc8" + Q
# "athletic track start line with shoes"
IMG_S_3 = U + "1526676037926-405f9a2c6b27" + Q
# "close up running shoe on track"
IMG_S_4 = U + "1574680178050-55c6a288d228" + Q


# CAMISETAS — IDs verificados
# "white crew-neck t-shirt"
IMG_C_WHITE   = U + "1521572163474-6864f9cf17ab" + Q
# "black t-shirt flat lay"
IMG_C_BLACK   = U + "1618354691373-d851c5c3a990" + Q
# "sport/running shirt on hanger"
IMG_C_SPORT1  = U + "1583743814966-8936f5b7be1a" + Q
# "athletic running shirt"
IMG_C_SPORT2  = U + "1586790170083-2f9ceadc732d" + Q
# "grey sport shirt"
IMG_C_GREY    = U + "1571945153237-4929e783af4a" + Q


# SHORTS — IDs verificados

# "running shorts close up"
IMG_SH_RUN1  = U + "1506629082955-511b1aa562c8" + Q
# "black athletic shorts"
IMG_SH_BLACK = U + "1591792111137-5b8219d5fad6" + Q
# "man in black shorts running on track" (Philip Strong, verified title)
IMG_SH_TRACK = U + "1529516548873-9ce57c8f155e" + Q
# "sport shorts on hanger"
IMG_SH_HANG  = U + "1538805060514-97d9cc17730c" + Q


# MEDIAS — IDs verificados por título de foto

# "man in gray t-shirt and white nike socks" (GRAHAM MANSFIELD, verified)
IMG_M_NIKE    = "https://images.unsplash.com/photo-IrAm1JhykYU" + Q
# "red and white nike sock" (bb mg, verified)
IMG_M_NIKE2   = "https://images.unsplash.com/photo-SbYGWYfhkWY" + Q
# "blue white and yellow socks on line" (Nick Page, verified)
IMG_M_COLOR   = "https://images.unsplash.com/photo-XMg8GBzNmgA" + Q
# "white nike socks with sport shoes" (Erwans Socks, verified)
IMG_M_SPORT   = "https://images.unsplash.com/photo-YGE42qjlWjE" + Q


# Base de datos de productos

PRODUCTOS_DB = [
    # ZAPATILLAS RUNNING
    {"nombre": "Nike Air Zoom Pegasus 41", "marca": "Nike", "categoria": "Zapatillas",
     "precio": 189000, "rating": 4.6, "resenas": 3200, "meses": 14, "peso": 268, "descuento": 10,
     "tiendas": ["Amazon", "MercadoLibre", "Decathlon"], "pct_positivas": 0.93,
     "imagen": IMG_Z_NIKE_RED},

    {"nombre": "Nike React Infinity Run 4", "marca": "Nike", "categoria": "Zapatillas",
     "precio": 215000, "rating": 4.5, "resenas": 1850, "meses": 8, "peso": 278, "descuento": 0,
     "tiendas": ["Amazon", "MercadoLibre"], "pct_positivas": 0.90,
     "imagen": IMG_Z_NIKE_WR},

    {"nombre": "Adidas Ultraboost 23", "marca": "Adidas", "categoria": "Zapatillas",
     "precio": 230000, "rating": 4.7, "resenas": 4100, "meses": 18, "peso": 312, "descuento": 15,
     "tiendas": ["Amazon", "MercadoLibre", "Decathlon"], "pct_positivas": 0.94,
     "imagen": IMG_Z_ADIDAS_WHITE},

    {"nombre": "Adidas Adizero Boston 12", "marca": "Adidas", "categoria": "Zapatillas",
     "precio": 198000, "rating": 4.4, "resenas": 1200, "meses": 6, "peso": 252, "descuento": 0,
     "tiendas": ["Amazon", "Decathlon"], "pct_positivas": 0.88,
     "imagen": IMG_Z_NIKE_BLACK},

    {"nombre": "Asics Gel-Nimbus 26", "marca": "Asics", "categoria": "Zapatillas",
     "precio": 210000, "rating": 4.8, "resenas": 2900, "meses": 12, "peso": 298, "descuento": 20,
     "tiendas": ["Amazon", "MercadoLibre", "Decathlon"], "pct_positivas": 0.96,
     "imagen": IMG_Z_RUNNING_PAIR},

    {"nombre": "Asics Gel-Kayano 31", "marca": "Asics", "categoria": "Zapatillas",
     "precio": 225000, "rating": 4.7, "resenas": 2100, "meses": 10, "peso": 310, "descuento": 5,
     "tiendas": ["Amazon", "Decathlon"], "pct_positivas": 0.94,
     "imagen": IMG_Z_NIKE_SIDE},

    {"nombre": "New Balance Fresh Foam X 1080v13", "marca": "New Balance", "categoria": "Zapatillas",
     "precio": 205000, "rating": 4.6, "resenas": 1700, "meses": 9, "peso": 290, "descuento": 10,
     "tiendas": ["MercadoLibre", "Decathlon"], "pct_positivas": 0.91,
     "imagen": IMG_Z_NIKE_WHITE},

    {"nombre": "Hoka Clifton 9", "marca": "Hoka", "categoria": "Zapatillas",
     "precio": 195000, "rating": 4.7, "resenas": 2400, "meses": 15, "peso": 252, "descuento": 0,
     "tiendas": ["Amazon", "MercadoLibre"], "pct_positivas": 0.95,
     "imagen": IMG_Z_NIKE_ORANGE},

    {"nombre": "Saucony Ride 17", "marca": "Saucony", "categoria": "Zapatillas",
     "precio": 178000, "rating": 4.5, "resenas": 980, "meses": 7, "peso": 270, "descuento": 12,
     "tiendas": ["Amazon", "MercadoLibre"], "pct_positivas": 0.89,
     "imagen": IMG_Z_AIRMAX},

    {"nombre": "Brooks Ghost 16", "marca": "Brooks", "categoria": "Zapatillas",
     "precio": 182000, "rating": 4.6, "resenas": 2200, "meses": 11, "peso": 285, "descuento": 8,
     "tiendas": ["Amazon", "Decathlon"], "pct_positivas": 0.92,
     "imagen": IMG_Z_RUN_LAT},

    {"nombre": "Puma Deviate Nitro 3", "marca": "Puma", "categoria": "Zapatillas",
     "precio": 165000, "rating": 4.3, "resenas": 750, "meses": 5, "peso": 265, "descuento": 20,
     "tiendas": ["MercadoLibre", "Decathlon"], "pct_positivas": 0.85,
     "imagen": IMG_Z_NIKE_PINK},

    {"nombre": "Mizuno Wave Rider 27", "marca": "Mizuno", "categoria": "Zapatillas",
     "precio": 172000, "rating": 4.5, "resenas": 1100, "meses": 13, "peso": 275, "descuento": 5,
     "tiendas": ["Amazon", "MercadoLibre"], "pct_positivas": 0.90,
     "imagen": IMG_Z_TRACK_SHOE},

    # SPIKES
    {"nombre": "Nike Dragonfly 2 Spikes", "marca": "Nike", "categoria": "Spikes",
     "precio": 285000, "rating": 4.8, "resenas": 620, "meses": 10, "peso": 178, "descuento": 0,
     "tiendas": ["Amazon", "MercadoLibre"], "pct_positivas": 0.97,
     "imagen": IMG_S_1},

    {"nombre": "Adidas Adizero Prime SP2 Spikes", "marca": "Adidas", "categoria": "Spikes",
     "precio": 310000, "rating": 4.9, "resenas": 480, "meses": 8, "peso": 165, "descuento": 0,
     "tiendas": ["Amazon"], "pct_positivas": 0.98,
     "imagen": IMG_S_2},

    {"nombre": "Asics Metaspeed Sky+ Spikes", "marca": "Asics", "categoria": "Spikes",
     "precio": 320000, "rating": 4.8, "resenas": 390, "meses": 12, "peso": 170, "descuento": 10,
     "tiendas": ["Amazon", "Decathlon"], "pct_positivas": 0.96,
     "imagen": IMG_S_3},

    {"nombre": "New Balance MD500 v8 Spikes", "marca": "New Balance", "categoria": "Spikes",
     "precio": 195000, "rating": 4.4, "resenas": 280, "meses": 6, "peso": 185, "descuento": 15,
     "tiendas": ["MercadoLibre"], "pct_positivas": 0.87,
     "imagen": IMG_S_4},

    # CAMISETAS
    {"nombre": "Nike Dri-FIT ADV Run Division", "marca": "Nike", "categoria": "Camisetas",
     "precio": 68000, "rating": 4.4, "resenas": 920, "meses": 20, "peso": 115, "descuento": 10,
     "tiendas": ["Amazon", "MercadoLibre"], "pct_positivas": 0.88,
     "imagen": IMG_C_WHITE},

    {"nombre": "Adidas Own The Run Tee", "marca": "Adidas", "categoria": "Camisetas",
     "precio": 55000, "rating": 4.3, "resenas": 1100, "meses": 24, "peso": 120, "descuento": 20,
     "tiendas": ["Amazon", "MercadoLibre", "Decathlon"], "pct_positivas": 0.86,
     "imagen": IMG_C_SPORT2},

    {"nombre": "Asics Core SS Top", "marca": "Asics", "categoria": "Camisetas",
     "precio": 48000, "rating": 4.2, "resenas": 680, "meses": 18, "peso": 110, "descuento": 0,
     "tiendas": ["Decathlon", "MercadoLibre"], "pct_positivas": 0.84,
     "imagen": IMG_C_BLACK},

    {"nombre": "Under Armour HeatGear Fitted", "marca": "Under Armour", "categoria": "Camisetas",
     "precio": 62000, "rating": 4.5, "resenas": 1450, "meses": 30, "peso": 130, "descuento": 15,
     "tiendas": ["Amazon", "MercadoLibre"], "pct_positivas": 0.91,
     "imagen": IMG_C_SPORT1},

    {"nombre": "Decathlon Kalenji Run 500", "marca": "Decathlon", "categoria": "Camisetas",
     "precio": 22000, "rating": 4.1, "resenas": 2300, "meses": 36, "peso": 105, "descuento": 0,
     "tiendas": ["Decathlon"], "pct_positivas": 0.82,
     "imagen": IMG_C_GREY},

    # SHORTS
    {"nombre": "Nike Dri-FIT Stride 5 Short", "marca": "Nike", "categoria": "Shorts",
     "precio": 72000, "rating": 4.5, "resenas": 1350, "meses": 22, "peso": 95, "descuento": 0,
     "tiendas": ["Amazon", "MercadoLibre"], "pct_positivas": 0.90,
     "imagen": IMG_SH_RUN1},

    {"nombre": "Adidas Own The Run Short", "marca": "Adidas", "categoria": "Shorts",
     "precio": 60000, "rating": 4.3, "resenas": 890, "meses": 18, "peso": 100, "descuento": 10,
     "tiendas": ["Amazon", "Decathlon"], "pct_positivas": 0.87,
     "imagen": IMG_SH_BLACK},

    {"nombre": "Brooks Sherpa 5 2-in-1 Short", "marca": "Brooks", "categoria": "Shorts",
     "precio": 78000, "rating": 4.6, "resenas": 560, "meses": 14, "peso": 105, "descuento": 5,
     "tiendas": ["Amazon"], "pct_positivas": 0.92,
     "imagen": IMG_SH_HANG},

    {"nombre": "Decathlon Kalenji Run 500 Short", "marca": "Decathlon", "categoria": "Shorts",
     "precio": 18000, "rating": 4.0, "resenas": 3100, "meses": 48, "peso": 90, "descuento": 0,
     "tiendas": ["Decathlon"], "pct_positivas": 0.80,
     "imagen": IMG_SH_TRACK},

    # MEDIAS
    {"nombre": "Balega Hidden Comfort Running Socks", "marca": "Balega", "categoria": "Medias",
     "precio": 18000, "rating": 4.8, "resenas": 4800, "meses": 48, "peso": 45, "descuento": 0,
     "tiendas": ["Amazon", "MercadoLibre"], "pct_positivas": 0.96,
     "imagen": IMG_M_SPORT},   # white nike socks with sport shoes

    {"nombre": "Nike Dri-FIT Running Crew Socks", "marca": "Nike", "categoria": "Medias",
     "precio": 14000, "rating": 4.4, "resenas": 2100, "meses": 36, "peso": 50, "descuento": 0,
     "tiendas": ["Amazon", "MercadoLibre", "Decathlon"], "pct_positivas": 0.88,
     "imagen": IMG_M_NIKE2},   # red and white nike sock

    {"nombre": "Asics Ultra Comfort Quarter Sock", "marca": "Asics", "categoria": "Medias",
     "precio": 16000, "rating": 4.6, "resenas": 980, "meses": 24, "peso": 48, "descuento": 10,
     "tiendas": ["Amazon", "Decathlon"], "pct_positivas": 0.93,
     "imagen": IMG_M_NIKE},    # man in gray shirt and white nike socks

    {"nombre": "Decathlon Kalenji Run 500 Socks", "marca": "Decathlon", "categoria": "Medias",
     "precio": 5000, "rating": 4.1, "resenas": 5200, "meses": 60, "peso": 42, "descuento": 0,
     "tiendas": ["Decathlon"], "pct_positivas": 0.81,
     "imagen": IMG_M_COLOR},   # blue white and yellow socks on line
]


def obtener_productos(nombre_busqueda: str) -> list[dict]:
    query = nombre_busqueda.lower().strip()
    tokens = re.split(r'\s+', query)

    resultados = []
    for p in PRODUCTOS_DB:
        texto = (p["nombre"] + " " + p["marca"] + " " + p["categoria"]).lower()
        if any(tok in texto for tok in tokens if len(tok) > 2):
            resultados.append(p.copy())

    if not resultados:
        resultados = [p.copy() for p in PRODUCTOS_DB]

    return resultados