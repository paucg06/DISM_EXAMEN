# -*- coding: utf-8 -*-
"""
Auditing blocks and generating missing questions for 100% full syllabus coverage.
"""

def get_wearables_touch_connectivity_questions():
    """Missing blocks from Tema 3.1: Wearables, Textillography, Touchscreens, Displays, Short-range connectivity"""
    return [
        # Wearables & Textillography
        {
            "tema": 3,
            "subtema": "Wearables y Textillography",
            "q": "¿Cuáles son los tres niveles de integración de la tecnología en prendas inteligentes (Textillography) según el temario?",
            "options": [
                "1. Electrónica añadida (módulo en bolsillo o clip) · 2. Electrónica integrada (sensores/conductores bordados o cosidos) · 3. La tela como dispositivo (fibras conductoras tejidas directamente en el telar)",
                "1. Bluetooth · 2. Wi-Fi · 3. Satelital",
                "1. Algodón · 2. Poliéster · 3. Seda",
                "1. Nivel usuario · 2. Nivel desarrollador · 3. Nivel fabricante"
            ],
            "correct": 0,
            "explanation": "El temario clasifica la integración textil en tres niveles evolutivos: Electrónica añadida (dispositivo externo fijado a la ropa), Electrónica integrada (componentes e hilos conductores cosidos/bordados sobre la tela) y La tela como dispositivo (la propia estructura del tejido utiliza hilos conductores de plata, cobre o polímeros para actuar como sensor, bus y teclado)."
        },
        {
            "tema": 3,
            "subtema": "Wearables y Textillography",
            "q": "¿Cuáles son las tres capas físicas típicas en el diseño de una prenda inteligente (e-textile) y cuál es la función de la capa intermedia?",
            "options": [
                "Capa exterior (protección), capa intermedia (electrónica, sensores y cableado conductor) y capa interior (confort en contacto con la piel)",
                "Capa de software, capa de firmware y capa de hardware",
                "Capa de batería, capa de memoria y capa de CPU",
                "Capa de red, capa de transporte y capa de aplicación"
            ],
            "correct": 0,
            "explanation": "La estructura textil se divide en: Capa exterior (protege frente al desgaste y climatología), Capa intermedia (aloja las pistas conductoras, sensores y electrónica protegida) y Capa interior (tejido transpirable y aislante en contacto directo con la piel humana)."
        },
        {
            "tema": 3,
            "subtema": "Wearables y Textillography",
            "q": "¿Cuál es uno de los mayores desafíos técnicos y de durabilidad en los textiles inteligentes (e-textiles)?",
            "options": [
                "La resistencia a los ciclos repetidos de lavado en lavadora, detergentes, secado, sudoración ácida/salina del cuerpo y flexión mecánica constante",
                "Que no pueden conducirse electrones por ningún material metálico",
                "Que la ropa solo se puede usar de noche",
                "Que la tela solo funciona si está mojada"
            ],
            "correct": 0,
            "explanation": "Los e-textiles deben soportar el estrés mecánico de doblado, el agua, los productos químicos de los detergentes en los ciclos de lavado, y la corrosión producida por el sudor salino humano."
        },
        # Touchscreens
        {
            "tema": 3,
            "subtema": "Pantallas Táctiles",
            "q": "¿Cómo funciona una pantalla táctil resistiva y cuáles son sus principales ventajas y limitaciones?",
            "options": [
                "Consta de dos capas conductoras transparentes (ITO) separadas por micro-espaciadores; al presionar físicamente entran en contacto. Ventaja: funciona con guantes, estiletes o cualquier objeto; Limitación: requiere presión física, suele soportar un solo toque y pierde brillo/transparencia",
                "Funciona emitiendo rayos láser desde la batería",
                "Utiliza una cámara frontal que graba los dedos en 3D",
                "Solo detecta el calor corporal y no funciona con frío"
            ],
            "correct": 0,
            "explanation": "La tecnología resistiva se basa en la presión mecánica que junta dos láminas conductoras flexibles. Es económica y operable con guantes o lápiz común (cajeros, terminales de pago TPV antiguos), pero carece de multitáctil fluido y ofrece menor visibilidad que las capacitivas."
        },
        {
            "tema": 3,
            "subtema": "Pantallas Táctiles",
            "q": "¿Qué tecnología de pantalla táctil es la estándar en prácticamente todos los smartphones modernos debido a su soporte multitáctil nativo, alta sensibilidad y excelente respuesta al deslizamiento de dedos?",
            "options": [
                "Capacitiva Proyectada (PCAP - Projected Capacitive)",
                "Resistiva de 4 hilos",
                "Onda acústica de superficie (SAW)",
                "Matriz de infrarrojos mecánica"
            ],
            "correct": 0,
            "explanation": "PCAP (Capacitiva Proyectada) utiliza una rejilla de electrodos X/Y que crea un campo electrostático proyectado a través del cristal protector. Cuando un conductor (el dedo) entra en el campo, altera la capacitancia local, permitiendo rastrear múltiples dedos simultáneamente con enorme precisión."
        },
        {
            "tema": 3,
            "subtema": "Pantallas Táctiles",
            "q": "¿Cómo funciona una pantalla táctil de onda acústica de superficie (SAW - Surface Acoustic Wave) y cuál es su principal ventaja?",
            "options": [
                "Emite ondas ultrasónicas sobre la superficie de un panel de vidrio puro. Al tocar con el dedo, se absorbe parte de la onda acústica. Ventaja: ofrece la máxima transparencia óptica y claridad de imagen (100% vidrio sin láminas conductoras que resten luz)",
                "Utiliza cables de cobre visibles a simple vista",
                "Requiere calentar el vidrio a 80 grados centígrados",
                "Solo funciona bajo el agua"
            ],
            "correct": 0,
            "explanation": "Las pantallas SAW emplean transductores piezoeléctricos que envían ondas acústicas superficiales por el cristal. Tienen una calidad de imagen inmejorable por ser vidrio puro, aunque son sensibles al agua, polvo o grasa en su superficie."
        },
        {
            "tema": 3,
            "subtema": "Pantallas Táctiles",
            "q": "¿Qué tecnología táctil utiliza un marco perimetral con emisores LED de luz infrarroja y fotodetectores enfrentados, activándose cuando un objeto interrumpe los haces de luz sin necesidad de tocar un cristal activo?",
            "options": [
                "Pantallas táctiles por infrarrojos (Optical IR)",
                "Pantalla capacitiva proyectada",
                "Pantalla resistiva analógica",
                "Pantalla E-Ink electroforética"
            ],
            "correct": 0,
            "explanation": "Las pantallas táctiles de infrarrojos crean una cuadrícula invisible de haces de luz sobre la pantalla; cualquier objeto (dedo, guante, lápiz) que interrumpa los haces es detectado sin degradar la pantalla con capas intermedias."
        },
        {
            "tema": 3,
            "subtema": "Pantallas Táctiles",
            "q": "¿Qué diferencia existe entre la integración táctil 'On-cell' e 'In-cell' en las pantallas de smartphones?",
            "options": [
                "En 'On-cell' la capa de sensores táctiles se sitúa sobre el filtro de color o cristal del display; en 'In-cell' los sensores táctiles están embebidos directamente dentro de las capas del propio panel LCD/OLED, haciendo la pantalla más delgada, ligera y con menos reflejos",
                "On-cell solo sirve para teléfonos plegables e In-cell para tablets",
                "In-cell requiere obligatoriamente una batería externa",
                "Son nombres comerciales sin ninguna diferencia técnica"
            ],
            "correct": 0,
            "explanation": "La tecnología In-cell fusiona los electrodos táctiles con el sustrato del display (LCD/OLED), eliminando una capa de vidrio intermedia, lo que reduce el grosor total del dispositivo y mejora sustancialmente la visibilidad a plena luz solar al reducir reflejos."
        },
        # Displays
        {
            "tema": 3,
            "subtema": "Displays y Pantallas",
            "q": "¿Cuál es la diferencia fundamental en el funcionamiento de una pantalla LCD frente a una pantalla OLED/AMOLED?",
            "options": [
                "LCD requiere una fuente de retroiluminación global (Backlight LED) trasera permanente con cristales líquidos que bloquean o dejan pasar la luz; OLED/AMOLED utiliza píxeles autoemisivos (diodos orgánicos) que emiten su propia luz de forma individual, logrando negros puros al apagarse por completo",
                "LCD no puede mostrar color rojo",
                "OLED consume siempre el triple de energía que LCD aunque la pantalla esté completamente en negro",
                "LCD utiliza tubos de rayos catódicos en miniatura"
            ],
            "correct": 0,
            "explanation": "En LCD, la luz trasera siempre está encendida y los cristales líquidos filtran la luz (los negros son grises oscuros). En OLED/AMOLED, cada subpíxel orgánico emite su propia luz; para mostrar el color negro, el píxel se apaga por completo (0 nits), logrando contraste infinito y ahorro de batería con interfaces oscuras."
        },
        {
            "tema": 3,
            "subtema": "Displays y Pantallas",
            "q": "¿Qué significa el concepto de pantalla 'Retina' introducido en la industria móvil?",
            "options": [
                "Una densidad de píxeles por pulgada (ppi) suficientemente alta (habitualmente >300-326 ppi a distancia de uso normal) como para que el ojo humano sea incapaz de distinguir los píxeles individuales a simple vista",
                "Una pantalla que escanea la retina del usuario para encenderse",
                "Una pantalla que proyecta la imagen directamente en el globo ocular mediante rayos X",
                "Un tipo de cristal fabricado con tejido biológico"
            ],
            "correct": 0,
            "explanation": "El término 'Retina Display' hace referencia a pantallas donde la resolución angular supera la agudeza visual del ojo humano promedio a la distancia típica de uso (~30 cm en móviles), haciendo que el texto y los bordes se perciban perfectamente lisos y continuos."
        },
        # Short-range connectivity
        {
            "tema": 3,
            "subtema": "Conectividad de Corto Alcance",
            "q": "¿Qué distingue a Bluetooth Low Energy (BLE / Bluetooth Smart) frente al Bluetooth Clásico (Basic Rate / EDR)?",
            "options": [
                "BLE está diseñado para transmitir pequeños paquetes de datos con consumo energético mínimo (capaz de operar meses o años con una pila de botón), permaneciendo la mayor parte del tiempo en reposo; el Bluetooth Clásico está optimizado para flujos continuos de datos pesados como audio de alta calidad",
                "BLE tiene un alcance de más de 500 kilómetros",
                "BLE no es compatible con teléfonos inteligentes",
                "El Bluetooth Clásico consume menos energía que BLE"
            ],
            "correct": 0,
            "explanation": "BLE (introducido en Bluetooth 4.0) reduce drásticamente el consumo enviando ráfagas cortas de datos y permaneciendo en 'deep sleep' el 99% del tiempo, siendo la base de la sincronización de pulseras de actividad, balizas (beacons) y sensores IoT."
        },
        {
            "tema": 3,
            "subtema": "Conectividad de Corto Alcance",
            "q": "¿Qué protocolo inalámbrico propietario de ultra bajo consumo, operando en la banda de 2,4 GHz, es ampliamente utilizado en monitores de frecuencia cardíaca, potenciómetros de ciclismo y sensores deportivos (respaldado por marcas como Garmin)?",
            "options": [
                "ANT y ANT+",
                "NFC",
                "IrDA",
                "LTE-M"
            ],
            "correct": 0,
            "explanation": "ANT y su perfil estandarizado ANT+ (propiedad de Dynastream / Garmin) es un protocolo de red inalámbrica de sensores de bajísimo consumo diseñado específicamente para la monitorización deportiva y de salud."
        },
        {
            "tema": 3,
            "subtema": "Conectividad de Corto Alcance",
            "q": "¿Qué tecnología inalámbrica basada en el estándar IEEE 802.15.4 permite crear redes en malla (Mesh) de bajo consumo, baja tasa de datos y auto-reconfigurables para domótica y automatización de edificios?",
            "options": [
                "Zigbee",
                "Wi-Fi 6E",
                "5G NR",
                "Ethernet Gigabit"
            ],
            "correct": 0,
            "explanation": "Zigbee opera sobre IEEE 802.15.4 y destaca por su topología Mesh (donde cada nodo conectado a la corriente puede reenviar mensajes de otros nodos), dotando de gran alcance y robustez a bombillas inteligentes, sensores de puertas y enchufes en el hogar."
        },
        {
            "tema": 3,
            "subtema": "Conectividad de Corto Alcance",
            "q": "¿Cuáles son las diferencias fundamentales entre RFID y NFC según el temario?",
            "options": [
                "RFID opera en múltiples bandas de frecuencia con alcances que pueden llegar a metros y comunicación habitualmente unidireccional (lector lee etiqueta); NFC es una evolución de RFID que opera estrictamente a 13,56 MHz con alcance ultra-corto (<4-10 cm), comunicación bidireccional y soporta tres modos (emulación de tarjeta, lectura/escritura y peer-to-peer)",
                "NFC requiere cables físicos y RFID no",
                "RFID solo sirve para pagos bancarios y NFC para identificar ganado",
                "No hay ninguna diferencia; son exactamente la misma palabra en distintos idiomas"
            ],
            "correct": 0,
            "explanation": "NFC es un subconjunto especializado de RFID en 13,56 MHz diseñado para máxima seguridad por proximidad extrema (<4-10 cm). Esto previene intercepciones y permite pagos móviles contactless mediante el modo de emulación de tarjeta segura (Apple Pay / Google Wallet)."
        }
    ]

