# -*- coding: utf-8 -*-
"""
Builds the Moodle-identical DISM exam and flashcard study web application.
"""

import json
from generate_flashcards import get_flashcards

with open('DISM_Examen/all_questions.json', 'r', encoding='utf-8') as f:
    questions_data = json.load(f)

flashcards_data = get_flashcards()

questions_json_str = json.dumps(questions_data, ensure_ascii=False)
flashcards_json_str = json.dumps(flashcards_data, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Simulador exámenes DISM</title>
  <meta name="theme-color" content="#0f4c81">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎓</text></svg>">
  <style>
    /* =========================================================
       MOODLE CLEAN THEME CSS (Identical to Official Moodle Quiz)
       ========================================================= */
    :root {{
      --moodle-blue: #0f4c81;
      --moodle-blue-hover: #0b375d;
      --moodle-light-blue: #e7f3f5;
      --moodle-light-blue-border: #bee5eb;
      --moodle-text: #212529;
      --moodle-muted: #6a737d;
      --moodle-border: #dee2e6;
      --moodle-bg: #f8f9fa;
      --moodle-card-bg: #ffffff;
      --moodle-red: #dc3545;
      --moodle-red-light: #f8d7da;
      --moodle-green: #28a745;
      --moodle-green-light: #d4edda;
      --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      font-family: var(--font-family);
      background-color: var(--moodle-bg);
      color: var(--moodle-text);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* Top Navigation Bar */
    .moodle-navbar {{
      background-color: #ffffff;
      border-bottom: 1px solid var(--moodle-border);
      padding: 10px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 1000;
    }}

    .navbar-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: var(--moodle-blue);
      font-weight: 700;
      font-size: 17px;
      cursor: pointer;
    }}

    .navbar-tabs {{
      display: flex;
      gap: 6px;
    }}

    .nav-tab-btn {{
      background: transparent;
      border: 1px solid transparent;
      padding: 7px 14px;
      border-radius: 4px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--moodle-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }}

    .nav-tab-btn:hover {{
      background: rgba(15, 76, 129, 0.05);
      color: var(--moodle-blue);
    }}

    .nav-tab-btn.active {{
      background: var(--moodle-blue);
      color: #ffffff;
    }}

    /* Main Container */
    main {{
      flex: 1;
      max-width: 1100px;
      width: 100%;
      margin: 0 auto;
      padding: 20px 16px 40px;
    }}

    /* Course / Home View */
    .course-header {{
      background: #ffffff;
      border: 1px solid var(--moodle-border);
      border-radius: 4px;
      padding: 18px 22px;
      margin-bottom: 20px;
    }}

    .course-title {{
      font-size: 22px;
      font-weight: 700;
      color: var(--moodle-blue);
      margin-bottom: 4px;
    }}

    .course-subtitle {{
      color: var(--moodle-muted);
      font-size: 14px;
    }}

    .activity-group {{
      background: #ffffff;
      border: 1px solid var(--moodle-border);
      border-radius: 4px;
      margin-bottom: 18px;
      overflow: hidden;
    }}

    .activity-group-header {{
      background: #f1f3f5;
      padding: 10px 18px;
      border-bottom: 1px solid var(--moodle-border);
      font-weight: 700;
      font-size: 14px;
      color: #495057;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .activity-item {{
      padding: 14px 18px;
      border-bottom: 1px solid #e9ecef;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      transition: background 0.15s;
    }}

    .activity-item:last-child {{
      border-bottom: none;
    }}

    .activity-item:hover {{
      background-color: #f8f9fa;
    }}

    .activity-info {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }}

    .activity-icon {{
      font-size: 20px;
      flex-shrink: 0;
      margin-top: 2px;
    }}

    .activity-title {{
      font-size: 15px;
      font-weight: 600;
      color: var(--moodle-blue);
      cursor: pointer;
      text-decoration: none;
    }}

    .activity-title:hover {{
      text-decoration: underline;
    }}

    .activity-desc {{
      font-size: 13px;
      color: var(--moodle-muted);
      margin-top: 2px;
      line-height: 1.4;
    }}

    /* Buttons */
    .btn-moodle {{
      background-color: var(--moodle-blue);
      color: #ffffff;
      border: 1px solid var(--moodle-blue);
      padding: 8px 16px;
      border-radius: 4px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      transition: background-color 0.15s;
    }}

    .btn-moodle:hover {{
      background-color: var(--moodle-blue-hover);
    }}

    .btn-moodle-secondary {{
      background-color: #6c757d;
      border-color: #6c757d;
      color: #ffffff;
    }}

    .btn-moodle-secondary:hover {{
      background-color: #5a6268;
    }}

    .btn-moodle-outline {{
      background-color: transparent;
      border-color: var(--moodle-border);
      color: var(--moodle-text);
    }}

    .btn-moodle-outline:hover {{
      background-color: #e9ecef;
    }}

    /* =========================================================
       MOODLE QUIZ INTERFACE (Matches screenshot exactly)
       ========================================================= */
    .quiz-layout {{
      display: flex;
      gap: 20px;
      align-items: flex-start;
    }}

    .quiz-main-area {{
      flex: 1;
      min-width: 0;
    }}

    .quiz-sidebar-area {{
      width: 250px;
      flex-shrink: 0;
    }}

    /* Top bar inside quiz */
    .quiz-topbar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}

    .btn-back {{
      background-color: var(--moodle-blue);
      color: #ffffff;
      border: none;
      padding: 6px 14px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
    }}

    .btn-back:hover {{
      background-color: var(--moodle-blue-hover);
    }}

    .time-left-box {{
      background-color: #ffffff;
      border: 1px solid var(--moodle-red);
      color: var(--moodle-red);
      padding: 6px 12px;
      border-radius: 4px;
      font-size: 14px;
      font-weight: 700;
      font-variant-numeric: tabular-nums;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    /* Question Container: Info Block on left + Formulation Block on right */
    .question-row {{
      display: flex;
      gap: 16px;
      margin-bottom: 20px;
    }}

    .info-block {{
      width: 125px;
      flex-shrink: 0;
      background: #ffffff;
      border: 1px solid var(--moodle-border);
      border-radius: 4px;
      padding: 12px;
      font-size: 12px;
      line-height: 1.4;
      align-self: flex-start;
    }}

    .info-question-num {{
      font-size: 14px;
      font-weight: 800;
      color: #212529;
      margin-bottom: 4px;
    }}

    .info-status {{
      color: var(--moodle-muted);
      margin-bottom: 6px;
    }}

    .info-points {{
      color: var(--moodle-muted);
      margin-bottom: 10px;
      border-bottom: 1px solid #f1f3f5;
      padding-bottom: 6px;
    }}

    .info-flag-btn {{
      background: transparent;
      border: none;
      color: var(--moodle-blue);
      cursor: pointer;
      font-size: 11.5px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 0;
    }}

    .info-flag-btn:hover {{
      text-decoration: underline;
    }}

    .info-flag-btn.flagged {{
      color: var(--moodle-red);
      font-weight: 700;
    }}

    /* Formulation Block (Cyan/Light Blue card) */
    .formulation-block {{
      flex: 1;
      background-color: var(--moodle-light-blue);
      border: 1px solid var(--moodle-light-blue-border);
      border-radius: 4px;
      padding: 20px;
    }}

    .formulation-text {{
      font-size: 15px;
      font-weight: 500;
      color: #212529;
      line-height: 1.5;
      margin-bottom: 16px;
    }}

    .select-prompt {{
      font-size: 13.5px;
      font-weight: 600;
      color: #495057;
      margin-bottom: 12px;
    }}

    .moodle-options {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .moodle-option-label {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      cursor: pointer;
      font-size: 14px;
      color: #212529;
      padding: 4px 6px;
      border-radius: 4px;
      transition: background 0.1s;
    }}

    .moodle-option-label:hover {{
      background: rgba(0,0,0,0.03);
    }}

    .moodle-option-label input[type="radio"] {{
      margin-top: 3px;
      cursor: pointer;
      width: 16px;
      height: 16px;
      accent-color: var(--moodle-blue);
      flex-shrink: 0;
    }}

    .moodle-option-text {{
      flex: 1;
      line-height: 1.4;
    }}

    /* Feedback Box in Review Mode */
    .moodle-feedback-box {{
      margin-top: 16px;
      padding: 12px 16px;
      border-radius: 4px;
      font-size: 13.5px;
      line-height: 1.5;
    }}

    .moodle-feedback-box.correct {{
      background-color: var(--moodle-green-light);
      border: 1px solid #c3e6cb;
      color: #155724;
    }}

    .moodle-feedback-box.incorrect {{
      background-color: var(--moodle-red-light);
      border: 1px solid #f5c6cb;
      color: #721c24;
    }}

    /* Bottom page navigation */
    .quiz-bottom-nav {{
      display: flex;
      justify-content: flex-end;
      gap: 10px;
      margin-top: 14px;
    }}

    /* Sidebar: Quiz navigation card */
    .quiz-nav-card {{
      background: #ffffff;
      border: 1px solid var(--moodle-border);
      border-radius: 4px;
      padding: 16px;
    }}

    .quiz-nav-title {{
      font-size: 14px;
      font-weight: 700;
      color: #212529;
      margin-bottom: 12px;
    }}

    .moodle-nav-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 6px;
      margin-bottom: 16px;
    }}

    .moodle-nav-btn {{
      height: 34px;
      border: 1px solid #6c757d;
      border-radius: 2px;
      background: #ffffff;
      color: #212529;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      transition: all 0.1s;
    }}

    .moodle-nav-btn:hover {{
      background: #e9ecef;
    }}

    /* Moodle current indicator */
    .moodle-nav-btn.current {{
      border-width: 2px;
      border-color: #000000;
      box-shadow: 0 0 0 1px #000000;
    }}

    /* Moodle answered indicator (bottom half shaded) */
    .moodle-nav-btn.answered::after {{
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 40%;
      background-color: #b0bec5;
      z-index: 1;
    }}

    .moodle-nav-btn.answered-text {{
      position: relative;
      z-index: 2;
    }}

    /* Moodle flagged indicator (red top-right corner) */
    .moodle-nav-btn.flagged::before {{
      content: '';
      position: absolute;
      top: 0;
      right: 0;
      width: 0;
      height: 0;
      border-style: solid;
      border-width: 0 8px 8px 0;
      border-color: transparent var(--moodle-red) transparent transparent;
      z-index: 3;
    }}

    .moodle-nav-btn.correct-rev {{
      background-color: var(--moodle-green-light) !important;
      border-color: var(--moodle-green) !important;
      color: var(--moodle-green) !important;
    }}

    .moodle-nav-btn.wrong-rev {{
      background-color: var(--moodle-red-light) !important;
      border-color: var(--moodle-red) !important;
      color: var(--moodle-red) !important;
    }}

    .finish-attempt-link {{
      font-size: 12.5px;
      color: var(--moodle-blue);
      text-decoration: none;
      display: block;
      cursor: pointer;
      padding-top: 4px;
      border-top: 1px solid #f1f3f5;
    }}

    .finish-attempt-link:hover {{
      text-decoration: underline;
    }}

    /* =========================================================
       SUMMARY / REVIEW ATTEMPT VIEW
       ========================================================= */
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
      background: #ffffff;
      border: 1px solid var(--moodle-border);
      border-radius: 4px;
      overflow: hidden;
      font-size: 13.5px;
    }}

    .summary-table th, .summary-table td {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--moodle-border);
      text-align: left;
    }}

    .summary-table th {{
      background: #f8f9fa;
      font-weight: 700;
    }}

    /* =========================================================
       TARJETAS DE ESTUDIO (Mobile Flashcards for Bus)
       ========================================================= */
    .flashcards-container {{
      max-width: 750px;
      margin: 0 auto;
    }}

    .flashcards-filters {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 8px;
      margin-bottom: 16px;
      -webkit-overflow-scrolling: touch;
    }}

    .filter-btn {{
      background: #ffffff;
      border: 1px solid var(--moodle-border);
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--moodle-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s;
    }}

    .filter-btn:hover {{
      border-color: var(--moodle-blue);
      color: var(--moodle-blue);
    }}

    .filter-btn.active {{
      background: var(--moodle-blue);
      border-color: var(--moodle-blue);
      color: #ffffff;
    }}

    /* Card Box */
    .study-card {{
      background: #ffffff;
      border: 1px solid var(--moodle-border);
      border-radius: 6px;
      padding: 24px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
      margin-bottom: 16px;
    }}

    .card-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      color: var(--moodle-muted);
      margin-bottom: 10px;
    }}

    .card-badge {{
      background: #e7f3f5;
      color: var(--moodle-blue);
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 3px;
      font-size: 11px;
      text-transform: uppercase;
    }}

    .card-title {{
      font-size: 18px;
      font-weight: 700;
      color: #212529;
      margin-bottom: 14px;
      line-height: 1.35;
    }}

    .card-bullets {{
      list-style-type: disc;
      padding-left: 20px;
      margin-bottom: 16px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 14px;
      color: #333333;
      line-height: 1.5;
    }}

    .card-key-box {{
      background-color: #fff9db;
      border: 1px solid #ffe066;
      border-radius: 4px;
      padding: 10px 14px;
      font-size: 13px;
      color: #856404;
      line-height: 1.4;
      font-weight: 500;
    }}

    .card-nav-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
    }}

    /* Responsive */
    @media (max-width: 768px) {{
      .quiz-layout {{
        flex-direction: column-reverse;
      }}
      .quiz-sidebar-area {{
        width: 100%;
      }}
      .question-row {{
        flex-direction: column;
        gap: 10px;
      }}
      .info-block {{
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px 12px;
      }}
      .info-points {{
        border-bottom: none;
        padding-bottom: 0;
        margin-bottom: 0;
      }}
      .formulation-block {{
        padding: 16px;
      }}
      .moodle-nav-grid {{
        grid-template-columns: repeat(10, 1fr);
      }}
    }}

    .hidden {{
      display: none !important;
    }}
  </style>
