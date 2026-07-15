"""
Generador de presentacion PPTX profesional:
"Fisiopatologia del riesgo trombotico asociado al uso de progestagenos"

5 diapositivas con diseno profesional: ilustraciones medicas, diagramas
vectoriales nativos (triada de Virchow, desequilibrio hemostatico,
comparacion de riesgo) y maquetacion tipo editorial.

Requiere: python-pptx, Pillow  (pip install python-pptx Pillow)
Recursos:  carpeta ./img con las ilustraciones .png
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from PIL import Image

# ---------------------------------------------------------------------------
# Sistema de diseno
# ---------------------------------------------------------------------------
NAVY = RGBColor(0x0A, 0x25, 0x40)      # azul marino profundo
NAVY2 = RGBColor(0x10, 0x38, 0x5E)     # azul marino secundario
AZUL = RGBColor(0x1E, 0x7A, 0xC2)      # azul acento
CIAN = RGBColor(0x2A, 0xB3, 0xB8)      # teal acento
ROJO = RGBColor(0xC0, 0x2A, 0x2A)      # rojo trombo / enfasis
ROJO_CL = RGBColor(0xF4, 0xDA, 0xDA)   # rojo claro fondo
AZUL_CL = RGBColor(0xE3, 0xEE, 0xF7)   # azul claro fondo
GRIS = RGBColor(0x37, 0x41, 0x4B)      # texto cuerpo
GRIS2 = RGBColor(0x6B, 0x76, 0x80)     # texto secundario
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
CREMA = RGBColor(0xF6, 0xF8, 0xFB)     # fondo diapositiva

FUENTE = "Calibri"
FUENTE_TIT = "Calibri"

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "img")

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
ANCHO = prs.slide_width
ALTO = prs.slide_height
BLANK = prs.slide_layouts[6]


# ---------------------------------------------------------------------------
# Utilidades de dibujo
# ---------------------------------------------------------------------------
def fondo(slide, color):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def _sin_sombra(shape):
    shape.shadow.inherit = False


def forma(slide, tipo, x, y, w, h, color, linea=None, linea_w=None):
    shp = slide.shapes.add_shape(tipo, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    if linea is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = linea
        shp.line.width = linea_w or Pt(1)
    _sin_sombra(shp)
    return shp


def rect(slide, x, y, w, h, color):
    return forma(slide, MSO_SHAPE.RECTANGLE, x, y, w, h, color)


def rrect(slide, x, y, w, h, color, linea=None, linea_w=None):
    shp = forma(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, color, linea, linea_w)
    try:
        shp.adjustments[0] = 0.08
    except Exception:
        pass
    return shp


def transparencia(shape, opacidad_pct):
    """Aplica opacidad (0-100) al relleno solido de una forma."""
    try:
        sf = shape.fill._xPr.find(qn('a:solidFill'))
        clr = sf.find(qn('a:srgbClr'))
        a = clr.makeelement(qn('a:alpha'), {'val': str(int(opacidad_pct * 1000))})
        clr.append(a)
    except Exception:
        pass


def texto(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    return tf


def par(tf, txt, size, color, bold=False, italic=False, align=PP_ALIGN.LEFT,
        after=6, before=0, primero=False, font=FUENTE, espaciado=1.0):
    p = tf.paragraphs[0] if primero else tf.add_paragraph()
    p.text = txt
    p.alignment = align
    p.space_after = Pt(after)
    p.space_before = Pt(before)
    try:
        p.line_spacing = espaciado
    except Exception:
        pass
    r = p.runs[0]
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.font.bold = bold
    r.font.italic = italic
    r.font.name = font
    return p


def vineta(tf, txt, size=15, color=GRIS, bold=False, nivel=0, after=7,
           primero=False, marca_color=None):
    p = tf.paragraphs[0] if primero else tf.add_paragraph()
    p.level = nivel
    marca = "▸  " if nivel == 0 else "·  "
    p.space_after = Pt(after)
    p.line_spacing = 1.02
    r0 = p.add_run()
    r0.text = marca
    r0.font.size = Pt(size)
    r0.font.bold = True
    r0.font.name = FUENTE
    r0.font.color.rgb = marca_color or (AZUL if nivel == 0 else CIAN)
    r1 = p.add_run()
    r1.text = txt
    r1.font.size = Pt(size)
    r1.font.bold = bold
    r1.font.name = FUENTE
    r1.font.color.rgb = color
    return p


def imagen_cover(slide, path, x, y, w, h):
    """Inserta imagen recortada tipo object-fit: cover (sin distorsion)."""
    with Image.open(path) as im:
        iw, ih = im.size
    ratio = iw / ih
    target = w / h
    pic = slide.shapes.add_picture(path, x, y, w, h)
    if ratio > target:
        crop = (1 - target / ratio) / 2
        pic.crop_left = crop
        pic.crop_right = crop
    else:
        crop = (1 - ratio / target) / 2
        pic.crop_top = crop
        pic.crop_bottom = crop
    return pic


def encabezado(slide, num, titulo, subtitulo=None):
    rect(slide, 0, 0, ANCHO, Inches(1.25), NAVY)
    rect(slide, 0, Inches(1.25), ANCHO, Inches(0.07), CIAN)
    # chip del numero
    chip = rrect(slide, Inches(0.45), Inches(0.30), Inches(0.66), Inches(0.66), AZUL)
    tf = texto(slide, Inches(0.45), Inches(0.30), Inches(0.66), Inches(0.66),
               MSO_ANCHOR.MIDDLE)
    par(tf, f"{num:02d}", 24, BLANCO, bold=True, align=PP_ALIGN.CENTER,
        after=0, primero=True)
    # titulo
    ty = Inches(0.24) if subtitulo else Inches(0.30)
    tf = texto(slide, Inches(1.3), ty, Inches(11.6), Inches(0.8),
               MSO_ANCHOR.MIDDLE if not subtitulo else MSO_ANCHOR.TOP)
    par(tf, titulo, 25, BLANCO, bold=True, after=0, primero=True, font=FUENTE_TIT)
    if subtitulo:
        tf2 = texto(slide, Inches(1.31), Inches(0.78), Inches(11.6), Inches(0.4))
        par(tf2, subtitulo, 13, RGBColor(0xAE, 0xC5, 0xDC), italic=True,
            after=0, primero=True)


def pie(slide, num):
    tf = texto(slide, Inches(0.45), Inches(7.08), Inches(10.5), Inches(0.35))
    par(tf, "Fisiopatologia del riesgo trombotico asociado a progestagenos",
        9, GRIS2, primero=True, after=0)
    tf = texto(slide, Inches(11.8), Inches(7.08), Inches(1.1), Inches(0.35))
    par(tf, f"{num} / 5", 9, GRIS2, align=PP_ALIGN.RIGHT, primero=True, after=0)


# ===========================================================================
# DIAPOSITIVA 1 - PORTADA
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo(s, NAVY)
imagen_cover(s, os.path.join(IMG, "cover_trombo.png"), 0, 0, ANCHO, ALTO)
# velo degradado (paneles superpuestos con transparencia)
velo = rect(s, 0, 0, ANCHO, ALTO, NAVY)
transparencia(velo, 42)
panel = rect(s, 0, Inches(3.9), ANCHO, Inches(3.6), NAVY)
transparencia(panel, 30)
# banda lateral e hilo rojo
rect(s, 0, 0, Inches(0.28), ALTO, CIAN)
rect(s, Inches(0.9), Inches(4.35), Inches(2.6), Inches(0.09), ROJO)

tf = texto(s, Inches(0.9), Inches(2.15), Inches(11.5), Inches(2.2))
par(tf, "FISIOPATOLOGIA", 20, CIAN, bold=True, after=2, primero=True)
par(tf, "Riesgo trombotico asociado", 46, BLANCO, bold=True, after=0,
    font=FUENTE_TIT)
par(tf, "al uso de progestagenos", 46, BLANCO, bold=True, after=0,
    font=FUENTE_TIT)

tf = texto(s, Inches(0.92), Inches(4.6), Inches(10.8), Inches(1.6))
par(tf, "Del equilibrio hemostatico normal a la alteracion inducida por los "
        "gestagenos", 18, RGBColor(0xD5, 0xE2, 0xEF), italic=True, after=10,
    primero=True)
par(tf, "Presentacion academica  ·  Hematologia y farmacologia clinica  ·  "
        "5 diapositivas", 13, RGBColor(0xA9, 0xBD, 0xD2), after=0)

# ===========================================================================
# DIAPOSITIVA 2 - BASE FISIOLOGICA + TRIADA DE VIRCHOW
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo(s, CREMA)
encabezado(s, 1, "Base fisiologica: el equilibrio hemostatico",
           "Como se rompe el balance y aparece el trombo")

# frase clave
kb = rrect(s, Inches(0.45), Inches(1.5), Inches(7.35), Inches(0.85), AZUL_CL)
tf = texto(s, Inches(0.7), Inches(1.5), Inches(6.9), Inches(0.85), MSO_ANCHOR.MIDDLE)
par(tf, "La trombosis surge cuando se rompe el balance entre los sistemas "
        "procoagulante, anticoagulante y fibrinolitico.",
    14.5, NAVY, bold=True, primero=True, after=0, espaciado=1.0)

# lista izquierda
tf = texto(s, Inches(0.5), Inches(2.55), Inches(7.3), Inches(4.3))
vineta(tf, "Hemostasia normal: equilibrio dinamico entre formacion y "
           "disolucion del coagulo.", 14.5, GRIS, bold=True, primero=True)
vineta(tf, "Procoagulantes: II, VII, IX, X, fibrinogeno, factor VIII, von Willebrand.",
       13.5, GRIS, nivel=1)
vineta(tf, "Anticoagulantes naturales: antitrombina, proteina C y S, TFPI.",
       13.5, GRIS, nivel=1)
vineta(tf, "Fibrinolisis: plasmina y t-PA frente al inhibidor PAI-1.",
       13.5, GRIS, nivel=1)
vineta(tf, "Triada de Virchow: los tres determinantes del trombo.",
       14.5, GRIS, bold=True)
vineta(tf, "Estasis venosa · lesion endotelial · hipercoagulabilidad.",
       13.5, GRIS, nivel=1)
vineta(tf, "Las hormonas sexuales modulan la sintesis hepatica de factores: "
           "aqui actuan los progestagenos.", 14, NAVY, bold=True,
       marca_color=ROJO)

# imagen derecha
imagen_cover(s, os.path.join(IMG, "vaso_coagulacion.png"),
             Inches(8.05), Inches(1.5), Inches(4.85), Inches(2.55))
rect(s, Inches(8.05), Inches(4.02), Inches(4.85), Inches(0.05), CIAN)
tf = texto(s, Inches(8.05), Inches(4.08), Inches(4.85), Inches(0.35))
par(tf, "Formacion del coagulo en la pared vascular", 10.5, GRIS2,
    italic=True, align=PP_ALIGN.CENTER, primero=True, after=0)

# --- Diagrama triada de Virchow (triangulo con 3 nodos) ---
cx, cy = Inches(10.47), Inches(5.75)   # centro
R = Inches(0.95)
nodo_w, nodo_h = Inches(1.9), Inches(0.62)
# nodo central
c = forma(s, MSO_SHAPE.OVAL, cx - Inches(0.78), cy - Inches(0.40),
          Inches(1.56), Inches(0.80), ROJO)
tf = c.text_frame; tf.word_wrap = False
par(tf, "TROMBO", 12, BLANCO, bold=True, align=PP_ALIGN.CENTER, primero=True, after=0)
# tres nodos
nodos = [
    ("Estasis", CIAN, cx - nodo_w/2, cy - R - Inches(0.15)),
    ("Lesion endotelial", AZUL, cx - nodo_w - Inches(0.05), cy + Inches(0.5)),
    ("Hipercoagulabilidad", NAVY2, cx + Inches(0.05), cy + Inches(0.5)),
]
for txt_n, col, nx, ny in nodos:
    n = rrect(s, nx, ny, nodo_w, nodo_h, col)
    tf = n.text_frame; tf.word_wrap = True
    par(tf, txt_n, 10.5, BLANCO, bold=True, align=PP_ALIGN.CENTER,
        primero=True, after=0)
pie(s, 2)

# ===========================================================================
# DIAPOSITIVA 3 - MECANISMOS MOLECULARES + DESEQUILIBRIO
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo(s, CREMA)
encabezado(s, 2, "Mecanismos protromboticos de los progestagenos",
           "Que cambia en la sangre y por que")

# imagen izquierda
imagen_cover(s, os.path.join(IMG, "higado_hormonas.png"),
             Inches(0.45), Inches(1.55), Inches(4.5), Inches(2.75))
rect(s, Inches(0.45), Inches(4.27), Inches(4.5), Inches(0.05), CIAN)
tf = texto(s, Inches(0.45), Inches(4.33), Inches(4.5), Inches(0.35))
par(tf, "Sintesis hepatica modulada por gestagenos", 10.5, GRIS2,
    italic=True, align=PP_ALIGN.CENTER, primero=True, after=0)

# diagrama desequilibrio (dos paneles + chip RPCa)
py = Inches(4.95)
izq = rrect(s, Inches(0.45), py, Inches(2.15), Inches(1.55), ROJO_CL)
tf = texto(s, Inches(0.5), py + Inches(0.08), Inches(2.05), Inches(1.4),
           MSO_ANCHOR.MIDDLE)
par(tf, "PROCOAGULANTES", 11, ROJO, bold=True, align=PP_ALIGN.CENTER,
    primero=True, after=2)
par(tf, "II · VII · VIII · X · fibrinogeno", 10.5, GRIS, align=PP_ALIGN.CENTER, after=2)
par(tf, "AUMENTAN", 11, ROJO, bold=True, align=PP_ALIGN.CENTER, after=0)
der = rrect(s, Inches(2.8), py, Inches(2.15), Inches(1.55), AZUL_CL)
tf = texto(s, Inches(2.85), py + Inches(0.08), Inches(2.05), Inches(1.4),
           MSO_ANCHOR.MIDDLE)
par(tf, "ANTICOAGULANTES", 11, NAVY, bold=True, align=PP_ALIGN.CENTER,
    primero=True, after=2)
par(tf, "antitrombina · proteina S", 10.5, GRIS, align=PP_ALIGN.CENTER, after=2)
par(tf, "DISMINUYEN", 11, NAVY, bold=True, align=PP_ALIGN.CENTER, after=0)

# lista derecha
tf = texto(s, Inches(5.25), Inches(1.55), Inches(7.6), Inches(5.3))
vineta(tf, "Resistencia adquirida a la proteina C activada (RPCa):",
       15, ROJO, bold=True, primero=True, marca_color=ROJO)
vineta(tf, "Mecanismo central; la sangre responde menos al principal freno "
           "anticoagulante fisiologico.", 13.5, GRIS, nivel=1)
vineta(tf, "Cambios en los factores de la coagulacion:", 15, NAVY, bold=True)
vineta(tf, "Aumento de procoagulantes y descenso de anticoagulantes naturales.",
       13.5, GRIS, nivel=1)
vineta(tf, "Alteracion de la fibrinolisis: mayor tendencia neta a formar y "
           "estabilizar el coagulo.", 13.5, GRIS, nivel=1)
vineta(tf, "Efecto segun potencia androgenica/glucocorticoide del gestageno:",
       15, NAVY, bold=True)
vineta(tf, "Modulan receptores de progesterona, androgenicos y de "
           "glucocorticoides en higado y endotelio.", 13.5, GRIS, nivel=1)
vineta(tf, "Sinergia con estrogenos (anticonceptivos combinados):", 15, ROJO,
       bold=True, marca_color=ROJO)
vineta(tf, "El estrogeno impulsa la sintesis hepatica de factores; ciertos "
           "gestagenos amplifican la RPCa y el riesgo global.", 13.5, GRIS, nivel=1)
pie(s, 3)

# ===========================================================================
# DIAPOSITIVA 4 - RIESGO DIFERENCIAL (DIAGRAMA DE BARRAS CUALITATIVO)
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo(s, CREMA)
encabezado(s, 3, "Riesgo diferencial: tipo de gestageno y via",
           "No todos los progestagenos conllevan el mismo riesgo")

# lista izquierda
tf = texto(s, Inches(0.5), Inches(1.55), Inches(6.3), Inches(5.3))
vineta(tf, "El riesgo depende del gestageno concreto:", 14.5, NAVY, bold=True,
       primero=True)
vineta(tf, "Mayor con etinilestradiol: desogestrel, gestodeno, drospirenona, "
           "ciproterona (3a-4a gen.).", 13, GRIS, nivel=1, marca_color=ROJO)
vineta(tf, "Menor relativo: levonorgestrel, norgestimato (2a gen.).",
       13, GRIS, nivel=1)
vineta(tf, "Progestageno solo (sin estrogeno):", 14.5, NAVY, bold=True)
vineta(tf, "Pildora de solo gestageno, implante y DIU-LNG: riesgo muy bajo o "
           "no significativo.", 13, GRIS, nivel=1)
vineta(tf, "Excepcion: medroxiprogesterona inyectable (senal de riesgo).",
       13, GRIS, nivel=1, marca_color=ROJO)
vineta(tf, "Via de administracion:", 14.5, NAVY, bold=True)
vineta(tf, "La via oral sufre primer paso hepatico y mayor impacto sobre la "
           "coagulacion.", 13, GRIS, nivel=1)
vineta(tf, "El riesgo absoluto individual es bajo, pero se multiplica con "
           "cofactores.", 13.5, NAVY, bold=True, marca_color=ROJO)

# --- diagrama de barras cualitativo (riesgo relativo) ---
gx = Inches(7.0)
gw = Inches(5.85)
titulo_g = rrect(s, gx, Inches(1.55), gw, Inches(0.5), NAVY)
tf = texto(s, gx, Inches(1.55), gw, Inches(0.5), MSO_ANCHOR.MIDDLE)
par(tf, "Riesgo trombotico relativo (esquematico)", 12.5, BLANCO, bold=True,
    align=PP_ALIGN.CENTER, primero=True, after=0)

barras = [
    ("Solo gestageno / DIU-LNG", 0.20, CIAN, "Muy bajo"),
    ("Levonorgestrel (2a gen.)", 0.48, AZUL, "Bajo-moderado"),
    ("Deso/gesto/drospirenona (3-4a)", 0.85, ROJO, "Mayor"),
]
by = Inches(2.35)
bh = Inches(0.5)
sep = Inches(1.18)
maxw = Inches(4.0)
for etiqueta, frac, col, nivel_txt in barras:
    tf = texto(s, gx, by, gw, Inches(0.32))
    par(tf, etiqueta, 12, GRIS, bold=True, primero=True, after=0)
    # riel
    rrect(s, gx, by + Inches(0.34), maxw, bh, RGBColor(0xE5, 0xEA, 0xEF))
    # barra
    b = rrect(s, gx, by + Inches(0.34), Emu_frac := int(maxw * frac), bh, col)
    # valor
    tf = texto(s, gx + maxw + Inches(0.12), by + Inches(0.34),
               Inches(1.7), bh, MSO_ANCHOR.MIDDLE)
    par(tf, nivel_txt, 11.5, col, bold=True, primero=True, after=0)
    by = by + sep

# nota
nb = rrect(s, gx, Inches(6.05), gw, Inches(0.62), AZUL_CL)
tf = texto(s, gx + Inches(0.15), Inches(6.05), gw - Inches(0.3), Inches(0.62),
           MSO_ANCHOR.MIDDLE)
par(tf, "Esquema cualitativo con fines docentes; las magnitudes no representan "
        "valores numericos exactos.", 10, GRIS2, italic=True, primero=True, after=0)
pie(s, 4)

# ===========================================================================
# DIAPOSITIVA 5 - COFACTORES E IMPLICACIONES CLINICAS
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo(s, CREMA)
encabezado(s, 4, "Cofactores e implicaciones clinicas",
           "Estratificar el riesgo y prescribir con criterio")

# tarjeta izquierda: factores
c1 = rrect(s, Inches(0.45), Inches(1.55), Inches(4.05), Inches(4.75), BLANCO,
           linea=RGBColor(0xE0, 0xE6, 0xEC), linea_w=Pt(1))
rect(s, Inches(0.45), Inches(1.55), Inches(4.05), Inches(0.62), ROJO)
tf = texto(s, Inches(0.6), Inches(1.55), Inches(3.8), Inches(0.62), MSO_ANCHOR.MIDDLE)
par(tf, "Factores que potencian", 14.5, BLANCO, bold=True, primero=True, after=0)
tf = texto(s, Inches(0.65), Inches(2.35), Inches(3.7), Inches(3.85))
vineta(tf, "Trombofilias hereditarias (factor V Leiden, protrombina G20210A).",
       12.5, GRIS, primero=True, marca_color=ROJO)
vineta(tf, "Tabaquismo y edad mayor de 35 anos.", 12.5, GRIS, marca_color=ROJO)
vineta(tf, "Obesidad (IMC elevado).", 12.5, GRIS, marca_color=ROJO)
vineta(tf, "Inmovilizacion, cirugia, puerperio.", 12.5, GRIS, marca_color=ROJO)
vineta(tf, "Antecedente personal o familiar de tromboembolismo.", 12.5, GRIS,
       marca_color=ROJO)

# tarjeta central: implicaciones
c2 = rrect(s, Inches(4.7), Inches(1.55), Inches(4.05), Inches(4.75), BLANCO,
           linea=RGBColor(0xE0, 0xE6, 0xEC), linea_w=Pt(1))
rect(s, Inches(4.7), Inches(1.55), Inches(4.05), Inches(0.62), AZUL)
tf = texto(s, Inches(4.85), Inches(1.55), Inches(3.8), Inches(0.62), MSO_ANCHOR.MIDDLE)
par(tf, "Implicaciones clinicas", 14.5, BLANCO, bold=True, primero=True, after=0)
tf = texto(s, Inches(4.9), Inches(2.35), Inches(3.7), Inches(3.85))
vineta(tf, "Anamnesis y estratificacion del riesgo antes de prescribir.",
       12.5, GRIS, primero=True)
vineta(tf, "Preferir gestagenos de menor riesgo o metodos de solo gestageno "
           "en pacientes de riesgo.", 12.5, GRIS)
vineta(tf, "Educar sobre signos de TVP y tromboembolismo pulmonar.", 12.5, GRIS)
vineta(tf, "El mayor riesgo es en los primeros meses de uso.", 12.5, GRIS)
vineta(tf, "Balance individualizado beneficio-riesgo.", 12.5, GRIS)

# imagen derecha
imagen_cover(s, os.path.join(IMG, "consulta_clinica.png"),
             Inches(8.95), Inches(1.55), Inches(3.95), Inches(3.35))
rect(s, Inches(8.95), Inches(4.87), Inches(3.95), Inches(0.05), CIAN)
tf = texto(s, Inches(8.95), Inches(4.95), Inches(3.95), Inches(0.7))
par(tf, "Valoracion individualizada del riesgo antes de indicar el metodo.",
    11, GRIS2, italic=True, align=PP_ALIGN.CENTER, primero=True, after=0)

# banda conclusion
rect(s, Inches(0.45), Inches(6.5), Inches(12.45), Inches(0.5), NAVY)
rect(s, Inches(0.45), Inches(6.5), Inches(0.12), Inches(0.5), CIAN)
tf = texto(s, Inches(0.72), Inches(6.5), Inches(12.1), Inches(0.5), MSO_ANCHOR.MIDDLE)
par(tf, "Conclusion: los progestagenos alteran la hemostasia (RPCa y factores "
        "de coagulacion); el riesgo depende del tipo, la via y los cofactores del paciente.",
    12.5, BLANCO, bold=True, primero=True, after=0)
pie(s, 5)

# ---------------------------------------------------------------------------
SALIDA = os.path.join(BASE, "Fisiopatologia_riesgo_trombotico_progestagenos.pptx")
prs.save(SALIDA)
print("Presentacion generada:", SALIDA)
print("Total de diapositivas:", len(prs.slides._sldIdLst))