def get_cellular_deep_questions():
    """Missing blocks from Tema 3.2: Cell splitting, Sectorization, Handover types & decisions, Guard channels, Paging"""
    return [
        {
            "tema": 3,
            "subtema": "Ingeniería Celular",
            "q": "¿En qué consiste la técnica de 'División Celular' (Cell Splitting) y cuál es su objetivo en una red móvil congestionada?",
            "options": [
                "Consiste en subdividir celdas de alta densidad de tráfico en celdas más pequeñas (microceldas o picoceldas) con estaciones base de menor potencia, aumentando la capacidad de usuarios por km² sin necesidad de adquirir nuevo espectro radioeléctrico",
                "Consiste en apagar la mitad de las antenas durante la noche para ahorrar energía",
                "Consiste en dividir a los usuarios según el operador al que pertenezcan",
                "Consiste en partir físicamente la tarjeta SIM en dos trozos"
            ],
            "correct": 0,
            "explanation": "Cell splitting es el método estándar de ampliación de capacidad en zonas urbanas: al reducir el radio de celda, las frecuencias se pueden reutilizar a distancias físicas mucho menores, multiplicando el número de canales disponibles por unidad de superficie."
        },
        {
            "tema": 3,
            "subtema": "Ingeniería Celular",
            "q": "¿Cómo contribuye la 'Sectorización' de antenas (por ejemplo, usar 3 sectores de 120° o 6 sectores de 60° en lugar de una antena omnidireccional de 360°) a la mejora de la red?",
            "options": [
                "Reduce drásticamente la interferencia cocanal, ya que las antenas direccionales solo irradian y reciben energía en un sector angular concreto, permitiendo utilizar tamaños de cluster N más pequeños y ganar capacidad",
                "Hace que los teléfonos no necesiten batería",
                "Elimina la necesidad de utilizar estaciones base en las ciudades",
                "Aumenta la velocidad de la luz en el aire"
            ],
            "correct": 0,
            "explanation": "Al sectorizar una estación base (típicamente en 3 sectores de 120°), cada sector solo 've' interferencias provenientes de su arco angular, reduciendo el número de células interferentes cocanal de 6 a solo 1 o 2, lo que mejora la relación S/I."
        },
        {
            "tema": 3,
            "subtema": "Traspaso (Handover)",
            "q": "¿Cuál es la diferencia fundamental entre un 'Hard Handover' y un 'Soft Handover'?",
            "options": [
                "Hard Handover sigue el principio 'break-before-make' (rompe la conexión con la celda actual antes de establecer enlace con la nueva); Soft Handover sigue el principio 'make-before-break' (mantiene la conexión simultánea con ambas celdas durante la transición antes de liberar la antigua)",
                "Hard Handover solo funciona con cables de red y Soft Handover por satélite",
                "Soft Handover requiere reiniciar el teléfono móvil",
                "Hard Handover solo se usa en llamadas internacionales"
            ],
            "correct": 0,
            "explanation": "Hard Handover desconecta momentáneamente la portadora antes de cambiar de frecuencia/canal (típico de GSM 2G y LTE inter-frecuencia). Soft Handover conecta con la nueva celda mientras aún transmite por la actual (característico de redes CDMA y 3G UMTS WCDMA en la misma frecuencia), evitando cortes perceptibles."
        },
        {
            "tema": 3,
            "subtema": "Traspaso (Handover)",
            "q": "¿Qué siglas identifican el tipo de traspaso donde el terminal móvil realiza periódicamente mediciones del nivel de señal de las estaciones base vecinas y las reporta a la red, siendo la estación base o el controlador (BSC/RNC) quien decide cuándo ejecutar el traspaso?",
            "options": [
                "MAHO (Mobile-Assisted Handover)",
                "NCHO (Network-Controlled Handover)",
                "MCHO (Mobile-Controlled Handover)",
                "DHCP (Dynamic Handover Protocol)"
            ],
            "correct": 0,
            "explanation": "En MAHO (Mobile-Assisted Handover, usado en GSM, 3G y 4G), el teléfono mide la calidad de los canales de control vecinos y envía los reportes a la red; la red evalúa y ordena el traspaso para una gestión óptima de recursos."
        },
        {
            "tema": 3,
            "subtema": "Traspaso (Handover)",
            "q": "¿Qué estrategia implementan los operadores de telefonía móvil para priorizar las llamadas en curso que realizan un traspaso (handover) sobre los intentos de inicio de llamadas nuevas?",
            "options": [
                "Asignación de 'Canales de Guarda' (Guard Channels), reservando una fracción de los canales de la celda exclusivamente para peticiones de traspaso",
                "Cobrar el triple por llamada al cambiar de antena",
                "Apagar los teléfonos de los usuarios que no estén hablando",
                "Obligar a todos los usuarios a usar Wi-Fi"
            ],
            "correct": 0,
            "explanation": "Para los usuarios, una llamada que se corta súbitamente en plena conversación (fallo de traspaso) resulta mucho más molesta que una llamada que no puede iniciarse por congestión (bloqueo). Por ello, se reservan canales de guarda exclusivos para absorber traspasos entrantes."
        },
        {
            "tema": 3,
            "subtema": "Procedimientos de Red Móvil",
            "q": "¿Cómo localiza la red celular a un terminal móvil que se encuentra en reposo (idle) para entregarle una llamada o mensaje entrante?",
            "options": [
                "Mediante el procedimiento de 'Paging' (búsqueda o radiolocalización), emitiendo un mensaje de aviso por el canal de control en todas las celdas pertenecientes al Área de Localización (Location Area - LA) donde el terminal está registrado en el VLR",
                "Enviando una señal acústica audible por los altavoces de todas las ciudades",
                "Esperando a que el usuario llame por teléfono para preguntarle dónde está",
                "Rastreando el terminal por satélite militar en tiempo real segundo a segundo"
            ],
            "correct": 0,
            "explanation": "Para no agotar la batería del móvil actualizando su celda exacta en cada esquina, la red agrupa celdas en 'Áreas de Localización' (Location Areas). Cuando llega una llamada, el MSC consulta el VLR y ordena un 'Paging' simultáneo en todas las celdas de esa área hasta que el terminal responde."
        }
    ]

