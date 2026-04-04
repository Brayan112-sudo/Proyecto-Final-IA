# AtleticaStore — Instrucciones de uso

## Archivos del proyecto
```
atletica/
├── tienda_atlet.py    ← App principal Gradio (tu archivo original, sin cambios)
├── api_conexion.py    ← Simula APIs de e-commerce (Amazon, MercadoLibre, Decathlon)
├── productos.py       ← Filtros, scoring del modelo y formateo de resultados
└── README.md
```

## Instalación
```bash
pip install gradio
```

## Ejecutar
```bash
python tienda_atlet.py
```
Luego abrir http://localhost:7860 en el navegador.

## En Google Colab
```python
!pip install gradio
!python tienda_atlet.py
```
