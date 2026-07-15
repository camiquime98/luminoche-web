"""
Generador de presentacion PPTX:
"Fisiopatologia del riesgo trombotico asociado al uso de progestagenos"

Genera un archivo .pptx de 5 diapositivas con contenido medico estructurado.
Requiere: python-pptx  (pip install python-pptx)
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# ---------------------------------------------------------------------------
# Paleta de colores
# ---------------------------------------------------------------------------
AZUL_OSCURO = RGBColor(0x0B, 0x2E, 0x4F)   # fondo / titulos
AZUL_MEDIO = RGBColor(0x1F, 0x6F, 0xB2)    # acentos
ROJO_SANGRE = RGBColor(0xB3, 0x1B, 0x1B)   # enfasis trombosis
GRIS_TEXTO = RGBColor(0x33, 0x33, 0x33)    # cuerpo de texto
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
GRIS_CLARO = RGBColor(0xF2, 0xF5, 0xF8)

# Dimensiones diapositiva 16:9
ANCHO = Inches(13.333)
ALTO = Inches(7.5)

prs = Presentation()
prs.slide_width = ANCHO
prs.slide_height = ALTO

BLANK = prs.slide_layouts[6]  # layout en blanco


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def fondo(slide, color):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color


def rect(slide, x, y, w, h, color):
    from pptx.enum.shapes import MSO_SHAPE
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    shp.shadow.inherit = False
    return shp


def caja_texto(slide, x, y, w, h):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    return tb, tf


def set_par(p, texto, size, color, bold=False, align=PP_ALIGN.LEFT,
            space_after=6, italic=False):
    p.text = texto
    p.alignment = align
    p.space_after = Pt(space_after)
    r = p.runs[0]
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.font.bold = bold
    r.font.italic = italic
    r.font.name = "Calibri"
    return p


def bullet(tf, texto, size=18, color=GRIS_TEXTO, bold=False, nivel=0,
           space_after=8, first=False):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.level = nivel
    prefijo = "•  " if nivel == 0 else "–  "
    p.text = prefijo + texto
    p.space_after = Pt(space_after)
    r = p.runs[0]
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.font.bold = bold
    r.font.name = "Calibri"
    return p


def encabezado(slide, numero, titulo):
    """Barra superior con numero y titulo de la diapositiva."""
    rect(slide, 0, 0, ANCHO, Inches(1.15), AZUL_OSCURO)
    rect(slide, 0, Inches(1.15), ANCHO, Inches(0.08), AZUL_MEDIO)
    # numero
    tb, tf = caja_texto(slide, Inches(0.35), Inches(0.18), Inches(0.9), Inches(0.8))
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_par(tf.paragraphs[0], str(numero), 40, AZUL_MEDIO, bold=True,
            align=PP_ALIGN.CENTER, space_after=0)
    # titulo
    tb, tf = caja_texto(slide, Inches(1.3), Inches(0.15), Inches(11.5), Inches(0.9))
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    set_par(tf.paragraphs[0], titulo, 26, BLANCO, bold=True, space_after=0)


def pie(slide, texto="Fisiopatologia del riesgo trombotico por progestagenos"):
    tb, tf = caja_texto(slide, Inches(0.35), Inches(7.05), Inches(12.6), Inches(0.4))
    set_par(tf.paragraphs[0], texto, 10, RGBColor(0x9A, 0xA5, 0xB1),
            align=PP_ALIGN.LEFT, space_after=0)


# ===========================================================================
# DIAPOSITIVA 1 - PORTADA
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo(s, AZUL_OSCURO)

# Banda de acento lateral
rect(s, 0, 0, Inches(0.35), ALTO, AZUL_MEDIO)
rect(s, 0, Inches(4.55), ANCHO, Inches(0.06), ROJO_SANGRE)

tb, tf = caja_texto(s, Inches(1.0), Inches(1.6), Inches(11.3), Inches(2.6))
set_par(tf.paragraphs[0], "Fisiopatologia del riesgo trombotico",
        44, BLANCO, bold=True, space_after=4)
p = tf.add_paragraph()
set_par(p, "asociado al uso de progestagenos", 44, AZUL_MEDIO, bold=True,
        space_after=0)

tb, tf = caja_texto(s, Inches(1.0), Inches(4.75), Inches(11.3), Inches(1.6))
set_par(tf.paragraphs[0],
        "Mecanismos de la hemostasia y su alteracion por los gestagenos",
        20, RGBColor(0xC9, 0xD6, 0xE3), italic=True, space_after=14)
p = tf.add_paragraph()
set_par(p, "Presentacion academica  ·  5 diapositivas", 15,
        RGBColor(0x9A, 0xA5, 0xB1), space_after=0)

# ===========================================================================
# DIAPOSITIVA 2 - HEMOSTASIA NORMAL (BASE FISIOLOGICA)
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo(s, GRIS_CLARO)
encabezado(s, 1, "Base fisiologica: el equilibrio hemostatico")

tb, tf = caja_texto(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(0.9))
set_par(tf.paragraphs[0],
        "La trombosis surge cuando se rompe el balance entre los sistemas "
        "procoagulante, anticoagulante y fibrinolitico (triada de Virchow).",
        18, AZUL_OSCURO, bold=True, space_after=0)

tb, tf = caja_texto(s, Inches(0.6), Inches(2.5), Inches(12.0), Inches(4.3))
bullet(tf, "Hemostasia normal: equilibrio dinamico entre formacion y "
           "disolucion del coagulo.", 18, GRIS_TEXTO, bold=True, first=True)
bullet(tf, "Factores procoagulantes: II, VII, IX, X, fibrinogeno, factor VIII, "
           "von Willebrand.", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Anticoagulantes naturales: antitrombina, proteina C, proteina S, "
           "inhibidor de la via del factor tisular (TFPI).", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Fibrinolisis: plasmina, activador tisular del plasminogeno (t-PA) "
           "frente al inhibidor PAI-1.", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Triada de Virchow: determinantes del trombo.", 18, GRIS_TEXTO, bold=True)
bullet(tf, "Estasis del flujo sanguineo (venoso).", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Lesion/disfuncion del endotelio vascular.", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Hipercoagulabilidad de la sangre (estado protrombotico).", 16,
       ROJO_SANGRE, bold=True, nivel=1)
bullet(tf, "Las hormonas sexuales modulan la sintesis hepatica de multiples "
           "factores: aqui actuan los progestagenos.", 17, AZUL_MEDIO, bold=True)
pie(s)

# ===========================================================================
# DIAPOSITIVA 3 - MECANISMOS MOLECULARES DE LOS PROGESTAGENOS
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo(s, GRIS_CLARO)
encabezado(s, 2, "Mecanismos protromboticos de los progestagenos")

tb, tf = caja_texto(s, Inches(0.6), Inches(1.45), Inches(12.0), Inches(5.4))
bullet(tf, "Resistencia adquirida a la proteina C activada (RPCa):",
       18, ROJO_SANGRE, bold=True, first=True)
bullet(tf, "Es el mecanismo central; la sangre responde menos al principal "
           "freno anticoagulante fisiologico.", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Cambios en factores de la coagulacion:", 18, AZUL_OSCURO, bold=True)
bullet(tf, "Aumento de factores procoagulantes (II, VII, VIII, X, fibrinogeno).",
       16, GRIS_TEXTO, nivel=1)
bullet(tf, "Descenso de anticoagulantes naturales (antitrombina, proteina S).",
       16, GRIS_TEXTO, nivel=1)
bullet(tf, "Alteracion de la fibrinolisis: aumento neto de la tendencia a "
           "formar y estabilizar el coagulo.", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Efecto dependiente del tipo y potencia androgenica/glucocorticoide "
           "del progestageno.", 18, AZUL_OSCURO, bold=True)
bullet(tf, "Los gestagenos modulan receptores de progesterona, androgenicos y "
           "de glucocorticoides en higado y endotelio.", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Sinergia con estrogenos (anticonceptivos combinados):", 18,
       ROJO_SANGRE, bold=True)
bullet(tf, "El estrogeno impulsa la sintesis hepatica de factores; ciertos "
           "progestagenos amplifican la RPCa y el riesgo global.", 16,
       GRIS_TEXTO, nivel=1)
pie(s)

# ===========================================================================
# DIAPOSITIVA 4 - RIESGO DIFERENCIAL SEGUN TIPO Y VIA
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo(s, GRIS_CLARO)
encabezado(s, 3, "Riesgo diferencial: tipo de gestageno y via")

tb, tf = caja_texto(s, Inches(0.6), Inches(1.45), Inches(12.0), Inches(5.4))
bullet(tf, "No todos los progestagenos tienen el mismo riesgo trombotico:",
       18, AZUL_OSCURO, bold=True, first=True)
bullet(tf, "Mayor riesgo (con etinilestradiol): desogestrel, gestodeno, "
           "drospirenona, acetato de ciproterona (3a-4a generacion).",
       16, ROJO_SANGRE, nivel=1)
bullet(tf, "Menor riesgo relativo: levonorgestrel, norgestimato (2a "
           "generacion), por menor induccion de RPCa.", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Progestageno solo (sin estrogeno):", 18, AZUL_OSCURO, bold=True)
bullet(tf, "Pildora de solo gestageno, implante y DIU-levonorgestrel: riesgo "
           "trombotico muy bajo o no significativo.", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Excepcion: acetato de medroxiprogesterona inyectable, con senal "
           "de riesgo aumentado.", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Importancia de la via de administracion:", 18, AZUL_OSCURO, bold=True)
bullet(tf, "La via oral sufre primer paso hepatico y mayor impacto sobre "
           "factores de coagulacion.", 16, GRIS_TEXTO, nivel=1)
bullet(tf, "Vias no orales pueden atenuar el efecto protrombotico hepatico.",
       16, GRIS_TEXTO, nivel=1)
bullet(tf, "El riesgo absoluto individual es bajo, pero se multiplica con "
           "factores asociados.", 17, AZUL_MEDIO, bold=True)
pie(s)

# ===========================================================================
# DIAPOSITIVA 5 - FACTORES DE RIESGO E IMPLICACIONES CLINICAS
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo(s, GRIS_CLARO)
encabezado(s, 4, "Cofactores e implicaciones clinicas")

# Dos columnas
# Columna izquierda: factores que potencian
rect(s, Inches(0.5), Inches(1.5), Inches(6.0), Inches(4.9), BLANCO)
tb, tf = caja_texto(s, Inches(0.75), Inches(1.65), Inches(5.5), Inches(4.6))
set_par(tf.paragraphs[0], "Factores que potencian el riesgo", 18,
        ROJO_SANGRE, bold=True, space_after=8)
bullet(tf, "Trombofilias hereditarias (factor V Leiden, mutacion protrombina).",
       15, GRIS_TEXTO)
bullet(tf, "Tabaquismo y edad > 35 anos.", 15, GRIS_TEXTO)
bullet(tf, "Obesidad (IMC elevado).", 15, GRIS_TEXTO)
bullet(tf, "Inmovilizacion, cirugia, puerperio.", 15, GRIS_TEXTO)
bullet(tf, "Antecedente personal o familiar de tromboembolismo.", 15, GRIS_TEXTO)

# Columna derecha: implicaciones clinicas
rect(s, Inches(6.85), Inches(1.5), Inches(6.0), Inches(4.9), BLANCO)
tb, tf = caja_texto(s, Inches(7.1), Inches(1.65), Inches(5.5), Inches(4.6))
set_par(tf.paragraphs[0], "Implicaciones clinicas", 18, AZUL_MEDIO,
        bold=True, space_after=8)
bullet(tf, "Anamnesis y estratificacion del riesgo antes de prescribir.",
       15, GRIS_TEXTO)
bullet(tf, "Preferir gestagenos de menor riesgo o metodos de solo gestageno "
           "en pacientes de riesgo.", 15, GRIS_TEXTO)
bullet(tf, "Educar sobre signos de TVP y tromboembolismo pulmonar.", 15,
       GRIS_TEXTO)
bullet(tf, "El mayor riesgo es en los primeros meses de uso.", 15, GRIS_TEXTO)
bullet(tf, "Balance individualizado beneficio-riesgo.", 15, GRIS_TEXTO)

# Mensaje de cierre
rect(s, Inches(0.5), Inches(6.55), Inches(12.35), Inches(0.62), AZUL_OSCURO)
tb, tf = caja_texto(s, Inches(0.7), Inches(6.6), Inches(12.0), Inches(0.55))
tf.vertical_anchor = MSO_ANCHOR.MIDDLE
set_par(tf.paragraphs[0],
        "Conclusion: los progestagenos alteran la hemostasia (RPCa y factores "
        "de coagulacion); el riesgo depende del tipo, la via y los cofactores del paciente.",
        14, BLANCO, bold=True, space_after=0)

# ---------------------------------------------------------------------------
prs.save("Fisiopatologia_riesgo_trombotico_progestagenos.pptx")
print("Presentacion generada: Fisiopatologia_riesgo_trombotico_progestagenos.pptx")
print("Total de diapositivas:", len(prs.slides._sldIdLst))
