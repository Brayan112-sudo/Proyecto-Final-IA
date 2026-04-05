# Nombres: Brayan Obed Solano Febles
# Matrícula: 23-SISN-2-005


import math

# Parámetros del modelo (reputación por marca y precio base por categoría)

REPUTACION_MARCA = {
    "Nike": 0.92, "Adidas": 0.90, "Asics": 0.88,
    "New Balance": 0.85, "Brooks": 0.87, "Saucony": 0.84,
    "Hoka": 0.89, "Puma": 0.80, "Under Armour": 0.78,
    "Mizuno": 0.86, "Balega": 0.83, "Decathlon": 0.72,
}

PRECIO_BASE_USD = {
    "Zapatillas": 150, "Spikes": 220,
    "Camisetas": 45,   "Shorts": 40,
    "Medias": 18,
}

USD_A_ARS = 1200  # tipo de cambio de referencia


# Función principal de puntaje

def calcular_puntaje(producto: dict) -> dict:
    if not producto:
        return {"calidad": "—", "precio": "—", "durabilidad": "—"}

    marca    = producto.get("marca", "")
    cat      = producto.get("categoria", "Zapatillas")
    precio   = producto.get("precio", 0)          # en ARS
    rating   = producto.get("rating", 3.0)
    resenas  = producto.get("resenas", 100)
    meses    = producto.get("meses", 12)
    pct_pos  = producto.get("pct_positivas", 0.75)
    descuento= producto.get("descuento", 0)
    peso     = producto.get("peso", 250)
    tiendas  = len(producto.get("tiendas", []))

    rep = REPUTACION_MARCA.get(marca, 0.80)
    precio_usd = precio / USD_A_ARS
    precio_base = PRECIO_BASE_USD.get(cat, 100)
    precio_rel  = precio_usd / precio_base

    # Calidad: rating, reputación, % positivas
    calidad = (rating / 5.0) * 4.0 + rep * 3.0 + pct_pos * 2.5
    calidad = _clip(calidad, 1, 10)

    # Precio-valor: precio relativo, descuento, disponibilidad
    score_precio = (2.0 - precio_rel) * 4.5 + (descuento / 40.0) * 3.0 + (tiendas / 3.0) * 2.0
    score_precio = _clip(score_precio, 1, 10)

    # Durabilidad: antigüedad, reseñas, reputación, peso
    durabilidad = (
        (meses / 60.0) * 2.5 +
        (math.log(resenas + 1) / math.log(5001)) * 3.0 +
        rep * 3.0 +
        (peso / 380.0) * 1.0
    )
    durabilidad = _clip(durabilidad, 1, 10)

    return {
        "calidad"     : round(calidad, 2),
        "precio"      : round(score_precio, 2),
        "durabilidad" : round(durabilidad, 2),
    }


def _clip(valor, minv, maxv):
    return max(minv, min(maxv, valor))


# Filtros

def filtrar_por_precio(productos: list[dict], precio_min: float, precio_max: float) -> list[dict]:
    """Filtra productos por rango de precio en ARS."""
    return [
        p for p in productos
        if precio_min <= p.get("precio", 0) <= precio_max
    ]


# Ordenamiento

def ordenar_productos(productos: list[dict], criterio: str = "calidad") -> list[dict]:
    """
    Ordena la lista de productos según el criterio elegido.
    criterio: 'calidad' | 'precio' | 'durabilidad' | 'relevancia'
    """
    criterio = criterio.lower().strip()

    if criterio == "relevancia":
        return productos  # orden original de búsqueda

    def clave(p):
        scores = calcular_puntaje(p)
        if criterio == "calidad":
            return scores["calidad"]
        elif criterio in ("precio", "precio-valor"):
            return scores["precio"]
        elif criterio == "durabilidad":
            return scores["durabilidad"]
        else:
            return (scores["calidad"] + scores["precio"] + scores["durabilidad"]) / 3

    return sorted(productos, key=clave, reverse=True)


# Formateo HTML

CATEGORIA_EMOJI = {
    "Zapatillas": "👟",
    "Spikes": "⚡",
    "Camisetas": "👕",
    "Shorts": "🩳",
    "Medias": "🧦",
}

