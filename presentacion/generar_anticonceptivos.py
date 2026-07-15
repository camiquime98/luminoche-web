"""
Presentacion PPTX: recomendaciones de INICIO/ADMINISTRACION de anticonceptivos
de solo progestageno.

Fondo blanco, letra negra. Contenido resumido de las
U.S. Selected Practice Recommendations for Contraceptive Use, 2024 (CDC),
MMWR 2024;73(RR-3). Fuente:
https://www.cdc.gov/mmwr/volumes/73/rr/rr7303a1.htm

Metodos (una diapositiva por metodo):
  1) DIU de levonorgestrel (LNG-IUD)
  2) Implante subdermico (etonogestrel)
  3) Inyeccion trimestral (DMPA)
  4) Pildoras de solo progestageno (POP)

Requiere: python-pptx  (pip install python-pptx)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

NEGRO = RGBColor(0x00, 0x00, 0x00)
GRIS = RGBColor(0x44, 0x44, 0x44)
GRIS_CL = RGBColor(0x88, 0x88, 0x88)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
FUENTE = "Calibri"

BASE = os.path.dirname(os.path.abspath(__file__))
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
ANCHO = prs.slide_width
BLANK = prs.slide_layouts[6]


def fondo_blanco(slide):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = BLANCO


def linea(slide, x, y, w, h=Pt(2.2), color=NEGRO):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    shp.shadow.inherit = False
    return shp


def caja(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    return tf


def parrafo(tf, txt, size, color=NEGRO, bold=False, italic=False,
            align=PP_ALIGN.LEFT, after=6, before=0, primero=False,
            espaciado=1.0):
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
    r.font.name = FUENTE
    return p


def item(tf, txt, size=14, bold=False, nivel=0, after=5, primero=False,
         color=NEGRO):
    p = tf.paragraphs[0] if primero else tf.add_paragraph()
    p.level = nivel
    p.space_after = Pt(after)
    p.line_spacing = 1.02
    marca = "•  " if nivel == 0 else "–  "
    r0 = p.add_run(); r0.text = marca
    r0.font.size = Pt(size); r0.font.name = FUENTE
    r0.font.bold = True; r0.font.color.rgb = NEGRO
    r1 = p.add_run(); r1.text = txt
    r1.font.size = Pt(size); r1.font.name = FUENTE
    r1.font.bold = bold; r1.font.color.rgb = color
    return p


def subtitulo(tf, txt, size=15, primero=False, before=8):
    p = tf.paragraphs[0] if primero else tf.add_paragraph()
    p.space_after = Pt(4)
    p.space_before = Pt(before)
    r = p.add_run(); r.text = txt
    r.font.size = Pt(size); r.font.bold = True
    r.font.name = FUENTE; r.font.color.rgb = NEGRO
    return p


def encabezado(slide, titulo, subt=None):
    tf = caja(slide, Inches(0.6), Inches(0.4), Inches(12.1), Inches(1.0))
    parrafo(tf, titulo, 30, NEGRO, bold=True, primero=True, after=0)
    if subt:
        parrafo(tf, subt, 15, GRIS, italic=True, after=0, before=2)
    linea(slide, Inches(0.6), Inches(1.35), Inches(12.1))


def pie(slide):
    tf = caja(slide, Inches(0.6), Inches(6.95), Inches(12.1), Inches(0.5))
    parrafo(tf, "Fuente: CDC. U.S. Selected Practice Recommendations for "
                "Contraceptive Use, 2024. MMWR 2024;73(RR-3).",
            9, GRIS_CL, primero=True, after=0)
    parrafo(tf, "* Iniciar en cualquier momento si hay certeza razonable de "
                "que la persona no esta embarazada (criterios del Box 3, U.S. SPR).",
            9, GRIS_CL, after=0)


# ===========================================================================
# DIAPOSITIVA 1 - PORTADA
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo_blanco(s)
linea(s, Inches(0.9), Inches(2.55), Inches(3.2), Pt(3))
tf = caja(s, Inches(0.9), Inches(2.7), Inches(11.5), Inches(2.6))
parrafo(tf, "Anticonceptivos de solo progestageno", 38, NEGRO, bold=True,
        primero=True, after=4)
parrafo(tf, "Recomendaciones de inicio y administracion", 24, NEGRO, after=16)
parrafo(tf, "Resumen basado en las U.S. Selected Practice Recommendations "
            "for Contraceptive Use, 2024 (CDC) — MMWR 2024;73(RR-3).",
        14, GRIS, italic=True, after=6)
tf = caja(s, Inches(0.9), Inches(5.4), Inches(11.5), Inches(1.3))
parrafo(tf, "1. DIU de levonorgestrel    2. Implante subdermico    "
            "3. Inyeccion trimestral (DMPA)    4. Pildoras de solo progestageno",
        13, NEGRO, bold=True, primero=True, after=0)

# ===========================================================================
# DIAPOSITIVA 2 - DIU DE LEVONORGESTREL (LNG-IUD)
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo_blanco(s)
encabezado(s, "1. DIU de levonorgestrel (LNG-IUD)",
           "Dispositivo intrauterino liberador de levonorgestrel")
tf = caja(s, Inches(0.6), Inches(1.55), Inches(12.1), Inches(5.3))
subtitulo(tf, "¿Cuando colocarlo?", primero=True)
item(tf, "Puede colocarse en cualquier momento si hay certeza razonable de "
         "que no hay embarazo.*", 14)
subtitulo(tf, "Necesidad de anticoncepcion de respaldo")
item(tf, "Colocado dentro de los primeros 7 dias desde el inicio del sangrado "
         "menstrual: NO necesita proteccion adicional.", 14)
item(tf, "Colocado >7 dias desde el inicio del sangrado: abstinencia o metodo "
         "de barrera (condon) durante los 7 dias siguientes.", 14)
subtitulo(tf, "Situaciones especiales")
item(tf, "Amenorrea: en cualquier momento; respaldo por 7 dias.", 13.5, nivel=1)
item(tf, "Posparto: en cualquier momento, incluso inmediato (U.S. MEC 1-2). "
         "No colocar si hay sepsis puerperal (MEC 4).", 13.5, nivel=1)
item(tf, "Posaborto: en cualquier momento, incluso inmediato tras aborto "
         "completo. No colocar tras aborto septico.", 13.5, nivel=1)
item(tf, "Cambio de metodo: colocacion inmediata; si han pasado >7 dias desde "
         "el sangrado, respaldo por 7 dias.", 13.5, nivel=1)
subtitulo(tf, "Nota clave")
item(tf, "Si no hay certeza de ausencia de embarazo, usar otro metodo hasta "
         "poder colocar el DIU (el embarazo con DIU tiene mas complicaciones).",
     13.5)
pie(s)

# ===========================================================================
# DIAPOSITIVA 3 - IMPLANTE SUBDERMICO
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo_blanco(s)
encabezado(s, "2. Implante subdermico (etonogestrel)",
           "Implante subdermico de progestageno")
tf = caja(s, Inches(0.6), Inches(1.55), Inches(12.1), Inches(5.3))
subtitulo(tf, "¿Cuando colocarlo?", primero=True)
item(tf, "Puede colocarse en cualquier momento si hay certeza razonable de "
         "que no hay embarazo.*", 14)
subtitulo(tf, "Necesidad de anticoncepcion de respaldo")
item(tf, "Colocado dentro de los primeros 5 dias desde el inicio del sangrado "
         "menstrual: NO necesita proteccion adicional.", 14)
item(tf, "Colocado >5 dias desde el inicio del sangrado: abstinencia o metodo "
         "de barrera (condon) durante los 7 dias siguientes.", 14)
subtitulo(tf, "Situaciones especiales")
item(tf, "Amenorrea: en cualquier momento; respaldo por 7 dias.", 13.5, nivel=1)
item(tf, "Posparto (lactancia): en cualquier momento (U.S. MEC 2 si <30 dias; "
         "MEC 1 si ≥30 dias).", 13.5, nivel=1)
item(tf, "Posparto (sin lactancia): en cualquier momento, incluso inmediato "
         "(U.S. MEC 1).", 13.5, nivel=1)
item(tf, "Posaborto: en cualquier momento, incluso inmediato tras aborto "
         "completo o al iniciar aborto con medicamentos.", 13.5, nivel=1)
item(tf, "Cambio de metodo: colocacion inmediata; respaldo por 7 dias si "
         ">5 dias desde el sangrado.", 13.5, nivel=1)
pie(s)

# ===========================================================================
# DIAPOSITIVA 4 - INYECCION TRIMESTRAL (DMPA)
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo_blanco(s)
encabezado(s, "3. Inyeccion trimestral (DMPA)",
           "Acetato de medroxiprogesterona de deposito — IM 150 mg o SC 104 mg")
tf = caja(s, Inches(0.6), Inches(1.55), Inches(12.1), Inches(5.3))
subtitulo(tf, "¿Cuando aplicar la primera inyeccion?", primero=True)
item(tf, "Puede administrarse en cualquier momento si hay certeza razonable de "
         "que no hay embarazo.*", 14)
subtitulo(tf, "Necesidad de anticoncepcion de respaldo (primera dosis)")
item(tf, "Iniciada dentro de los primeros 7 dias desde el inicio del sangrado "
         "menstrual: NO necesita proteccion adicional.", 14)
item(tf, "Iniciada >7 dias desde el inicio del sangrado: abstinencia o metodo "
         "de barrera (condon) durante los 7 dias siguientes.", 14)
subtitulo(tf, "Reinyecciones (dosis siguientes)")
item(tf, "Repetir cada 3 meses (13 semanas).", 13.5, nivel=1)
item(tf, "Puede adelantarse cuando sea necesario.", 13.5, nivel=1)
item(tf, "Hasta 2 semanas de retraso (15 semanas desde la ultima): sin "
         "proteccion adicional.", 13.5, nivel=1)
item(tf, ">2 semanas de retraso (>15 semanas): aplicar si hay certeza de no "
         "embarazo, usar respaldo 7 dias y considerar anticoncepcion de "
         "emergencia (excepto UPA).", 13.5, nivel=1)
subtitulo(tf, "Nota")
item(tf, "Existe la opcion autoadministrada (DMPA-SC) con las mismas "
         "recomendaciones; no requiere seguimiento de rutina.", 13.5)
pie(s)

# ===========================================================================
# DIAPOSITIVA 5 - PILDORAS DE SOLO PROGESTAGENO (POP)
# ===========================================================================
s = prs.slides.add_slide(BLANK)
fondo_blanco(s)
encabezado(s, "4. Pildoras de solo progestageno (POP)",
           "Noretindrona, norgestrel o drospirenona")
tf = caja(s, Inches(0.6), Inches(1.55), Inches(12.1), Inches(5.3))
subtitulo(tf, "¿Cuando iniciarlas?", primero=True)
item(tf, "Todas las POP pueden iniciarse en cualquier momento si hay certeza "
         "razonable de que no hay embarazo.*", 14)
subtitulo(tf, "Respaldo — POP de noretindrona o norgestrel")
item(tf, "Iniciadas dentro de los primeros 5 dias desde el inicio del "
         "sangrado: NO necesita proteccion adicional.", 14, nivel=1)
item(tf, "Iniciadas >5 dias desde el inicio del sangrado: abstinencia o "
         "barrera (condon) durante los 2 dias siguientes.", 14, nivel=1)
subtitulo(tf, "Respaldo — POP de drospirenona (DRSP)")
item(tf, "Iniciadas el primer dia del sangrado menstrual: NO necesita "
         "proteccion adicional.", 14, nivel=1)
item(tf, "Iniciadas >1 dia desde el inicio del sangrado: abstinencia o barrera "
         "(condon) durante los 7 dias siguientes.", 14, nivel=1)
subtitulo(tf, "Situaciones especiales y nota")
item(tf, "Posparto y posaborto: pueden iniciarse en cualquier momento, incluso "
         "de forma inmediata.", 13.5, nivel=1)
item(tf, "Tomar la pildora aproximadamente a la misma hora todos los dias.",
     13.5, nivel=1)
pie(s)

# ---------------------------------------------------------------------------
SALIDA = os.path.join(BASE, "Anticonceptivos_soloprogestageno_recomendaciones_CDC.pptx")
prs.save(SALIDA)
print("Presentacion generada:", SALIDA)
print("Total de diapositivas:", len(prs.slides._sldIdLst))
