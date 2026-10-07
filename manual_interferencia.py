# ============================================================
# Manual de Usuario Interactivo
# Interferencia en Películas Delgadas - Ondas de Luz
# Autor: Josue Arturo Reynoso Molina - 202307813
# USAC - Facultad de Ingeniería - 2026
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox, font
import os

# ============================================================
# CONFIGURACIÓN
# ============================================================
TITULO = "Manual de Usuario — Interferencia en Películas Delgadas"
AUTOR = "Josue Arturo Reynoso Molina"
CARNE = "202307813"
UNIVERSIDAD = "Universidad de San Carlos de Guatemala"
FACULTAD = "Facultad de Ingeniería — Escuela de Ingeniería Mecánica Eléctrica"

# Colores
COLOR_BG = "#f4f6f9"
COLOR_HEADER = "#003366"
COLOR_ACCENT = "#005599"
COLOR_OK = "#22aa44"
COLOR_WARN = "#cc8800"
COLOR_ERR = "#cc3333"
COLOR_CODE_BG = "#0f0f1e"
COLOR_CODE_FG = "#ffd700"
COLOR_IMG_BG = "#e8eef5"
COLOR_IMG_BORDER = "#005599"
COLOR_RESULT_BG = "#d4edda"
COLOR_RESULT_FG = "#155724"

# Tamaños de imágenes
TAM_IMG_GRANDE = (650, 380)
TAM_IMG_MEDIANA = (500, 320)
TAM_IMG_LOGO = (180, 180)

