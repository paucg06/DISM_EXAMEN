# 📱 Simulador de Exámenes DISM

> Aplicación web interactiva y autocontenida para preparar exámenes de **Dispositivos e Infraestructuras para Sistemas Multimedia (DISM)** con **348 preguntas tipo test oficiales**, explicaciones razonadas paso a paso y todos los ejercicios de desarrollo y cálculo matemático del temario.

🌐 **Demo en vivo (GitHub Pages)**: `https://paucg06.github.io/DISM_EXAMEN/`

---

## 🎯 Características Principales

- **Exámenes por Tema (30 preguntas)**:
  - **Tema 1**: Desarrollo Multiplataforma (PWA, Service Workers, Ionic, Capacitor, Flutter, React Native, .NET MAUI, KMP, Tauri, Uno Platform).
  - **Tema 2**: Infraestructuras Multimedia & Cálculos RAID / Resoluciones (Streaming ABR, Netflix Open Connect, RAID 0/1/5/6/10, XOR de paridad, vídeos 4K UHD, fotos 12/48 Mpx, audio CD/Hi-Res, MOPS/GOPS, DSP/NPU/ASIC/FPGA).
  - **Tema 3**: Dispositivos Móviles & Telefonía Celular (SoC, ARM, RISC vs CISC, redes 1G a 5G, cell splitting, sectorización, handover hard/soft, fórmulas de cluster $N=i^2+ij+j^2$, distancia cocanal $D/R$, relación $S/I$ en dB, tráfico y GoS).
  - **Tema 4**: IoT & Diseño de APIs REST (Kevin Ashton, MQTT, CoAP, OpenAPI 3.0 vs Swagger 2.0, RAML, verbos idempotentes, códigos HTTP, componentes y schemas).
- **Examen Global (40 preguntas)**:
  - Extrae exactamente **10 preguntas aleatorias de cada tema** para un simulacro equilibrado y completo.
- **Modo Práctica de Cálculos (35 preguntas)**:
  - Entrena específicamente los ejercicios numéricos que entran en la parte de desarrollo del examen.
- **Modos de Corrección**:
  - *Examen Oficial*: Sin pistas hasta finalizar (muestra nota, porcentaje, calificación y desglose por temas).
  - *Feedback Inmediato*: Muestra al instante si has acertado y despliega la explicación detallada.
- **Banco de Falladas Automático**:
  - Guarda tus fallos en `localStorage` del navegador para reintentar solo las preguntas que te cuesten.
- **100% Autocontenido y Offline**:
  - Funciona sin internet ni dependencias externas.
  - Diseño *mobile-first* optimizado para iPhone y Android (añadible a la pantalla de inicio).
  - Selector de tema Claro / Oscuro y cronómetro integrado.

---

## 📂 Estructura del Repositorio

- `index.html`: La aplicación web completa (CSS, JavaScript, banco de 348 preguntas y lógica en un solo archivo).
- `all_questions.json`: Base de datos de preguntas y explicaciones en formato JSON.
- `Tema_*.txt`: Apuntes y resúmenes completos del temario oficial (Temas 1, 2.1, 2.2, 3.1, 3.2 y 4).
- `build_html_app.py`, `build_full_database.py`: Scripts generadores y auditores del banco de preguntas.

---

## 🚀 Cómo activar GitHub Pages

1. Ve a la pestaña **Settings** de este repositorio en GitHub.
2. En el menú lateral izquierdo, haz clic en **Pages**.
3. En **Build and deployment** > **Branch**, selecciona `main` y la carpeta `/ (root)`.
4. Haz clic en **Save**. En 1 minuto tendrás la web online en:
   `https://paucg06.github.io/DISM_EXAMEN/`