</head>
<body>

  <!-- MOODLE TOP NAVBAR -->
  <header class="moodle-navbar">
    <div class="navbar-brand" onclick="app.showHome()">
      <span>📘</span>
      <span>Simulador exámenes DISM</span>
    </div>
    <div class="navbar-tabs">
      <button class="nav-tab-btn active" id="tabExams" onclick="app.showHome()">
        <span>📝</span> Cuestionarios
      </button>
      <button class="nav-tab-btn" id="tabFlashcards" onclick="app.showFlashcards()">
        <span>🗂️</span> Tarjetas de Estudio
      </button>
    </div>
  </header>

  <main>

    <!-- VIEW 1: MOODLE COURSE PAGE (CUESTIONARIOS / EXÁMENES) -->
    <section id="viewHome">
      <div class="course-header">
        <h1 class="course-title">Desarrollo de Interfaces para Sistemas Móviles</h1>
        <p class="course-subtitle">Preparación para el examen parcial y final con banco oficial de preguntas tipo test y ejercicios de cálculo.</p>
      </div>

      <!-- PRIMER EXAMEN PARCIAL (FEATURED) -->
      <div class="activity-group" style="border: 2px solid var(--moodle-blue);">
        <div class="activity-group-header" style="background: #e7f3f5; color: var(--moodle-blue);">
          <span>🎯</span> PRIMER EXAMEN PARCIAL (TEMAS 1 Y 2)
        </div>
        <div class="activity-item" style="padding: 18px;">
          <div class="activity-info">
            <span class="activity-icon">📝</span>
            <div>
              <a href="javascript:void(0)" class="activity-title" onclick="app.startExam('parcial1')" style="font-size: 16px;">
                Cuestionario: Simulacro Primer Examen Parcial
              </a>
              <div class="activity-desc">
                Engloba los <strong>Temas 1 y 2</strong>: Desarrollo Multiplataforma (PWA, Ionic, Flutter, React Native, MAUI) e Infraestructuras Multimedia con <strong>ejercicios de desarrollo y cálculos de discos RAID y resoluciones</strong>. 30 preguntas tipo test.
              </div>
            </div>
          </div>
          <button class="btn-moodle" onclick="app.startExam('parcial1')">
            Comenzar cuestionario →
          </button>
        </div>
      </div>

      <!-- CUESTIONARIOS POR TEMA -->
      <div class="activity-group">
        <div class="activity-group-header">
          <span>📂</span> Cuestionarios por Temas (30 preguntas cada uno)
        </div>

        <!-- Tema 1 -->
        <div class="activity-item">
          <div class="activity-info">
            <span class="activity-icon">📱</span>
            <div>
              <a href="javascript:void(0)" class="activity-title" onclick="app.startExam(1)">
                Cuestionario Tema 1: Desarrollo Multiplataforma
              </a>
              <div class="activity-desc">
                Nativo vs híbrido, PWA, Service Workers, Ionic, Capacitor, .NET MAUI, Flutter, React Native, KMP y Tauri.
              </div>
            </div>
          </div>
          <button class="btn-moodle btn-moodle-outline" onclick="app.startExam(1)">Entrar</button>
        </div>

        <!-- Tema 2 -->
        <div class="activity-item">
          <div class="activity-info">
            <span class="activity-icon">🎬</span>
            <div>
              <a href="javascript:void(0)" class="activity-title" onclick="app.startExam(2)">
                Cuestionario Tema 2: Infraestructuras Multimedia & Cálculos
              </a>
              <div class="activity-desc">
                Streaming ABR, Netflix Open Connect, <strong>cálculos RAID (0, 1, 5, 6, 10, XOR)</strong>, <strong>resoluciones vídeo 4K/audio</strong>, MOPS y hardware MMA.
              </div>
            </div>
          </div>
          <button class="btn-moodle btn-moodle-outline" onclick="app.startExam(2)">Entrar</button>
        </div>

        <!-- Tema 3 -->
        <div class="activity-item">
          <div class="activity-info">
            <span class="activity-icon">📡</span>
            <div>
              <a href="javascript:void(0)" class="activity-title" onclick="app.startExam(3)">
                Cuestionario Tema 3: Dispositivos & Telefonía Móvil
              </a>
              <div class="activity-desc">
                Hardware móvil SoC, redes GSM a 5G, handover, <strong>cálculos cluster N=i²+ij+j²</strong>, <strong>tráfico Erlangs</strong> y relación S/I.
              </div>
            </div>
          </div>
          <button class="btn-moodle btn-moodle-outline" onclick="app.startExam(3)">Entrar</button>
        </div>

        <!-- Tema 4 -->
        <div class="activity-item">
          <div class="activity-info">
            <span class="activity-icon">🌐</span>
            <div>
              <a href="javascript:void(0)" class="activity-title" onclick="app.startExam(4)">
                Cuestionario Tema 4: IoT & Diseño de APIs REST
              </a>
              <div class="activity-desc">
                Internet of Things (MQTT, CoAP), diseño de APIs REST, Swagger 2.0 vs OpenAPI 3.0, RAML y componentes.
              </div>
            </div>
          </div>
          <button class="btn-moodle btn-moodle-outline" onclick="app.startExam(4)">Entrar</button>
        </div>
      </div>

      <!-- EXAMEN GLOBAL Y REPASO ESPECIAL -->
      <div class="activity-group">
        <div class="activity-group-header">
          <span>🌐</span> Exámenes Globales y Repaso Práctico
        </div>

        <div class="activity-item">
          <div class="activity-info">
            <span class="activity-icon">🔥</span>
            <div>
              <a href="javascript:void(0)" class="activity-title" onclick="app.startExam('global')">
                Examen Global Completo (Temas 1, 2, 3 y 4)
              </a>
              <div class="activity-desc">
                Simulacro de examen general: 40 preguntas (10 preguntas de cada tema).
              </div>
            </div>
          </div>
          <button class="btn-moodle btn-moodle-outline" onclick="app.startExam('global')">Entrar</button>
        </div>

        <div class="activity-item">
          <div class="activity-info">
            <span class="activity-icon">🧮</span>
            <div>
              <a href="javascript:void(0)" class="activity-title" onclick="app.startCalculationsOnly()">
                Práctica Exclusiva: Ejercicios de Cálculo (RAID, Bits, Resoluciones, Erlangs)
              </a>
              <div class="activity-desc">
                Filtra únicamente los problemas matemáticos y de desarrollo del temario con resolución paso a paso.
              </div>
            </div>
          </div>
          <button class="btn-moodle btn-moodle-outline" onclick="app.startCalculationsOnly()">Entrar</button>
        </div>

        <div class="activity-item" id="failedRow" style="display:none;">
          <div class="activity-info">
            <span class="activity-icon">⚠️</span>
            <div>
              <a href="javascript:void(0)" class="activity-title" onclick="app.startFailedOnly()" style="color: var(--moodle-red);">
                Cuestionario de Preguntas Falladas (<span id="failedCountBadge">0</span>)
              </a>
              <div class="activity-desc">
                Repasa solo las preguntas que hayas marcado erróneas en tus intentos anteriores.
              </div>
            </div>
          </div>
          <button class="btn-moodle btn-moodle-outline" onclick="app.startFailedOnly()">Repasar</button>
        </div>
      </div>
    </section>

    <!-- VIEW 2: MOODLE QUIZ INTERFACE (Matches user screenshot) -->
    <section id="viewQuiz" class="hidden">
      <!-- Quiz Topbar -->
      <div class="quiz-topbar">
        <button class="btn-back" onclick="app.confirmExitExam()">Back</button>
        <div class="time-left-box">
          <span>Time left</span> <span id="quizTimer">0:29:50</span>
        </div>
      </div>

      <div class="quiz-layout">
        <!-- Main Question Area -->
        <div class="quiz-main-area">
          <div class="question-row">
            <!-- Left Info Block -->
            <div class="info-block">
              <div class="info-question-num" id="infoQNum">Question 1</div>
              <div class="info-status" id="infoQStatus">Not yet answered</div>
              <div class="info-points" id="infoQPoints">Points out of 1.00</div>
              <button class="info-flag-btn" id="infoFlagBtn" onclick="app.toggleFlagCurrent()">
                <span id="flagIcon">⚐</span> <span id="flagText">Flag question</span>
              </button>
            </div>

            <!-- Right Formulation Block -->
            <div class="formulation-block">
              <div class="formulation-text" id="qText">Texto de la pregunta...</div>
              <div class="select-prompt">Select one:</div>
              <div class="moodle-options" id="optionsContainer">
                <!-- Radio options dynamically injected -->
              </div>

              <!-- Moodle Review Feedback Box (Shown in review mode) -->
              <div class="moodle-feedback-box hidden" id="moodleFeedbackBox">
                <div style="font-weight:700; margin-bottom:4px;" id="feedbackStatusText">Respuesta correcta.</div>
                <div id="feedbackExplanation" style="white-space: pre-line;"></div>
              </div>
            </div>
          </div>

          <!-- Bottom navigation -->
          <div class="quiz-bottom-nav">
            <button class="btn-moodle btn-moodle-secondary hidden" id="prevPageBtn" onclick="app.prevQuestion()">
              Previous page
            </button>
            <button class="btn-moodle" id="nextPageBtn" onclick="app.nextQuestion()">
              Next page
            </button>
          </div>
        </div>

        <!-- Sidebar Quiz Navigation -->
        <div class="quiz-sidebar-area">
          <div class="quiz-nav-card">
            <div class="quiz-nav-title">Quiz navigation</div>
            <div class="moodle-nav-grid" id="moodleNavGrid">
              <!-- Numbered buttons 1..N dynamically injected -->
            </div>
            <a href="javascript:void(0)" class="finish-attempt-link" onclick="app.finishAttemptSummary()">
              Finish attempt ...
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- VIEW 3: SUMMARY OF ATTEMPT (MOODLE SUMMARY SCREEN) -->
    <section id="viewSummary" class="hidden">
      <div class="course-header" style="margin-bottom: 16px;">
        <h2 style="font-size: 19px; color: var(--moodle-blue);">Summary of attempt</h2>
      </div>

      <table class="summary-table">
        <thead>
          <tr>
            <th>Question</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody id="summaryTableBody">
          <!-- Dynamically inserted -->
        </tbody>
      </table>

      <div style="display: flex; gap: 10px; justify-content: flex-end; flex-wrap: wrap;">
        <button class="btn-moodle btn-moodle-outline" onclick="app.returnToAttempt()">
          Return to attempt
        </button>
        <button class="btn-moodle" onclick="app.submitAttempt()">
          Submit all and finish
        </button>
      </div>
    </section>

    <!-- VIEW 4: REVIEW / RESULTS SCREEN -->
    <section id="viewResults" class="hidden">
      <div class="course-header" style="margin-bottom: 16px;">
        <h2 style="font-size: 20px; color: var(--moodle-blue);" id="reviewTitle">Review of attempt</h2>
        <div style="margin-top: 8px; font-size: 14px; line-height: 1.6;" id="reviewDetails">
          <!-- Grade, time, status -->
        </div>
      </div>

      <div style="display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap;">
        <button class="btn-moodle" onclick="app.startReviewQuestions()">
          Revisar preguntas una a una →
        </button>
        <button class="btn-moodle btn-moodle-outline" onclick="app.showHome()">
          Finalizar revisión y volver al curso
        </button>
      </div>
    </section>

    <!-- VIEW 5: TARJETAS DE ESTUDIO (Mobile Flashcards for bus) -->
    <section id="viewFlashcards" class="hidden">
      <div class="flashcards-container">
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <h2 style="font-size: 20px; color: var(--moodle-blue);">Tarjetas de Estudio</h2>
            <div style="font-size: 13px; color: var(--moodle-muted);">Ideal para repasar rápido desde el móvil en el bus.</div>
          </div>
          <div style="display: flex; gap: 6px;">
            <button class="btn-moodle btn-moodle-outline" style="padding: 5px 10px; font-size: 12px;" onclick="app.toggleCardViewMode()" id="viewModeBtn">
              📜 Ver Lista
            </button>
          </div>
        </div>

        <!-- Filter Chips -->
        <div class="flashcards-filters">
          <button class="filter-btn active" onclick="app.setFlashcardFilter('all', this)">Todas (<span id="fcCountAll">0</span>)</button>
          <button class="filter-btn" onclick="app.setFlashcardFilter(1, this)">Tema 1: Multiplataforma</button>
          <button class="filter-btn" onclick="app.setFlashcardFilter(2, this)">Tema 2: Multimedia & RAID</button>
          <button class="filter-btn" onclick="app.setFlashcardFilter(3, this)">Tema 3: Móviles & Redes</button>
          <button class="filter-btn" onclick="app.setFlashcardFilter(4, this)">Tema 4: IoT & APIs REST</button>
          <button class="filter-btn" onclick="app.setFlashcardFilter('calc', this)">🧮 Solo Cálculos</button>
        </div>

        <!-- Single Card Swipe View -->
        <div id="singleCardView">
          <div class="study-card">
            <div class="card-meta">
              <span class="card-badge" id="cardCategory">Tema 1</span>
              <span id="cardCounterText">Tarjeta 1 de 25</span>
            </div>
            <div class="card-title" id="cardTitle">Título de la tarjeta</div>
            <ul class="card-bullets" id="cardBullets">
              <!-- Bullets -->
            </ul>
            <div class="card-key-box" id="cardKey">
              Punto clave / regla de examen...
            </div>
          </div>

          <!-- Bottom Card Controls -->
          <div class="card-nav-bar">
            <button class="btn-moodle btn-moodle-outline" onclick="app.prevCard()">
              ← Anterior
            </button>
            <button class="btn-moodle btn-moodle-outline" onclick="app.randomCard()">
              🔀 Aleatoria
            </button>
            <button class="btn-moodle" onclick="app.nextCard()">
              Siguiente →
            </button>
          </div>
        </div>

        <!-- Continuous Scroll List View -->
        <div id="listCardsView" class="hidden" style="display: flex; flex-direction: column; gap: 14px;">
          <!-- All cards dynamically rendered -->
        </div>

      </div>
    </section>

  </main>

  <!-- JAVASCRIPT & DATA -->
  <script>
    const ALL_QUESTIONS = {questions_json_str};
    const ALL_FLASHCARDS = {flashcards_json_str};

    const app = {{
      questions: ALL_QUESTIONS,
      flashcards: ALL_FLASHCARDS,

      // Quiz state
      currentExam: null,
      currentIndex: 0,
      userAnswers: {{}},
      flags: {{}},
      timerInterval: null,
      secondsRemaining: 30 * 60,
      isReviewMode: false,
      failedQuestions: new Set(),

      // Flashcards state
      currentCardIndex: 0,
      cardFilter: 'all',
      filteredCards: [],
      isListView: false,

      init() {{
        try {{
          const stored = localStorage.getItem('dism_failed_questions');
          if (stored) {{
            this.failedQuestions = new Set(JSON.parse(stored));
          }}
        }} catch(e) {{}}

        this.updateFailedBadge();
        this.filteredCards = [...this.flashcards];
        document.getElementById('fcCountAll').textContent = this.flashcards.length;
        this.renderCard();
      }},

      updateFailedBadge() {{
        const count = this.failedQuestions.size;
        document.getElementById('failedCountBadge').textContent = count;
        const row = document.getElementById('failedRow');
        if (row) row.style.display = count > 0 ? 'flex' : 'none';
      }},

      saveFailed() {{
        try {{
          localStorage.setItem('dism_failed_questions', JSON.stringify(Array.from(this.failedQuestions)));
        }} catch(e) {{}}
        this.updateFailedBadge();
      }},

      showView(viewId) {{
        ['viewHome', 'viewQuiz', 'viewSummary', 'viewResults', 'viewFlashcards'].forEach(id => {{
          const el = document.getElementById(id);
          if (el) el.classList.add('hidden');
        }});
        const target = document.getElementById(viewId);
        if (target) target.classList.remove('hidden');
        window.scrollTo(0, 0);
      }},

      showHome() {{
        if (this.timerInterval) clearInterval(this.timerInterval);
        document.getElementById('tabExams').classList.add('active');
        document.getElementById('tabFlashcards').classList.remove('active');
        this.showView('viewHome');
      }},

      showFlashcards() {{
        if (this.timerInterval) clearInterval(this.timerInterval);
        document.getElementById('tabExams').classList.remove('active');
        document.getElementById('tabFlashcards').classList.add('active');
        this.showView('viewFlashcards');
      }},

      shuffle(arr) {{
        const copy = [...arr];
        for (let i = copy.length - 1; i > 0; i--) {{
          const j = Math.floor(Math.random() * (i + 1));
          [copy[i], copy[j]] = [copy[j], copy[i]];
        }}
        return copy;
      }},

      startExam(type) {{
        let pool = [];
        let title = '';

        if (type === 'parcial1') {{
          // PRIMER EXAMEN PARCIAL: TEMAS 1 Y 2
          title = 'Simulacro Primer Examen Parcial (Temas 1 y 2)';
          const t1 = this.shuffle(this.questions.filter(q => q.tema === 1)).slice(0, 15);
          const t2 = this.shuffle(this.questions.filter(q => q.tema === 2)).slice(0, 15);
          pool = this.shuffle([...t1, ...t2]);
        }} else if (type === 'global') {{
          title = 'Examen Global Completo (Temas 1 al 4)';
          const t1 = this.shuffle(this.questions.filter(q => q.tema === 1)).slice(0, 10);
          const t2 = this.shuffle(this.questions.filter(q => q.tema === 2)).slice(0, 10);
          const t3 = this.shuffle(this.questions.filter(q => q.tema === 3)).slice(0, 10);
          const t4 = this.shuffle(this.questions.filter(q => q.tema === 4)).slice(0, 10);
          pool = this.shuffle([...t1, ...t2, ...t3, ...t4]);
        }} else if (typeof type === 'number') {{
          title = `Cuestionario Tema ${{type}}`;
          const temaQuestions = this.questions.filter(q => q.tema === type);
          pool = this.shuffle(temaQuestions).slice(0, 30);
        }}

        this.setupQuiz(pool, title);
      }},

      startCalculationsOnly() {{
        const calcQuestions = this.questions.filter(q => 
          q.q.toUpperCase().includes('EJERCICIO') || 
          q.q.toUpperCase().includes('CÁLCUL') || 
          q.q.toUpperCase().includes('CALCULA') ||
          (q.subtema && q.subtema.includes('Cálcul'))
        );
        this.setupQuiz(this.shuffle(calcQuestions), 'Práctica de Cálculos Numéricos');
      }},

      startFailedOnly() {{
        const failedPool = this.questions.filter(q => this.failedQuestions.has(q.id));
        if (failedPool.length === 0) {{
          alert('No tienes preguntas falladas registradas.');
          return;
        }}
        this.setupQuiz(this.shuffle(failedPool), 'Cuestionario de Preguntas Falladas');
      }},

      setupQuiz(pool, title) {{
        this.currentExam = {{
          title: title,
          questions: pool
        }};
        this.currentIndex = 0;
        this.userAnswers = {{}};
        this.flags = {{}};
        this.isReviewMode = false;

        // Timer: 30 minutes
        this.secondsRemaining = 30 * 60;
        if (this.timerInterval) clearInterval(this.timerInterval);
        this.timerInterval = setInterval(() => {{
          this.secondsRemaining--;
          if (this.secondsRemaining <= 0) {{
            clearInterval(this.timerInterval);
            this.submitAttempt();
            return;
          }}
          const mins = Math.floor(this.secondsRemaining / 60);
          const secs = String(this.secondsRemaining % 60).padStart(2, '0');
          document.getElementById('quizTimer').textContent = `${{mins}}:${{secs}}`;
        }}, 1000);

        this.showView('viewQuiz');
        this.renderQuestion();
        this.renderMoodleNav();
      }},

      renderQuestion() {{
        const q = this.currentExam.questions[this.currentIndex];
        const total = this.currentExam.questions.length;

        // Left info block
        document.getElementById('infoQNum').textContent = `Question ${{this.currentIndex + 1}}`;
        const ans = this.userAnswers[this.currentIndex];

        if (this.isReviewMode) {{
          const isCorrect = ans === q.correct;
          document.getElementById('infoQStatus').textContent = isCorrect ? 'Correct' : 'Incorrect';
          document.getElementById('infoQPoints').textContent = isCorrect ? 'Mark 1.00 out of 1.00' : 'Mark 0.00 out of 1.00';
        }} else {{
          document.getElementById('infoQStatus').textContent = ans !== undefined ? 'Answer saved' : 'Not yet answered';
          document.getElementById('infoQPoints').textContent = 'Points out of 1.00';
        }}

        // Flag button
        const isFlagged = !!this.flags[this.currentIndex];
        const flagBtn = document.getElementById('infoFlagBtn');
        flagBtn.className = 'info-flag-btn ' + (isFlagged ? 'flagged' : '');
        document.getElementById('flagIcon').textContent = isFlagged ? '⚑' : '⚐';
        document.getElementById('flagText').textContent = isFlagged ? 'Remove flag' : 'Flag question';

        // Question formulation text
        document.getElementById('qText').textContent = q.q;

        // Render radio options (Moodle style)
        const container = document.getElementById('optionsContainer');
        container.innerHTML = '';

        const letters = ['a', 'b', 'c', 'd'];
        q.options.forEach((optText, i) => {{
          const label = document.createElement('label');
          label.className = 'moodle-option-label';

          const radio = document.createElement('input');
          radio.type = 'radio';
          radio.name = `moodle_q_${{this.currentIndex}}`;
          radio.value = i;
          radio.checked = ans === i;

          if (this.isReviewMode) {{
            radio.disabled = true;
          }} else {{
            radio.onchange = () => this.selectOption(i);
          }}

          const textSpan = document.createElement('span');
          textSpan.className = 'moodle-option-text';

          let indicator = '';
          if (this.isReviewMode) {{
            if (i === q.correct) {{
              indicator = ' <strong style="color:var(--moodle-green);">✔</strong>';
            }} else if (ans === i && ans !== q.correct) {{
              indicator = ' <strong style="color:var(--moodle-red);">✖</strong>';
            }}
          }}

          textSpan.innerHTML = `<strong>${{letters[i]}}.</strong> ${{optText}}${{indicator}}`;

          label.appendChild(radio);
          label.appendChild(textSpan);
          container.appendChild(label);
        }});

        // Feedback in Review Mode
        const feedbackBox = document.getElementById('moodleFeedbackBox');
        if (this.isReviewMode) {{
          feedbackBox.classList.remove('hidden');
          const isCorrect = ans === q.correct;
          feedbackBox.className = 'moodle-feedback-box ' + (isCorrect ? 'correct' : 'incorrect');
          document.getElementById('feedbackStatusText').textContent = isCorrect 
            ? 'Respuesta correcta.' 
            : `Respuesta incorrecta. La respuesta correcta es: ${{letters[q.correct]}}. ${{q.options[q.correct]}}`;
          document.getElementById('feedbackExplanation').textContent = q.explanation || 'Respuesta según el temario oficial.';
        }} else {{
          feedbackBox.classList.add('hidden');
        }}

        // Navigation buttons
        const prevBtn = document.getElementById('prevPageBtn');
        const nextBtn = document.getElementById('nextPageBtn');

        if (this.currentIndex > 0) {{
          prevBtn.classList.remove('hidden');
        }} else {{
          prevBtn.classList.add('hidden');
        }}

        if (this.currentIndex === total - 1) {{
          nextBtn.textContent = this.isReviewMode ? 'Finish review' : 'Finish attempt ...';
        }} else {{
          nextBtn.textContent = 'Next page';
        }}

        this.renderMoodleNav();
      }},

      selectOption(index) {{
        this.userAnswers[this.currentIndex] = index;
        document.getElementById('infoQStatus').textContent = 'Answer saved';
        this.renderMoodleNav();
      }},

      toggleFlagCurrent() {{
        this.flags[this.currentIndex] = !this.flags[this.currentIndex];
        this.renderQuestion();
      }},

      nextQuestion() {{
        const total = this.currentExam.questions.length;
        if (this.currentIndex < total - 1) {{
          this.currentIndex++;
          this.renderQuestion();
          window.scrollTo(0, 0);
        }} else {{
          if (this.isReviewMode) {{
            this.showHome();
          }} else {{
            this.finishAttemptSummary();
          }}
        }}
      }},

      prevQuestion() {{
        if (this.currentIndex > 0) {{
          this.currentIndex--;
          this.renderQuestion();
          window.scrollTo(0, 0);
        }}
      }},

      goToQuestion(idx) {{
        this.currentIndex = idx;
        this.showView('viewQuiz');
        this.renderQuestion();
      }},

      renderMoodleNav() {{
        const grid = document.getElementById('moodleNavGrid');
        grid.innerHTML = '';

        this.currentExam.questions.forEach((q, idx) => {{
          const btn = document.createElement('div');
          btn.className = 'moodle-nav-btn';

          if (idx === this.currentIndex) btn.classList.add('current');
          if (this.flags[idx]) btn.classList.add('flagged');

          const ans = this.userAnswers[idx];
          if (ans !== undefined) {{
            if (this.isReviewMode) {{
              if (ans === q.correct) btn.classList.add('correct-rev');
              else btn.classList.add('wrong-rev');
            }} else {{
              btn.classList.add('answered');
            }}
          }}

          const span = document.createElement('span');
          span.className = 'answered-text';
          span.textContent = idx + 1;
          btn.appendChild(span);

          btn.onclick = () => this.goToQuestion(idx);
          grid.appendChild(btn);
        }});
      }},

      confirmExitExam() {{
        if (confirm('¿Deseas volver al curso? Tu intento actual se cerrará.')) {{
          this.showHome();
        }}
      }},

      finishAttemptSummary() {{
        this.showView('viewSummary');
        const tbody = document.getElementById('summaryTableBody');
        tbody.innerHTML = '';

        this.currentExam.questions.forEach((q, idx) => {{
          const tr = document.createElement('tr');
          const isAnswered = this.userAnswers[idx] !== undefined;

          tr.innerHTML = `
            <td>
              <a href="javascript:void(0)" onclick="app.goToQuestion(${{idx}})" style="color:var(--moodle-blue); font-weight:600; text-decoration:none;">
                Question ${{idx + 1}}
              </a>
              ${{this.flags[idx] ? ' <span style="color:var(--moodle-red); font-size:11px;">⚑ Flagged</span>' : ''}}
            </td>
            <td style="color:${{isAnswered ? 'var(--moodle-text)' : 'var(--moodle-muted)'}}">
              ${{isAnswered ? 'Answer saved' : 'Not yet answered'}}
            </td>
          `;
          tbody.appendChild(tr);
        }});
      }},

      returnToAttempt() {{
        this.showView('viewQuiz');
      }},

      submitAttempt() {{
        if (this.timerInterval) clearInterval(this.timerInterval);

        let correct = 0;
        const total = this.currentExam.questions.length;

        this.currentExam.questions.forEach((q, idx) => {{
          const ans = this.userAnswers[idx];
          if (ans === q.correct) {{
            correct++;
          }} else {{
            this.failedQuestions.add(q.id);
          }}
        }});

        this.saveFailed();

        const grade = ((correct / total) * 10).toFixed(2);
        const percent = Math.round((correct / total) * 100);

        this.showView('viewResults');
        document.getElementById('reviewTitle').textContent = `Review of attempt - ${{this.currentExam.title}}`;
        document.getElementById('reviewDetails').innerHTML = `
          <strong>State:</strong> Finished<br>
          <strong>Marks:</strong> ${{correct}}.00 / ${{total}}.00<br>
          <strong>Grade:</strong> <span style="font-size:16px; font-weight:700; color:${{grade >= 5 ? 'var(--moodle-green)' : 'var(--moodle-red)'}}">${{grade}} out of 10.00 (${{percent}}%)</span>
        `;
      }},

      startReviewQuestions() {{
        this.isReviewMode = true;
        this.currentIndex = 0;
        this.showView('viewQuiz');
        this.renderQuestion();
      }},

      // ==========================================
      // FLASHCARDS LOGIC
      // ==========================================
      setFlashcardFilter(filter, btn) {{
        this.cardFilter = filter;
        document.querySelectorAll('.flashcards-filters .filter-btn').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');

        if (filter === 'all') {{
          this.filteredCards = [...this.flashcards];
        }} else if (filter === 'calc') {{
          this.filteredCards = this.flashcards.filter(c => c.category.includes('Cálcul') || c.category.includes('RAID') || c.title.includes('Cálculo') || c.title.includes('Fórmula'));
        }} else {{
          this.filteredCards = this.flashcards.filter(c => c.tema === Number(filter));
        }}

        this.currentCardIndex = 0;
        this.renderCard();
        if (this.isListView) this.renderListCards();
      }},

      renderCard() {{
        if (this.filteredCards.length === 0) return;
        const card = this.filteredCards[this.currentCardIndex];
        const total = this.filteredCards.length;

        document.getElementById('cardCategory').textContent = `Tema ${{card.tema}} · ${{card.category}}`;
        document.getElementById('cardCounterText').textContent = `Tarjeta ${{this.currentCardIndex + 1}} de ${{total}}`;
        document.getElementById('cardTitle').textContent = card.title;

        const bulletsContainer = document.getElementById('cardBullets');
        bulletsContainer.innerHTML = '';
        card.bullets.forEach(b => {{
          const li = document.createElement('li');
          li.textContent = b;
          bulletsContainer.appendChild(li);
        }});

        document.getElementById('cardKey').textContent = `💡 ${{card.key}}`;
      }},

      nextCard() {{
        if (this.currentCardIndex < this.filteredCards.length - 1) {{
          this.currentCardIndex++;
        }} else {{
          this.currentCardIndex = 0;
        }}
        this.renderCard();
      }},

      prevCard() {{
        if (this.currentCardIndex > 0) {{
          this.currentCardIndex--;
        }} else {{
          this.currentCardIndex = this.filteredCards.length - 1;
        }}
        this.renderCard();
      }},

      randomCard() {{
        this.currentCardIndex = Math.floor(Math.random() * this.filteredCards.length);
        this.renderCard();
      }},

      toggleCardViewMode() {{
        this.isListView = !this.isListView;
        const btn = document.getElementById('viewModeBtn');
        const single = document.getElementById('singleCardView');
        const list = document.getElementById('listCardsView');

        if (this.isListView) {{
          btn.textContent = '🃏 Modo Tarjeta';
          single.classList.add('hidden');
          list.classList.remove('hidden');
          this.renderListCards();
        }} else {{
          btn.textContent = '📜 Ver Lista';
          single.classList.remove('hidden');
          list.classList.add('hidden');
          this.renderCard();
        }}
      }},

      renderListCards() {{
        const container = document.getElementById('listCardsView');
        container.innerHTML = '';

        this.filteredCards.forEach((card, idx) => {{
          const box = document.createElement('div');
          box.className = 'study-card';
          box.style.marginBottom = '0';

          let bulletsHtml = '';
          card.bullets.forEach(b => bulletsHtml += `<li>${{b}}</li>`);

          box.innerHTML = `
            <div class="card-meta">
              <span class="card-badge">Tema ${{card.tema}} · ${{card.category}}</span>
              <span>#${{idx + 1}}</span>
            </div>
            <div class="card-title" style="font-size:16px;">${{card.title}}</div>
            <ul class="card-bullets" style="font-size:13.5px;">${{bulletsHtml}}</ul>
            <div class="card-key-box" style="font-size:12.5px;">💡 ${{card.key}}</div>
          `;
          container.appendChild(box);
        }});
      }}
    }};

    document.addEventListener('DOMContentLoaded', () => {{
      app.init();
    }});
  </script>
</body>
</html>
'''

# Write to DISM_Examen/index.html
with open('DISM_Examen/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated DISM_Examen/index.html successfully ({len(html_content)} bytes)")