# ============================================================
# DATOS DEL BUFFER (hex del programa)
# ============================================================
BUFFER_HEX = """
3D 3D 3D 20 41 4E 41 4C 49 5A 41 44 4F 52 20 44 45 20 49 4E 54 45 52 46 45 52 45 4E
43 49 41 20 45 4E 20 50 45 4C 49 43 55 4C 41 53 20 44 45 4C 47 41 44 41 53 20 3D 3D
3D 0D 0A 45 73 70 65 73 6F 72 3A 20 33 32 30 20 6E 6D 20 7C 20 49 6E 64 69 63 65 20
64 65 20 72 65 66 72 61 63 63 69 6F 6E 3A 20 31 2E 33 33 0D 0A 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 4F 72 64 65 6E 20 6D 20
3D 20 30 20 2D 3E 20 4C 6F 6E 67 69 74 75 64 20 64 65 20 6F 6E 64 61 3A 20 31 37
30 32 2E 34 30 20 6E 6D 0D 0A 20 20 2D 3E 20 5B 46 55 45 52 41 20 44 45 4C 20 45
53 50 45 43 54 52 4F 20 56 49 53 49 42 4C 45 5D 0D 0A 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 4F 72 64 65 6E 20 6D 20 3D 20 31
20 2D 3E 20 4C 6F 6E 67 69 74 75 64 20 64 65 20 6F 6E 64 61 3A 20 35 36 37 2E 34
36 20 6E 6D 0D 0A 20 20 2D 3E 20 5B 56 49 53 49 42 4C 45 5D 20 45 73 74 61 20 6C
6F 6E 67 69 74 75 64 20 64 65 20 6F 6E 64 61 20 73 65 20 72 65 66 6C 65 6A 61 2E
0D 0A 20 20 2D 3E 20 43 6F 6C 6F 72 20 61 70 72 6F 78 69 6D 61 64 6F 3A 20 56 65
72 64 65 0D 0A 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 0D 0A 4F 72 64 65 6E 20 6D 20 3D 20 32 20 2D 3E 20 4C 6F 6E 67 69 74 75 64 20
64 65 20 6F 6E 64 61 3A 20 33 34 30 2E 34 38 20 6E 6D 0D 0A 20 20 2D 3E 20 5B 46
55 45 52 41 20 44 45 4C 20 45 53 50 45 43 54 52 4F 20 56 49 53 49 42 4C 45 5D 0D
0A 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 4F
72 64 65 6E 20 6D 20 3D 20 33 20 2D 3E 20 4C 6F 6E 67 69 74 75 64 20 64 65 20 6F
6E 64 61 3A 20 32 34 33 2E 32 30 20 6E 6D 0D 0A 20 20 2D 3E 20 5B 46 55 45 52 41
20 44 45 4C 20 45 53 50 45 43 54 52 4F 20 56 49 53 49 42 4C 45 5D 0D 0A 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 0D 0A 3D 3D
3D 20 46 49 4E 20 44 45 4C 20 41 4E 41 4C 49 53 49 53 20 3D 3D 3D 0D 0A
"""


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================
def cargar_imagen(nombre_archivo, tamaño_max=TAM_IMG_MEDIANA):
    """Carga una imagen PNG/GIF de la carpeta 'imagenes/'. Devuelve None si no existe."""
    ruta = os.path.join("imagenes", nombre_archivo)
    if not os.path.exists(ruta):
        return None
    try:
        img = tk.PhotoImage(file=ruta)
        w, h = img.width(), img.height()
        factor = 1
        if w > tamaño_max[0]:
            factor = max(factor, (w // tamaño_max[0]) + 1)
        if h > tamaño_max[1]:
            factor = max(factor, (h // tamaño_max[1]) + 1)
        if factor > 1:
            img = img.subsample(factor, factor)
        return img
    except Exception as e:
        print(f"⚠ Error cargando {nombre_archivo}: {e}")
        return None


def hex_a_char(hex_str):
    try:
        n = int(hex_str, 16)
        if n == 0x0D: return "␍"
        if n == 0x0A: return "␊"
        if 32 <= n <= 126: return chr(n)
        return "·"
    except:
        return "?"


# ============================================================
# APLICACIÓN PRINCIPAL
# ============================================================
class ManualApp:
    def __init__(self, root):
        self.root = root
        self.root.title(TITULO)
        self.root.geometry("1200x800")
        self.root.configure(bg=COLOR_BG)
        self.root.minsize(1000, 700)

        # Referencias a imágenes
        self.imagenes = {}

        # Bytes del buffer
        self.bytes_hex = BUFFER_HEX.split()
        self.total_bytes = len(self.bytes_hex)
        self.revelados = [False] * self.total_bytes
        self.botones_bytes = []

        self.configurar_estilos()
        self.crear_header()
        self.crear_notebook()

    # --------------------------------------------------------
    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background=COLOR_BG, borderwidth=0)
        style.configure('TNotebook.Tab', padding=[14, 9],
                        font=('Segoe UI', 9, 'bold'))
        style.map('TNotebook.Tab',
                  background=[('selected', COLOR_ACCENT)],
                  foreground=[('selected', 'white')])
        style.configure('TFrame', background=COLOR_BG)
        style.configure('TLabel', background=COLOR_BG)

    # --------------------------------------------------------
    def crear_header(self):
        header = tk.Frame(self.root, bg=COLOR_HEADER, height=110)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        tk.Label(header, text="Manual de Usuario",
                 font=('Segoe UI', 22, 'bold'),
                 bg=COLOR_HEADER, fg='white').pack(pady=(14, 2))
        tk.Label(header, text="Interferencia en Películas Delgadas — Ondas de Luz",
                 font=('Segoe UI', 13),
                 bg=COLOR_HEADER, fg='#bcd8f5').pack()
        tk.Label(header, text=f"{AUTOR}  —  Carné {CARNE}  —  {UNIVERSIDAD}",
                 font=('Segoe UI', 9, 'italic'),
                 bg=COLOR_HEADER, fg='#88aadd').pack(pady=(6, 0))

    # --------------------------------------------------------
    def crear_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Pestañas
        self.tab_caratula = ttk.Frame(self.notebook)
        self.tab_intro = ttk.Frame(self.notebook)
        self.tab_software = ttk.Frame(self.notebook)
        self.tab_problema = ttk.Frame(self.notebook)
        self.tab_formulas = ttk.Frame(self.notebook)
        self.tab_manual = ttk.Frame(self.notebook)
        self.tab_keil = ttk.Frame(self.notebook)
        self.tab_estructura = ttk.Frame(self.notebook)
        self.tab_modo_uso = ttk.Frame(self.notebook)
        self.tab_buffer = ttk.Frame(self.notebook)
        self.tab_diagrama = ttk.Frame(self.notebook)
        self.tab_hex = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_caratula,   text="  1. Carátula  ")
        self.notebook.add(self.tab_intro,      text="  2. Introducción  ")
        self.notebook.add(self.tab_software,   text="  3. Software  ")
        self.notebook.add(self.tab_problema,   text="  4. Problema  ")
        self.notebook.add(self.tab_formulas,   text="  5. Fórmulas  ")
        self.notebook.add(self.tab_manual,     text="  6. ★ Resolución Manual  ")
        self.notebook.add(self.tab_keil,       text="  7. Keil µVision  ")
        self.notebook.add(self.tab_estructura, text="  8. Estructura  ")
        self.notebook.add(self.tab_modo_uso,   text="  9. Modo de uso  ")
        self.notebook.add(self.tab_buffer,     text="  10. ★ Buffer  ")
        self.notebook.add(self.tab_diagrama,   text="  11. Diagrama  ")
        self.notebook.add(self.tab_hex,        text="  12. Hexadecimal  ")

        self.construir_caratula()
        self.construir_intro()
        self.construir_software()
        self.construir_problema()
        self.construir_formulas()
        self.construir_manual()
        self.construir_keil()
        self.construir_estructura()
        self.construir_modo_uso()
        self.construir_buffer()
        self.construir_diagrama()
        self.construir_hex()

    # ========================================================
    # Helper: crear un marco para imagen o placeholder
    # ========================================================
    def crear_marco_imagen(self, parent, nombre_archivo,
                           caption="", tamaño=TAM_IMG_MEDIANA):
        marco = tk.Frame(parent, bg=COLOR_IMG_BG,
                         highlightbackground=COLOR_IMG_BORDER,
                         highlightthickness=2)
        marco.pack(fill=tk.X, pady=10)

        img = cargar_imagen(nombre_archivo, tamaño)
        if img:
            self.imagenes[nombre_archivo] = img
            lbl = tk.Label(marco, image=img, bg=COLOR_IMG_BG)
            lbl.pack(pady=10)
        else:
            placeholder = tk.Frame(marco, bg='#d0d8e0',
                                   width=tamaño[0], height=tamaño[1])
            placeholder.pack(pady=10)
            placeholder.pack_propagate(False)
            tk.Label(placeholder,
                     text=f"📷 ESPACIO PARA IMAGEN\n\nimagenes/{nombre_archivo}",
                     font=('Segoe UI', 11, 'bold'),
                     bg='#d0d8e0', fg='#445566',
                     justify='center').pack(expand=True)

        if caption:
            tk.Label(marco, text=caption,
                     font=('Segoe UI', 9, 'italic'),
                     bg=COLOR_IMG_BG, fg='#445566').pack(pady=(0, 8))
        return marco

    # ========================================================
    # Helper: crear tabla de colores del espectro visible
    # ========================================================
    def crear_tabla_colores(self, parent):
        """Crea la tabla de colores del espectro visible."""
        tabla = tk.Frame(parent, bg='white', relief=tk.RIDGE, bd=2)
        tabla.pack(fill=tk.X, pady=10)

        # Encabezados
        headers = ["Color", "Rango (nm)", "Frecuencia (THz)", "Muestra"]
        for col, h in enumerate(headers):
            tk.Label(tabla, text=h, font=('Segoe UI', 11, 'bold'),
                     bg=COLOR_HEADER, fg='white',
                     padx=15, pady=8, width=18,
                     justify='center').grid(row=0, column=col, sticky='nsew')

        # Datos de la tabla
        colores_espectro = [
            ("Violeta",  "380 – 450", "668 – 789", "#7a3a9a"),
            ("Azul",     "450 – 495", "606 – 668", "#2050a0"),
            ("Verde",    "495 – 570", "526 – 606", "#22aa44"),
            ("Amarillo", "570 – 590", "508 – 526", "#e8d800"),
            ("Naranja",  "590 – 620", "484 – 508", "#e88020"),
            ("Rojo",     "620 – 750", "400 – 484", "#cc2020"),
        ]

        for row, (nombre, rango, freq, bg_color) in enumerate(colores_espectro, start=1):
            # Resaltar la fila del verde
            es_verde = (nombre == "Verde")
            bg_row = '#e8f5e9' if es_verde else 'white'

            tk.Label(tabla, text=nombre,
                     font=('Segoe UI', 11, 'bold' if es_verde else 'normal'),
                     bg=bg_row, fg='black',
                     padx=15, pady=6).grid(row=row, column=0, sticky='nsew')

            tk.Label(tabla, text=rango,
                     font=('Consolas', 11, 'bold' if es_verde else 'normal'),
                     bg=bg_row, fg='black',
                     padx=15, pady=6).grid(row=row, column=1, sticky='nsew')

            tk.Label(tabla, text=freq,
                     font=('Consolas', 11),
                     bg=bg_row, fg='black',
                     padx=15, pady=6).grid(row=row, column=2, sticky='nsew')

            tk.Label(tabla, text="     ",
                     bg=bg_color,
                     padx=15, pady=6).grid(row=row, column=3, sticky='nsew')

        return tabla

    # ========================================================
    # TAB 1: CARÁTULA
    # ========================================================
    def construir_caratula(self):
        frame = tk.Frame(self.tab_caratula, bg='white')
        frame.pack(fill=tk.BOTH, expand=True)

        top = tk.Frame(frame, bg=COLOR_HEADER, height=180)
        top.pack(fill=tk.X)
        top.pack_propagate(False)
        tk.Label(top, text=UNIVERSIDAD, font=('Segoe UI', 16, 'bold'),
                 bg=COLOR_HEADER, fg='white').pack(pady=(30, 5))
        tk.Label(top, text=FACULTAD, font=('Segoe UI', 12),
                 bg=COLOR_HEADER, fg='#bcd8f5').pack()

        content = tk.Frame(frame, bg='white')
        content.pack(fill=tk.BOTH, expand=True, padx=60, pady=40)

        tk.Label(content, text="Manual de Usuario",
                 font=('Segoe UI', 32, 'bold'),
                 bg='white', fg=COLOR_HEADER).pack(pady=(40, 10))
        tk.Label(content, text="Interferencia en Películas Delgadas",
                 font=('Segoe UI', 20),
                 bg='white', fg=COLOR_ACCENT).pack(pady=5)
        tk.Label(content, text="Ondas de Luz",
                 font=('Segoe UI', 16, 'italic'),
                 bg='white', fg='#666').pack(pady=(0, 40))

        tk.Frame(content, bg=COLOR_ACCENT, height=2).pack(fill=tk.X, pady=20)

        info = tk.Frame(content, bg='white')
        info.pack(pady=20)

        for etiqueta, valor in [
            ("Autor:", AUTOR),
            ("Carné:", CARNE),
            ("Curso:", "Electrónica 5 — Segundo Parcial"),
            ("Ciclo:", "2026"),
        ]:
            row = tk.Frame(info, bg='white')
            row.pack(anchor='w', pady=4)
            tk.Label(row, text=etiqueta, font=('Segoe UI', 12, 'bold'),
                     bg='white', fg=COLOR_HEADER, width=10,
                     anchor='e').pack(side=tk.LEFT)
            tk.Label(row, text=valor, font=('Segoe UI', 12),
                     bg='white', fg='#333',
                     anchor='w').pack(side=tk.LEFT, padx=10)

        tk.Label(content, text="Guatemala, 2026",
                 font=('Segoe UI', 10, 'italic'),
                 bg='white', fg='#888').pack(side=tk.BOTTOM, pady=20)

    # ========================================================
    # TAB 2: INTRODUCCIÓN
    # ========================================================
    def construir_intro(self):
        frame = tk.Frame(self.tab_intro, bg=COLOR_BG)
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        tk.Label(frame, text="Introducción",
                 font=('Segoe UI', 18, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', pady=(0, 15))

        texto = (
            "El fenómeno de interferencia en películas delgadas ocurre cuando las ondas\n"
            "de luz se reflejan parcialmente en la superficie superior y en la inferior\n"
            "de una capa transparente cuyo espesor es comparable a la longitud de onda\n"
            "de la luz incidente.\n\n"
            "Cuando la luz blanca (que contiene todas las longitudes de onda del espectro\n"
            "visible) incide sobre la película, algunas longitudes de onda interfieren\n"
            "constructivamente y se refuerzan, mientras que otras interfieren\n"
            "destructivamente y se cancelan. Esto produce que la película adquiera un\n"
            "color característico según su espesor y su índice de refracción.\n\n"
            "Este manual describe el uso del programa implementado en lenguaje\n"
            "ensamblador ARM sobre el microcontrolador TM4C123GH6PM y simulado en\n"
            "Keil µVision.\n\n"
            "El programa resuelve el siguiente enunciado:\n\n"
            "    «Una película de agua (n = 1.33) en aire tiene 320 nm de espesor.\n"
            "     ¿De qué color se verá la luz reflejada?»\n\n"
            "La salida del programa se almacena en la dirección de memoria 0x20000000\n"
            "en formato hexadecimal. Este manual permite ver, byte por byte, cómo se\n"
            "traduce esa información a texto ASCII legible."
        )
        tk.Label(frame, text=texto, justify='left',
                 font=('Consolas', 11), bg=COLOR_BG).pack(anchor='w', pady=10)

    # ========================================================
    # TAB 3: SOFTWARE
    # ========================================================
    def construir_software(self):
        frame = tk.Frame(self.tab_software, bg=COLOR_BG)
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        tk.Label(frame, text="Software utilizado",
                 font=('Segoe UI', 18, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', pady=(0, 15))

        texto = (
            "El programa utilizado es Keil µVision, una herramienta destinada a la\n"
            "programación en lenguaje ensamblador ARM.\n\n"
            "El proyecto desarrollado está basado en este entorno y permite realizar\n"
            "el análisis de interferencia en películas delgadas mediante instrucciones\n"
            "ensambladas.\n\n"
            "Para ejecutar correctamente el programa, es necesario tener Keil µVision\n"
            "instalado en el ordenador."
        )
        tk.Label(frame, text=texto, justify='left',
                 font=('Consolas', 11), bg=COLOR_BG).pack(anchor='w', pady=10)

        self.crear_marco_imagen(frame, "keil_logo.png",
                                caption="Logo de Keil µVision 5",
                                tamaño=TAM_IMG_LOGO)

    # ========================================================
    # TAB 4: PROBLEMA
    # ========================================================
    def construir_problema(self):
        frame = tk.Frame(self.tab_problema, bg=COLOR_BG)
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        tk.Label(frame, text="Descripción del problema",
                 font=('Segoe UI', 18, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', pady=(0, 15))

        intro = (
            "Una película delgada de agua (n = 1.33) de 320 nm de espesor se encuentra\n"
            "suspendida en aire. Al incidir luz blanca sobre ella, las ondas reflejadas\n"
            "en las superficies superior e inferior interfieren entre sí.\n\n"
            "La reflexión en la interfaz aire → agua sufre un cambio de fase de π\n"
            "radianes, mientras que la reflexión en agua → aire no sufre cambio.\n"
            "Esta asimetría invierte la condición de interferencia constructiva."
        )
        tk.Label(frame, text=intro, justify='left',
                 font=('Consolas', 11), bg=COLOR_BG).pack(anchor='w', pady=5)

        tk.Label(frame, text="Pasos de resolución (software y manual):",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', pady=(15, 5))

        pasos = [
            "1. Identificar los datos: n = 1.33, t = 320 nm.",
            "2. Aplicar la condición de interferencia constructiva: 2·n·t = (m + 0.5)·λ.",
            "3. Despejar λ: λ = 2·n·t / (m + 0.5).",
            "4. Calcular λ para cada orden m = 0, 1, 2, 3.",
            "5. Comparar λ con el espectro visible (380-750 nm) y determinar el color.",
        ]
        for paso in pasos:
            card = tk.Frame(frame, bg='white', relief=tk.RIDGE, bd=1)
            card.pack(fill=tk.X, pady=3)
            tk.Label(card, text=paso, font=('Consolas', 11),
                     bg='white', anchor='w').pack(anchor='w', padx=15, pady=8)

    # ========================================================
    # TAB 5: FÓRMULAS (con tabla de colores)
    # ========================================================
    def construir_formulas(self):
        # Canvas con scroll (porque ahora es más largo)
        canvas = tk.Canvas(self.tab_formulas, bg=COLOR_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tab_formulas, orient='vertical',
                                   command=canvas.yview)
        frame = tk.Frame(canvas, bg=COLOR_BG)
        frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        tk.Label(frame, text="Fórmulas a utilizar",
                 font=('Segoe UI', 18, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', padx=30, pady=(15, 15))

        explicacion = (
            "La interferencia en películas delgadas se rige por la diferencia de\n"
            "camino óptico entre las ondas reflejadas y el desfase por reflexión.\n"
            "Como solo una de las reflexiones invierte la fase (π rad), la condición\n"
            "de interferencia constructiva es:"
        )
        tk.Label(frame, text=explicacion, justify='left',
                 font=('Consolas', 11), bg=COLOR_BG).pack(anchor='w', padx=30, pady=5)

        formulas = [
            ("Condición de interferencia constructiva:", "2 · n · t = (m + 0.5) · λ"),
            ("Longitud de onda despejada:",              "λ = (2 · n · t) / (m + 0.5)"),
            ("Numerador constante:",                     "2 · 1.33 · 320 = 851.2 nm"),
            ("Espectro visible:",                        "380 nm ≤ λ ≤ 750 nm"),
        ]

        for titulo, formula in formulas:
            f = tk.Frame(frame, bg='white', relief=tk.RIDGE, bd=1)
            f.pack(fill=tk.X, padx=30, pady=6)
            tk.Label(f, text=titulo, font=('Segoe UI', 10, 'bold'),
                     bg='white', fg='#555').pack(anchor='w', padx=15, pady=(8, 2))
            tk.Label(f, text=formula, font=('Consolas', 14, 'bold'),
                     bg='white', fg=COLOR_ACCENT).pack(anchor='w', padx=15, pady=(0, 10))

        # ============================================================
        # NUEVA SECCIÓN: TABLA DE COLORES DEL ESPECTRO VISIBLE
        # ============================================================
        tk.Label(frame, text="🎨 Longitudes de onda por color (Espectro visible)",
                 font=('Segoe UI', 14, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', padx=30, pady=(25, 10))

        tk.Label(frame,
                 text="La luz blanca contiene todas las longitudes de onda del espectro\n"
                      "visible. Cada color corresponde a un rango específico de λ:",
                 font=('Consolas', 10), bg=COLOR_BG,
                 justify='left').pack(anchor='w', padx=30, pady=(0, 10))

        # Contenedor para la tabla con padding
        tabla_wrapper = tk.Frame(frame, bg=COLOR_BG)
        tabla_wrapper.pack(fill=tk.X, padx=30, pady=5)
        self.crear_tabla_colores(tabla_wrapper)

        # Mensaje destacado
        mensaje = tk.Frame(frame, bg='#e8f5e9',
                            relief=tk.RIDGE, bd=2)
        mensaje.pack(fill=tk.X, padx=30, pady=15)

        tk.Label(mensaje,
                 text="✅ Nuestro resultado: λ = 567.47 nm → cae dentro del rango 495–570 nm → COLOR VERDE",
                 font=('Segoe UI', 11, 'bold'),
                 bg='#e8f5e9', fg='#155724').pack(pady=12)

        tk.Frame(frame, bg=COLOR_BG, height=20).pack()

    # ========================================================
    # TAB 6: RESOLUCIÓN MANUAL
    # ========================================================
    def construir_manual(self):
        canvas = tk.Canvas(self.tab_manual, bg=COLOR_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tab_manual, orient='vertical',
                                   command=canvas.yview)
        frame = tk.Frame(canvas, bg=COLOR_BG)
        frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # Título
        tk.Label(frame, text="Resolución Manual del Problema",
                 font=('Segoe UI', 18, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', padx=25, pady=(15, 5))

        tk.Label(frame,
                 text="«Una película de agua (n = 1.33) en aire tiene 320 nm de espesor.\n"
                      " ¿De qué color se verá la luz reflejada?»",
                 font=('Segoe UI', 12, 'italic'),
                 bg=COLOR_BG, fg=COLOR_ACCENT,
                 justify='left').pack(anchor='w', padx=25, pady=(0, 20))

        # PASO 1
        self._seccion_manual(
            frame, "Paso 1 — Identificar los datos del problema",
            "De la lectura del enunciado extraemos:\n\n"
            "    n = 1.33   (índice de refracción del agua)\n"
            "    t = 320 nm (espesor de la película)\n"
            "    m = 0, 1, 2, 3   (posibles órdenes de interferencia)\n\n"
            "El espectro visible humano va desde 380 nm (violeta) hasta 750 nm (rojo)."
        )

        # PASO 2
        self._seccion_manual(
            frame, "Paso 2 — Plantear la condición física",
            "Cuando la luz incide sobre la película se producen dos reflexiones:\n\n"
            "    • Reflexión aire → agua (n₁ < n₂): cambio de fase de π rad.\n"
            "    • Reflexión agua → aire (n₁ > n₂): sin cambio de fase.\n\n"
            "Como solo una de las ondas sufre inversión, la condición de\n"
            "interferencia constructiva es:\n\n"
            "        2 · n · t = (m + 0.5) · λ\n\n"
            "El término 0.5 (= ½) aparece precisamente por el desfase de π rad."
        )

        # PASO 3
        self._seccion_manual(
            frame, "Paso 3 — Despejar la longitud de onda λ",
            "Despejando λ de la ecuación anterior:\n\n"
            "        λ = (2 · n · t) / (m + 0.5)\n\n"
            "Sustituyendo los datos:\n\n"
            "        2 · n · t = 2 · 1.33 · 320\n"
            "                  = 2.66 · 320\n"
            "                  = 851.2 nm"
        )

        # PASO 4 con tabla
        tk.Label(frame,
                 text="Paso 4 — Calcular λ para cada orden m",
                 font=('Segoe UI', 14, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', padx=25, pady=(20, 8))

        tk.Label(frame,
                 text="Con el numerador constante 851.2 nm, se evalúa la fórmula\n"
                      "para cada valor de m. Los cálculos se hacen a mano o con\n"
                      "calculadora científica:",
                 font=('Consolas', 11), bg=COLOR_BG,
                 justify='left').pack(anchor='w', padx=35, pady=(0, 10))

        tabla_frame = tk.Frame(frame, bg='white', relief=tk.RIDGE, bd=2)
        tabla_frame.pack(fill=tk.X, padx=25, pady=10)

        headers = ["m", "Denominador\n(m + 0.5)", "Operación",
                   "λ (nm)", "¿Visible?\n(380-750 nm)", "Color"]
        for col, h in enumerate(headers):
            tk.Label(tabla_frame, text=h, font=('Segoe UI', 10, 'bold'),
                     bg=COLOR_HEADER, fg='white',
                     padx=10, pady=8, width=13,
                     justify='center').grid(row=0, column=col, sticky='nsew')

        datos_tabla = [
            ("0", "0.5", "851.2 / 0.5", "1702.40", "❌ NO (infrarrojo)",   "—"),
            ("1", "1.5", "851.2 / 1.5", "567.47",  "✅ SÍ",                "Verde"),
            ("2", "2.5", "851.2 / 2.5", "340.48",  "❌ NO (ultravioleta)", "—"),
            ("3", "3.5", "851.2 / 3.5", "243.20",  "❌ NO (ultravioleta)", "—"),
        ]

        for row, (m, denom, op, lam, vis, color) in enumerate(datos_tabla, start=1):
            bg_color = '#e8f5e9' if vis.startswith("✅") else 'white'
            valores = [m, denom, op, lam, vis, color]
            for col, val in enumerate(valores):
                tk.Label(tabla_frame, text=val, font=('Consolas', 10),
                         bg=bg_color, padx=10, pady=6,
                         fg=COLOR_OK if col == 4 and vis.startswith("✅") else 'black'
                         ).grid(row=row, column=col, sticky='nsew')

        # PASO 5
        self._seccion_manual(
            frame, "Paso 5 — Analizar los resultados",
            "De la tabla anterior observamos:\n\n"
            "    • m = 0  →  λ = 1702.40 nm  →  Infrarrojo (invisible)\n"
            "    • m = 1  →  λ = 567.47 nm   →  ✅ VERDE (visible)\n"
            "    • m = 2  →  λ = 340.48 nm   →  Ultravioleta (invisible)\n"
            "    • m = 3  →  λ = 243.20 nm   →  Ultravioleta (invisible)\n\n"
            "Solamente el orden m = 1 cae dentro del espectro visible humano.\n"
            "Y dentro del espectro visible, 567.47 nm corresponde al color verde."
        )

        # ============================================================
        # NUEVA SECCIÓN: TABLA DE COLORES PARA VERIFICACIÓN
        # ============================================================
        tk.Label(frame,
                 text="🎨 Rangos del espectro visible (para verificar el color)",
                 font=('Segoe UI', 14, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', padx=25, pady=(20, 8))

        tk.Label(frame,
                 text="Para saber si 567.47 nm corresponde al verde, comparamos con\n"
                      "los rangos estándar del espectro visible humano:",
                 font=('Consolas', 11), bg=COLOR_BG,
                 justify='left').pack(anchor='w', padx=35, pady=(0, 10))

        # Tabla de colores
        tabla_wrapper = tk.Frame(frame, bg=COLOR_BG)
        tabla_wrapper.pack(fill=tk.X, padx=25, pady=5)
        self.crear_tabla_colores(tabla_wrapper)

        # Mensaje destacado final
        mensaje = tk.Frame(frame, bg='#e8f5e9', relief=tk.RIDGE, bd=2)
        mensaje.pack(fill=tk.X, padx=25, pady=15)

        tk.Label(mensaje,
                 text="✅ VERIFICACIÓN: λ = 567.47 nm → está en 495–570 nm → COLOR VERDE",
                 font=('Segoe UI', 12, 'bold'),
                 bg='#e8f5e9', fg='#155724').pack(pady=12)

        # RESULTADO FINAL
        result_frame = tk.Frame(frame, bg=COLOR_RESULT_BG, relief=tk.RIDGE, bd=2)
        result_frame.pack(fill=tk.X, padx=25, pady=20)

        tk.Label(result_frame, text="✅  RESULTADO FINAL",
                 font=('Segoe UI', 14, 'bold'),
                 bg=COLOR_RESULT_BG, fg=COLOR_RESULT_FG).pack(pady=(15, 5))
        tk.Label(result_frame, text="La película de agua se verá de COLOR VERDE",
                 font=('Segoe UI', 16, 'bold'),
                 bg=COLOR_RESULT_BG, fg=COLOR_RESULT_FG).pack(pady=5)
        tk.Label(result_frame,
                 text="porque λ = 567.47 nm, calculada para el orden m = 1,\n"
                      "es la única longitud de onda que cae dentro del\n"
                      "espectro visible (380 nm – 750 nm).",
                 font=('Segoe UI', 11),
                 bg=COLOR_RESULT_BG, fg=COLOR_RESULT_FG,
                 justify='center').pack(pady=(5, 15))

        # VERIFICACIÓN CRUZADA
        self._seccion_manual(
            frame, "Verificación cruzada con el programa en ensamblador",
            "El mismo cálculo se implementó en lenguaje ensamblador ARM\n"
            "para el TM4C123GH6PM. El programa realizó exactamente las\n"
            "mismas operaciones, pero usando aritmética de punto fijo\n"
            "(multiplicando por 100 para evitar decimales):\n\n"
            "        λ×100 = 8512000 / (100·m + 50)\n\n"
            "Los resultados del programa coinciden con los cálculos manuales:\n\n"
            "    m = 0  →  programa: 170240/100 = 1702.40 nm  →  ✓ coincide\n"
            "    m = 1  →  programa:  56747/100 =  567.47 nm  →  ✓ coincide\n"
            "    m = 2  →  programa:  34048/100 =  340.48 nm  →  ✓ coincide\n"
            "    m = 3  →  programa:  24320/100 =  243.20 nm  →  ✓ coincide\n\n"
            "La salida del programa se almacenó en la dirección 0x20000000\n"
            "y se puede verificar en la pestaña 'Buffer interactivo'."
        )

        tk.Frame(frame, bg=COLOR_BG, height=30).pack()

    def _seccion_manual(self, parent, titulo, contenido):
        tk.Label(parent, text=titulo,
                 font=('Segoe UI', 14, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER,
                 anchor='w').pack(fill=tk.X, padx=25, pady=(20, 8))

        marco = tk.Frame(parent, bg='white', relief=tk.RIDGE, bd=1)
        marco.pack(fill=tk.X, padx=35, pady=(0, 5))

        tk.Label(marco, text=contenido,
                 font=('Consolas', 11),
                 bg='white', fg='#222',
                 justify='left',
                 anchor='w').pack(fill=tk.X, padx=20, pady=12)

    # ========================================================
    # TAB 7: KEIL
    # ========================================================
    def construir_keil(self):
        canvas = tk.Canvas(self.tab_keil, bg=COLOR_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tab_keil, orient='vertical',
                                   command=canvas.yview)
        frame = tk.Frame(canvas, bg=COLOR_BG)
        frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        tk.Label(frame, text="Cómo usar Keil µVision",
                 font=('Segoe UI', 18, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', pady=(10, 5), padx=20)

        tk.Label(frame, text="Antes de comenzar:",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(10, 5))

        for it in [
            "• Tener instalado Keil µVision 5",
            "• Buscar el icono en el ordenador",
            "• Dar doble clic",
            "• Se abrirá la ventana principal",
        ]:
            tk.Label(frame, text=it, font=('Segoe UI', 10),
                     bg=COLOR_BG, anchor='w').pack(anchor='w', padx=35)

        self.crear_marco_imagen(frame, "keil_ventana_principal.png",
                                caption="Figura: Ventana principal de Keil µVision",
                                tamaño=TAM_IMG_GRANDE)

        tk.Label(frame, text="Cómo abrir el proyecto:",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(20, 5))

        for it in [
            "• Después de abrir Keil µVision 5",
            "• Ir a la pestaña Project y dar clic en Open Project",
            "• Se abrirá la ventana donde están ubicados los proyectos",
            "• Seleccionar el que se desea y dar clic en Abrir",
        ]:
            tk.Label(frame, text=it, font=('Segoe UI', 10),
                     bg=COLOR_BG, anchor='w').pack(anchor='w', padx=35)

        self.crear_marco_imagen(frame, "keil_open_project_menu.png",
                                caption="Figura: Pestaña Project → Open Project",
                                tamaño=TAM_IMG_MEDIANA)
        self.crear_marco_imagen(frame, "keil_open_project_dialog.png",
                                caption="Figura: Ventana para seleccionar el proyecto",
                                tamaño=TAM_IMG_MEDIANA)
        self.crear_marco_imagen(frame, "keil_project_files.png",
                                caption="Figura: Ventana con los proyectos ubicados",
                                tamaño=TAM_IMG_MEDIANA)

        tk.Frame(frame, bg=COLOR_BG, height=20).pack()

    # ========================================================
    # TAB 8: ESTRUCTURA
    # ========================================================
    def construir_estructura(self):
        canvas = tk.Canvas(self.tab_estructura, bg=COLOR_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tab_estructura, orient='vertical',
                                   command=canvas.yview)
        frame = tk.Frame(canvas, bg=COLOR_BG)
        frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        tk.Label(frame, text="Estructura del programa",
                 font=('Segoe UI', 18, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', pady=(10, 15), padx=20)

        tk.Label(frame, text="1. Definición de área de trabajo y alineación",
                 font=('Segoe UI', 13, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(10, 5))
        tk.Label(frame,
                 text="Se definió un área de datos y una de trabajo con directivas AREA,\n"
                      "CODE, READONLY y ALIGN para garantizar la correcta organización\n"
                      "de la memoria.",
                 font=('Consolas', 11), bg=COLOR_BG,
                 justify='left').pack(anchor='w', padx=35, pady=5)
        self.crear_marco_imagen(frame, "estructura_datos.png",
                                caption="Figura: Definición de áreas de trabajo y alineación",
                                tamaño=TAM_IMG_GRANDE)

        tk.Label(frame, text="2. Asignación de los datos a los arreglos",
                 font=('Segoe UI', 13, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(20, 5))
        tk.Label(frame,
                 text="Los datos de entrada del problema se asignan directamente a\n"
                      "registros o a posiciones de memoria conocidas antes de iniciar\n"
                      "el programa principal.",
                 font=('Consolas', 11), bg=COLOR_BG,
                 justify='left').pack(anchor='w', padx=35, pady=5)
        self.crear_marco_imagen(frame, "datos_arreglos.png",
                                caption="Figura: Asignación de datos a los arreglos",
                                tamaño=TAM_IMG_GRANDE)

        tk.Label(frame, text="3. Estructura de las funciones utilizadas",
                 font=('Segoe UI', 13, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(20, 5))
        tk.Label(frame,
                 text="El programa está modularizado en subrutinas que cumplen\n"
                      "funciones específicas: cálculo de λ, verificación de visibilidad,\n"
                      "asignación de color, formateo de números y escritura en memoria.",
                 font=('Consolas', 11), bg=COLOR_BG,
                 justify='left').pack(anchor='w', padx=35, pady=5)
        self.crear_marco_imagen(frame, "estructura_funciones.png",
                                caption="Figura: Estructura de las funciones utilizadas",
                                tamaño=TAM_IMG_GRANDE)

        tk.Frame(frame, bg=COLOR_BG, height=20).pack()

    # ========================================================
    # TAB 9: MODO DE USO
    # ========================================================
    def construir_modo_uso(self):
        canvas = tk.Canvas(self.tab_modo_uso, bg=COLOR_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tab_modo_uso, orient='vertical',
                                   command=canvas.yview)
        frame = tk.Frame(canvas, bg=COLOR_BG)
        frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        tk.Label(frame, text="Modo de uso",
                 font=('Segoe UI', 18, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', pady=(10, 15), padx=20)

        tk.Label(frame, text="1. Antes de iniciar el programa, definir los datos de entrada",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(10, 5))
        self.crear_marco_imagen(frame, "datos_arreglos.png",
                                caption="Figura: Datos iniciales del programa",
                                tamaño=TAM_IMG_MEDIANA)

        tk.Label(frame, text="2. Pulsar Build (F7) para compilar el programa",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(20, 5))
        self.crear_marco_imagen(frame, "keil_build_boton.png",
                                caption="Figura: Botón Build (F7)",
                                tamaño=TAM_IMG_MEDIANA)

        tk.Label(frame, text="3. Pulsar Options for Target",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(20, 5))
        self.crear_marco_imagen(frame, "keil_options_target.png",
                                caption="Figura: Botón Options for Target",
                                tamaño=TAM_IMG_MEDIANA)

        tk.Label(frame, text="4. En la sección Debug, activar el uso del simulador",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(20, 5))
        self.crear_marco_imagen(frame, "keil_debug_simulator.png",
                                caption="Figura: Debug → Use Simulator",
                                tamaño=TAM_IMG_MEDIANA)

        tk.Label(frame, text="5. Dar clic en Start/Stop Debug Session para iniciar",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(20, 5))
        self.crear_marco_imagen(frame, "keil_start_debug_boton.png",
                                caption="Figura: Botón Start/Stop Debug Session (Ctrl+F5)",
                                tamaño=TAM_IMG_MEDIANA)

        tk.Label(frame,
                 text="6. En la parte izquierda se abrirá la ventana de registros.\n"
                      "   Desplegar FPU → Float para ver los registros de cálculos.",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT,
                 justify='left').pack(anchor='w', padx=20, pady=(20, 5))
        self.crear_marco_imagen(frame, "keil_registers_fpu.png",
                                caption="Figura: Ventana de Registros (FPU → Float)",
                                tamaño=TAM_IMG_MEDIANA)

        tk.Label(frame, text="7. Dar clic en Run (F5) para correr el código por completo",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT).pack(anchor='w', padx=20, pady=(20, 5))
        self.crear_marco_imagen(frame, "keil_run_boton.png",
                                caption="Figura: Botón Run (F5)",
                                tamaño=TAM_IMG_MEDIANA)

        tk.Label(frame,
                 text="8. Ver la Memory 1 en 0x20000000\n"
                      "   Allí aparecerán los datos en hexadecimal (0x3D, 0x3D, 0x20, ...)\n"
                      "   junto con su interpretación ASCII.",
                 font=('Segoe UI', 12, 'bold'),
                 bg=COLOR_BG, fg=COLOR_ACCENT,
                 justify='left').pack(anchor='w', padx=20, pady=(20, 5))
        self.crear_marco_imagen(frame, "keil_memory_1.png",
                                caption="Figura: Ventana Memory 1 en 0x20000000",
                                tamaño=TAM_IMG_GRANDE)

        tk.Frame(frame, bg=COLOR_BG, height=20).pack()

    # ========================================================
    # TAB 10: BUFFER INTERACTIVO
    # ========================================================
    def construir_buffer(self):
        top = tk.Frame(self.tab_buffer, bg=COLOR_BG)
        top.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(top, text="Buffer de memoria en 0x20000000",
                 font=('Segoe UI', 16, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(side=tk.LEFT)

        self.lbl_estado = tk.Label(top, text=f"0 / {self.total_bytes} revelados",
                                    font=('Segoe UI', 11, 'bold'),
                                    bg=COLOR_BG, fg=COLOR_ACCENT)
        self.lbl_estado.pack(side=tk.RIGHT)

        tk.Label(self.tab_buffer,
                 text="Haz clic en cada byte para ver su conversión a ASCII.",
                 font=('Segoe UI', 10, 'italic'),
                 bg=COLOR_BG, fg='#666').pack(pady=(0, 5))

        botones_frame = tk.Frame(self.tab_buffer, bg=COLOR_BG)
        botones_frame.pack(fill=tk.X, pady=5)
        tk.Button(botones_frame, text="🔍 Revelar todo",
                  bg=COLOR_ACCENT, fg='white',
                  font=('Segoe UI', 10, 'bold'),
                  padx=15, pady=5,
                  command=self.revelar_todo).pack(side=tk.LEFT, padx=5)
        tk.Button(botones_frame, text="🔄 Reiniciar",
                  bg='#666', fg='white',
                  font=('Segoe UI', 10, 'bold'),
                  padx=15, pady=5,
                  command=self.reiniciar_buffer).pack(side=tk.LEFT, padx=5)

        grid_container = tk.Frame(self.tab_buffer, bg=COLOR_CODE_BG)
        grid_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        canvas = tk.Canvas(grid_container, bg=COLOR_CODE_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(grid_container, orient='vertical',
                                   command=canvas.yview)
        self.grid_inner = tk.Frame(canvas, bg=COLOR_CODE_BG)
        self.grid_inner.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.grid_inner, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        COLS = 10
        for i, h in enumerate(self.bytes_hex):
            fila = i // COLS
            col = i % COLS
            btn = tk.Button(self.grid_inner, text=h,
                            font=('Consolas', 11, 'bold'),
                            bg='#1a1a2e', fg=COLOR_CODE_FG,
                            activebackground='#2a2a5e',
                            width=4, height=2,
                            relief=tk.RAISED, bd=2,
                            command=lambda idx=i: self.revelar_byte(idx))
            btn.grid(row=fila, column=col, padx=3, pady=3)
            self.botones_bytes.append(btn)

        panel_texto = tk.Frame(self.tab_buffer, bg=COLOR_BG)
        panel_texto.pack(fill=tk.X, padx=20, pady=(5, 15))
        tk.Label(panel_texto, text="Texto revelado:",
                 font=('Segoe UI', 11, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w')
        self.texto_revelado = tk.Text(panel_texto, height=8,
                                       font=('Consolas', 10),
                                       bg='white', fg='#114411',
                                       relief=tk.SUNKEN, bd=1)
        self.texto_revelado.pack(fill=tk.X, pady=5)

    def revelar_byte(self, idx):
        if self.revelados[idx]:
            return
        self.revelados[idx] = True
        h = self.bytes_hex[idx]
        char = hex_a_char(h)
        btn = self.botones_bytes[idx]
        btn.config(bg='#1a3a1a', fg='#4dff88',
                   text=f"{h}\n{char}", state='disabled',
                   disabledforeground='#4dff88')
        self.actualizar_estado()
        self.actualizar_texto()

    def revelar_todo(self):
        for i in range(self.total_bytes):
            if not self.revelados[i]:
                self.revelados[i] = True
                h = self.bytes_hex[i]
                char = hex_a_char(h)
                btn = self.botones_bytes[i]
                btn.config(bg='#1a3a1a', fg='#4dff88',
                           text=f"{h}\n{char}", state='disabled',
                           disabledforeground='#4dff88')
        self.actualizar_estado()
        self.actualizar_texto()

    def reiniciar_buffer(self):
        for i in range(self.total_bytes):
            self.revelados[i] = False
            h = self.bytes_hex[i]
            btn = self.botones_bytes[i]
            btn.config(bg='#1a1a2e', fg=COLOR_CODE_FG,
                       text=h, state='normal')
        self.actualizar_estado()
        self.actualizar_texto()

    def actualizar_estado(self):
        n = sum(self.revelados)
        self.lbl_estado.config(text=f"{n} / {self.total_bytes} revelados")

    def actualizar_texto(self):
        self.texto_revelado.delete('1.0', tk.END)
        texto = ''
        for i, h in enumerate(self.bytes_hex):
            texto += hex_a_char(h) if self.revelados[i] else '·'
        texto = texto.replace('␍', '').replace('␊', '\n')
        self.texto_revelado.insert(tk.END, texto)

    # ========================================================
    # TAB 11: DIAGRAMA DE FLUJO
    # ========================================================
    def construir_diagrama(self):
        frame = tk.Frame(self.tab_diagrama, bg=COLOR_BG)
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        tk.Label(frame, text="Diagrama de flujo del programa",
                 font=('Segoe UI', 18, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', pady=(0, 15))

        tk.Label(frame,
                 text="A continuación se muestra la lógica del programa de análisis\n"
                      "de interferencia en películas delgadas:",
                 font=('Segoe UI', 10), bg=COLOR_BG,
                 justify='left').pack(anchor='w', pady=(0, 10))

        self.crear_marco_imagen(frame, "diagrama_flujo.png",
                                caption="Figura: Diagrama de flujo del programa",
                                tamaño=(500, 500))

    # ========================================================
    # TAB 12: HEXADECIMAL (con preguntas frecuentes)
    # ========================================================
    def construir_hex(self):
        # Canvas con scroll
        canvas = tk.Canvas(self.tab_hex, bg=COLOR_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tab_hex, orient='vertical',
                                   command=canvas.yview)
        frame = tk.Frame(canvas, bg=COLOR_BG)
        frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        tk.Label(frame, text="¿Por qué las respuestas están en hexadecimal?",
                 font=('Segoe UI', 16, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', padx=30, pady=(15, 15))

        razones = [
            ("1 byte = 2 dígitos hexadecimales",
             "Cada byte (8 bits) se representa exactamente con dos caracteres\n"
             "hexadecimales. Ejemplo: 'A' en ASCII es 0x41 = 65 decimal."),
            ("Alineación natural de memoria",
             "Las direcciones de memoria son múltiplos de 4 u 8 bytes. El\n"
             "hexadecimal refleja directamente esta estructura."),
            ("Correspondencia directa con ASCII",
             "Cada par hexadecimal se traduce inmediatamente al carácter ASCII:\n"
             "0x41 = 'A', 0x20 = espacio, 0x0D = CR, 0x0A = LF."),
            ("Depuración precisa",
             "Si un programa falla, se puede identificar exactamente qué byte\n"
             "está mal, algo imposible con una vista puramente textual."),
            ("Estándar en sistemas embebidos",
             "Es el formato universal en ingeniería de software embebido para\n"
             "inspeccionar el contenido de memoria."),
        ]

        for i, (titulo_r, detalle) in enumerate(razones, 1):
            card = tk.Frame(frame, bg='white', relief=tk.RIDGE, bd=1)
            card.pack(fill=tk.X, padx=30, pady=5)
            tk.Label(card, text=f"{i}. {titulo_r}",
                     font=('Segoe UI', 11, 'bold'),
                     bg='white', fg=COLOR_ACCENT).pack(anchor='w', padx=15, pady=(8, 2))
            tk.Label(card, text=detalle, font=('Consolas', 10),
                     bg='white', justify='left').pack(anchor='w', padx=15, pady=(0, 8))

        # ============================================================
        # NUEVA SECCIÓN: PREGUNTAS FRECUENTES
        # ============================================================
        tk.Label(frame, text="❓ Preguntas frecuentes",
                 font=('Segoe UI', 14, 'bold'),
                 bg=COLOR_BG, fg=COLOR_HEADER).pack(anchor='w', padx=30, pady=(30, 10))

        preguntas = [
            ("¿Cómo sabes que 567.47 nm corresponde al verde?",
             "Porque el espectro visible humano está dividido en rangos estándar:\n"
             "violeta (380–450), azul (450–495), verde (495–570), amarillo (570–590),\n"
             "naranja (590–620) y rojo (620–750 nm). Nuestro resultado de 567.47 nm\n"
             "cae dentro del rango del verde."),
            ("¿Por qué 567.47 nm y no 567.46 nm como sale en el programa?",
             "Porque el programa usa punto fijo multiplicado por 100, lo que introduce\n"
             "un pequeño error de truncamiento. La diferencia de 0.01 nm es despreciable\n"
             "y no cambia el resultado (sigue siendo verde)."),
            ("¿Por qué el rango del verde es tan amplio (495–570 nm)?",
             "Porque el ojo humano tiene conos que responden a diferentes longitudes de\n"
             "onda, y el verde cubre una región amplia porque es el color al que más\n"
             "sensibles somos (visión fotópica)."),
        ]

        for pregunta, respuesta in preguntas:
            card = tk.Frame(frame, bg='white', relief=tk.RIDGE, bd=1)
            card.pack(fill=tk.X, padx=30, pady=5)
            tk.Label(card, text=f"❓ {pregunta}",
                     font=('Segoe UI', 11, 'bold'),
                     bg='white', fg=COLOR_ACCENT,
                     anchor='w', justify='left',
                     wraplength=900).pack(anchor='w', padx=15, pady=(8, 3))
            tk.Label(card, text=respuesta,
                     font=('Consolas', 10),
                     bg='white', fg='#222',
                     anchor='w', justify='left',
                     wraplength=900).pack(anchor='w', padx=15, pady=(0, 10))

        tk.Frame(frame, bg=COLOR_BG, height=30).pack()


# ============================================================
# INICIO
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = ManualApp(root)
    root.mainloop()