def get_multimedia_deep_questions():
    """Missing blocks from Tema 2.1 & 2.2: Adaptive Bitrate Streaming (ABR), Hardware architectures for MMA (DSP, NPU, ASIC, FPGA)"""
    return [
        {
            "tema": 2,
            "subtema": "Arquitectura de Streaming",
            "q": "¿Cómo funciona el Streaming con Bitrate Adaptativo (ABR - Adaptive Bitrate Streaming) utilizado en plataformas como Netflix, YouTube o Twitch?",
            "options": [
                "El vídeo se codifica previamente en múltiples perfiles con distintas resoluciones y bitrates (ladder), y se trocea en segmentos cortos (de 2 a 10 segundos). El reproductor del cliente mide continuamente el ancho de banda disponible y la ocupación del búfer, solicitando dinámicamente el segmento de mayor calidad que pueda reproducirse sin interrupciones",
                "El servidor reduce la velocidad de la CPU del usuario cuando la red va lenta",
                "Se envía siempre un archivo binario comprimido con ZIP que debe descargarse al 100% antes de ver el primer fotograma",
                "El proveedor de internet corta la conexión si el usuario cambia de resolución"
            ],
            "correct": 0,
            "explanation": "ABR (la base de HLS y MPEG-DASH) segmenta el contenido en fragmentos temporales indexados en un archivo manifiesto (.m3u8 o .mpd). El cliente adapta en tiempo real la calidad pedida segmento a segmento según la salud de su búfer y la velocidad de descarga."
        },
        {
            "tema": 2,
            "subtema": "Procesadores Multimedia (MMA)",
            "q": "¿Qué características arquitectónicas definen a un procesador de señal digital (DSP - Digital Signal Processor) utilizado para procesamiento de audio y telecomunicaciones?",
            "options": [
                "Arquitectura Harvard (buses de memoria separados para datos e instrucciones), unidades aritméticas especializadas capaces de ejecutar instrucciones MAC (Multiply-Accumulate: A = A + B×C) en un único ciclo de reloj, y modos de direccionamiento circular y de inversión de bits (bit-reversal para algoritmos FFT)",
                "Arquitectura Von Neumann estricta sin registros aritméticos",
                "Incompatibilidad total con cualquier operación con números enteros",
                "Un procesador que solo funciona conectado a una pantalla de televisión"
            ],
            "correct": 0,
            "explanation": "Los DSPs están optimizados para filtrado digital, convoluciones y transformadas rápidas de Fourier (FFT), procesando streams continuos en tiempo real gracias a su arquitectura Harvard y operaciones Multiply-Accumulate (MAC) por ciclo."
        },
        {
            "tema": 2,
            "subtema": "Procesadores Multimedia (MMA)",
            "q": "¿Cuál es la diferencia fundamental entre un circuito integrado de aplicación específica (ASIC) y una matriz de puertas lógicas programable en campo (FPGA)?",
            "options": [
                "Un ASIC tiene sus circuitos de silicio permanentemente grabados durante la fabricación (máximo rendimiento y eficiencia energética, coste unitario bajo a gran escala, pero cero modificabilidad y altísimo coste inicial de diseño NRE); una FPGA está compuesta por bloques lógicos reconfigurables mediante software (HDL como VHDL/Verilog), permitiendo reprogramar el circuito tras su fabricación",
                "Un ASIC solo se utiliza para crear software en Python y una FPGA es una placa madre de PC",
                "Las FPGAs consumen diez veces menos energía que cualquier ASIC equivalente",
                "Un ASIC se puede reprogramar ilimitadas veces desde una página web"
            ],
            "correct": 0,
            "explanation": "Los ASICs son chips 'cableados' de fábrica para una tarea fija (como los codificadores hardware de vídeo H.264/AV1); las FPGAs ofrecen flexibilidad de hardware reconfigurable en campo, siendo ideales para prototipos o algoritmos en evolución."
        },
        {
            "tema": 2,
            "subtema": "Procesadores Multimedia (MMA)",
            "q": "¿Qué función cumple una NPU (Neural Processing Unit) integrada en los chipsets móviles modernos?",
            "options": [
                "Acelera de forma masiva y con alta eficiencia energética operaciones de cálculo matricial y tensorial (multiplicaciones y acumulaciones en enteros de 8/16 bits) requeridas por algoritmos de Machine Learning, visión por computador y fotografía computacional",
                "Se encarga de enfriar físicamente la batería del terminal mediante un ventilador",
                "Sustituye a la antena 5G para enviar datos por microondas",
                "Formatea el almacenamiento interno del smartphone cada 24 horas"
            ],
            "correct": 0,
            "explanation": "Las NPUs (como el Apple Neural Engine o las Tensor/Hexagon NPUs) están optimizadas en hardware para la inferencia ultrarrápida y de muy bajo consumo de modelos de inteligencia artificial en el propio dispositivo (on-device AI)."
        }
    ]

