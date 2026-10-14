# -*- coding: utf-8 -*-
"""
Builds the standalone single-file HTML exam app for DISM.
"""

import json
import os

with open('DISM_Examen/all_questions.json', 'r', encoding='utf-8') as f:
    questions_data = json.load(f)

json_str = json.dumps(questions_data, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>DISM Exámenes & Test - Preparación Completa</title>
  <meta name="description" content="Simulador interactivo de exámenes de DISM con banco completo de preguntas, cálculos prácticos y explicaciones paso a paso.">
  <meta name="theme-color" content="#1e293b">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📱</text></svg>">
  <style>
    :root {{
      --bg: #0f172a;
      --card-bg: #1e293b;
      --card-border: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
      --primary-hover: #0284c7;
      --primary-light: rgba(56, 189, 248, 0.12);
      --success: #10b981;
      --success-light: rgba(16, 185, 129, 0.16);
      --danger: #f43f5e;
      --danger-light: rgba(244, 63, 94, 0.16);
      --warning: #f59e0b;
      --warning-light: rgba(245, 158, 11, 0.16);
      --accent: #818cf8;
      --radius: 14px;
      --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}

    .light-theme {{
      --bg: #f1f5f9;
      --card-bg: #ffffff;
      --card-border: #cbd5e1;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --primary-light: rgba(2, 132, 199, 0.1);
      --success: #059669;
      --success-light: rgba(5, 150, 105, 0.12);
      --danger: #e11d48;
      --danger-light: rgba(225, 29, 72, 0.12);
      --warning: #d97706;
      --warning-light: rgba(217, 119, 6, 0.12);
      --accent: #6366f1;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      font-family: var(--font);
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      transition: background-color 0.2s, color 0.2s;
    }}

    header {{
      background: var(--card-bg);
      border-bottom: 1px solid var(--card-border);
      padding: 12px 18px;
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      backdrop-filter: blur(8px);
    }}

    .logo-area {{
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
    }}

    .logo-badge {{
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: #fff;
      font-weight: 800;
      font-size: 14px;
      padding: 6px 10px;
      border-radius: 8px;
      letter-spacing: 0.5px;
    }}

    .logo-title {{
      font-size: 17px;
      font-weight: 700;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .icon-btn {{
      background: transparent;
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 7px 11px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 14px;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
    }}

    .icon-btn:hover {{
      background: var(--primary-light);
      border-color: var(--primary);
    }}

    main {{
      flex: 1;
      max-width: 900px;
      width: 100%;
      margin: 0 auto;
      padding: 18px 16px 40px;
    }}

    /* Card standard */
    .card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 20px;
      margin-bottom: 18px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }}

    /* Menu / Home Screen */
    .hero-banner {{
      text-align: center;
      padding: 28px 16px 20px;
    }}

    .hero-banner h1 {{
      font-size: 26px;
      font-weight: 800;
      margin-bottom: 8px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .hero-banner p {{
      color: var(--text-muted);
      font-size: 15px;
      max-width: 600px;
      margin: 0 auto 16px;
    }}

    .stats-pills {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 24px;
    }}

    .pill {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 500;
    }}

    .pill strong {{
      color: var(--primary);
    }}

    .section-title {{
      font-size: 17px;
      font-weight: 700;
      margin: 18px 0 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--text-main);
    }}

    .exam-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 14px;
      margin-bottom: 24px;
    }}

    .exam-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 18px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
    }}

    .exam-card:hover {{
      transform: translateY(-3px);
      border-color: var(--primary);
      box-shadow: 0 8px 20px rgba(0,0,0,0.18);
    }}

    .exam-card.featured {{
      border-color: var(--accent);
      background: linear-gradient(180deg, var(--card-bg), rgba(129, 140, 248, 0.08));
      grid-column: 1 / -1;
    }}

    .exam-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 10px;
    }}

    .exam-badge {{
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .badge-t1 {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; }}
    .badge-t2 {{ background: rgba(245, 158, 11, 0.15); color: #f59e0b; }}
    .badge-t3 {{ background: rgba(16, 185, 129, 0.15); color: #10b981; }}
    .badge-t4 {{ background: rgba(168, 85, 247, 0.15); color: #a855f7; }}
    .badge-global {{ background: rgba(236, 72, 153, 0.15); color: #ec4899; }}

    .exam-card h3 {{
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 6px;
    }}

    .exam-card p {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.4;
      margin-bottom: 14px;
    }}

    .exam-meta {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      color: var(--text-muted);
      border-top: 1px solid rgba(255,255,255,0.06);
      padding-top: 10px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: var(--primary);
      color: #0f172a;
      font-weight: 700;
      font-size: 14px;
      padding: 10px 18px;
      border-radius: 8px;
      border: none;
      cursor: pointer;
      transition: all 0.2s;
      width: 100%;
    }}

    .btn:hover {{
      background: var(--primary-hover);
      color: #ffffff;
    }}

    .btn-secondary {{
      background: transparent;
      color: var(--text-main);
      border: 1px solid var(--card-border);
    }}

    .btn-secondary:hover {{
      background: var(--card-border);
    }}

    .btn-sm {{
      padding: 6px 12px;
      font-size: 13px;
      width: auto;
    }}

    /* Active Exam View */
    .exam-header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 0 16px;
      border-bottom: 1px solid var(--card-border);
      margin-bottom: 16px;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .exam-progress-info {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 14px;
      font-weight: 600;
    }}

    .timer-badge {{
      display: flex;
      align-items: center;
      gap: 5px;
      background: var(--primary-light);
      color: var(--primary);
      padding: 5px 10px;
      border-radius: 6px;
      font-variant-numeric: tabular-nums;
      font-weight: 700;
    }}

    .progress-bar-container {{
      width: 100%;
      height: 6px;
      background: var(--card-border);
      border-radius: 3px;
      overflow: hidden;
      margin-bottom: 20px;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--primary), var(--accent));
      width: 0%;
      transition: width 0.3s ease;
    }}

    .question-box {{
      margin-bottom: 20px;
    }}

    .question-meta-tag {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      color: var(--primary);
      background: var(--primary-light);
      padding: 3px 8px;
      border-radius: 4px;
      margin-bottom: 8px;
      text-transform: uppercase;
    }}

    .question-title {{
      font-size: 17px;
      font-weight: 600;
      line-height: 1.45;
      margin-bottom: 18px;
      color: var(--text-main);
    }}

    .options-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 24px;
    }}

    .option-btn {{
      background: var(--card-bg);
      border: 1.5px solid var(--card-border);
      border-radius: 10px;
      padding: 14px 16px;
      text-align: left;
      font-size: 14px;
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      line-height: 1.4;
      transition: all 0.15s ease;
    }}

    .option-btn:hover:not(:disabled) {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}

    .option-letter {{
      font-weight: 800;
      font-size: 13px;
      background: rgba(255,255,255,0.08);
      border-radius: 6px;
      width: 26px;
      height: 26px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      color: var(--text-muted);
    }}

    .option-btn.selected {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}

    .option-btn.selected .option-letter {{
      background: var(--primary);
      color: #0f172a;
    }}

    .option-btn.correct {{
      border-color: var(--success) !important;
      background: var(--success-light) !important;
    }}

    .option-btn.correct .option-letter {{
      background: var(--success) !important;
      color: #ffffff !important;
    }}

    .option-btn.incorrect {{
      border-color: var(--danger) !important;
      background: var(--danger-light) !important;
    }}

    .option-btn.incorrect .option-letter {{
      background: var(--danger) !important;
      color: #ffffff !important;
    }}

    /* Explanation Accordion / Box */
    .explanation-box {{
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 10px;
      padding: 14px 16px;
      margin-bottom: 20px;
      font-size: 13.5px;
      line-height: 1.5;
    }}

    .explanation-box.correct-box {{
      background: var(--success-light);
      border-color: var(--success);
    }}

    .explanation-box.wrong-box {{
      background: var(--danger-light);
      border-color: var(--danger);
    }}

    .explanation-header {{
      font-weight: 700;
      font-size: 14px;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .nav-buttons {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-top: 10px;
    }}

    /* Question Navigator Drawer / Grid */
    .quick-nav-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(36px, 1fr));
      gap: 6px;
      margin-top: 14px;
      padding: 12px;
      background: rgba(0,0,0,0.15);
      border-radius: 10px;
      max-height: 160px;
      overflow-y: auto;
    }}

    .nav-circle {{
      height: 34px;
      border-radius: 8px;
      border: 1px solid var(--card-border);
      background: var(--card-bg);
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s;
    }}

    .nav-circle.current {{
      border-color: var(--primary);
      box-shadow: 0 0 0 2px var(--primary);
      color: var(--text-main);
    }}

    .nav-circle.answered {{
      background: var(--primary);
      color: #0f172a;
      border-color: var(--primary);
    }}

    .nav-circle.correct-nav {{
      background: var(--success);
      color: #fff;
      border-color: var(--success);
    }}

    .nav-circle.wrong-nav {{
      background: var(--danger);
      color: #fff;
      border-color: var(--danger);
    }}

    .nav-circle.flagged {{
      position: relative;
    }}

    .nav-circle.flagged::after {{
      content: '';
      position: absolute;
      top: 2px;
      right: 2px;
      width: 6px;
      height: 6px;
      background: var(--warning);
      border-radius: 50%;
    }}

    /* Results Screen */
    .results-card {{
      text-align: center;
      padding: 30px 20px;
    }}

    .score-circle {{
      width: 130px;
      height: 130px;
      border-radius: 50%;
      margin: 0 auto 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border: 6px solid var(--primary);
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.25);
    }}

    .score-number {{
      font-size: 36px;
      font-weight: 900;
      line-height: 1;
    }}

    .score-label {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .result-status {{
      font-size: 22px;
      font-weight: 800;
      margin-bottom: 8px;
    }}

    .theme-breakdown {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin: 24px 0;
      text-align: left;
    }}

    .theme-row {{
      background: rgba(0,0,0,0.15);
      border-radius: 8px;
      padding: 10px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13.5px;
    }}

    /* Search & Practice Mode */
    .search-input {{
      width: 100%;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 12px 16px;
      border-radius: 10px;
      font-size: 14px;
      margin-bottom: 16px;
      outline: none;
    }}

    .search-input:focus {{
      border-color: var(--primary);
    }}

    .filter-chips {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 10px;
      margin-bottom: 18px;
      -webkit-overflow-scrolling: touch;
    }}

    .chip {{
      padding: 6px 14px;
      border-radius: 20px;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      font-size: 13px;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }}

    .chip.active {{
      background: var(--primary);
      color: #0f172a;
      font-weight: 700;
      border-color: var(--primary);
    }}

    /* Utility */
    .hidden {{
      display: none !important;
    }}

    .flex-center {{
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    @media (max-width: 600px) {{
      header {{
        padding: 10px 14px;
      }}
      .logo-title {{
        font-size: 15px;
      }}
      .hero-banner h1 {{
        font-size: 22px;
      }}
      .exam-grid {{
        grid-template-columns: 1fr;
      }}
      .option-btn {{
        padding: 12px 14px;
        font-size: 13.5px;
      }}
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div class="logo-area" onclick="app.showHome()">
      <span class="logo-badge">DISM</span>
      <span class="logo-title">Exámenes DAM / DAW</span>
    </div>
    <div class="header-actions">
      <button class="icon-btn" onclick="app.togglePracticeMode()" id="practiceToggleBtn" title="Modo Práctica / Repaso">
        <span>📖</span> <span style="display:none;" class="sm-hide">Práctica</span>
      </button>
      <button class="icon-btn" onclick="app.toggleTheme()" id="themeBtn" title="Cambiar tema claro/oscuro">
        <span id="themeIcon">🌓</span>
      </button>
      <button class="icon-btn" onclick="app.showFailedQuestions()" id="failedQuestionsBtn" title="Banco de Falladas">
        <span>⚠️</span> <span id="failedCountBadge">0</span>
      </button>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <main>

    <!-- VIEW 1: HOME / MENU -->
    <section id="viewHome">
      <div class="hero-banner">
        <h1>Simulador Oficial DISM</h1>
        <p>Prepárate para el examen con preguntas extraídas del temario, ejercicios prácticos de desarrollo (RAID, bits, resoluciones, Erlangs) y exámenes tipo test reales.</p>
        
        <div class="stats-pills">
          <div class="pill">📚 Total Preguntas: <strong id="totalBankCount">320</strong></div>
          <div class="pill">⏱️ Examen Tema: <strong>30 preguntas</strong></div>
          <div class="pill">🌐 Examen Global: <strong>40 preguntas</strong> (10/tema)</div>
          <div class="pill">🎯 Modo: <strong id="modeLabel">Examen Oficial</strong></div>
        </div>
      </div>

      <!-- Settings card in menu -->
      <div class="card" style="padding: 14px 18px; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
          <div>
            <strong style="font-size: 14px;">Modo de Corrección:</strong>
            <span style="font-size: 13px; color: var(--text-muted); display: block;" id="modeDesc">Al finalizar el examen (Simulacro real)</span>
          </div>
          <div style="display: flex; gap: 8px;">
            <button class="icon-btn" id="instantFeedbackBtn" onclick="app.toggleInstantFeedback()">
              <span id="feedbackCheck">⬜</span> Feedback Inmediato
            </button>
            <button class="icon-btn" id="shuffleBtn" onclick="app.toggleShuffle()">
              <span id="shuffleCheck">☑️</span> Aleatorizar
            </button>
          </div>
        </div>
      </div>

      <div class="section-title">
        <span>🌐</span> Examen Global Multitema
      </div>
      <div class="exam-grid">
        <div class="exam-card featured" onclick="app.startExam('global')">
          <div class="exam-card-header">
            <span class="exam-badge badge-global">Examen Completo</span>
            <span style="font-size: 18px;">🔥</span>
          </div>
          <h3>Examen Global (Temas 1, 2, 3 y 4)</h3>
          <p>Simulacro definitivo de examen: engloba los 4 temas con exactamente 10 preguntas aleatorias de cada tema (40 preguntas en total), incluyendo teoría y ejercicios de desarrollo/cálculos.</p>
          <div class="exam-meta">
            <span>📝 40 Preguntas (10 por tema)</span>
            <button class="btn btn-sm">Comenzar Global →</button>
          </div>
        </div>
      </div>

      <div class="section-title">
        <span>📂</span> Exámenes Monográficos por Tema (30 preguntas)
      </div>
      <div class="exam-grid">
        <!-- Tema 1 -->
        <div class="exam-card" onclick="app.startExam(1)">
          <div class="exam-card-header">
            <span class="exam-badge badge-t1">Tema 1</span>
            <span style="font-size: 18px;">📱</span>
          </div>
          <h3>Tema 1: Desarrollo Multiplataforma</h3>
          <p>Ecosistema móvil, apps nativas vs híbridas vs PWA, Ionic, Capacitor, Service Workers, .NET MAUI, Flutter, React Native, KMP y Tauri.</p>
          <div class="exam-meta">
            <span>📝 30 preguntas de <span id="t1Bank">60</span></span>
            <span style="color:var(--primary); font-weight:700;">Empezar →</span>
          </div>
        </div>

        <!-- Tema 2 -->
        <div class="exam-card" onclick="app.startExam(2)">
          <div class="exam-card-header">
            <span class="exam-badge badge-t2">Tema 2</span>
            <span style="font-size: 18px;">🎬</span>
          </div>
          <h3>Tema 2: Infraestructuras Multimedia & Cálculos</h3>
          <p>Sistemas multimedia, streaming VOD/OTT, CDN Netflix, <strong>cálculos RAID (0, 1, 5, 6, 10, XOR)</strong>, <strong>cálculos de resoluciones de imagen, vídeo 4K y audio</strong>, y QoS.</p>
          <div class="exam-meta">
            <span>📝 30 preguntas de <span id="t2Bank">75</span></span>
            <span style="color:var(--warning); font-weight:700;">Empezar →</span>
          </div>
        </div>

        <!-- Tema 3 -->
        <div class="exam-card" onclick="app.startExam(3)">
          <div class="exam-card-header">
            <span class="exam-badge badge-t3">Tema 3</span>
            <span style="font-size: 18px;">📡</span>
          </div>
          <h3>Tema 3: Dispositivos & Telefonía Móvil</h3>
          <p>Hardware móvil (SoC, ARM, RISC vs CISC), redes celulares (GSM a 5G), <strong>cálculos de clusters N=i²+ij+j²</strong>, <strong>cálculos de tráfico en Erlangs</strong>, GoS y relación S/I.</p>
          <div class="exam-meta">
            <span>📝 30 preguntas de <span id="t3Bank">130</span></span>
            <span style="color:var(--success); font-weight:700;">Empezar →</span>
          </div>
        </div>

        <!-- Tema 4 -->
        <div class="exam-card" onclick="app.startExam(4)">
          <div class="exam-card-header">
            <span class="exam-badge badge-t4">Tema 4</span>
            <span style="font-size: 18px;">🌐</span>
          </div>
          <h3>Tema 4: IoT & Diseño de APIs REST</h3>
          <p>Internet of Things (sensores, actuadores, MQTT, CoAP), diseño de APIs REST (métodos HTTP, códigos estado), Swagger 2.0 vs OpenAPI 3.0, RAML y componentes.</p>
          <div class="exam-meta">
            <span>📝 30 preguntas de <span id="t4Bank">55</span></span>
            <span style="color:var(--accent); font-weight:700;">Empezar →</span>
          </div>
        </div>
      </div>

      <!-- Quick Practice Options -->
      <div class="card" style="margin-top: 20px;">
        <h4 style="margin-bottom: 8px;">🚀 Modos de Aprendizaje Rápido</h4>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <button class="btn btn-secondary btn-sm" onclick="app.startCalculationsOnly()">
            🧮 Solo Ejercicios de Cálculo (RAID, Resoluciones, Erlangs)
          </button>
          <button class="btn btn-secondary btn-sm" onclick="app.showFailedQuestions()">
            ⚠️ Repasar Preguntas Falladas (<span id="failedCountText">0</span>)
          </button>
          <button class="btn btn-secondary btn-sm" onclick="app.togglePracticeMode()">
            🔍 Explorar Banco Completo
          </button>
        </div>
      </div>
    </section>

    <!-- VIEW 2: ACTIVE EXAM -->
    <section id="viewExam" class="hidden">
      <div class="card">
        <div class="exam-header-bar">
          <div class="exam-progress-info">
            <button class="icon-btn btn-sm" onclick="app.confirmExitExam()">✕ Salir</button>
            <span id="examTitleBadge" class="exam-badge badge-global">Examen</span>
            <span id="questionCounter">Pregunta 1 de 30</span>
          </div>
          <div style="display:flex; align-items:center; gap:8px;">
            <button class="icon-btn btn-sm" onclick="app.toggleFlagCurrent()" id="flagBtn" title="Marcar para revisar">
              🚩 <span style="display:none;" class="sm-hide">Marcar</span>
            </button>
            <div class="timer-badge">
              <span>⏱️</span> <span id="examTimer">00:00</span>
            </div>
          </div>
        </div>

        <div class="progress-bar-container">
          <div class="progress-bar-fill" id="progressBarFill"></div>
        </div>

        <!-- Question content -->
        <div class="question-box">
          <div class="question-meta-tag" id="qSubtema">Subtema</div>
          <div class="question-title" id="qText">Texto de la pregunta aquí...</div>
          
          <div class="options-list" id="optionsContainer">
            <!-- Options dynamically inserted -->
          </div>

          <!-- Explanation box (shown in instant feedback or review mode) -->
          <div class="explanation-box hidden" id="explanationBox">
            <div class="explanation-header">
              <span id="explanationIcon">💡</span>
              <span id="explanationTitle">Explicación y Resolución:</span>
            </div>
            <div id="explanationText" style="white-space: pre-line;"></div>
          </div>
        </div>

        <!-- Navigation buttons -->
        <div class="nav-buttons">
          <button class="btn btn-secondary btn-sm" onclick="app.prevQuestion()" id="prevBtn">
            ← Anterior
          </button>
          
          <div style="display:flex; gap:8px;">
            <button class="btn btn-secondary btn-sm" onclick="app.toggleGridDrawer()">
              📑 Índice
            </button>
            <button class="btn btn-sm" onclick="app.nextQuestion()" id="nextBtn" style="min-width: 110px;">
              Siguiente →
            </button>
          </div>
        </div>

        <!-- Quick navigation drawer / grid -->
        <div id="gridDrawer" class="hidden">
          <div class="quick-nav-grid" id="navGridContainer">
            <!-- Circles dynamically inserted -->
          </div>
        </div>
      </div>
    </section>

    <!-- VIEW 3: RESULTS SCREEN -->
    <section id="viewResults" class="hidden">
      <div class="card results-card">
        <div class="score-circle" id="scoreCircle">
          <div class="score-number" id="scorePercent">0%</div>
          <div class="score-label" id="scorePoints">0 / 30</div>
        </div>

        <div class="result-status" id="resultStatus">¡Examen Completado!</div>
        <p id="resultFeedback" style="color: var(--text-muted); font-size: 14.5px; max-width: 500px; margin: 0 auto 20px;">
          Resumen de tu rendimiento en este examen.
        </p>

        <!-- Breakdown by topic -->
        <div class="theme-breakdown" id="themeBreakdownContainer">
          <!-- Dynamically inserted -->
        </div>

        <div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-top: 24px;">
          <button class="btn btn-sm" onclick="app.reviewExamAnswers()" style="width: auto; min-width: 160px;">
            🔍 Revisar Respuestas
          </button>
          <button class="btn btn-secondary btn-sm" onclick="app.retryExam()" style="width: auto;">
            🔄 Repetir Examen
          </button>
          <button class="btn btn-secondary btn-sm" onclick="app.retryFailedOnly()" id="retryFailedBtn" style="width: auto;">
            ⚠️ Reintentar Falladas
          </button>
          <button class="btn btn-secondary btn-sm" onclick="app.showHome()" style="width: auto;">
            🏠 Volver al Menú
          </button>
        </div>
      </div>
    </section>

    <!-- VIEW 4: PRACTICE / EXPLORER / FAILED QUESTIONS -->
    <section id="viewPractice" class="hidden">
      <div class="card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <h2 style="font-size: 18px;" id="practiceHeaderTitle">Explorador del Banco de Preguntas</h2>
          <button class="btn btn-secondary btn-sm" onclick="app.showHome()">✕ Volver</button>
        </div>

        <input type="text" id="practiceSearch" class="search-input" placeholder="🔍 Buscar por palabra clave (ej. RAID, Erlangs, Flutter, OpenAPI, 4K, GHz...)" oninput="app.filterPracticeList()">

        <div class="filter-chips">
          <button class="chip active" onclick="app.setPracticeFilter('all', this)">Todas (<span id="countAll">0</span>)</button>
          <button class="chip" onclick="app.setPracticeFilter(1, this)">Tema 1 (<span id="countT1">0</span>)</button>
          <button class="chip" onclick="app.setPracticeFilter(2, this)">Tema 2 (<span id="countT2">0</span>)</button>
          <button class="chip" onclick="app.setPracticeFilter(3, this)">Tema 3 (<span id="countT3">0</span>)</button>
          <button class="chip" onclick="app.setPracticeFilter(4, this)">Tema 4 (<span id="countT4">0</span>)</button>
          <button class="chip" onclick="app.setPracticeFilter('calc', this)">🧮 Solo Cálculos</button>
          <button class="chip" onclick="app.setPracticeFilter('failed', this)">⚠️ Falladas (<span id="countFailedChip">0</span>)</button>
        </div>

        <div id="practiceListContainer" style="display: flex; flex-direction: column; gap: 14px;">
          <!-- List of cards dynamically rendered -->
        </div>
      </div>
    </section>

  </main>

  <footer style="text-align: center; padding: 20px 10px; font-size: 12.5px; color: var(--text-muted); border-top: 1px solid var(--card-border);">
    Simulador de Examen DISM · 320 Preguntas Oficiales con Cálculos & Temario Completo · Listo para Móvil y GitHub Pages
  </footer>

  <!-- CORE LOGIC & DATA -->
  <script>
    // Embedded question database
    const ALL_QUESTIONS = {json_str};

    const app = {{
      questions: ALL_QUESTIONS,
      currentExam: null,
      currentIndex: 0,
      userAnswers: {{}},
      flags: {{}},
      examTimerInterval: null,
      examSeconds: 0,
      instantFeedback: false,
      shuffleEnabled: true,
      failedQuestions: new Set(),
      isReviewMode: false,
      practiceFilter: 'all',

      init() {{
        // Load stored failed questions and settings
        try {{
          const storedFailed = localStorage.getItem('dism_failed_questions');
          if (storedFailed) {{
            this.failedQuestions = new Set(JSON.parse(storedFailed));
          }}
          const storedInstant = localStorage.getItem('dism_instant_feedback');
          if (storedInstant !== null) {{
            this.instantFeedback = storedInstant === 'true';
          }}
          const storedTheme = localStorage.getItem('dism_theme');
          if (storedTheme === 'light') {{
            document.body.classList.add('light-theme');
          }}
        }} catch(e) {{}}

        this.updateCounts();
        this.updateSettingsUI();
      }},

      toggleTheme() {{
        document.body.classList.toggle('light-theme');
        const isLight = document.body.classList.contains('light-theme');
        try {{ localStorage.setItem('dism_theme', isLight ? 'light' : 'dark'); }} catch(e) {{}}
      }},

      toggleInstantFeedback() {{
        this.instantFeedback = !this.instantFeedback;
        try {{ localStorage.setItem('dism_instant_feedback', this.instantFeedback); }} catch(e) {{}}
        this.updateSettingsUI();
      }},

      toggleShuffle() {{
        this.shuffleEnabled = !this.shuffleEnabled;
        this.updateSettingsUI();
      }},

      updateSettingsUI() {{
        const btn = document.getElementById('instantFeedbackBtn');
        const check = document.getElementById('feedbackCheck');
        const desc = document.getElementById('modeDesc');
        const label = document.getElementById('modeLabel');
        const shuffleCheck = document.getElementById('shuffleCheck');

        if (this.instantFeedback) {{
          check.textContent = '☑️';
          desc.textContent = 'Modo Aprendizaje: Respuesta inmediata tras elegir opción';
          label.textContent = 'Modo Aprendizaje';
        }} else {{
          check.textContent = '⬜';
          desc.textContent = 'Simulacro Real: Resultados y corrección al finalizar';
          label.textContent = 'Examen Oficial';
        }}

        shuffleCheck.textContent = this.shuffleEnabled ? '☑️' : '⬜';
      }},

      updateCounts() {{
        document.getElementById('totalBankCount').textContent = this.questions.length;
        document.getElementById('t1Bank').textContent = this.questions.filter(q => q.tema === 1).length;
        document.getElementById('t2Bank').textContent = this.questions.filter(q => q.tema === 2).length;
        document.getElementById('t3Bank').textContent = this.questions.filter(q => q.tema === 3).length;
        document.getElementById('t4Bank').textContent = this.questions.filter(q => q.tema === 4).length;

        const failedCount = this.failedQuestions.size;
        document.getElementById('failedCountBadge').textContent = failedCount;
        document.getElementById('failedCountText').textContent = failedCount;
        const chip = document.getElementById('countFailedChip');
        if (chip) chip.textContent = failedCount;
      }},

      saveFailedQuestions() {{
        try {{
          localStorage.setItem('dism_failed_questions', JSON.stringify(Array.from(this.failedQuestions)));
        }} catch(e) {{}}
        this.updateCounts();
      }},

      showView(viewId) {{
        ['viewHome', 'viewExam', 'viewResults', 'viewPractice'].forEach(id => {{
          document.getElementById(id).classList.add('hidden');
        }});
        document.getElementById(viewId).classList.remove('hidden');
        window.scrollTo(0, 0);
      }},

      showHome() {{
        if (this.examTimerInterval) clearInterval(this.examTimerInterval);
        this.showView('viewHome');
      }},

      // Shuffle helper
      shuffleArray(arr) {{
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
        let badgeClass = 'badge-global';

        if (type === 'global') {{
          title = 'Examen Global (Temas 1 al 4)';
          badgeClass = 'badge-global';
          // Exactly 10 questions per topic
          const t1 = this.shuffleArray(this.questions.filter(q => q.tema === 1)).slice(0, 10);
          const t2 = this.shuffleArray(this.questions.filter(q => q.tema === 2)).slice(0, 10);
          const t3 = this.shuffleArray(this.questions.filter(q => q.tema === 3)).slice(0, 10);
          const t4 = this.shuffleArray(this.questions.filter(q => q.tema === 4)).slice(0, 10);
          pool = [...t1, ...t2, ...t3, ...t4];
          if (this.shuffleEnabled) {{
            pool = this.shuffleArray(pool);
          }}
        }} else if (typeof type === 'number') {{
          title = `Examen Tema ${{type}}`;
          badgeClass = `badge-t${{type}}`;
          const temaPool = this.questions.filter(q => q.tema === type);
          pool = this.shuffleEnabled ? this.shuffleArray(temaPool).slice(0, 30) : temaPool.slice(0, 30);
        }}

        this.setupExam(pool, title, badgeClass);
      }},

      startCalculationsOnly() {{
        const calcQuestions = this.questions.filter(q => 
          q.q.toUpperCase().includes('EJERCICIO') || 
          q.q.toUpperCase().includes('CÁLCUL') || 
          q.q.toUpperCase().includes('CALCULA') ||
          (q.subtema && q.subtema.includes('Cálcul'))
        );
        const pool = this.shuffleEnabled ? this.shuffleArray(calcQuestions) : calcQuestions;
        this.setupExam(pool, 'Ejercicios de Cálculo (RAID, Bits, Erlangs)', 'badge-t2');
      }},

      setupExam(pool, title, badgeClass) {{
        this.currentExam = {{
          title: title,
          badgeClass: badgeClass,
          questions: pool
        }};
        this.currentIndex = 0;
        this.userAnswers = {{}};
        this.flags = {{}};
        this.isReviewMode = false;

        // Timer
        this.examSeconds = 0;
        if (this.examTimerInterval) clearInterval(this.examTimerInterval);
        this.examTimerInterval = setInterval(() => {{
          this.examSeconds++;
          const mins = String(Math.floor(this.examSeconds / 60)).padStart(2, '0');
          const secs = String(this.examSeconds % 60).padStart(2, '0');
          document.getElementById('examTimer').textContent = `${{mins}}:${{secs}}`;
        }}, 1000);

        const badge = document.getElementById('examTitleBadge');
        badge.className = `exam-badge ${{badgeClass}}`;
        badge.textContent = title;

        this.showView('viewExam');
        this.renderQuestion();
        this.renderGrid();
      }},

      renderQuestion() {{
        const q = this.currentExam.questions[this.currentIndex];
        const total = this.currentExam.questions.length;

        document.getElementById('questionCounter').textContent = `Pregunta ${{this.currentIndex + 1}} de ${{total}}`;
        document.getElementById('progressBarFill').style.width = `${{((this.currentIndex + 1) / total) * 100}}%`;
        
        document.getElementById('qSubtema').textContent = `${{q.subtema || 'Tema ' + q.tema}} · ID: ${{q.id}}`;
        document.getElementById('qText').textContent = q.q;

        // Flag button
        const flagBtn = document.getElementById('flagBtn');
        flagBtn.style.color = this.flags[this.currentIndex] ? 'var(--warning)' : 'inherit';

        // Prev button state
        document.getElementById('prevBtn').disabled = this.currentIndex === 0;

        // Next button text
        const nextBtn = document.getElementById('nextBtn');
        if (this.currentIndex === total - 1) {{
          nextBtn.textContent = this.isReviewMode ? 'Volver a Resultados' : 'Finalizar Examen ✔';
        }} else {{
          nextBtn.textContent = 'Siguiente →';
        }}

        // Render options
        const container = document.getElementById('optionsContainer');
        container.innerHTML = '';

        const letters = ['A', 'B', 'C', 'D'];
        const selectedIdx = this.userAnswers[this.currentIndex];
        const showSolution = this.isReviewMode || (this.instantFeedback && selectedIdx !== undefined);

        q.options.forEach((optText, i) => {{
          const btn = document.createElement('button');
          btn.className = 'option-btn';

          if (selectedIdx === i) btn.classList.add('selected');

          if (showSolution) {{
            btn.disabled = true;
            if (i === q.correct) {{
              btn.classList.add('correct');
            }} else if (selectedIdx === i && selectedIdx !== q.correct) {{
              btn.classList.add('incorrect');
            }}
          }} else {{
            btn.onclick = () => this.selectOption(i);
          }}

          btn.innerHTML = `
            <span class="option-letter">${{letters[i]}}</span>
            <span style="flex:1;">${{optText}}</span>
          `;
          container.appendChild(btn);
        }});

        // Render explanation
        const expBox = document.getElementById('explanationBox');
        if (showSolution) {{
          expBox.classList.remove('hidden');
          const isCorrect = selectedIdx === q.correct;
          expBox.className = 'explanation-box ' + (isCorrect ? 'correct-box' : 'wrong-box');
          document.getElementById('explanationIcon').textContent = isCorrect ? '✅' : '❌';
          document.getElementById('explanationTitle').textContent = isCorrect ? '¡Correcto! Explicación:' : '¡Incorrecto! Solución correcta:';
          document.getElementById('explanationText').textContent = q.explanation || `La respuesta correcta es: ${{q.options[q.correct]}}`;
        }} else {{
          expBox.classList.add('hidden');
        }}

        this.updateGridItem(this.currentIndex);
      }},

      selectOption(index) {{
        this.userAnswers[this.currentIndex] = index;
        const q = this.currentExam.questions[this.currentIndex];

        // Track failed questions
        if (index !== q.correct) {{
          this.failedQuestions.add(q.id);
        }} else {{
          // If answered correctly, we can keep or leave in failed
        }}
        this.saveFailedQuestions();

        this.renderQuestion();
        this.renderGrid();
      }},

      nextQuestion() {{
        if (this.currentIndex < this.currentExam.questions.length - 1) {{
          this.currentIndex++;
          this.renderQuestion();
          window.scrollTo(0, 0);
        }} else {{
          if (this.isReviewMode) {{
            this.showView('viewResults');
          }} else {{
            this.finishExam();
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

      toggleFlagCurrent() {{
        this.flags[this.currentIndex] = !this.flags[this.currentIndex];
        this.renderQuestion();
        this.renderGrid();
      }},

      toggleGridDrawer() {{
        const drawer = document.getElementById('gridDrawer');
        drawer.classList.toggle('hidden');
      }},

      renderGrid() {{
        const grid = document.getElementById('navGridContainer');
        grid.innerHTML = '';
        this.currentExam.questions.forEach((q, idx) => {{
          const item = document.createElement('div');
          item.className = 'nav-circle';
          item.textContent = idx + 1;

          if (idx === this.currentIndex) item.classList.add('current');
          if (this.flags[idx]) item.classList.add('flagged');

          const ans = this.userAnswers[idx];
          if (ans !== undefined) {{
            if (this.isReviewMode || this.instantFeedback) {{
              if (ans === q.correct) item.classList.add('correct-nav');
              else item.classList.add('wrong-nav');
            }} else {{
              item.classList.add('answered');
            }}
          }}

          item.onclick = () => {{
            this.currentIndex = idx;
            this.renderQuestion();
          }};
          grid.appendChild(item);
        }});
      }},

      updateGridItem(idx) {{
        // Lightweight update
        const circles = document.querySelectorAll('.nav-circle');
        if (circles[idx]) {{
          circles.forEach((c, i) => {{
            if (i === idx) c.classList.add('current');
            else c.classList.remove('current');
          }});
        }}
      }},

      confirmExitExam() {{
        if (confirm('¿Deseas salir del examen actual? El progreso no guardado se perderá.')) {{
          this.showHome();
        }}
      }},

      finishExam() {{
        if (this.examTimerInterval) clearInterval(this.examTimerInterval);

        let correctCount = 0;
        const total = this.currentExam.questions.length;
        const themeStats = {{ 1: {{ c: 0, t: 0 }}, 2: {{ c: 0, t: 0 }}, 3: {{ c: 0, t: 0 }}, 4: {{ c: 0, t: 0 }} }};

        this.currentExam.questions.forEach((q, idx) => {{
          const ans = this.userAnswers[idx];
          const isCorrect = ans === q.correct;
          if (isCorrect) correctCount++;
          else this.failedQuestions.add(q.id);

          if (themeStats[q.tema]) {{
            themeStats[q.tema].t++;
            if (isCorrect) themeStats[q.tema].c++;
          }}
        }});

        this.saveFailedQuestions();

        const pct = Math.round((correctCount / total) * 100);
        document.getElementById('scorePercent').textContent = `${{pct}}%`;
        document.getElementById('scorePoints').textContent = `${{correctCount}} / ${{total}}`;

        const circle = document.getElementById('scoreCircle');
        const status = document.getElementById('resultStatus');
        const feedback = document.getElementById('resultFeedback');

        if (pct >= 90) {{
          circle.style.borderColor = 'var(--success)';
          status.textContent = '🌟 ¡Sobresaliente!';
          feedback.textContent = '¡Dominio total del temario y de los ejercicios de cálculo!';
        }} else if (pct >= 70) {{
          circle.style.borderColor = 'var(--primary)';
          status.textContent = '👏 ¡Notable!';
          feedback.textContent = 'Muy buen examen. Revisa los pocos fallos cometidos para asegurar el 10.';
        }} else if (pct >= 50) {{
          circle.style.borderColor = 'var(--warning)';
          status.textContent = '👍 Aprobado';
          feedback.textContent = 'Has superado el examen, pero conviene repasar los temas más flojos y los cálculos.';
        }} else {{
          circle.style.borderColor = 'var(--danger)';
          status.textContent = '📚 Necesitas Repasar';
          feedback.textContent = 'No te desanimes. Revisa las explicaciones de cada pregunta y vuelve a intentarlo.';
        }}

        // Render theme breakdown
        const breakdown = document.getElementById('themeBreakdownContainer');
        breakdown.innerHTML = '<h4 style="margin-bottom:8px;">Desglose por Temas:</h4>';
        
        const themeNames = {{
          1: 'Tema 1: Multiplataforma (PWA, Ionic, Flutter, React Native, MAUI)',
          2: 'Tema 2: Multimedia & Cálculos RAID / Resoluciones',
          3: 'Tema 3: Hardware Móvil & Cálculos Telefonía (Clusters, Erlangs)',
          4: 'Tema 4: IoT & Diseño APIs REST (OpenAPI 3.0 / Swagger)'
        }};

        Object.keys(themeStats).forEach(t => {{
          const data = themeStats[t];
          if (data.t > 0) {{
            const row = document.createElement('div');
            row.className = 'theme-row';
            const rowPct = Math.round((data.c / data.t) * 100);
            row.innerHTML = `
              <div>
                <strong>${{themeNames[t]}}</strong>
              </div>
              <div style="font-weight:700; color:${{rowPct >= 50 ? 'var(--success)' : 'var(--danger)'}}">
                ${{data.c}} / ${{data.t}} (${{rowPct}}%)
              </div>
            `;
            breakdown.appendChild(row);
          }}
        }});

        // Show/hide retry failed button
        const failedInExam = total - correctCount;
        document.getElementById('retryFailedBtn').style.display = failedInExam > 0 ? 'inline-flex' : 'none';

        this.showView('viewResults');
      }},

      reviewExamAnswers() {{
        this.isReviewMode = true;
        this.currentIndex = 0;
        this.showView('viewExam');
        this.renderQuestion();
        this.renderGrid();
      }},

      retryExam() {{
        this.setupExam(this.currentExam.questions, this.currentExam.title, this.currentExam.badgeClass);
      }},

      retryFailedOnly() {{
        const failedInExam = this.currentExam.questions.filter((q, idx) => {{
          return this.userAnswers[idx] !== q.correct;
        }});
        if (failedInExam.length === 0) {{
          alert('¡No tuviste ningún fallo en este examen!');
          return;
        }}
        this.setupExam(failedInExam, 'Repaso de Falladas del Examen', 'badge-t2');
      }},

      // Practice & Explorer Mode
      togglePracticeMode() {{
        this.showView('viewPractice');
        document.getElementById('practiceHeaderTitle').textContent = 'Explorador del Banco Completo de Preguntas';
        this.setPracticeFilter('all');
      }},

      showFailedQuestions() {{
        if (this.failedQuestions.size === 0) {{
          alert('¡Enhorabuena! Todavía no tienes preguntas registradas como falladas.');
          return;
        }}
        this.showView('viewPractice');
        document.getElementById('practiceHeaderTitle').textContent = `Banco de Preguntas Falladas (${{this.failedQuestions.size}})`;
        this.setPracticeFilter('failed');
      }},

      setPracticeFilter(filter, chipElement) {{
        this.practiceFilter = filter;
        document.querySelectorAll('.filter-chips .chip').forEach(c => c.classList.remove('active'));
        if (chipElement) chipElement.classList.add('active');

        // Update counts
        document.getElementById('countAll').textContent = this.questions.length;
        document.getElementById('countT1').textContent = this.questions.filter(q => q.tema === 1).length;
        document.getElementById('countT2').textContent = this.questions.filter(q => q.tema === 2).length;
        document.getElementById('countT3').textContent = this.questions.filter(q => q.tema === 3).length;
        document.getElementById('countT4').textContent = this.questions.filter(q => q.tema === 4).length;
        document.getElementById('countFailedChip').textContent = this.failedQuestions.size;

        this.filterPracticeList();
      }},

      filterPracticeList() {{
        const query = (document.getElementById('practiceSearch').value || '').toLowerCase().trim();
        let list = [...this.questions];

        if (this.practiceFilter === 'all') {{
          // no filter
        }} else if (this.practiceFilter === 'failed') {{
          list = list.filter(q => this.failedQuestions.has(q.id));
        }} else if (this.practiceFilter === 'calc') {{
          list = list.filter(q => 
            q.q.toUpperCase().includes('EJERCICIO') || 
            q.q.toUpperCase().includes('CÁLCUL') || 
            q.q.toUpperCase().includes('CALCULA') ||
            (q.subtema && q.subtema.includes('Cálcul'))
          );
        }} else {{
          list = list.filter(q => q.tema === Number(this.practiceFilter));
        }}

        if (query) {{
          list = list.filter(q => 
            q.q.toLowerCase().includes(query) ||
            q.options.some(o => o.toLowerCase().includes(query)) ||
            (q.subtema && q.subtema.toLowerCase().includes(query)) ||
            (q.explanation && q.explanation.toLowerCase().includes(query))
          );
        }}

        const container = document.getElementById('practiceListContainer');
        container.innerHTML = '';

        if (list.length === 0) {{
          container.innerHTML = `<div style="text-align:center; padding:30px; color:var(--text-muted);">No se encontraron preguntas con los filtros seleccionados.</div>`;
          return;
        }}

        const letters = ['A', 'B', 'C', 'D'];

        list.slice(0, 80).forEach((q) => {{
          const card = document.createElement('div');
          card.className = 'card';
          card.style.marginBottom = '12px';
          card.style.padding = '16px';

          const isFailed = this.failedQuestions.has(q.id);

          let optionsHtml = '';
          q.options.forEach((opt, idx) => {{
            const isCorrect = idx === q.correct;
            optionsHtml += `
              <div style="display:flex; align-items:flex-start; gap:8px; padding:6px 10px; border-radius:6px; margin-bottom:4px; font-size:13.5px; background:${{isCorrect ? 'var(--success-light)' : 'rgba(0,0,0,0.06)'}}; border: 1px solid ${{isCorrect ? 'var(--success)' : 'transparent'}}">
                <strong>${{letters[idx]}})</strong>
                <span style="flex:1; color:${{isCorrect ? 'var(--success)' : 'inherit'}}">${{opt}} ${{isCorrect ? '✅' : ''}}</span>
              </div>
            `;
          }});

          card.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="question-meta-tag">Tema ${{q.tema}} · ${{q.subtema || ''}} · ${{q.id}}</span>
              <div>
                ${{isFailed ? '<span style="font-size:11px; background:var(--danger-light); color:var(--danger); padding:2px 8px; border-radius:4px; font-weight:700;">Fallada</span>' : ''}}
              </div>
            </div>
            <div style="font-weight:600; font-size:15px; margin-bottom:12px; line-height:1.4;">${{q.q}}</div>
            <div style="margin-bottom:12px;">${{optionsHtml}}</div>
            <div class="explanation-box" style="margin-bottom:0; padding:10px 14px; font-size:13px;">
              <strong>💡 Explicación / Resolución:</strong><br>
              <span style="white-space: pre-line;">${{q.explanation || 'Respuesta según el temario oficial.'}}</span>
            </div>
          `;
          container.appendChild(card);
        }});

        if (list.length > 80) {{
          const note = document.createElement('div');
          note.style.textAlign = 'center';
          note.style.color = 'var(--text-muted)';
          note.style.fontSize = '13px';
          note.textContent = `Mostrando las primeras 80 de ${{list.length}} preguntas. Usa el buscador para filtrar más específicamente.`;
          container.appendChild(note);
        }}
      }}
    }};

    document.addEventListener('DOMContentLoaded', () => {{
      app.init();
    }});
  </script>
</body>
</html>
'''

# Write to root index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

# Also write to DISM_Examen/examen_dism.html and DISM_Examen/index.html
with open('DISM_Examen/examen_dism.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

with open('DISM_Examen/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Generated index.html and DISM_Examen/examen_dism.html successfully!")
print(f"File size: {len(html_template)} bytes")
