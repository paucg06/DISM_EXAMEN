# -*- coding: utf-8 -*-
"""
Flashcards data for DISM exam preparation.
Focused strictly on the syllabus for the official exam (Topics 1, 2, and 3).
"""

def get_flashcards():
    return [
        # ==========================================
        # TEMA 1: FRAMEWORKS (HÍBRIDO VS NATIVO)
        # ==========================================
        {
            "tema": 1,
            "category": "Frameworks",
            "title": "Apps Híbridas vs Nativas (Clave Examen)",
            "bullets": [
                "Apps Híbridas: Se ejecutan dentro de un WebView o contenedor web usando HTML, CSS y JavaScript. Requieren plugins/bridges para acceder al hardware del móvil.",
                "Apps Nativas: Se compilan y ejecutan directamente sobre el sistema operativo, interactuando directamente con las APIs y componentes nativos.",
                "Clasificación Oficial del Temario: Son Híbridas: Apache Cordova, Ionic y Unity (por requerir contenedor/runtime). Son Nativas: React Native, NativeScript, Xamarin y .NET MAUI."
            ],
            "key": "Híbrido = WebView / Contenedor. Nativo = Ejecución directa en SO sin WebView."
        },
        {
            "tema": 1,
            "category": "Frameworks",
            "title": "Catálogo de Frameworks por Nombre Propio",
            "bullets": [
                "Apache Cordova / PhoneGap: Híbrido histórico (HTML/CSS/JS en WebView con plugins).",
                "Ionic + Capacitor: Híbrido moderno (Web Components en WebView con puente nativo).",
                "React Native: Nativo (lógica en JavaScript, pero UI renderizada con componentes nativos de iOS y Android).",
                "Flutter: Nativo (lenguaje Dart, motor gráfico propio en canvas nativo a 60/120 fps sin WebView ni widgets del SO).",
                "Xamarin / .NET MAUI: Nativo (lenguaje C# y XAML, compila a código nativo en cada plataforma).",
                "NativeScript: Nativo (código JS/TS con mapeo directo a APIs nativas de iOS/Android).",
                "Kotlin Multiplatform (KMP): Nativo (comparte lógica en Kotlin compilando a nativo en iOS y JVM en Android)."
            ],
            "key": "Memoriza: Ionic/Cordova/Unity -> HÍBRIDOS. React Native/Flutter/MAUI/Xamarin/NativeScript/KMP -> NATIVOS."
        },
        {
            "tema": 1,
            "category": "Frameworks",
            "title": "Ventajas e Inconvenientes: Nativo vs Híbrido",
            "bullets": [
                "Nativo: Máximo rendimiento, fluidez en gráficos/animaciones complejas y acceso directo a sensores/cámara. Desventaja: Mayor coste y duplicidad de equipos de desarrollo.",
                "Híbrido: Menor tiempo de desarrollo (Time-to-Market) y menor coste al compartir una sola base de código web. Desventaja: Rendimiento inferior en WebView y dependencia de plugins para el hardware."
            ],
            "key": "Regla: Nativo para rendimiento extremo; Híbrido para rapidez de lanzamiento y bajo coste."
        },

        # ==========================================
        # TEMA 2: STREAMING, RAID, FORMATOS Y ARQUITECTURA
        # ==========================================
        {
            "tema": 2,
            "category": "Streaming",
            "title": "Streaming vs Descarga y Modelos OTT",
            "bullets": [
                "Streaming: Reproducción continua sin esperar a completar la descarga; los datos se almacenan en un buffer temporal y se descartan tras verse (no guarda archivo permanente).",
                "Live Streaming vs VOD: Live es emisión en directo con retraso mínimo y sin control de avance rápido; VOD (Video on Demand) permite pausar, rebobinar y elegir el momento.",
                "Modelos OTT: AVOD (gratuito con publicidad, ej. YouTube gratis), SVOD (suscripción periódica, ej. Netflix), TVOD / PPV (alquiler puntual o pago por evento único)."
            ],
            "key": "Streaming = buffer temporal en RAM sin copia permanente en disco local."
        },
        {
            "tema": 2,
            "category": "Streaming",
            "title": "Arquitectura Streaming, ABR y Protocolos",
            "bullets": [
                "ABR (Adaptive Bitrate): El vídeo se divide en fragmentos cortos (2-10 s) a múltiples calidades/bitrates. El cliente conmuta dinámicamente según ancho de banda y CPU.",
                "HLS (HTTP Live Streaming de Apple) y MPEG-DASH (estándar ISO abierto): Ambos usan HTTP y TCP mediante manifiestos (.m3u8 en HLS, .mpd en DASH).",
                "RTSP (Real-Time Streaming Protocol): Protocolo de control de sesión (Play, Pause, Record, Teardown) actuando como mando a distancia de red.",
                "RTP (Real-time Transport Protocol) sobre UDP: Envía los paquetes de medios con marcas de tiempo (timestamp) y números de secuencia.",
                "Proxy de Streaming: Servidor intermedio que almacena segmentos en caché, reduciendo el tráfico saliente del servidor principal y la latencia."
            ],
            "key": "RTSP controla sesión. RTP transmite medios sobre UDP. HLS/DASH usan HTTP/TCP con ABR."
        },
        {
            "tema": 2,
            "category": "RAID",
            "title": "Matrices RAID: Fórmulas y Tolerancia a Fallos",
            "bullets": [
                "RAID 0 (Striping): Capacidad = N * C. Tolera 0 fallos (si falla 1 disco, se pierde todo). Máximo rendimiento.",
                "RAID 1 (Mirroring): Capacidad = C. Tolera N - 1 fallos. Espejo exacto con redundancia total.",
                "RAID 5 (Paridad distribuida): Mínimo 3 discos. Capacidad = (N - 1) * C. Tolera 1 fallo. Paridad calculada con XOR.",
                "RAID 6 (Doble paridad distribuida): Mínimo 4 discos. Capacidad = (N - 2) * C. Tolera hasta 2 fallos simultáneos.",
                "RAID 10 (1+0, Striping de Mirrors): Mínimo 4 discos. Capacidad = (N / 2) * C. Tolera 1 fallo por subgrupo espejo.",
                "Cálculo de Paridad XOR: A ⊕ B ⊕ C = P. Bits con número impar de 1s dan 1; número par de 1s dan 0. Para actualizar: P_nueva = D_nueva ⊕ D_antigua ⊕ P_antigua."
            ],
            "key": "Capacidades: RAID 5 -> (N-1)*C. RAID 6 -> (N-2)*C. RAID 10 -> (N/2)*C."
        },
        {
            "tema": 2,
            "category": "Formatos y Codificación",
            "title": "Formatos: Texto, Imagen, Audio y Compresión",
            "bullets": [
                "Texto: ASCII usa 7 bits (128 caracteres); ASCII extendido usa 8 bits (1 byte); UTF-8 usa entre 1 y 4 bytes (compatible con ASCII).",
                "Imagen: RGB de 24 bits (3 canales x 8 bits = 16,7 millones de colores). BMP (sin comprimir), PNG (lossless con canal alfa), GIF (8 bits, 256 colores), JPEG (lossy mediante DCT).",
                "Audio Digital: Muestreo de Nyquist (fs >= 2 * fmax). Calidad CD = 44.1 kHz, 16 bits, 2 canales (estéreo). Bitrate CD = 44.100 * 16 * 2 = 1.411.200 bps (~1,41 Mbps).",
                "Compresión Lossless vs Lossy: Lossless (PNG, FLAC, RLE, ZIP) recupera el 100% idéntico. Lossy (JPEG, MP3) descarta información psicovisual/psicoacústica imperceptible.",
                "Compresión RLE: Sustituye repeticiones 'AAAAABBBCC' por '5A3B2C'. Ratio = Tamaño Original / Tamaño Comprimido."
            ],
            "key": "Fórmula Nyquist: fs >= 2 * fmax. Bitrate = Frecuencia * Bits * Canales."
        },
        {
            "tema": 2,
            "category": "Arquitectura Multimedia",
            "title": "Procesadores y Hardware Multimedia (MMA)",
            "bullets": [
                "CISC vs RISC: CISC tiene instrucciones complejas multietapa; RISC tiene instrucciones simples de un solo ciclo y arquitectura regular.",
                "DSP (Digital Signal Processor): Arquitectura Harvard y unidad MAC (Multiplicación-Acumulación) en un solo ciclo para procesar señales de audio/vídeo en tiempo real.",
                "NPU (Neural Processing Unit): Hardware especializado en operaciones matriciales masivas para acelerar redes neuronales e IA móvil.",
                "ASIC: Circuito integrado dedicado no programable. Máximo rendimiento y eficiencia energética, pero coste fijo de diseño muy alto y cero flexibilidad.",
                "FPGA: Dispositivo reconfigurable en campo por hardware mediante descripción HDL (VHDL/Verilog). Alta flexibilidad post-fabricación.",
                "Métricas: Complejidad computacional en MOPS (millones de operaciones/s) y GOPS (giga-operaciones/s)."
            ],
            "key": "DSP para señal y MAC. NPU para IA. ASIC para eficiencia máxima fija. FPGA para reconfigurabilidad."
        },

        # ==========================================
        # TEMA 3: PANTALLAS, WEARABLES, CONECTIVIDADES Y REDES
        # ==========================================
        {
            "tema": 3,
            "category": "Pantallas",
            "title": "Pantallas Táctiles y Tecnologías de Display",
            "bullets": [
                "Resistivas: Presión mecánica entre 2 láminas conductoras flexibles. Funcionan con cualquier puntero o guantes, pero no admiten multitouch y tienen menor luminosidad.",
                "Capacitivas Proyectadas (PCAP): Matriz de electrodos en cuadrícula X-Y; detectan distorsión electrostática del dedo humano. Admiten multitouch real (pinch to zoom) y gran durabilidad.",
                "SAW (Onda Acústica Superficial): Transductores ultrasónicos en cristal puro. Claridad óptica total (100%), pero sensibles a gotas de agua o suciedad.",
                "In-Cell vs On-Cell: On-cell coloca la capa táctil sobre el filtro de color; In-cell integra los sensores táctiles directamente dentro de la matriz del display (más finas y brillantes).",
                "Displays: LCD requiere retroiluminación trasera (backlight). IPS ofrece amplios ángulos de visión (178°). OLED/AMOLED: cada píxel orgánico emite su propia luz; negros puros (píxel apagado = contraste infinito) y menor consumo con fondos negros."
            ],
            "key": "PCAP = multitouch con dedo. Resistiva = presión con guante/objeto. OLED = negros puros y contraste infinito."
        },
        {
            "tema": 3,
            "category": "Wearables",
            "title": "Wearables y Textillography (Prendas Inteligentes)",
            "bullets": [
                "Wearables: Dispositivos electrónicos diseñados para ser vestidos pegados al cuerpo, 'always-on', ergonómicos y con bajo consumo energético.",
                "Textillography: Disciplina tecnológica que integra electrónica, sensores, interconexiones y fibras conductoras dentro de la estructura propia de los tejidos textiles.",
                "Capas de la prenda inteligente: Capa interna (contacto piel / bioseñales), capa intermedia (interconexión y buses conductores) y capa exterior (protección y aislamiento).",
                "Materiales conductores: Hilos de plata, cobre, acero inoxidable o polímeros conductores electroactivos.",
                "Principales retos técnicos: Resistencia mecánica al doblado y lavados agresivos continuos, autonomía/alimentación energética y privacidad de datos biomédicos."
            ],
            "key": "Textillography = e-textiles con fibras conductoras integradas en la prenda. Retos = lavados y batería."
        },
        {
            "tema": 3,
            "category": "Conectividad",
            "title": "Bluetooth frente a otras Conectividades",
            "bullets": [
                "Bluetooth / BLE: Banda ISM 2.4 GHz con salto de frecuencia (FHSS). BLE (Bluetooth Low Energy) optimizado para ráfagas cortas de datos con batería de meses o años (pila de botón).",
                "Wi-Fi (IEEE 802.11): Gran caudal de datos (Mbps a Gbps) y alcance (~50-100 m), pero alto consumo de batería (no apto para sensores diminutos).",
                "Zigbee (IEEE 802.15.4): Bajo consumo, baja velocidad (250 kbps), banda 2.4 GHz y topología en malla (Mesh) para domótica e IoT.",
                "ANT / ANT+: Protocolo propietario ultraligero en 2.4 GHz para sensores deportivos de fitness (pulsómetros, cadencia) con topología uno a muchos.",
                "RFID vs NFC: RFID pasivo no usa batería (se alimenta del campo electromagnético del lector) para inventario. NFC opera a 13.56 MHz a menos de 4-10 cm con seguridad física extrema para pagos móviles y emparejamiento instantáneo."
            ],
            "key": "BLE para bajo consumo en periféricos. Wi-Fi para ancho de banda. Zigbee para malla. NFC para pagos (<10 cm)."
        },
        {
            "tema": 3,
            "category": "Telefonía Celular",
            "title": "Redes Móviles, Clusters Celulares y Handover",
            "bullets": [
                "Generaciones: 1G (analógica, voz), 2G (GSM digital, SMS), 3G (UMTS datos), 4G (LTE todo IP), 5G (baja latencia <1ms y alta densidad IoT).",
                "Fórmula de Clúster Celular: N = i^2 + i*j + j^2 (valores válidos: 1, 3, 4, 7, 9, 12, 13, 19...). Canales por celda: k = T / N.",
                "Distancia de Reutilización Cocanal: D/R = sqrt(3*N). A mayor clúster N, mayor distancia cocanal D/R y menor interferencia (mayor S/I), pero menor capacidad de tráfico por celda.",
                "Handover (Traspaso): Hard Handover ('break before make', corta antes de conectar, típico en GSM); Soft Handover ('make before break', conecta a la nueva celda antes de soltar la vieja, en 3G/CDMA).",
                "Aumento de Capacidad: Cell Splitting (división celular en microceldas conservando D/R) y Sectorización (antenas directivas a 120° o 60° para reducir interferentes cocanales)."
            ],
            "key": "Clúster: N = i^2+ij+j^2. Distancia cocanal: D/R = sqrt(3N). Hard = break before make. Soft = make before break."
        }
    ]
