# -*- coding: utf-8 -*-
"""
Module providing extra calculation questions and missing theory for:
Tema 2 (RAID parity XOR, disk sizing, 4K video, audio sampling, MOPS)
Tema 3 (Cellular cluster formula, Erlangs traffic, S/I, channel distribution, dB)
Tema 4 (OpenAPI 3.0, Swagger 2.0 vs 3.0, REST architecture, RAML, HTTP status codes)
"""

def get_tema2_extra_questions():
    return [
        {
            "tema": 2,
            "subtema": "Cálculos RAID",
            "q": "EJERCICIO RAID: Se dispone de una matriz RAID 5 compuesta por 5 discos duros de 4 TB cada uno. ¿Cuál es la capacidad lógica utilizable del conjunto?",
            "options": [
                "16 TB",
                "20 TB",
                "12 TB",
                "8 TB"
            ],
            "correct": 0,
            "explanation": "En un RAID 5, la capacidad útil se calcula con la fórmula: Capacidad = (N - 1) × S, donde N es el número de discos y S la capacidad del disco más pequeño. Con N = 5 discos de 4 TB: (5 - 1) × 4 TB = 4 × 4 TB = 16 TB útiles. El equivalente a 1 disco (4 TB) se reserva distribuido para la paridad."
        },
        {
            "tema": 2,
            "subtema": "Cálculos RAID",
            "q": "EJERCICIO RAID: Se monta un sistema RAID 6 con 8 discos de 2 TB cada uno. ¿Cuál es la capacidad neta utilizable y cuántos discos pueden fallar simultáneamente sin pérdida de datos?",
            "options": [
                "Capacidad útil 12 TB, y tolera el fallo simultáneo de hasta 2 discos",
                "Capacidad útil 14 TB, y tolera el fallo de solo 1 disco",
                "Capacidad útil 16 TB, y tolera el fallo de hasta 4 discos",
                "Capacidad útil 8 TB, y tolera el fallo de hasta 3 discos"
            ],
            "correct": 0,
            "explanation": "En RAID 6 se utiliza doble paridad distribuida: Capacidad = (N - 2) × S. Con N = 8 discos de 2 TB: (8 - 2) × 2 TB = 6 × 2 TB = 12 TB utilizables. Al tener dos bloques de paridad independientes, tolera el fallo simultáneo de hasta 2 discos mecánicos cualesquiera."
        },
        {
            "tema": 2,
            "subtema": "Cálculos RAID",
            "q": "EJERCICIO RAID: En un RAID 5 con tres discos de datos D1, D2 y D3, calcula el valor del bloque de paridad P mediante XOR bit a bit si D1 = 1010, D2 = 1100 y D3 = 0011.",
            "options": [
                "0101",
                "1111",
                "0011",
                "1001"
            ],
            "correct": 0,
            "explanation": "Aplicamos XOR bit a bit de los tres discos:\n1) D1 ⊕ D2 = 1010 ⊕ 1100 = 0110 (los bits iguales dan 0, diferentes dan 1).\n2) (D1 ⊕ D2) ⊕ D3 = 0110 ⊕ 0011 = 0101.\nPor tanto, la paridad P es 0101."
        },
        {
            "tema": 2,
            "subtema": "Cálculos RAID",
            "q": "EJERCICIO RAID (Actualización de Paridad): En un RAID 5, cuando se modifica un solo bloque de datos, la nueva paridad se calcula eficientemente como P_nuevo = P_viejo ⊕ D_viejo ⊕ D_nuevo. Si P_viejo = 1111, D_viejo = 1010 y el nuevo dato a escribir es D_nuevo = 0001, ¿cuál es el valor de P_nuevo?",
            "options": [
                "0100",
                "1100",
                "0011",
                "1110"
            ],
            "correct": 0,
            "explanation": "Paso 1: P_viejo ⊕ D_viejo = 1111 ⊕ 1010 = 0101.\nPaso 2: 0101 ⊕ D_nuevo = 0101 ⊕ 0001 = 0100.\nPor tanto, P_nuevo = 0100. Esta técnica (Read-Modify-Write) evita tener que leer todos los demás discos de la matriz, requiriendo solo 2 lecturas y 2 escrituras."
        },
        {
            "tema": 2,
            "subtema": "Cálculos de Imagen",
            "q": "EJERCICIO MULTIMEDIA: Calcula el espacio en megabytes (MB) necesario para almacenar sin comprimir una fotografía de 12 Megapíxeles (resolución de 4000 × 3000 píxeles) con una profundidad de color TrueColor de 24 bits por píxel (RGB de 8 bits por canal).",
            "options": [
                "36 MB",
                "12 MB",
                "288 MB",
                "4,5 MB"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) Píxeles totales = 4000 × 3000 = 12.000.000 píxeles.\n2) 24 bits/píxel equivalen a 24 / 8 = 3 Bytes por píxel.\n3) Tamaño total en Bytes = 12.000.000 × 3 = 36.000.000 Bytes.\n4) En MB decimales: 36.000.000 / 10^6 = 36 MB (en MiB binarios: 36.000.000 / 1024^2 ≈ 34,33 MiB)."
        },
        {
            "tema": 2,
            "subtema": "Cálculos de Imagen",
            "q": "EJERCICIO MULTIMEDIA: Una cámara de smartphone toma una foto de 48 Mpx (resolución de 8000 × 6000 píxeles) en formato RAW con profundidad de 24 bits/píxel sin comprimir. ¿Cuánto espacio ocupa dicho archivo?",
            "options": [
                "144 MB",
                "48 MB",
                "96 MB",
                "1152 MB"
            ],
            "correct": 0,
            "explanation": "Píxeles totales = 8000 × 6000 = 48.000.000 píxeles.\nProfundidad: 24 bits = 3 Bytes por píxel.\nTamaño = 48.000.000 × 3 Bytes = 144.000.000 Bytes = 144 MB."
        },
        {
            "tema": 2,
            "subtema": "Cálculos de Vídeo",
            "q": "EJERCICIO MULTIMEDIA: Calcula el tamaño aproximado de un vídeo 4K UHD (3840 × 2160 píxeles) de 15 minutos de duración, a 25 fotogramas por segundo (fps) y 24 bits por píxel, totalmente sin comprimir.",
            "options": [
                "~560 GB (559,87 GB)",
                "~56 GB",
                "~15 GB",
                "~1,2 TB"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) Píxeles por fotograma = 3840 × 2160 = 8.294.400 píxeles.\n2) Tamaño de 1 fotograma (24 bits = 3 Bytes) = 8.294.400 × 3 = 24.883.200 Bytes (~24,88 MB).\n3) Tamaño por segundo (25 fps) = 24.883.200 × 25 = 622.080.000 Bytes/s (~622 MB/s).\n4) En 15 minutos hay 15 × 60 = 900 segundos.\n5) Tamaño total = 622.080.000 Bytes/s × 900 s = 559.872.000.000 Bytes ≈ 559,87 GB (ó 521,4 GiB).\nEsto demuestra por qué la compresión de vídeo es absolutamente imprescindible."
        },
        {
            "tema": 2,
            "subtema": "Cálculos de Vídeo",
            "q": "EJERCICIO MULTIMEDIA: Se transmite un vídeo 4K comprimido cuyo bitrate constante es de 15 Mbit/s. ¿Cuál es el tamaño total del archivo transferido tras 15 minutos de reproducción?",
            "options": [
                "~1,69 GB (1687,5 MB)",
                "~13,5 GB",
                "~450 MB",
                "~3,38 GB"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) Duración en segundos = 15 minutos × 60 s = 900 segundos.\n2) Bits totales = 15 Mbit/s × 900 s = 13.500 Mbit.\n3) Para pasar a MegaBytes (MB), dividimos entre 8 bits por byte: 13.500 / 8 = 1687,5 MB.\n4) En Gigabytes: 1687,5 / 1000 ≈ 1,69 GB (ó 1687,5 / 1024 ≈ 1,65 GiB)."
        },
        {
            "tema": 2,
            "subtema": "Cálculos de Vídeo",
            "q": "EJERCICIO MULTIMEDIA: Un vídeo Full HD (1920 × 1080) se graba a 30 fps con una profundidad de color de 32 bits por píxel (RGBA). ¿Cuánto espacio sin comprimir ocupa exactamente cada minuto de grabación?",
            "options": [
                "~13,90 GB/min (14.929.920.000 Bytes)",
                "~1,39 GB/min",
                "~60 GB/min",
                "~4,5 GB/min"
            ],
            "correct": 0,
            "explanation": "Píxeles por frame = 1920 × 1080 = 2.073.600 píxeles.\nBytes por frame (32 bits = 4 Bytes) = 2.073.600 × 4 = 8.294.400 Bytes/frame.\nPor segundo (30 fps) = 8.294.400 × 30 = 248.832.000 Bytes/s.\nPor minuto (60 segundos) = 248.832.000 × 60 = 14.929.920.000 Bytes ≈ 14,93 GB decimales (o 13,90 GiB binarios por minuto)."
        },
        {
            "tema": 2,
            "subtema": "Cálculos de Audio",
            "q": "EJERCICIO MULTIMEDIA: ¿Qué tamaño aproximado tiene un archivo de audio digital de alta resolución sin comprimir de 1 minuto de duración con calidad 24 bits, 96 kHz y 2 canales (estéreo)?",
            "options": [
                "~34,56 MB/min",
                "~10 MB/min",
                "~5 MB/min",
                "~120 MB/min"
            ],
            "correct": 0,
            "explanation": "Fórmula: Tamaño = Frecuencia de muestreo × Nº de canales × Bytes por muestra × Tiempo (s).\n1) Frecuencia = 96.000 muestras/segundo.\n2) 2 canales (estéreo).\n3) 24 bits = 3 Bytes por muestra.\n4) Por segundo = 96.000 × 2 × 3 = 576.000 Bytes/s.\n5) En 1 minuto (60 s) = 576.000 × 60 = 34.560.000 Bytes ≈ 34,56 MB/min."
        },
        {
            "tema": 2,
            "subtema": "Cálculos de Audio",
            "q": "EJERCICIO MULTIMEDIA: Un archivo de audio sin comprimir con estándar de CD Audio (44.100 Hz, 16 bits) dura 1 minuto. ¿Cuánto ocupa en mono (1 canal) y en estéreo (2 canales)?",
            "options": [
                "Aproximadamente 5,29 MB en mono y 10,58 MB en estéreo",
                "Aproximadamente 1 MB en mono y 2 MB en estéreo",
                "Aproximadamente 44 MB en mono y 88 MB en estéreo",
                "Aproximadamente 20 MB en mono y 40 MB en estéreo"
            ],
            "correct": 0,
            "explanation": "16 bits = 2 Bytes por muestra.\nEn mono (1 canal): 44.100 × 1 × 2 = 88.200 Bytes/s × 60 s = 5.292.000 Bytes ≈ 5,29 MB (~5 MB).\nEn estéreo (2 canales): 88.200 × 2 = 176.400 Bytes/s × 60 s = 10.584.000 Bytes ≈ 10,58 MB (~10 MB)."
        },
        {
            "tema": 2,
            "subtema": "Rendimiento y Complejidad",
            "q": "¿Qué rango de complejidad computacional (medido en MOPS) requiere la decodificación en tiempo real de un flujo de vídeo MPEG-2 con resolución estándar (720×480 a 30 fps y bitrate de 4 Mbps)?",
            "options": [
                "Entre 609 y 740 MOPS",
                "Menos de 10 MOPS",
                "Más de 100 GOPS",
                "Exactamente 50 MOPS"
            ],
            "correct": 0,
            "explanation": "Según el desglose del temario (Parser + VLC = 12 MOPS, Compensación de movimiento = 7 MOPS, Decuantificación = 148 MOPS, IDCT = 143-274 MOPS, Conversión YUV a RGB = 299 MOPS), el total oscila entre 609 y 740 MOPS."
        },
        {
            "tema": 2,
            "subtema": "Estándares MPEG",
            "q": "¿Qué estándar del grupo MPEG definió el perfil H.265 (HEVC), diseñado para la distribución eficiente de contenido en 4K UHD y HDR?",
            "options": [
                "MPEG-H (ISO/IEC 23008, Parte 2)",
                "MPEG-1",
                "MPEG-2",
                "MPEG-7"
            ],
            "correct": 0,
            "explanation": "MPEG-H (publicado en 2013) contiene en su Parte 2 el estándar HEVC/H.265, que duplica la eficiencia de compresión respecto a AVC/H.264 para soportar vídeo en ultra alta definición 4K/8K."
        },
        {
            "tema": 2,
            "subtema": "Estándares MPEG",
            "q": "¿Cuál es la función del estándar MPEG-7 frente a estándares como MPEG-2 o MPEG-4?",
            "options": [
                "No define un códec de vídeo ni de audio; es un estándar para la descripción formal de contenidos multimedia mediante metadatos (XML) para búsqueda y catalogación",
                "Es un códec de audio lossless para sustituir al FLAC",
                "Es un protocolo de cable físico de fibra óptica",
                "Es un sistema operativo para televisiones inteligentes"
            ],
            "correct": 0,
            "explanation": "MPEG-7 (ISO/IEC 15938) se titula 'Multimedia Content Description Interface' y su objetivo no es codificar la señal audiovisual, sino estructurar descriptores y esquemas en XML/JSON para indexación, búsqueda y recuperación de contenido."
        },
        {
            "tema": 2,
            "subtema": "Arquitectura Streaming",
            "q": "¿Cómo resuelve Netflix la distribución masiva de vídeo a nivel global para no saturar las troncales de internet?",
            "options": [
                "Utiliza Open Connect: instala servidores CDN propios (Open Connect Appliances - OCA) directamente dentro de los centros de datos de los proveedores de internet (ISP) locales, manteniendo en AWS solo la lógica de catálogo y control",
                "Transmite todo el vídeo mediante redes peer-to-peer (P2P) entre los televisores de los usuarios",
                "Envía discos duros por mensajería postal cada mes",
                "Emite todo el contenido por ondas de radio analógicas de televisión abierta"
            ],
            "correct": 0,
            "explanation": "La arquitectura Open Connect de Netflix despliega miles de servidores 'OCA' (Open Connect Appliances) integrados directamente en las redes de los operadores de telecomunicaciones (ISPs), sirviendo el tráfico de vídeo localmente mientras AWS gestiona el procesamiento, autenticación y catálogo."
        }
    ]

