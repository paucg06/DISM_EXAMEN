# -*- coding: utf-8 -*-
"""
Script to build the complete DISM question database combining:
1. Existing extracted questions from HTML files (218 questions)
2. Enriched explanations for existing questions
3. New questions covering Tema 1 (all 47 blocks)
4. New practical calculation questions for Tema 2 (RAID parity, XOR, disk sizes, video/audio 4K resolutions, MOPS)
5. New practical calculation questions for Tema 3 (cellular clusters N=i^2+ij+j^2, Erlangs, S/I, channels, dB)
6. New questions for Tema 4 (OpenAPI 3.0, Swagger 2.0 vs 3.0, REST API design, RAML, components/schemas)
"""

import json
import os
import sys

# Load extracted HTML questions
with open('DISM_Examen/html_questions.json', 'r', encoding='utf-8') as f:
    existing_qs = json.load(f)

print(f"Loaded {len(existing_qs)} existing questions from HTMLs.")

# Let's count by tema
tema_counts = {}
for q in existing_qs:
    t = q['tema']
    tema_counts[t] = tema_counts.get(t, 0) + 1
print("Existing counts by tema:", tema_counts)
