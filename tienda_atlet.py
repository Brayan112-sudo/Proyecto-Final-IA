# Nombres: Brayan Obed Solano Febles
# Matrícula: 23-SISN-2-005


import gradio as gr
from api_conexion import obtener_productos
from productos import filtrar_por_precio, ordenar_productos, formatear_resultados, calcular_puntaje


def buscar_producto(nombre, precio_min, precio_max, ordenar_por, categorias):
    try:
        if not nombre.strip():
            return "<p style='color:#999;padding:20px'>Ingresá el nombre de un artículo para buscar.</p>"

        productos = obtener_productos(nombre)

        if not productos:
            return "<p style='color:#999;padding:20px'>No se encontraron productos.</p>"

        productos_filtrados = filtrar_por_precio(productos, precio_min, precio_max)

        if categorias:
            criterio = categorias[0].lower()
            productos_filtrados = [
                p for p in productos_filtrados
                if criterio in p.get("nombre", "").lower()
                or criterio in p.get("categoria", "").lower()
            ]

        if not productos_filtrados:
            return "<p style='color:#999;padding:20px'>No hay productos que coincidan con los filtros.</p>"

        criterio_orden = (ordenar_por or "calidad").lower()
        productos_ordenados = ordenar_productos(productos_filtrados, criterio_orden)

        return formatear_resultados(productos_ordenados)

    except Exception as e:
        return f"<p style='color:#f87171;padding:20px'>Error: {str(e)}</p>"


css = """
body { background: #0a0c0f !important; }
#header {
    background: linear-gradient(135deg,#0a0c0f 0%,#12161c 100%);
    border-bottom: 1px solid #232a35;
    padding: 28px 32px 20px;
    margin-bottom: 8px;
}
#header h1 {
    font-size: 2.4rem; font-weight: 900; letter-spacing: 4px;
    text-transform: uppercase; color: #f0f2f5; margin: 0 0 4px;
}
#header h1 span { color: #e8ff47; }
#header p { color: #6b7585; font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; margin: 0; }
.gradio-container { background: #0a0c0f !important; max-width: 1280px !important; }
label { color: #9ca3af !important; font-size: 0.72rem !important; letter-spacing: 1.5px !important; text-transform: uppercase !important; font-weight: 500 !important; }
input, select, textarea { background: #12161c !important; border: 1px solid #232a35 !important; color: #f0f2f5 !important; border-radius: 6px !important; }
#btn-buscar {
    background: #e8ff47 !important; color: #0a0c0f !important; font-weight: 800 !important;
    letter-spacing: 3px !important; text-transform: uppercase !important; border: none !important;
    border-radius: 6px !important; padding: 14px !important; font-size: 1rem !important;
    cursor: pointer !important; width: 100% !important;
}
#btn-buscar:hover { box-shadow: 0 6px 20px rgba(232,255,71,0.3) !important; }
.block, .panel { background: #12161c !important; border: 1px solid #232a35 !important; border-radius: 10px !important; }
footer { display: none !important; }
"""

with gr.Blocks(title="AtleticaStore", css=css, theme=gr.themes.Base()) as tienda_atlet:

    gr.HTML("""
    <div id="header">
        <h1>ATLETICA<span>STORE</span></h1>
        <p>Equipamiento de atletismo · Clasificación inteligente por IA</p>
    </div>
    """)

    with gr.Row(equal_height=False):

        with gr.Column(scale=1, min_width=280):
            txt_nombre = gr.Textbox(
                label="Artículo",
                placeholder="Ej: zapatillas Nike running, spikes atletismo...",
                lines=1
            )
            with gr.Row():
                slider_min = gr.Slider(minimum=0, maximum=500000, value=0, step=5000, label="Precio mínimo (ARS$)")
                slider_max = gr.Slider(minimum=0, maximum=500000, value=500000, step=5000, label="Precio máximo (ARS$)")

            dd_orden = gr.Dropdown(
                choices=["Calidad", "Precio", "Durabilidad", "Relevancia"],
                value="Calidad", label="Ordenar por"
            )
            chk_categorias = gr.CheckboxGroup(
                choices=["Zapatillas", "Camisetas", "Shorts", "Medias", "Spikes"],
                label="Categoría"
            )
            gr.Examples(
                examples=[
                    ["zapatillas Nike running", 0, 300000, "Calidad", ["Zapatillas"]],
                    ["spikes atletismo", 0, 500000, "Durabilidad", ["Spikes"]],
                    ["camiseta running", 0, 150000, "Precio", ["Camisetas"]],
                    ["shorts atletismo", 0, 100000, "Precio", ["Shorts"]],
                    ["medias running", 0, 50000, "Calidad", ["Medias"]],
                ],
                inputs=[txt_nombre, slider_min, slider_max, dd_orden, chk_categorias],
                label="Búsquedas rápidas"
            )
            btn_buscar = gr.Button("⚡ BUSCAR", elem_id="btn-buscar")

        with gr.Column(scale=2):
            html_resultados = gr.HTML(
                value="<p style='color:#6b7585;padding:32px;text-align:center;font-size:0.9em'>🏃 Los resultados aparecerán aquí...</p>"
            )

    btn_buscar.click(
        fn=buscar_producto,
        inputs=[txt_nombre, slider_min, slider_max, dd_orden, chk_categorias],
        outputs=[html_resultados]
    )
    txt_nombre.submit(
        fn=buscar_producto,
        inputs=[txt_nombre, slider_min, slider_max, dd_orden, chk_categorias],
        outputs=[html_resultados]
    )

tienda_atlet.launch()