def get_tema3_extra_questions():
    return [
        {
            "tema": 3,
            "subtema": "Cálculos Celulares",
            "q": "EJERCICIO DE SISTEMAS CELULARES: La fórmula del tamaño del cluster es N = i² + j² + i·j, donde i y j son enteros no negativos. ¿Cuál es el tamaño de cluster N resultante para los desplazamientos (i = 2, j = 1)?",
            "options": [
                "N = 7",
                "N = 4",
                "N = 12",
                "N = 9"
            ],
            "correct": 0,
            "explanation": "Aplicando la fórmula: N = 2² + 1² + (2 · 1) = 4 + 1 + 2 = 7 células por cluster. Los valores permitidos más habituales en telefonía móvil hexagonal son N = 4 (para 2,0), N = 7 (para 2,1) y N = 12 (para 2,2)."
        },
        {
            "tema": 3,
            "subtema": "Cálculos Celulares",
            "q": "EJERCICIO DE SISTEMAS CELULARES: Un operador móvil dispone de un total de T = 420 canales dúplex para dar cobertura a una ciudad con 84 celdas hexagonales. Si se adopta un diseño con cluster de N = 7 (i=2, j=1), ¿cuántos canales por celda (K) y cuántos clusters (M) tendrá el sistema?",
            "options": [
                "K = 60 canales por celda y M = 12 clusters (capacidad total del sistema = 5.040 canales)",
                "K = 105 canales por celda y M = 21 clusters",
                "K = 35 canales por celda y M = 7 clusters",
                "K = 14 canales por celda y M = 6 clusters"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) Canales por celda: K = T / N = 420 / 7 = 60 canales.\n2) Número de réplicas o clusters: M = 84 celdas / N = 84 / 7 = 12 clusters.\n3) Capacidad total del sistema = M × T = 12 × 420 = 5.040 canales simultáneos.\n(Si se hubiera elegido N = 4, K = 105 y la capacidad sería 8.820 canales, pero con mayor interferencia cocanal)."
        },
        {
            "tema": 3,
            "subtema": "Cálculos Celulares",
            "q": "EJERCICIO DE SISTEMAS CELULARES: ¿Cuál es el compromiso (trade-off) fundamental al elegir un tamaño de cluster N pequeño (por ejemplo, N = 4) frente a uno grande (por ejemplo, N = 12)?",
            "options": [
                "Un N menor proporciona mayor cantidad de canales por celda y más capacidad global (M×T), pero aumenta la interferencia cocanal porque las celdas que reutilizan la misma frecuencia están más cerca",
                "Un N menor reduce el coste de los smartphones",
                "Un N mayor siempre produce menos cobertura de radio",
                "El tamaño de cluster no tiene ninguna relación con la interferencia ni con los canales"
            ],
            "correct": 0,
            "explanation": "Cuanto menor es N, mayor es el número de canales disponibles por célula (K = T/N) y la capacidad total de abonados, pero las celdas cocanal quedan situadas a menor distancia relativa (D/R = √(3N)), incrementando la interferencia cocanal."
        },
        {
            "tema": 3,
            "subtema": "Cálculos Celulares",
            "q": "EJERCICIO DE SISTEMAS CELULARES: La relación de distancia de reutilización cocanal viene dada por D/R = √(3N). Para un cluster de tamaño N = 7 en celdas con un radio R = 2 km, ¿a qué distancia aproximada D se encuentran las estaciones base de las celdas cocanal más cercanas?",
            "options": [
                "Aproximadamente 9,17 km (D/R ≈ 4,58)",
                "Aproximadamente 4,2 km",
                "Aproximadamente 14 km",
                "Aproximadamente 2 km"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) D/R = √(3 × 7) = √21 ≈ 4,5826.\n2) Despejando la distancia D: D = 4,5826 × R = 4,5826 × 2 km ≈ 9,17 km.\n(Para comparar: con N=4, D/R ≈ 3,46 y D ≈ 6,9 km; con N=12, D/R = 6,0 y D = 12 km)."
        },
        {
            "tema": 3,
            "subtema": "Cálculos de Señal e Interferencia",
            "q": "EJERCICIO DE SISTEMAS CELULARES: Considerando un entorno celular urbano con exponente de pérdidas n = 4 y las 6 celdas interferentes del primer anillo (i0 = 6), ¿cuál es la relación señal/interferencia (S/I) en decibelios (dB) para un cluster N = 7 según la fórmula S/I = (√(3N))^n / 6?",
            "options": [
                "~18,66 dB (relación lineal de 73,5)",
                "~12,2 dB",
                "~25,4 dB",
                "~9,0 dB"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) D/R = √(3 × 7) = √21.\n2) (D/R)^4 = (√21)^4 = 21² = 441.\n3) S/I lineal = 441 / 6 = 73,5.\n4) En decibelios (dB): S/I (dB) = 10 · log10(73,5) ≈ 18,66 dB.\nComo el estándar GSM exige un mínimo de ~18 dB de S/I para comunicaciones de voz aceptables, N = 7 es el tamaño de cluster estándar por excelencia en redes 2G."
        },
        {
            "tema": 3,
            "subtema": "Cálculos en Decibelios",
            "q": "EJERCICIO DE POTENCIA EN dB: Según las reglas de cálculo rápido en decibelios vistas en clase (×10 de potencia = +10 dB, ×2 de potencia = +3 dB), si una señal P1 tiene una potencia de 40 mW y el ruido/interferencia P2 es de 1 mW, ¿cuál es su relación en dB?",
            "options": [
                "16 dB",
                "40 dB",
                "4 dB",
                "6 dB"
            ],
            "correct": 0,
            "explanation": "La relación de potencia es 40 / 1 = 40.\nPodemos descomponer 40 como 10 × 2 × 2:\n- El factor 10 aporta +10 dB.\n- Cada factor 2 aporta +3 dB.\nTotal = 10 dB + 3 dB + 3 dB = 16 dB.\n(Cálculo exacto: 10 · log10(40) = 10 · 1,602 = 16,02 dB)."
        },
        {
            "tema": 3,
            "subtema": "Cálculos de Tráfico (Erlangs)",
            "q": "EJERCICIO DE TRÁFICO (Erlangs): ¿Qué representa exactamente la unidad 'Erlang' en ingeniería de telecomunicaciones?",
            "options": [
                "La ocupación continua y completa de un circuito o canal de comunicaciones durante un periodo de observación de una hora (equivalente a 60 minutos de llamada)",
                "El número máximo de antenas repetidoras que puede tener un operador",
                "La frecuencia de refresco de la pantalla en hercios",
                "La pérdida de paquetes en una red Wi-Fi por kilómetro"
            ],
            "correct": 0,
            "explanation": "El Erlang es una unidad adimensional de intensidad de tráfico: 1 Erlang equivale al uso continuo al 100% de un canal de voz durante una hora (por ejemplo, una llamada que dura 60 minutos, o 30 llamadas que duran 2 minutos en una hora)."
        },
        {
            "tema": 3,
            "subtema": "Cálculos de Tráfico (Erlangs)",
            "q": "EJERCICIO DE TRÁFICO (Ejercicio 4 del temario): Un grupo de circuitos cursan en un periodo de 3 horas un total de 500 llamadas con un tiempo medio de duración de 4 minutos. ¿Cuál es el volumen de tráfico y la intensidad de tráfico cursado en Erlangs?",
            "options": [
                "Volumen: 2.000 minutos de llamada (33,33 horas-Erlang); Intensidad: 11,11 Erlangs",
                "Volumen: 500 llamadas; Intensidad: 55,5 Erlangs",
                "Volumen: 120 minutos; Intensidad: 3 Erlangs",
                "Volumen: 6.000 minutos; Intensidad: 20 Erlangs"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) Volumen de tráfico = Nº de llamadas × duración media = 500 × 4 min = 2.000 minutos de llamada (ó 2000 / 60 ≈ 33,33 horas-Erlang).\n2) Tiempo de observación T = 3 horas = 180 minutos.\n3) Intensidad de tráfico cursado: A = Volumen / T = 2.000 min / 180 min ≈ 11,11 Erlangs."
        },
        {
            "tema": 3,
            "subtema": "Cálculos de Tráfico (Erlangs)",
            "q": "EJERCICIO DE TRÁFICO (Ejercicio 5 del temario): Calcula la intensidad de tráfico en Erlangs para un grupo de circuitos sabiendo que se registran 600 llamadas con una duración media de 3 minutos durante un tiempo de observación de 3 horas.",
            "options": [
                "10 Erlangs",
                "6 Erlangs",
                "18 Erlangs",
                "1 Erlang"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) Tiempo total ocupado = 600 llamadas × 3 minutos = 1.800 minutos.\n2) Tiempo de observación = 3 horas = 180 minutos.\n3) Intensidad de tráfico A = 1.800 min / 180 min = 10 Erlangs."
        },
        {
            "tema": 3,
            "subtema": "Cálculos de Tráfico (Erlangs)",
            "q": "EJERCICIO DE TRÁFICO (Ejercicio 6 del temario): En un grupo de circuitos el tráfico ofrecido es de 25 Erlangs y el tráfico efectivamente cursado es de 15 Erlangs. ¿Cuál es el Grado de Servicio (GoS o probabilidad de bloqueo) de la red?",
            "options": [
                "40% (GoS = 0,40)",
                "10%",
                "60%",
                "25%"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) Tráfico perdido = Tráfico Ofrecido - Tráfico Cursado = 25 - 15 = 10 Erlangs.\n2) Grado de Servicio (GoS) = Tráfico Perdido / Tráfico Ofrecido = 10 / 25 = 0,40 = 40%."
        },
        {
            "tema": 3,
            "subtema": "Cálculos de Tráfico (Erlangs)",
            "q": "EJERCICIO DE TRÁFICO: En la hora cargada, una central celular recibe 1.200 llamadas de 3 minutos de duración media. 60 llamadas encuentran todos los canales ocupados y se descartan. ¿Cuáles son el tráfico ofrecido (TO), el tráfico cursado (TC) y el grado de servicio (GoS)?",
            "options": [
                "TO = 60 Erlangs, GoS = 5%, TC = 57 Erlangs (tráfico perdido = 3 Erlangs)",
                "TO = 100 Erlangs, GoS = 10%, TC = 90 Erlangs",
                "TO = 36 Erlangs, GoS = 1%, TC = 35 Erlangs",
                "TO = 60 Erlangs, GoS = 60%, TC = 0 Erlangs"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) Tasa de llegada λ = 1.200 llamadas/hora. Duración media h = 3 min = 3/60 horas = 0,05 h.\n2) Tráfico ofrecido: TO = λ · h = 1.200 × (3/60) = 60 Erlangs.\n3) GoS = Llamadas perdidas / Llamadas totales = 60 / 1.200 = 0,05 = 5%.\n4) Tráfico cursado: TC = TO × (1 - GoS) = 60 × 0,95 = 57 Erlangs.\n5) Tráfico perdido = 60 - 57 = 3 Erlangs."
        },
        {
            "tema": 3,
            "subtema": "Canales Celulares",
            "q": "EJERCICIO DE ANCHO DE BANDA: Un operador tiene asignada una banda de 33 MHz para un sistema móvil donde cada canal dúplex requiere dos portadoras simplex de 25 kHz (una de subida y una de bajada). ¿Cuántos canales dúplex totales hay y cuántos corresponden a cada celda si se utiliza un cluster de N = 7?",
            "options": [
                "Total T = 660 canales dúplex; en un cluster N=7 corresponden ~94 canales por célula",
                "Total T = 1.320 canales dúplex; corresponden 188 canales por célula",
                "Total T = 330 canales dúplex; corresponden 47 canales por célula",
                "Total T = 100 canales dúplex; corresponden 10 canales por célula"
            ],
            "correct": 0,
            "explanation": "Paso a paso:\n1) Cada canal dúplex necesita 2 canales simplex de 25 kHz = 50 kHz por canal dúplex.\n2) Ancho de banda total = 33 MHz = 33.000 kHz.\n3) Número total de canales dúplex: T = 33.000 kHz / 50 kHz = 660 canales dúplex.\n4) Para N = 7 células por cluster: K = T / N = 660 / 7 ≈ 94,28 (94 canales utilizables por cada célula)."
        }
    ]