def get_openapi_deep_questions():
    """Missing blocks from Tema 4: OpenAPI 3.0 types, formats, parameter schema, securitySchemes"""
    return [
        {
            "tema": 4,
            "subtema": "OpenAPI 3.0",
            "q": "En la especificación OpenAPI 3.0, ¿cuál es la diferencia entre la propiedad 'type' y la propiedad 'format' al definir un campo en un esquema de datos (Schema)?",
            "options": [
                "'type' especifica el tipo de dato primitivo estándar (por ejemplo 'integer' o 'string'), mientras que 'format' es un modificador opcional que define la precisión o semántica concreta (por ejemplo format: 'int64', 'float', 'date-time', 'email', 'binary')",
                "'type' es para la base de datos y 'format' para el color del texto en el navegador",
                "Son dos propiedades que hacen lo mismo y nunca se deben combinar",
                "'format' indica obligatoriamente la extensión de archivo (.jpg, .mp3)"
            ],
            "correct": 0,
            "explanation": "OpenAPI 3.0 basa sus tipos en JSON Schema: `type` fija la categoría primitiva (string, number, integer, boolean, array, object) y `format` concreta la representación precisa (ej. `type: integer, format: int64` o `type: string, format: date-time`)."
        },
        {
            "tema": 4,
            "subtema": "OpenAPI 3.0",
            "q": "En un esquema de tipo objeto en OpenAPI 3.0, ¿cómo se definen los campos que son obligatorios para que la petición sea válida?",
            "options": [
                "Mediante un array de cadenas a nivel del objeto llamado 'required', que lista los nombres de las propiedades obligatorias (por ejemplo: required: ['id', 'nombre'])",
                "Añadiendo la etiqueta <mandatory> en cada línea",
                "Poniendo un asterisco '*' al final del nombre de la variable",
                "Escribiendo la palabra 'obligatorio: true' dentro de la URL"
            ],
            "correct": 0,
            "explanation": "En OpenAPI / JSON Schema, los campos obligatorios de un objeto se declaran en una lista en la raíz del schema: `required: [nombre_campo1, nombre_campo2]`."
        },
        {
            "tema": 4,
            "subtema": "OpenAPI 3.0",
            "q": "¿Cómo se define un parámetro de tipo 'path' (parámetro de ruta en la URL, como '/dispositivos/{id}') en OpenAPI 3.0?",
            "options": [
                "Se define con 'name: id', 'in: path' y la propiedad 'required: true' (la cual es estrictamente obligatoria en todos los parámetros de tipo path)",
                "Se define con 'in: body' y 'required: false'",
                "Se coloca en un archivo .txt separado en el servidor",
                "Los parámetros de path no se pueden describir en OpenAPI"
            ],
            "correct": 0,
            "explanation": "Para parámetros de ruta en la URL (`in: path`), la especificación OpenAPI 3.0 exige taxativamente que la propiedad `required` tenga el valor booleano `true`, ya que un endpoint no puede resolverse sin el segmento de ruta."
        },
        {
            "tema": 4,
            "subtema": "OpenAPI 3.0",
            "q": "En OpenAPI 3.0, ¿bajo qué subsección de 'components' se declaran los mecanismos de autenticación y autorización (como Bearer JWT, API Keys, OAuth2 u OpenID Connect)?",
            "options": [
                "components.securitySchemes",
                "components.passwords",
                "components.logins",
                "components.tokens"
            ],
            "correct": 0,
            "explanation": "Todos los esquemas de seguridad reutilizables se configuran bajo `components: securitySchemes:`, y luego se aplican a nivel global o por endpoint mediante la propiedad `security:`."
        }
    ]

print("Deep audit modules defined successfully")