def formatear_resultados(productos: list[dict]) -> str:
    if not productos:
        return "<p style='color:#999;padding:20px'>No se encontraron productos.</p>"

    TIENDA_URLS = {
        "Amazon":       "https://www.amazon.com",
        "MercadoLibre": "https://www.mercadolibre.com.ar",
        "Decathlon":    "https://www.decathlon.com.ar",
    }
    TIENDA_COLORES = {
        "Amazon":       "#FF9900",
        "MercadoLibre": "#FFE600",
        "Decathlon":    "#0082C3",
    }

    cards_html = []
    for i, p in enumerate(productos[:8]):
        scores   = calcular_puntaje(p)
        promedio = (scores["calidad"] + scores["precio"] + scores["durabilidad"]) / 3
        rating   = p.get("rating", 3.0)
        estrellas_llenas = int(round(rating))
        estrellas_html = (
            "★" * estrellas_llenas + "☆" * (5 - estrellas_llenas)
        )

        precio_ars = p["precio"]
        desc       = p.get("descuento", 0)
        precio_fmt = f"${precio_ars:,.0f}".replace(",", ".")
        if desc > 0:
            precio_final = precio_ars * (1 - desc / 100)
            precio_html = (
                f"<span style='text-decoration:line-through;color:#888;font-size:0.85em'>{precio_fmt}</span> "
                f"<span style='color:#4ade80;font-weight:700'>${precio_final:,.0f} ARS</span> "
                f"<span style='background:#16a34a;color:#fff;border-radius:4px;padding:1px 6px;font-size:0.75em'>{desc}% OFF</span>"
            ).replace(",", ".")
        else:
            precio_html = f"<span style='font-weight:700'>{precio_fmt} ARS</span>"

        # Imagen con fallback a emoji de categoría
        imagen_url = p.get("imagen", "")
        emoji = CATEGORIA_EMOJI.get(p.get("categoria", ""), "🏃")
        placeholder_style = (
            "width:140px;height:140px;flex-shrink:0;border-radius:8px;"
            "background:#1e2430;display:flex;align-items:center;"
            "justify-content:center;font-size:3.2rem"
        )

        if imagen_url:
            imagen_html = (
                f"<div style='{placeholder_style}' id='imgbox-{i}'>"
                f"<img src='{imagen_url}' alt='{p['nombre']}' "
                f"style='width:140px;height:140px;object-fit:contain;"
                f"border-radius:8px;background:#1e2430;padding:8px' "
                f"onerror=\"this.parentElement.innerHTML='<span>{emoji}</span>'\">"
                f"</div>"
            )
        else:
            imagen_html = (
                f"<div style='{placeholder_style}'>"
                f"<span>{emoji}</span>"
                f"</div>"
            )

        def barra_html(score, color):
            pct = score / 10 * 100
            return (
                f"<div style='background:#1e2430;border-radius:4px;height:8px;width:100%'>"
                f"<div style='background:{color};height:8px;border-radius:4px;width:{pct:.1f}%'></div>"
                f"</div>"
            )

        def btn_tienda(t):
            url   = TIENDA_URLS.get(t, "#")
            color = TIENDA_COLORES.get(t, "#555")
            return (
                f"<a href='{url}' target='_blank' "
                f"style='background:{color};color:#111;padding:4px 10px;"
                f"border-radius:4px;text-decoration:none;font-size:0.75em;font-weight:600'>{t}</a>"
            )

        tiendas_btns = " ".join([btn_tienda(t) for t in p.get("tiendas", [])])

        card = f"""
        <div style='display:flex;gap:16px;background:#12161c;border:1px solid #232a35;
                    border-radius:10px;padding:16px;margin-bottom:14px;align-items:flex-start'>
            {imagen_html}
            <div style='flex:1;min-width:0'>
                <div style='font-size:0.72em;color:#6b7585;text-transform:uppercase;
                            letter-spacing:1px;margin-bottom:3px'>{p['marca']} · {p['categoria']}</div>
                <div style='font-weight:700;font-size:1.05em;margin-bottom:6px'>{p['nombre']}</div>
                <div style='color:#f59e0b;font-size:1em;letter-spacing:2px;margin-bottom:2px'>{estrellas_html}
                    <span style='color:#6b7585;font-size:0.8em;margin-left:4px'>{rating}/5 · {p['resenas']:,} reseñas</span>
                </div>
                <div style='margin:8px 0'>{precio_html}</div>

                <div style='display:grid;grid-template-columns:90px 1fr 36px;
                            align-items:center;gap:6px 10px;margin:10px 0'>
                    <span style='font-size:0.75em;color:#9ca3af'>✨ Calidad</span>
                    {barra_html(scores['calidad'], '#e8ff47')}
                    <span style='font-size:0.85em;font-weight:700;color:#e8ff47'>{scores['calidad']:.1f}</span>

                    <span style='font-size:0.75em;color:#9ca3af'>💰 Precio</span>
                    {barra_html(scores['precio'], '#ff6b4a')}
                    <span style='font-size:0.85em;font-weight:700;color:#ff6b4a'>{scores['precio']:.1f}</span>

                    <span style='font-size:0.75em;color:#9ca3af'>🔩 Durabilidad</span>
                    {barra_html(scores['durabilidad'], '#4ae8c2')}
                    <span style='font-size:0.85em;font-weight:700;color:#4ae8c2'>{scores['durabilidad']:.1f}</span>

                    <span style='font-size:0.75em;color:#9ca3af'>⭐ Promedio</span>
                    {barra_html(promedio, '#a78bfa')}
                    <span style='font-size:0.85em;font-weight:700;color:#a78bfa'>{promedio:.1f}</span>
                </div>

                <div style='margin-top:10px;display:flex;gap:6px;flex-wrap:wrap;align-items:center'>
                    <span style='font-size:0.72em;color:#6b7585;margin-right:2px'>🛒</span>
                    {tiendas_btns}
                </div>
            </div>
        </div>
        """
        cards_html.append(card)

    resto = f"<p style='color:#6b7585;font-size:0.85em;padding:4px 0'>... y {len(productos)-8} producto(s) más.</p>" if len(productos) > 8 else ""

    return f"""
    <div style='font-family:system-ui,sans-serif;color:#f0f2f5'>
        <p style='color:#6b7585;font-size:0.8em;letter-spacing:1.5px;text-transform:uppercase;
                  margin-bottom:14px'>🏃 {len(productos)} producto(s) encontrado(s)</p>
        {''.join(cards_html)}
        {resto}
    </div>
    """