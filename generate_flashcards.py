# -*- coding: utf-8 -*-
"""
Flashcards data for DISM exam preparation.
100% focused on the official exam requirements (Topics 1, 2.1, 2.2, 3.1, and 3.2).
"""

def get_flashcards():
    return [
        # ==========================================
        # TEMA 1: FRAMEWORKS (HÍBRIDO VS NATIVO)
        # ==========================================
        {
            "tema": 1,
            "category": "Frameworks",
            "title": "Apps Híbridas vs Nativas (Concepto y Rendimiento)",
            "bullets": [
                "Apps Híbridas: Se ejecutan dentro de un WebView o contenedor web mediante HTML, CSS y JavaScript. Requieren plugins/bridges para interactuar con el hardware del teléfono.",
                "Apps Nativas: Se compilan y ejecutan directamente sobre el sistema operativo, aprovechando las APIs y widgets nativos de iOS y Android sin capas de navegador intermedias.",
                "Rendimiento: Las nativas ofrecen máxima fluidez en animaciones y acceso directo a la GPU/cámara. Las híbridas reducen costes y tiempo de desarrollo pero tienen rendimiento inferior en el WebView."
            ],
            "key": "Híbrido = WebView / Contenedor. Nativo = Ejecución directa en SO sin WebView."
        },
        {
            "tema": 1,
            "category": "Frameworks",
            "title": "Catálogo de Frameworks por Nombre Propio",
            "bullets": [
                "HÍBRIDOS (según temario): Apache Cordova, PhoneGap, Ionic (+ Capacitor) y Unity (por requerir contenedor/runtime).",
                "NATIVOS (según temario): React Native (UI nativa con lógica JS), Flutter (lenguaje Dart y motor gráfico en canvas nativo), Xamarin y .NET MAUI (C# compilado a nativo), NativeScript (JS a APIs nativas) y Kotlin Multiplatform (KMP).",
                "Clave de examen: Saber identificar qué es cada framework (ej. ¿Qué es .NET MAUI? -> Framework nativo de Microsoft evolución de Xamarin. No entra su arquitectura interna en detalle)."
            ],
            "key": "Híbridos: Ionic, Cordova, PhoneGap, Unity. Nativos: React Native, Flutter, MAUI, Xamarin, NativeScript, KMP."
        },

        # ==========================================
        # TEMA 2.1: INTRODUCCIÓN MULTIMEDIA & STREAMING
        # ==========================================
        {
            "tema": 2,
            "category": "Multimedia Básica",
            "title": "Sistemas Multimedia y Clasificación (Primeras 15 Páginas)",
            "bullets": [
                "Multimedia: Integración controlada por computador de medios (texto, gráficos, imágenes, audio y vídeo) donde cada tipo es digitalizado, almacenado y transmitido.",
                "Multimedia Lineal: El usuario no tiene control sobre la secuencia de visualización y lo visualiza en orden fijo (ejemplo típico: el cine).",
                "Hipermedia Interactiva: El usuario tiene control activo sobre el proyecto mediante navegación, decidiendo la secuencia, velocidad y momento de reproducción (típico en educación y web).",
                "Etapas de un Proyecto: Planificación/diseño -> Adquisición/digitalización -> Compresión/almacenamiento -> Transmisión y visualización."
            ],
            "key": "Lineal = sin control (cine). Hipermedia interactiva = control de orden y ritmo."
        },
        {
            "tema": 2,
            "category": "Streaming y Redes",
            "title": "Streaming, Buffer, Jitter y Modelos OTT",
            "bullets": [
                "Streaming: Reproducción continua sin esperar a la descarga total; almacena paquetes temporalmente en un buffer de memoria RAM y no guarda archivo local permanente.",
                "Buffer y Jitter: El buffer del cliente absorbe el JITTER (la variación del tiempo de llegada de paquetes en la red), transformando una recepción irregular en una reproducción regular y sin cortes.",
                "Servicios: Live Streaming (en directo, sin control de avance rápido) vs VOD (Vídeo Bajo Demanda, permite pausar y rebobinar).",
                "Modelos de Negocio: AVOD (gratuito con anuncios, ej. YouTube), SVOD (suscripción periódica, ej. Netflix), TVOD / PPV (pago por visión / alquiler individual de un evento)."
            ],
            "key": "El buffer del cliente absorbe el jitter (variaciones de retardo) para evitar cortes."
        },
        {
            "tema": 2,
            "category": "Streaming y Redes",
            "title": "Protocolos de Streaming y Caso Netflix (OCA - Pág. 64)",
            "bullets": [
                "Protocolos de Control y Transporte: RTSP actúa como mando a distancia de red (Play, Pause, Stop); RTP transporta los medios sobre UDP con marcas de tiempo (timestamp) y números de secuencia.",
                "ABR (Adaptive Bitrate): HLS (Apple) y MPEG-DASH dividen el vídeo en fragmentos (2-10 s) con manifiestos (.m3u8, .mpd); el cliente conmuta de calidad según ancho de banda y CPU.",
                "Netflix OCA (Open Connect Appliances, Pág. 64): Servidores especializados de caché que Netflix despliega dentro o cerca de los ISP e IXP para servir directamente el vídeo al cliente por HTTP(S) localmente.",
                "División de Funciones: AWS gestiona el backend (login, catálogo, recomendaciones, licencias); los servidores OCA entregan los gigabytes de vídeo al usuario."
            ],
            "key": "RTSP controla sesión. RTP sobre UDP transmite medios. OCA sirve el vídeo desde los ISP; AWS gestiona la lógica."
        },

        # ==========================================
        # TEMA 2.2: RAID, FORMATOS, COMPRESIÓN Y HARDWARE MMA
        # ==========================================
        {
            "tema": 2,
            "category": "Sistemas RAID",
            "title": "Matrices RAID y Tipos de Escritura (Pág. 13)",
            "bullets": [
                "Capacidades y Fallos: RAID 0 = N*C (0 fallos). RAID 1 = C (N-1 fallos). RAID 5 = (N-1)*C (1 fallo). RAID 6 = (N-2)*C (2 fallos simultáneos). RAID 10 = (N/2)*C (1 fallo por subgrupo espejo).",
                "Paridad XOR en RAID 5: A ⊕ B ⊕ C = P. Bits con número impar de 1s dan 1; par dan 0.",
                "Escritura Franja Completa: La paridad se calcula en RAM y se escribe en paralelo en los discos sin lecturas previas (óptimo para streaming de audio/vídeo).",
                "Escritura Parcial (Read-Modify-Write, Pág. 13): Modificar 1 solo bloque penaliza con 4 accesos a disco (2 lecturas: dato viejo y paridad vieja + 2 escrituras: dato nuevo y paridad nueva: P_nueva = D_nueva ⊕ D_vieja ⊕ P_vieja)."
            ],
            "key": "Escritura pequeña en RAID 5 = Read-Modify-Write (4 accesos: 2 lecturas + 2 escrituras)."
        },
        {
            "tema": 2,
            "category": "Formatos y Codificación",
            "title": "Formatos de Texto (UTFs - Pág. 23) e Imágenes (Pág. 41)",
            "bullets": [
                "Codificación de Texto (UTFs): ASCII usa 7 bits (128 caract.); ASCII extendido usa 1 byte (256 caract.). UTF-8 usa de 1 a 4 bytes (compacto en texto latino, pero caracteres ideográficos chinos/japoneses ocupan 3 bytes en UTF-8 frente a sólo 2 bytes en UTF-16). UTF-32 usa 4 bytes fijos.",
                "Imágenes y Compresión (Pág. 41): Modelo RGB de 24 bits (3 canales x 8 bits = 16,7 millones de colores). BMP (sin comprimir), PNG (lossless con canal alfa), GIF (8 bits, 256 colores), JPEG (lossy mediante DCT).",
                "Compresión Lossless vs Lossy: Lossless (PNG, FLAC, RLE) es reversible al 100%; Lossy (JPEG, MP3) descarta información psicovisual/psicoacústica redundante.",
                "Algoritmo RLE: Sustituye repeticiones 'AAAAABBBCC' por '5A3B2C'. Ratio = Tamaño Original / Tamaño Comprimido."
            ],
            "key": "UTF-8: 1 byte en ASCII, 3 bytes en asiático (UTF-16 usa 2 bytes en asiático). RLE = contador + símbolo."
        },
        {
            "tema": 2,
            "category": "Arquitectura Multimedia",
            "title": "MMA: Localidad (Pág. 45) y Dedicadas vs Reconfigurables (Pág. 47)",
            "bullets": [
                "Localidad en MMA (Pág. 45): Las aplicaciones multimedia procesan flujos continuos masivos y presentan ALTA localidad espacial (acceso a posiciones contiguas de memoria como píxeles) pero BAJA localidad temporal (raramente se reutilizan los mismos datos).",
                "Dedicadas (ASIC) vs Reconfigurables (FPGA) (Pág. 47): El ASIC tiene un circuito físico fijo impreso en silicio (máximo rendimiento y mínimo consumo, pero cero flexibilidad); la FPGA posee bloques lógicos reconfigurables en campo mediante HDL si el algoritmo evoluciona.",
                "Procesadores Específicos: DSP (Digital Signal Processor: arquitectura Harvard y unidad MAC de un ciclo para audio/señal) y NPU (redes neuronales matriciales).",
                "Métricas: MOPS (Millones de operaciones/s) y GOPS (Giga-operaciones/s)."
            ],
            "key": "MMA = Alta localidad espacial, baja temporal. ASIC = fijo de máxima eficiencia. FPGA = reprogramable."
        },

        # ==========================================
        # TEMA 3.1: PANTALLAS, WEARABLES Y CONECTIVIDAD
        # ==========================================
        {
            "tema": 3,
            "category": "Pantallas",
            "title": "Pantallas Táctiles (Pág. 55) y Tecnologías de Display",
            "bullets": [
                "Táctiles Resistivas: Dos láminas conductoras que hacen contacto por presión física. Operan con guantes o cualquier puntero, pero no soportan multitouch y tienen menor luminosidad.",
                "Capacitivas Proyectadas (PCAP): Matriz de electrodos X-Y que detecta la distorsión electrostática del dedo humano. Permiten multitouch real (zoom con dos dedos) y gran resistencia.",
                "Otras Táctiles: SAW (ondas acústicas en cristal puro al 100% de transparencia, pero sensibles a suciedad/agua), Infrarrojos/Óptica (malla invisible de haces de luz perimetrales).",
                "Integración Táctil: In-Cell integra los sensores directamente dentro de la matriz del display (paneles más delgados y brillantes) frente a On-Cell (capa sobre el filtro).",
                "Displays LCD vs OLED/AMOLED: LCD requiere retroiluminación trasera (TFT o IPS con 178° de visión). OLED/AMOLED: píxeles orgánicos autoemisores; negros puros y contraste infinito (píxel apagado = 0 consumo)."
            ],
            "key": "PCAP = multitouch con dedo. Resistiva = presión con guante. In-Cell = sensor integrado en matriz. OLED = negros puros."
        },
        {
            "tema": 3,
            "category": "Wearables",
            "title": "Wearables y Textillography (Prendas Inteligentes)",
            "bullets": [
                "Wearables: Dispositivos electrónicos pegados al cuerpo, siempre activos ('always-on'), ergonómicos y con bajo consumo de energía.",
                "Textillography: Tecnología que integra sensores, electrónica, interconexiones y fibras conductoras dentro de la propia estructura de los tejidos textiles.",
                "Capas de la Prenda Inteligente: Capa interna (contacto piel y bioseñales), capa intermedia (interconexiones y buses de datos conductores) y capa externa (aislamiento ambiental).",
                "Materiales Conductores: Hilos de plata, acero inoxidable, cobre o polímeros electroactivos.",
                "Principales Retos: Resistencia a ciclos repetidos de lavado/detergentes, fatiga por torsión mecánica continua, suministro de batería y privacidad de datos biométricos."
            ],
            "key": "Textillography = electrónica y fibras conductoras tejidas en la prenda. Retos = lavabilidad y batería."
        },
        {
            "tema": 3,
            "category": "Conectividad",
            "title": "Bluetooth, ANT vs ANT+ y Alcance Wi-Fi 1 vs Wi-Fi 7",
            "bullets": [
                "Bluetooth y BLE: Banda ISM 2.4 GHz con salto de frecuencia FHSS. BLE está diseñado para ráfagas cortas de datos con meses/años de batería con pila de botón.",
                "ANT vs ANT+: ANT es el protocolo base de red de ultra baja potencia (2400-2524 MHz). ANT+ añade la definición de perfiles de datos estandarizados en 2457 MHz para que dispositivos de distintos fabricantes puedan entender la información intercambiada.",
                "Alcance Wi-Fi (¿Quién tiene más alcance, Wi-Fi 1 o Wi-Fi 7?): Las frecuencias más bajas como 2.4 GHz (Wi-Fi 1 / 802.11b) tienen mayor alcance físico y atraviesan mejor paredes y obstáculos que frecuencias más altas como 5 GHz o 6 GHz (Wi-Fi 7), las cuales dan enorme velocidad pero sufren mayor atenuación.",
                "Zigbee: Protocolo en malla (Mesh) de bajo consumo basado en IEEE 802.15.4 para domótica."
            ],
            "key": "ANT+ permite entender los datos de ANT. Frecuencias bajas (2.4 GHz) tienen MÁS alcance físico que 5 o 6 GHz."
        },
        {
            "tema": 3,
            "category": "Conectividad",
            "title": "RFID vs NFC (Frecuencias, Modos y Alcance)",
            "bullets": [
                "Frecuencias y Modos: RFID opera en 3 frecuencias principales (baja LF, alta HF y ultra alta UHF) y 2 modos (activo con batería y pasivo sin batería alimentado por la onda del lector).",
                "NFC: Extensión especializada de RFID que opera en UNA SOLA frecuencia fija (13,56 MHz).",
                "Alcance: RFID alcanza varios metros en logística e inventario empresarial. NFC está restringido a un alcance estrictamente inferior a 10 cm (habitual <= 4 cm).",
                "Casos de Uso de NFC: Comunicación bidireccional segura para pagos móviles (Apple/Google Pay), control de accesos y emparejamiento instantáneo 'tocar y conectar'."
            ],
            "key": "RFID = 3 frecuencias y 2 modos, alcance de metros. NFC = 1 frecuencia (13,56 MHz), alcance <= 10 cm."
        },

        # ==========================================
        # TEMA 3.2: REDES CELULARES Y CÁLCULOS DE ERLANG
        # ==========================================
        {
            "tema": 3,
            "category": "Telefonía Celular",
            "title": "Telefonía Celular: Clusters, Distancia D/R y Handover",
            "bullets": [
                "Tamaño de Clúster Celular: N = i^2 + i*j + j^2 (valores válidos: 1, 3, 4, 7, 9, 12, 13, 19...). Canales por celda: k = T / N.",
                "Distancia Cocanal y S/I: D/R = sqrt(3*N). A mayor clúster N, mayor es la distancia cocanal D/R y mayor la relación señal/interferencia (S/I), pero disminuye la capacidad de canales por celda.",
                "Handover (Traspaso): Hard Handover ('break before make', se corta la celda vieja antes de conectar la nueva, típico en GSM); Soft Handover ('make before break', conecta a la nueva celda antes de soltar la vieja, en 3G/CDMA).",
                "Decisión del Handover: NCHO (red decide), MAHO (móvil asiste en las medidas), MCHO (móvil controla la decisión).",
                "Aumento de Capacidad: Cell Splitting (división celular en microceldas) y Sectorización (antenas directivas a 120° o 60° para reducir interferentes cocanales)."
            ],
            "key": "Clúster: N = i^2+ij+j^2. Distancia cocanal: D/R = sqrt(3N). Hard = break before make. Soft = make before break."
        },
        {
            "tema": 3,
            "category": "Cálculos de Tráfico",
            "title": "Cálculos de Tráfico Telefónico en Erlangs (Sin Erlang B)",
            "bullets": [
                "Definición de Erlang: Unidad adimensional que representa la intensidad de tráfico telefónico continuo en un canal durante una hora cargada.",
                "Fórmula de Tráfico Ofrecido: TO = λ · h (donde λ es el número de llamadas por hora y h es la duración media por llamada expresada en horas).",
                "Fórmula de Tráfico Cursado: TC = TO · (1 - GoS) (donde GoS es el Grado de Servicio o probabilidad de bloqueo).",
                "Fórmula de Tráfico Perdido: TP = TO - TC = TO · GoS.",
                "Cálculo del Grado de Servicio: GoS = TP / TO (fracción de llamadas o tráfico bloqueado).",
                "Ejemplo de Examen: 1.200 llam/h de 3 min (3/60 = 0,05 h) -> TO = 1.200 * 0,05 = 60 Erlangs. Con GoS = 5% (0,05), TC = 60 * 0,95 = 57 Erlangs y TP = 3 Erlangs."
            ],
            "key": "Fórmulas: TO = λ · h. TC = TO · (1 - GoS). TP = TO - TC. GoS = TP / TO."
        }
    ]