def get_tema4_extra_questions():
    return [
        {
            "tema": 4,
            "subtema": "APIs REST",
            "q": "¿Cuáles son los métodos HTTP estándar que se consideran 'idempotentes' según la especificación REST y HTTP?",
            "options": [
                "GET, PUT y DELETE (ejecutar la misma petición múltiples veces produce el mismo efecto en el estado del servidor)",
                "Únicamente POST",
                "POST y PATCH",
                "Ningún método HTTP es idempotente"
            ],
            "correct": 0,
            "explanation": "En HTTP/REST, un método es idempotente si realizar la misma petición una o varias veces produce el mismo estado en el servidor. GET (solo lee), PUT (reemplaza por completo el recurso) y DELETE (elimina el recurso) son idempotentes; POST no lo es porque múltiples llamadas generan múltiples recursos nuevos."
        },
        {
            "tema": 4,
            "subtema": "APIs REST",
            "q": "¿Qué código de estado HTTP debe devolver típicamente un endpoint REST tras procesar con éxito una petición POST que crea un nuevo recurso en la base de datos?",
            "options": [
                "201 Created",
                "200 OK",
                "204 No Content",
                "304 Not Modified"
            ],
            "correct": 0,
            "explanation": "El código HTTP estándar para indicar que la solicitud se ha completado con éxito y ha tenido como resultado la creación de un nuevo recurso es '201 Created' (habitualmente acompañado de la cabecera 'Location' con la URI del recurso creado)."
        },
        {
            "tema": 4,
            "subtema": "APIs REST",
            "q": "¿Qué código de estado HTTP se utiliza cuando una petición PUT o DELETE se ejecuta con éxito pero el servidor decide no enviar ningún cuerpo en la respuesta?",
            "options": [
                "204 No Content",
                "404 Not Found",
                "200 OK",
                "400 Bad Request"
            ],
            "correct": 0,
            "explanation": "'204 No Content' significa que el servidor ha procesado con éxito la solicitud pero no devuelve ningún contenido en el cuerpo del mensaje."
        },
        {
            "tema": 4,
            "subtema": "APIs REST",
            "q": "¿Cuál es la diferencia fundamental entre los códigos de error HTTP 401 Unauthorized y 403 Forbidden?",
            "options": [
                "401 significa que el cliente no se ha autenticado (falta token o credenciales inválidas), mientras que 403 significa que el cliente está autenticado pero no tiene los permisos suficientes para acceder al recurso",
                "401 es un error del servidor interno y 403 es un error de conexión Wi-Fi",
                "Son exactamente sinónimos y se usan indistintamente",
                "401 solo se usa en páginas HTML y 403 en JSON"
            ],
            "correct": 0,
            "explanation": "401 Unauthorized indica ausencia o fallo de autenticación (requiere autenticarse); 403 Forbidden significa que el servidor conoce la identidad del usuario pero este carece de autorización/permisos para realizar la acción."
        },
        {
            "tema": 4,
            "subtema": "OpenAPI vs Swagger",
            "q": "¿Cuál es la relación histórica y conceptual exacta entre Swagger y la especificación OpenAPI (OAS)?",
            "options": [
                "OpenAPI es la especificación estándar abierta (creada tras donar Swagger 2.0 a la Linux Foundation en 2015), mientras que 'Swagger' se refiere hoy a las herramientas de software de SmartBear (Swagger Editor, Swagger UI, Swagger Codegen)",
                "Swagger es el nombre moderno de OpenAPI creado por Google en 2024",
                "Swagger es un lenguaje binario y OpenAPI es un framework de Python",
                "OpenAPI fue abandonado y sustituido por Swagger 5.0"
            ],
            "correct": 0,
            "explanation": "Tony Tam creó Swagger en 2010. En 2015, SmartBear donó la especificación Swagger a la Linux Foundation, creando la iniciativa OpenAPI Specification (OAS). Hoy, OpenAPI es el formato estándar independiente del proveedor y Swagger son las herramientas que lo implementan."
        },
        {
            "tema": 4,
            "subtema": "RAML",
            "q": "¿Qué es RAML y qué empresa lo promovió principalmente?",
            "options": [
                "RESTful API Modeling Language, una especificación basada en YAML para diseñar APIs desarrollada por MuleSoft",
                "Un microcontrolador para dispositivos Arduino",
                "Un tipo de memoria RAM volátil",
                "Un servidor web escrito en Erlang"
            ],
            "correct": 0,
            "explanation": "RAML (RESTful API Modeling Language) es un lenguaje basado en YAML diseñado por MuleSoft para describir y modelar APIs RESTful antes de escribirlas."
        },
        {
            "tema": 4,
            "subtema": "Swagger 2.0 vs OpenAPI 3.0",
            "q": "¿Cómo se especifica la versión del estándar al inicio del documento en Swagger 2.0 frente a OpenAPI 3.0?",
            "options": [
                "En la versión antigua: 'swagger: \"2.0\"'; en la versión moderna: 'openapi: \"3.0.0\"'",
                "En ambas se escribe 'version: 1.0'",
                "En Swagger 2.0 es 'api: 2.0' y en OpenAPI es 'oas: 3.0'",
                "No se indica ninguna versión en el encabezado"
            ],
            "correct": 0,
            "explanation": "La propiedad raíz que identifica la especificación cambió de `swagger: \"2.0\"` a `openapi: \"3.0.0\"` (o versiones 3.0.x / 3.1.x)."
        },
        {
            "tema": 4,
            "subtema": "Swagger 2.0 vs OpenAPI 3.0",
            "q": "¿Cómo cambió la definición de la URL base del servidor entre Swagger 2.0 y OpenAPI 3.0?",
            "options": [
                "Swagger 2.0 separaba 'host', 'basePath' y 'schemes' (limitado a un único host), mientras que OpenAPI 3.0 los unificó en una lista flexible 'servers' con soporte para múltiples URLs y variables",
                "En Swagger 2.0 se usaba IP numérica y en OpenAPI 3.0 solo nombres de dominio .org",
                "OpenAPI 3.0 eliminó por completo el concepto de servidor",
                "Swagger 2.0 no permitía definir URLs"
            ],
            "correct": 0,
            "explanation": "En OpenAPI 3.0 se define `servers: [{ url: 'https://api.empresa.com/v1', description: 'Producción' }, { url: 'https://staging.empresa.com/v1' }]`, permitiendo definir múltiples servidores y parámetros variables en la URL."
        },
        {
            "tema": 4,
            "subtema": "Swagger 2.0 vs OpenAPI 3.0",
            "q": "¿Cómo se define el cuerpo de la petición (payload enviado en un POST o PUT) en OpenAPI 3.0 frente a Swagger 2.0?",
            "options": [
                "Swagger 2.0 usaba un parámetro con 'in: body'; OpenAPI 3.0 utiliza el objeto dedicado 'requestBody', permitiendo mapear el esquema a distintos tipos MIME (application/json, multipart/form-data, etc.)",
                "OpenAPI 3.0 prohíbe enviar cuerpos en las peticiones HTTP",
                "En OpenAPI 3.0 el body se envía obligatoriamente en las cabeceras HTTP",
                "Swagger 2.0 no permitía peticiones POST"
            ],
            "correct": 0,
            "explanation": "OpenAPI 3.0 reemplazó `in: body` y `in: formData` por el elemento `requestBody: { content: { 'application/json': { schema: ... } } }`, otorgando mucha más flexibilidad para múltiples formatos de contenido."
        },
        {
            "tema": 4,
            "subtema": "Swagger 2.0 vs OpenAPI 3.0",
            "q": "¿Cuáles son los cuatro tipos válidos de parámetros según su ubicación ('in') en OpenAPI 3.0?",
            "options": [
                "path, query, header y cookie",
                "body, form, query y file",
                "url, json, xml y stream",
                "get, post, put y delete"
            ],
            "correct": 0,
            "explanation": "En OpenAPI 3.0 los parámetros solo pueden residir en cuatro ubicaciones: `in: path` (ej. `/usuarios/{id}`), `in: query` (ej. `?filtro=activo`), `in: header` (cabeceras HTTP) e `in: cookie` (cookies del cliente)."
        },
        {
            "tema": 4,
            "subtema": "OpenAPI 3.0",
            "q": "En un documento OpenAPI 3.0, ¿bajo qué sección principal se declaran los modelos de datos, esquemas, respuestas y parámetros reutilizables?",
            "options": [
                "components (ej. components.schemas, components.responses, components.parameters)",
                "definitions",
                "globals",
                "models"
            ],
            "correct": 0,
            "explanation": "OpenAPI 3.0 unificó todas las declaraciones reutilizables bajo la clave `components:` (incluyendo `components/schemas`, `components/responses`, `components/parameters`, `components/securitySchemes`), reemplazando al antiguo `definitions:` de Swagger 2.0."
        },
        {
            "tema": 4,
            "subtema": "OpenAPI 3.0",
            "q": "¿Cuál es la sintaxis JSON Pointer correcta en OpenAPI 3.0 para hacer referencia ($ref) a un esquema de datos llamado 'Dispositivo' definido en la sección de componentes reutilizables?",
            "options": [
                "$ref: '#/components/schemas/Dispositivo'",
                "$ref: 'Dispositivo.class'",
                "$ref: 'import Dispositivo from components'",
                "$ref: 'file://schemas.json#Dispositivo'"
            ],
            "correct": 0,
            "explanation": "La especificación utiliza referencias JSON Reference: `$ref: '#/components/schemas/Dispositivo'`, donde `#` representa la raíz del documento actual."
        },
        {
            "tema": 4,
            "subtema": "Herramientas Swagger",
            "q": "¿Cuál de las siguientes herramientas oficiales de Swagger permite visualizar una documentación interactiva en el navegador desde la cual probar las peticiones directamente contra la API?",
            "options": [
                "Swagger UI",
                "Swagger Codegen",
                "Swagger Compiler",
                "Swagger Monitor"
            ],
            "correct": 0,
            "explanation": "Swagger UI renderiza la especificación OpenAPI en una página web interactiva donde cualquier usuario o desarrollador puede explorar los endpoints y ejecutarlos mediante el botón 'Try it out'."
        },
        {
            "tema": 4,
            "subtema": "Herramientas Swagger",
            "q": "¿Qué herramienta del ecosistema Swagger permite generar automáticamente el código esqueleto del servidor (Stubs en Node, Spring, etc.) y las librerías cliente (SDKs en Java, Swift, Python) a partir de una especificación OpenAPI?",
            "options": [
                "Swagger Codegen / OpenAPI Generator",
                "Swagger Viewer",
                "Swagger Inspector",
                "Swagger Proxy"
            ],
            "correct": 0,
            "explanation": "Swagger Codegen (y su fork OpenAPI Generator) procesa el archivo YAML/JSON de la API y genera automáticamente clientes y servidores en más de 40 lenguajes de programación."
        },
        {
            "tema": 4,
            "subtema": "OpenAPI 3.0",
            "q": "En la sección 'paths' de una especificación OpenAPI 3.0, ¿qué representa cada clave de primer nivel?",
            "options": [
                "La ruta relativa del endpoint (por ejemplo '/dispositivos/{id}') comenzando obligatoriamente por una barra '/'",
                "El nombre de la tabla de la base de datos",
                "La contraseña del administrador",
                "La dirección IP del cliente"
            ],
            "correct": 0,
            "explanation": "La sección `paths` mapea cada ruta relativa de la API (endpoint, comenzando por `/`) con las operaciones HTTP asociadas (get, post, put, delete, etc.)."
        }
    ]
