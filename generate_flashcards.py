# -*- coding: utf-8 -*-
"""
Flashcards data for DISM mobile study.
Concise, direct, high-yield summary cards per topic for quick study on the bus.
"""

def get_flashcards():
    return [
        # ==========================================
        # TEMA 1: DESARROLLO MULTIPLATAFORMA
        # ==========================================
        {
            "tema": 1,
            "category": "Conceptos",
            "title": "Nativo vs Híbrido vs PWA",
            "bullets": [
                "Nativo: Escrito en el lenguaje oficial (Swift en iOS, Kotlin en Android). Máximo rendimiento, acceso total al hardware, pero requiere mantener dos equipos de desarrollo separados.",
                "Híbrido: Web technologies (HTML+CSS+JS) empaquetadas en un contenedor nativo (WebView). Reutiliza código pero tiene menor rendimiento en animaciones 3D y juegos.",
                "PWA (Progressive Web App): Aplicación web estándar que utiliza Service Workers y Web App Manifest para instalarse en el launcher y funcionar offline sin pasar por las tiendas de apps."
            ],
            "key": "Regla: Nativo para rendimiento extremo; Híbrido/PWA para rentabilidad y reutilización de equipo web."
        },
        {
            "tema": 1,
            "category": "Mercado",
            "title": "Mercado: App Store vs Google Play",
            "bullets": [
                "Google Play Store tiene más del doble de descargas totales en el mundo debido a la cuota de mercado de Android.",
                "Apple App Store genera casi el doble de ingresos monetarios y gasto de usuarios que Google Play.",
                "Categoría líder: Los videojuegos móviles (Gaming) generan más del 60-70% de todos los ingresos de las tiendas de apps."
            ],
            "key": "Clave examen: App Store gana en facturación; Google Play gana en número de descargas."
        },
        {
            "tema": 1,
            "category": "Frameworks",
            "title": "Historia: PhoneGap, Cordova y Xamarin",
            "bullets": [
                "PhoneGap: Creado por Nitobi en 2009, comprado por Adobe en 2011 y donado a Apache como Apache Cordova.",
                "Cordova: Desfasado hoy frente a Capacitor por su gestión rígida de plugins y ocultación de proyectos nativos.",
                "Xamarin: Creado sobre Mono (C#) y adquirido por Microsoft en 2016. Su evolución y sustituto oficial desde mayo de 2022 es .NET MAUI."
            ],
            "key": "Clave examen: PhoneGap -> Apache Cordova. Xamarin -> .NET MAUI."
        },
        {
            "tema": 1,
            "category": "Ionic",
            "title": "Ionic & Capacitor",
            "bullets": [
                "Ionic: Librería de Web Components (creada con Stencil.js) compatible con Angular, React, Vue o JS plano.",
                "Capacitor: Runtime moderno que sustituye a Cordova. Los proyectos 'android' e 'ios' son carpetas nativas reales de primer nivel (editables en Android Studio y Xcode).",
                "Native Bridge: Inyecta window.Capacitor.Plugins para comunicar JavaScript con las APIs nativas del SO.",
                "Platform Styling: Aplica automáticamente Material Design ('md') en Android y Cupertino ('ios') en iPhone.",
                "Comando clave: 'npx cap sync' copia los assets web y actualiza dependencias nativas."
            ],
            "key": "Ventaja: Misma base de código web para iOS, Android y Web. Desventaja: Rendimiento en WebView."
        },
        {
            "tema": 1,
            "category": "PWA",
            "title": "PWA: Manifest y Service Worker",
            "bullets": [
                "Web App Manifest (manifest.json): Define nombre, iconos, color de tema, orientación y 'display: standalone'.",
                "Service Worker: Script JavaScript que corre en segundo plano en un hilo separado del DOM (proxy de red).",
                "Requisito obligatorio: Debe servirse bajo HTTPS (salvo en localhost) por seguridad.",
                "Ciclo de vida: 1. Install (cachear App Shell inicial) -> 2. Activate (limpiar cachés viejas) -> 3. Fetch/Push (interceptar peticiones de red o recibir push)."
            ],
            "key": "Clave examen: En el evento 'install' se usa 'event.waitUntil()' para esperar a que termine de cachear."
        },
        {
            "tema": 1,
            "category": "PWA",
            "title": "PWA: Estrategias de Caché",
            "bullets": [
                "Cache First: Busca en caché primero; si no está, va a la red. Ideal para App Shell y assets estáticos inmutables.",
                "Network First: Intenta la red primero; si falla o hay timeout, usa la caché. Ideal para noticias y cotizaciones frescas.",
                "Stale-While-Revalidate: Devuelve la versión en caché instantáneamente y descarga en segundo plano la nueva versión para actualizar la caché. Ideal para avatares y perfiles.",
                "Network Only: Solo red (transacciones bancarias). Cache Only: Solo caché (modo offline forzado)."
            ],
            "key": "Regla: Estático -> Cache First. Dinámico -> Network First. Rápido + fresco -> Stale-While-Revalidate."
        },
        {
            "tema": 1,
            "category": "Frameworks",
            "title": ".NET MAUI & Uno Platform",
            "bullets": [
                ".NET MAUI (.NET Multi-platform App UI): Framework oficial de Microsoft en C# y XAML para iOS, Android, Windows y macOS.",
                "Arquitectura: Utiliza el patrón 'Handlers / Mappers' para conectar directamente con los widgets nativos del SO (sustituyendo a los lentos 'Renderers' de Xamarin).",
                "Uno Platform: Alternativa comunitaria que lleva la API de WinUI / XAML a Web (WebAssembly), Linux, iOS y Android."
            ],
            "key": "Clave examen: .NET MAUI renderiza controles nativos reales del SO usando C# y XAML."
        },
        {
            "tema": 1,
            "category": "Frameworks",
            "title": "Flutter (Google & Dart)",
            "bullets": [
                "Lenguaje: Dart. Creado y mantenido por Google.",
                "Renderizado único: NO usa los widgets de Android ni iOS. Flutter dibuja cada píxel en un canvas de la GPU mediante su propio motor gráfico (Skia y modernamente Impeller en C++).",
                "Compilación: En modo release compila AOT (Ahead-Of-Time) a código máquina ARM nativo.",
                "Widgets: Todo es un Widget. StatelessWidget (inmutable) y StatefulWidget (mantiene estado con setState()).",
                "Desarrollo: Stateful Hot Reload inyecta código en caliente en menos de un segundo sin perder el estado."
            ],
            "key": "Clave examen: Garantiza consistencia pixel-perfect idéntica en cualquier pantalla porque dibuja su propia UI."
        },
        {
            "tema": 1,
            "category": "Frameworks",
            "title": "React Native (Meta)",
            "bullets": [
                "Lenguaje: JavaScript / TypeScript con sintaxis declarativa de React y JSX.",
                "Renderizado: Mapea componentes (<View>, <Text>) a componentes nativos reales (UIView en iOS, View en Android).",
                "Motor de Layout: Yoga (motor Flexbox escrito en C++ de alto rendimiento).",
                "Motor JS: Hermes (motor ligero optimizado para móviles de Meta con precompilación de bytecode).",
                "Nueva Arquitectura: JSI (JavaScript Interface) permite invocar C++ síncronamente sin serializar en JSON; Fabric (renderizado) y TurboModules (módulos nativos bajo demanda)."
            ],
            "key": "Clave examen: React Native renderiza widgets nativos del SO calculados con Yoga Flexbox."
        },
        {
            "tema": 1,
            "category": "Frameworks",
            "title": "Kotlin Multiplatform (KMP) & Tauri",
            "bullets": [
                "KMP (JetBrains): Comparte la lógica de negocio (red, base de datos, modelos) en Kotlin común, pero deja la UI 100% nativa (SwiftUI en iOS, Jetpack Compose en Android).",
                "Kotlin/Native: Compila a binario nativo Objective-C/Swift para iOS sin necesitar máquina virtual Java (JVM).",
                "Tauri: Backend en Rust de ultra alta seguridad y frontend web (HTML/CSS/JS). No empaqueta Chromium (como Electron), sino que usa el WebView nativo del SO (WebView2 en Windows, WebKit en Apple). Binarios de <10 MB."
            ],
            "key": "KMP = Lógica compartida en Kotlin + UI nativa. Tauri = Backend Rust + WebView nativo."
        },

        # ==========================================
        # TEMA 2: MULTIMEDIA & CÁLCULOS
        # ==========================================
        {
            "tema": 2,
            "category": "Streaming",
            "title": "Streaming ABR & Netflix",
            "bullets": [
                "ABR (Adaptive Bitrate Streaming): El vídeo se trocea en fragmentos (2 a 10 s) en varias calidades. El reproductor mide el ancho de banda y pide el segmento adecuado. Protocolos: HLS (Apple, .m3u8) y MPEG-DASH (.mpd).",
                "Modelos OTT: SVOD (Suscripción: Netflix), AVOD (Publicidad: YouTube), TVOD (Transaccional/Alquiler: iTunes).",
                "Caso Netflix: Servidores OCA (Open Connect Appliances) instalados dentro de los centros de datos de los ISPs locales para servir el vídeo; AWS gestiona catálogo, usuarios y transcodificación."
            ],
            "key": "Clave examen: Open Connect en ISPs locales evita saturar las troncales de internet."
        },
        {
            "tema": 2,
            "category": "RAID",
            "title": "Fórmulas Clave de RAID",
            "bullets": [
                "RAID 0 (Striping): Capacidad = N × S. Velocidad = N×. Tolerancia = 0 fallos (si muere 1 disco, se pierde todo).",
                "RAID 1 (Mirroring): Capacidad = 1 × S (en 2 discos). Tolera fallo de 1 disco.",
                "RAID 5 (Paridad distribuida): Capacidad = (N - 1) × S. Mínimo 3 discos. Tolera fallo de 1 disco. Paridad XOR bit a bit.",
                "RAID 6 (Doble paridad): Capacidad = (N - 2) × S. Mínimo 4 discos. Tolera fallo simultáneo de 2 discos.",
                "RAID 10 (1+0): Capacidad = (N / 2) × S. Mínimo 4 discos. Tolera hasta 1 fallo por pareja espejo."
            ],
            "key": "Ejemplo: 4 discos de 4 TB en RAID 5 = (4 - 1) × 4 = 12 TB útiles."
        },
        {
            "tema": 2,
            "category": "Cálculos RAID",
            "title": "Cálculo de Paridad XOR en RAID 5",
            "bullets": [
                "Regla XOR: Bits iguales dan 0 (0⊕0=0, 1⊕1=0). Bits diferentes dan 1 (1⊕0=1, 0⊕1=1).",
                "Ejemplo de clase: D1 = 1010, D2 = 1100, D3 = 0011.\n1) 1010 ⊕ 1100 = 0110\n2) 0110 ⊕ 0011 = 0101 -> Paridad P = 0101.",
                "Actualización de paridad (Read-Modify-Write): Para no leer todos los discos, se calcula:\nP_nuevo = P_viejo ⊕ D_viejo ⊕ D_nuevo.\nRequiere solo 2 lecturas y 2 escrituras."
            ],
            "key": "Si P_viejo = 1111, D_viejo = 1010, D_nuevo = 0001:\n1111 ⊕ 1010 = 0101 -> 0101 ⊕ 0001 = 0100."
        },
        {
            "tema": 2,
            "category": "Cálculos Multimedia",
            "title": "Cálculo: Tamaño de Imagen sin comprimir",
            "bullets": [
                "Fórmula: Tamaño = Ancho × Alto × (Profundidad en bits / 8).",
                "Foto 12 Mpx (4000 × 3000) a 24 bits (TrueColor = 3 Bytes/píxel):\n4000 × 3000 = 12.000.000 píxeles.\n12.000.000 × 3 Bytes = 36.000.000 Bytes = 36 MB.",
                "Foto 48 Mpx (8000 × 6000) a 24 bits (3 Bytes):\n48.000.000 × 3 = 144.000.000 Bytes = 144 MB.",
                "Imagen 320 × 240 a 24 bits:\n76.800 × 3 = 230.400 Bytes / 1024 = 225 KB."
            ],
            "key": "24 bits/píxel siempre equivale a multiplicar por 3 Bytes. 32 bits equivale a 4 Bytes."
        },
        {
            "tema": 2,
            "category": "Cálculos Multimedia",
            "title": "Cálculo: Tamaño de Vídeo sin comprimir",
            "bullets": [
                "Fórmula: Píxeles/frame × Bytes/píxel × FPS × Segundos de duración.",
                "Vídeo 4K UHD (3840 × 2160), 24 bits (3 B), 25 fps, 15 min (900 s):\n1) 3840 × 2160 = 8.294.400 píxeles/frame.\n2) 8.294.400 × 3 = 24.883.200 Bytes/frame (~24,88 MB).\n3) × 25 fps = 622.080.000 Bytes/s (~622 MB/s).\n4) × 900 s = 559.872.000.000 Bytes ≈ 559,87 GB.",
                "Vídeo 1080p (1920 × 1080), 32 bits (4 B), 30 fps en 1 minuto:\n2.073.600 × 4 × 30 × 60 ≈ 14,93 GB/min (~13,90 GiB/min)."
            ],
            "key": "Muestra por qué la compresión de vídeo es imprescindible para almacenar o transmitir."
        },
        {
            "tema": 2,
            "category": "Cálculos Multimedia",
            "title": "Cálculo: Vídeo por Bitrate & Audio",
            "bullets": [
                "Vídeo por Bitrate: Tamaño = Bitrate (bps) × Segundos / 8.\nVídeo 4K a 15 Mbit/s en 15 minutos (900 s):\n15 Mbit/s × 900 s = 13.500 Mbit / 8 = 1687,5 MB ≈ 1,69 GB.",
                "Audio CD (44.100 Hz, 16 bits = 2 B, 2 canales estéreo):\n44.100 × 2 × 2 = 176.400 Bytes/s × 60 s = 10,58 MB/min (mono: 5,29 MB/min).",
                "Audio Hi-Res (96.000 Hz, 24 bits = 3 B, 2 canales estéreo):\n96.000 × 2 × 3 = 576.000 Bytes/s × 60 s = 34,56 MB/min."
            ],
            "key": "Para pasar de Megabits a MegaBytes siempre divide entre 8."
        },
        {
            "tema": 2,
            "category": "Hardware",
            "title": "Hardware Multimedia (MMA): DSP, NPU, ASIC, FPGA",
            "bullets": [
                "DSP (Digital Signal Processor): Arquitectura Harvard (buses separados para código y datos), instrucción MAC (Multiply-Accumulate en 1 ciclo), direccionamiento circular y de inversión de bits para FFT.",
                "NPU (Neural Processing Unit): Acelera operaciones matriciales/tensoriales para inferencia de redes neuronales e IA on-device con bajo consumo.",
                "ASIC: Circuito integrado dedicado cableado en silicio de fábrica. Máximo rendimiento, 0 flexibilidad.",
                "FPGA: Matriz de puertas lógicas reconfigurable mediante software (HDL). Flexible y sin costes NRE de fabricación."
            ],
            "key": "MPEG-2 decode complejidad: 609-740 MOPS (IDCT, YUV->RGB, decuantificación, compensación de movimiento)."
        },

        # ==========================================
        # TEMA 3: DISPOSITIVOS & REDES CELULARES
        # ==========================================
        {
            "tema": 3,
            "category": "Hardware Móvil",
            "title": "Procesadores Móviles: RISC, ARM y SoC",
            "bullets": [
                "RISC vs CISC: RISC domina en móviles porque sus instrucciones simples de longitud fija requieren menos transistores, reduciendo drásticamente el consumo energético y el calor disipado.",
                "Modelo ARM: No fabrica chips; diseña y licencia arquitecturas e IP cores (Cortex-A para apps, Cortex-R para tiempo real, Cortex-M para IoT).",
                "big.LITTLE / DynamIQ: Combina núcleos de alta eficiencia con núcleos de alta potencia en el mismo procesador.",
                "SoC (System on a Chip): Integra CPU, GPU, NPU/DSP, módem 4G/5G, ISP de cámara y RAM en una única pastilla de silicio."
            ],
            "key": "Clave examen: RISC domina en smartphones por su relación rendimiento/vatio."
        },
        {
            "tema": 3,
            "category": "Wearables",
            "title": "Wearables & Textillography",
            "bullets": [
                "Niveles de integración textil: 1. Electrónica añadida (módulo externo o clip) -> 2. Electrónica integrada (sensores/hilos cosidos o bordados) -> 3. La tela como dispositivo (la propia tela tejida con hilos conductores es sensor y bus).",
                "Capas de la prenda inteligente: Capa exterior (protección), capa intermedia (electrónica y cableado conductor), capa interior (confort en contacto con la piel).",
                "Retos principales: Resistencia a ciclos de lavado, detergentes químicos, sudor salino humano y flexión mecánica."
            ],
            "key": "Clave examen: La textillografía utiliza fibras de plata, cobre y polímeros conductores."
        },
        {
            "tema": 3,
            "category": "Pantallas",
            "title": "Pantallas Táctiles & Displays",
            "bullets": [
                "Resistiva: Presión mecánica entre 2 capas conductoras ITO. Funciona con guantes o estilete. Un solo toque. Menor transparencia.",
                "Capacitiva Proyectada (PCAP): Rejilla de electrodos X/Y que detecta cambios de capacitancia por el dedo. Multitáctil nativa. Estándar en todos los smartphones.",
                "SAW (Onda acústica): Ondas ultrasónicas sobre vidrio puro. Máxima transparencia y claridad.",
                "In-cell vs On-cell: In-cell integra los sensores táctiles dentro de las capas del propio display LCD/OLED, haciéndolo más delgado y con menos reflejos.",
                "LCD vs AMOLED: LCD necesita retroiluminación trasera permanente. AMOLED tiene píxeles autoemisivos, logrando negros puros al apagarse (contraste infinito y ahorro de batería)."
            ],
            "key": "Pantalla Retina: Densidad de píxeles (>300 ppi) donde el ojo humano a distancia normal no distingue los píxeles."
        },
        {
            "tema": 3,
            "category": "Conectividad",
            "title": "Conectividad de Corto Alcance",
            "bullets": [
                "BLE (Bluetooth Low Energy): Ráfagas cortas de datos con reposo profundo (años con pila de botón). Ideal para pulseras y beacons.",
                "ANT / ANT+: Protocolo propietario de ultra bajo consumo en 2,4 GHz para sensores deportivos (Garmin).",
                "Zigbee: Redes en malla (Mesh) de bajo consumo para domótica basadas en IEEE 802.15.4.",
                "RFID vs NFC: RFID alcanza metros (unidireccional); NFC opera estrictamente a 13,56 MHz con alcance <4-10 cm, bidireccional y soporta modo emulación de tarjeta segura (Apple Pay / Google Wallet)."
            ],
            "key": "Clave examen: NFC deriva de RFID en 13,56 MHz con alcance de centímetros para pagos seguros."
        },
        {
            "tema": 3,
            "category": "Red Celular",
            "title": "Arquitectura Red Celular & Handover",
            "bullets": [
                "Elementos: Terminal (MS) -> Estación Base (BTS en 2G, NodeB en 3G, eNodeB en 4G, gNodeB en 5G) -> Controlador (BSC/RNC) -> Núcleo (MSC).",
                "Registros: HLR (base de datos permanente de abonados), VLR (visitantes en la zona), EIR (IMEI listas blanca/negra), AUC (autenticación y claves).",
                "Paging: Búsqueda del móvil en reposo por aviso en todas las celdas del Location Area.",
                "Handover: Hard Handover (break-before-make en GSM/LTE) vs Soft Handover (make-before-break en 3G UMTS).",
                "MAHO (Mobile-Assisted Handover): El móvil mide la señal vecina y la red decide el traspaso.",
                "Canales de guarda: Reserva de canales en la celda para dar prioridad a los traspasos sobre llamadas nuevas."
            ],
            "key": "Cell Splitting: Subdivide celdas en microceldas para multiplicar la capacidad sin nuevo espectro."
        },
        {
            "tema": 3,
            "category": "Cálculos Celulares",
            "title": "Fórmula de Cluster Celular & Canales",
            "bullets": [
                "Fórmula del cluster: N = i² + j² + i·j (con i, j enteros no negativos).\n- (2, 0) -> N = 4 + 0 + 0 = 4\n- (2, 1) -> N = 4 + 1 + 2 = 7\n- (2, 2) -> N = 4 + 4 + 4 = 12",
                "Canales por celda: K = T / N (T = canales dúplex totales).\nSi T = 420 y N = 7 -> K = 420 / 7 = 60 canales/celda.",
                "Factor de reutilización: 1 / N (en cluster 7 es 1/7).",
                "Capacidad del sistema: M × T (donde M = Nº total celdas / N).\nPara 84 celdas y N = 7: M = 84 / 7 = 12 clusters -> Capacidad = 12 × 420 = 5.040 canales."
            ],
            "key": "Compromiso: Menor N da más canales y capacidad (M×T), pero aumenta la interferencia cocanal."
        },
        {
            "tema": 3,
            "category": "Cálculos Celulares",
            "title": "Cálculo: Interferencia Cocanal (S/I) & Decibelios",
            "bullets": [
                "Distancia cocanal: D/R = √(3N).\nPara N = 7: D/R = √21 ≈ 4,58. Si R = 2 km -> Distancia D ≈ 9,17 km.",
                "Relación S/I: S/I = (√(3N))^n / 6 (con 6 interferentes y exponente n=4).\nS/I = (√21)⁴ / 6 = 21² / 6 = 441 / 6 = 73,5 lineal.\nEn decibelios: 10 · log10(73,5) ≈ 18,66 dB (estándar GSM exige ~18 dB).",
                "Reglas rápidas en dB:\n- Factor ×10 de potencia = +10 dB.\n- Factor ×2 de potencia = +3 dB (÷2 = -3 dB).\nEjemplo: Relación 40 = 10 × 2 × 2 -> 10 + 3 + 3 = 16 dB."
            ],
            "key": "Clave examen: N = 7 proporciona exactamente ~18,66 dB, por eso es el cluster estándar en 2G."
        },
        {
            "tema": 3,
            "category": "Cálculos Celulares",
            "title": "Cálculo: Tráfico en Erlangs & Grado de Servicio",
            "bullets": [
                "Erlang: Unidad de tráfico telefónico. 1 Erlang = uso continuo de 1 canal durante 1 hora (60 minutos de llamada).",
                "Intensidad de tráfico: A = (Nº llamadas × duración media) / Tiempo de observación.",
                "Ejercicio de examen: 500 llamadas de 4 minutos en 3 horas (180 min):\nVolumen = 500 × 4 = 2.000 min de llamada.\nIntensidad A = 2.000 / 180 ≈ 11,11 Erlangs.",
                "Grado de Servicio (GoS o bloqueo): GoS = Tráfico Perdido / Tráfico Ofrecido.\nSi se ofrecen 60 Erlangs y se pierden 3 Erlangs: GoS = 3 / 60 = 5% (Tráfico cursado = 57 Erlangs)."
            ],
            "key": "Clave examen: A = (N × d) / T. Tráfico Perdido = Tráfico Ofrecido - Tráfico Cursado."
        },

        # ==========================================
        # TEMA 4: IoT & DISEÑO DE APIs REST
        # ==========================================
        {
            "tema": 4,
            "category": "IoT",
            "title": "Internet of Things: Fundamentos",
            "bullets": [
                "Origen: Kevin Ashton acuñó el término en 1999 en el Auto-ID Center del MIT (con tecnología RFID).",
                "Sensores vs Actuadores: Sensores miden magnitudes físicas (temperatura, luz, presión); Actuadores ejecutan acciones físicas en el entorno (motores, relés, válvulas).",
                "Protocolo MQTT: Publicación/Suscripción mediante Broker. Cabecera ultra ligera de 2 bytes. Niveles de calidad: QoS 0 (como mucho una vez), QoS 1 (al menos una vez), QoS 2 (exactamente una vez).",
                "Protocolo CoAP: Modelo REST sobre UDP (cabecera de 4 bytes) para nodos extremadamente limitados."
            ],
            "key": "Clave examen: MQTT = Publish/Subscribe sobre TCP con Broker. CoAP = REST sobre UDP."
        },
        {
            "tema": 4,
            "category": "APIs REST",
            "title": "Principios REST & Verbos HTTP",
            "bullets": [
                "Principios REST: Stateless (sin estado en servidor), Cliente-Servidor, Cacheable, Interfaz Uniforme, Sistema en Capas.",
                "Idempotencia: Ejecutar la petición varias veces produce el mismo estado en el servidor.\n- Idempotentes: GET (seguro/lectura), PUT (reemplazo completo), DELETE (borrado).\n- No idempotente: POST (cada llamada crea un nuevo recurso independiente).",
                "Códigos HTTP clave:\n- 200 OK (éxito con datos) · 201 Created (recurso creado por POST) · 204 No Content (éxito sin cuerpo).\n- 400 Bad Request · 401 Unauthorized (falta autenticación) · 403 Forbidden (sin permisos) · 404 Not Found."
            ],
            "key": "Clave examen: 401 = no identificado; 403 = identificado pero sin permisos. PUT y DELETE son idempotentes."
        },
        {
            "tema": 4,
            "category": "OpenAPI / Swagger",
            "title": "Swagger vs OpenAPI 3.0",
            "bullets": [
                "Historia: Creado por Tony Tam (2010); en 2015 SmartBear dona la especificación a Linux Foundation como OpenAPI Specification (OAS). Swagger ahora son las herramientas (Editor, UI, Codegen).",
                "RAML: Lenguaje de modelado en YAML promovido por MuleSoft.",
                "Cabecera raíz: 'swagger: \"2.0\"' frente a 'openapi: \"3.0.0\"'.",
                "Servidores: 'host', 'basePath' y 'schemes' se unificaron en el array 'servers: [{url: \"...\"}]' (múltiples entornos).",
                "Cuerpo de petición: 'in: body' se sustituye por 'requestBody' con selector de tipos MIME ('application/json', 'multipart/form-data').",
                "Ubicación de parámetros en 3.0: path (con required: true obligatorio), query, header y cookie.",
                "Componentes: 'definitions' se sustituyó por 'components' (components.schemas, components.responses, components.securitySchemes)."
            ],
            "key": "Referencia JSON Pointer: $ref: '#/components/schemas/NombreEsquema'."
        }
    ]

if __name__ == '__main__':
    cards = get_flashcards()
    print(f"Total flashcards generated: {len(cards)}")
