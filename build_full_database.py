# -*- coding: utf-8 -*-
"""
Builder for consolidated question database including 100% full syllabus deep audit.
"""

import json
from generate_tema1 import get_tema1_questions
from generate_calculations_and_extra import (
    get_tema2_extra_questions,
    get_tema3_extra_questions,
    get_tema4_extra_questions
)
from generate_deep_audit_questions import (
    get_wearables_touch_connectivity_questions,
    get_cellular_deep_questions,
    get_multimedia_deep_questions,
    get_openapi_deep_questions
)

def enrich_existing_explanations(q):
    if q.get('explanation') and len(q['explanation'].strip()) > 5:
        return q['explanation'].strip()

    correct_text = q['options'][q['correct']]
    question_text = q['q']

    # Specific math enrichments for Tema 2 original exercises
    if "320×240" in question_text:
        return "Cálculo: 320 × 240 = 76.800 píxeles. Con 24 bits/píxel (3 Bytes/píxel): 76.800 × 3 = 230.400 Bytes. En formato binario de almacenamiento: 230.400 / 1024 = 225 KB."
    if "12 bits/píxel" in question_text and "Full HD" in question_text:
        return "Cálculo: 1920 × 1080 = 2.073.600 píxeles/frame. Con 12 bits = 1,5 Bytes por píxel: 2.073.600 × 1,5 = 3.110.400 Bytes/frame. A 30 fps: 3.110.400 × 30 = 93.312.000 Bytes/s. En MB binarios: 93.312.000 / (1024 × 1024) ≈ 88,99 MB/s (~89 MB/s)."
    if "calidad CD" in question_text and "5 minutos" in question_text:
        return "Cálculo: 44.100 muestras/s × 2 canales (estéreo) × 2 Bytes (16 bits) = 176.400 Bytes/s. En 5 minutos (300 s): 176.400 × 300 = 52.920.000 Bytes. En MB: 52.920.000 / (1024 × 1024) ≈ 50,47 MB (~50 MB)."
    if "A=1010, B=0101 y C=1100" in question_text:
        return "Cálculo XOR bit a bit: A ⊕ B = 1010 ⊕ 0101 = 1111. Luego 1111 ⊕ C = 1111 ⊕ 1100 = 0011. La paridad resultante es 0011."
    if "RAID 10 con 6 discos de 2 TB" in question_text:
        return "Cálculo RAID 10 (1+0): La capacidad lógica efectiva es la mitad del total debido al mirroring: Capacidad = (N / 2) × S = (6 / 2) × 2 TB = 3 × 2 TB = 6 TB."
    if "4.000 kbps y una duración de 40 minutos" in question_text:
        return "Cálculo: 40 minutos = 2.400 s. Bits totales = 4.000 kbps × 2.400 s = 9.600.000 kb. En Bytes (/8) = 1.200.000 kB. En GB binarios: 1.200.000 / (1024 × 1024) ≈ 1,117 GB (~1,12 GB)."

    return f"Respuesta correcta: '{correct_text}'. Concepto fundamental evaluado según el temario oficial de la asignatura."

def build_all_questions():
    # 1. Load HTML questions
    with open('DISM_Examen/html_questions.json', 'r', encoding='utf-8') as f:
        html_qs = json.load(f)

    for q in html_qs:
        q['explanation'] = enrich_existing_explanations(q)
        if 'subtema' not in q:
            q['subtema'] = f"Tema {q['tema']}"

    # 2. Get Tema 1
    t1_qs = get_tema1_questions()

    # 3. Get Extra questions
    t2_extra = get_tema2_extra_questions() + get_multimedia_deep_questions()
    t3_extra = get_tema3_extra_questions() + get_wearables_touch_connectivity_questions() + get_cellular_deep_questions()
    t4_extra = get_tema4_extra_questions() + get_openapi_deep_questions()

    # Combine everything by theme
    t1_all = t1_qs
    t2_all = [q for q in html_qs if q['tema'] == 2] + t2_extra
    t3_all = [q for q in html_qs if q['tema'] == 3] + t3_extra
    t4_all = [q for q in html_qs if q['tema'] == 4] + t4_extra

    all_questions = []

    for idx, q in enumerate(t1_all, 1):
        q['id'] = f"t1_{idx:03d}"
        q['tema'] = 1
        all_questions.append(q)

    for idx, q in enumerate(t2_all, 1):
        q['id'] = f"t2_{idx:03d}"
        q['tema'] = 2
        all_questions.append(q)

    for idx, q in enumerate(t3_all, 1):
        q['id'] = f"t3_{idx:03d}"
        q['tema'] = 3
        all_questions.append(q)

    for idx, q in enumerate(t4_all, 1):
        q['id'] = f"t4_{idx:03d}"
        q['tema'] = 4
        all_questions.append(q)

    print(f"Total questions generated: {len(all_questions)}")
    print(f"  Tema 1: {len(t1_all)}")
    print(f"  Tema 2: {len(t2_all)}")
    print(f"  Tema 3: {len(t3_all)}")
    print(f"  Tema 4: {len(t4_all)}")

    with open('DISM_Examen/all_questions.json', 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    return all_questions

if __name__ == '__main__':
    build_all_questions()
