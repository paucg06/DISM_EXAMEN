# -*- coding: utf-8 -*-
import json
import re

def build_curated_database():
    with open('all_questions.json', 'r', encoding='utf-8') as f:
        original_data = json.load(f)

    # 1. FILTRAR TEMA 1
    # Mantener preguntas de conceptos generales nativo vs hibrido, frameworks y comparativas
    # Excluir detalles de arquitectura profunda de cada framework (ej. Stencil, Yoga, Fabric, CLI capacitor npx sync, Rust en Tauri, Sensor Tower)
    t1_excluded_patterns = [
        'sensor tower', 'q1 2025', 'gasto global', 'juegos vs', 
        'stencil', 'yoga', 'fabric', 'turbomodules', 'npx cap sync', 
        'tauri', 'pwa (progressive web app)', 'service worker', 'manifest.json', 'cache-first', 'network-first',
        'app bundle', '.aab', '.apk', 'emulacin/virtualiz'
    ]
    
    t1_curated = []
    for q in original_data:
        if q.get('tema') == 1:
            q_text = (q['q'] + ' ' + q.get('explanation', '')).lower()
            if any(p in q_text for p in t1_excluded_patterns):
                continue
            t1_curated.append(q)

    # Añadir preguntas clave y explícitas de clasificación de Frameworks (Híbrido vs Nativo)
    t1_extra = [
        {
            "id": "t1_fw_01",
            "tema": 1,
            "subtema": "Clasificación de Frameworks",
            "q": "¿Cuál de los siguientes frameworks se clasifica como una aplicación HÍBRIDA debido a que requiere un WebView o contenedor web para ejecutarse?",
            "options": [
                "React Native",
                "Apache Cordova / Ionic",
                ".NET MAUI",
                "NativeScript"
            ],
            "correct": 1,
            "explanation": "Ionic y Apache Cordova son aplicaciones híbridas: se desarrollan con tecnologías web (HTML, CSS y JS) y se ejecutan dentro de un contenedor o WebView en el dispositivo móvil."
        },
        {
            "id": "t1_fw_02",
            "tema": 1,
            "subtema": "Clasificación de Frameworks",
            "q": "¿Cuál de los siguientes frameworks se clasifica como NATIVO porque compila sus componentes y se ejecuta directamente sobre el sistema operativo sin usar un WebView?",
            "options": [
                "Ionic",
                "Apache Cordova",
                "PhoneGap",
                "React Native"
            ],
            "correct": 3,
            "explanation": "React Native es nativo: aunque el desarrollador escribe en JavaScript/JSX, la interfaz se renderiza utilizando los widgets nativos del sistema operativo móvil (sin WebView)."
        },
        {
            "id": "t1_fw_03",
            "tema": 1,
            "subtema": "Clasificación de Frameworks",
            "q": "Según la clasificación del temario oficial, ¿cómo se catalogan Unity y Apache Cordova?",
            "options": [
                "Ambas se catalogan como Híbridas porque requieren una capa adicional (contenedor o navegador) para ejecutarse",
                "Ambas se catalogan como Nativas porque se distribuyen a través de las tiendas oficiales de apps",
                "Unity es Nativa y Apache Cordova es Progresiva (PWA)",
                "Ninguna de las anteriores es correcta"
            ],
            "correct": 0,
            "explanation": "En el temario de DISM se establece textualmente: si requieren una capa adicional para ejecutarse como un navegador o un contenedor, son híbridas (Apache Cordova, Ionic, Unity)."
        },
        {
            "id": "t1_fw_04",
            "tema": 1,
            "subtema": "Clasificación de Frameworks",
            "q": "¿A qué categoría corresponde el framework Xamarin / .NET MAUI según el temario?",
            "options": [
                "Aplicación Web / PWA",
                "Aplicación Híbrida ejecutada en WebView",
                "Aplicación Nativa (se compila y ejecuta directamente en el SO aprovechando controles nativos)",
                "Aplicación Emulada por script de servidor"
            ],
            "correct": 2,
            "explanation": "Xamarin y su sucesor .NET MAUI son clasificados como frameworks nativos: permiten escribir en C# y compilan código que se ejecuta directamente sobre el SO utilizando la UI nativa de cada plataforma."
        },
        {
            "id": "t1_fw_05",
            "tema": 1,
            "subtema": "Clasificación de Frameworks",
            "q": "¿Qué caracteriza a Flutter en la clasificación del desarrollo multiplataforma?",
            "options": [
                "Es una aplicación híbrida porque encapsula HTML y CSS dentro de una ventana de navegador",
                "Es un framework que genera aplicaciones nativas dibujando su propia interfaz píxel a píxel mediante un motor gráfico en un lienzo nativo",
                "Es una aplicación web que requiere conexión permanente a un servidor remoto",
                "Es un framework exclusivamente interpretado en JavaScript sin acceso a aceleración gráfica"
            ],
            "correct": 1,
            "explanation": "Flutter no utiliza WebViews ni tampoco widgets nativos del SO: dibuja su propia interfaz mediante su motor gráfico directamente en un canvas nativo, ofreciendo rendimiento nativo a 60/120 fps."
        },
        {
            "id": "t1_fw_06",
            "tema": 1,
            "subtema": "Clasificación de Frameworks",
            "q": "¿Cuál es la principal ventaja de rendimiento de una aplicación nativa frente a una híbrida basada en WebView?",
            "options": [
                "La app nativa consume mucho más almacenamiento pero no usa memoria RAM",
                "La app nativa trabaja directamente con el hardware y la GPU del dispositivo sin la sobrecarga de capas de abstracción del navegador web",
                "La app híbrida siempre es más rápida porque HTML y CSS son lenguajes de bajo nivel",
                "No existe ninguna diferencia medible de rendimiento entre nativo e híbrido"
            ],
            "correct": 1,
            "explanation": "El rendimiento de las aplicaciones nativas es superior porque interactúan directamente con el procesador, la memoria y las APIs del SO sin requerir el motor del navegador (WebView) ni bridges de traducción."
        },
        {
            "id": "t1_fw_07",
            "tema": 1,
            "subtema": "Clasificación de Frameworks",
            "q": "Si un framework requiere plugins intermedios para acceder a la cámara, el acelerómetro o el GPS debido a que la lógica corre en un navegador interno, se trata de:",
            "options": [
                "Un desarrollo Nativo puro",
                "Una Aplicación Híbrida (como Ionic o Apache Cordova)",
                "Un microcontrolador embebido",
                "Una máquina virtual Java independiente del hardware"
            ],
            "correct": 1,
            "explanation": "En las aplicaciones híbridas la webview no tiene acceso directo al hardware del móvil, por lo que depende de plugins o bridges (como Capacitor o Cordova Plugins) para acceder a periféricos nativos."
        },
        {
            "id": "t1_fw_08",
            "tema": 1,
            "subtema": "Clasificación de Frameworks",
            "q": "¿Cuál de los siguientes frameworks NO es híbrido (es decir, NO ejecuta la interfaz dentro de un WebView)?",
            "options": [
                "Apache Cordova",
                "PhoneGap",
                "Ionic",
                "NativeScript"
            ],
            "correct": 3,
            "explanation": "NativeScript es nativo: accede directamente a las APIs y controles nativos de Android e iOS en tiempo real sin utilizar ningún WebView."
        },
        {
            "id": "t1_fw_09",
            "tema": 1,
            "subtema": "Clasificación de Frameworks",
            "q": "En el desarrollo multiplataforma, ¿qué tecnología promueve JetBrains para compartir lógica de negocio en lenguaje Kotlin compilando a nativo en iOS y bytecode en Android?",
            "options": [
                "Kotlin Multiplatform (KMP)",
                "Apache Cordova",
                "Sencha Touch",
                "Ionic Stencil"
            ],
            "correct": 0,
            "explanation": "Kotlin Multiplatform (KMP) permite compartir código en Kotlin compilando a binario nativo en iOS (mediante Kotlin/Native) y ejecutándose nativamente en la JVM de Android."
        },
        {
            "id": "t1_fw_10",
            "tema": 1,
            "subtema": "Clasificación de Frameworks",
            "q": "¿Cuál es la principal ventaja empresarial de optar por un desarrollo híbrido (Ionic/Cordova) frente a dos desarrollos nativos independientes?",
            "options": [
                "Rendimiento gráfico 3D superior al nativo",
                "Menor coste y menor tiempo de desarrollo (Time-to-Market), al usar una sola base de código web para todas las plataformas",
                "Acceso directo sin permisos al kernel del sistema operativo",
                "Elimina la necesidad de disponer de un ordenador Mac para compilar en iOS"
            ],
            "correct": 1,
            "explanation": "El desarrollo híbrido reduce costes y tiempo porque un solo equipo con competencias web (HTML/CSS/JS) puede construir la aplicación para Android e iOS a partir de una única base de código."
        }
    ]
    t1_all = t1_curated + t1_extra

    # 2. FILTRAR TEMA 2
    # Excluir t2_001 a t2_008 (introducción previa a streaming)
    t2_curated = []
    for q in original_data:
        if q.get('tema') == 2:
            if q['id'] in ['t2_001', 't2_002', 't2_003', 't2_004', 't2_005', 't2_006', 't2_007', 't2_008']:
                continue
            t2_curated.append(q)

    # Añadir preguntas de refuerzo de compresión básica y streaming
    t2_extra = [
        {
            "id": "t2_comp_01",
            "tema": 2,
            "subtema": "Compresión de Datos",
            "q": "EJERCICIO DE COMPRESIÓN: Una cadena de texto sin comprimir ocupa 100 KB. Tras aplicar un algoritmo de compresión, su tamaño final es de 25 KB. ¿Cuál es la tasa o factor de compresión (Compression Ratio)?",
            "options": [
                "2:1 (factor 2)",
                "4:1 (factor 4, o reducción del 75%)",
                "10:1 (factor 10)",
                "0.25:1"
            ],
            "correct": 1,
            "explanation": "El factor de compresión es Ratio = Tamaño Original / Tamaño Comprimido = 100 KB / 25 KB = 4:1 (factor 4). El porcentaje de reducción de espacio es ((100-25)/100)*100 = 75%."
        },
        {
            "id": "t2_comp_02",
            "tema": 2,
            "subtema": "Compresión de Datos",
            "q": "EJERCICIO DE COMPRESIÓN (RLE - Run-Length Encoding): Al aplicar el algoritmo RLE a la secuencia de píxeles 'AAAAABBBCCCCCD', ¿cuál es la secuencia codificada resultante?",
            "options": [
                "5A3B5C1D",
                "A5B3C5D1",
                "14ABCD",
                "AABBCCDD"
            ],
            "correct": 0,
            "explanation": "La codificación RLE sustituye secuencias consecutivas repetidas por el recuento seguido del valor: 5 veces 'A' (5A), 3 veces 'B' (3B), 5 veces 'C' (5C) y 1 vez 'D' (1D) -> 5A3B5C1D."
        },
        {
            "id": "t2_comp_03",
            "tema": 2,
            "subtema": "Compresión de Datos",
            "q": "¿Cuál es la diferencia fundamental entre una compresión con pérdida (lossy) y una compresión sin pérdida (lossless)?",
            "options": [
                "Lossless destruye información visual imperceptible y lossy recupera el 100% de los datos originales",
                "Lossless permite reconstruir exactamente los datos originales bit a bit (ej. PNG, FLAC, ZIP), mientras que lossy descarta datos imperceptibles para lograr mayor compresión (ej. JPEG, MP3)",
                "Lossy solo se utiliza para texto y Lossless para vídeo",
                "No hay diferencia, son dos nombres para el mismo algoritmo"
            ],
            "correct": 1,
            "explanation": "La compresión sin pérdida (lossless) es completamente reversible y exacta bit a bit. La compresión con pérdida (lossy) elimina redundancia psicovisual o psicoacústica para obtener archivos mucho menores a costa de perder fidelidad imperceptible."
        },
        {
            "id": "t2_stream_01",
            "tema": 2,
            "subtema": "Arquitectura de Streaming",
            "q": "¿Cuál es la función del servidor Proxy de Streaming en la arquitectura multimedia?",
            "options": [
                "Codificar en tiempo real el audio analógico a MP3",
                "Servir de intermediario que almacena en caché los segmentos solicitados, reduciendo el tráfico de salida del servidor principal y la latencia para los clientes",
                "Sustituir a los discos duros RAID dentro de la matriz de almacenamiento",
                "Calcular la paridad XOR en las tramas de red"
            ],
            "correct": 1,
            "explanation": "El Proxy de Streaming se coloca entre el cliente y el servidor: reutiliza y distribuye flujos almacenando segmentos temporales, lo que descongestiona el servidor central y acerca los datos al usuario."
        },
        {
            "id": "t2_stream_02",
            "tema": 2,
            "subtema": "Arquitectura de Streaming",
            "q": "¿Qué protocolo de streaming trabaja a nivel de transporte sobre UDP y añade marcas de tiempo (timestamp) y números de secuencia para permitir la reconstrucción en tiempo real de flujos de audio y vídeo?",
            "options": [
                "TCP puro",
                "RTP (Real-time Transport Protocol)",
                "FTP",
                "SMTP"
            ],
            "correct": 1,
            "explanation": "RTP corre típicamente sobre UDP para minimizar el retraso; incluye timestamps y números de secuencia para que el cliente ordene los paquetes y detecte pérdidas o jitter."
        }
    ]
    t2_all = t2_curated + t2_extra

    # 3. FILTRAR TEMA 3
    # Excluir preguntas que contengan Erlang B o fórmulas de dimensionamiento de canales por probabilidad de bloqueo
    t3_curated = []
    for q in original_data:
        if q.get('tema') == 3:
            q_text = (q['q'] + ' ' + q.get('explanation', '')).lower()
            if 'erlang b' in q_text or 'tabla de erlang' in q_text:
                continue
            t3_curated.append(q)

    # Añadir preguntas de refuerzo sobre Pantallas Técnicas, Wearables / Textillography y Conectividad (Bluetooth vs otras)
    t3_extra = [
        {
            "id": "t3_disp_01",
            "tema": 3,
            "subtema": "Displays y Pantallas",
            "q": "¿Por qué un display OLED / AMOLED logra un 'contraste infinito' y negros puros a diferencia de una pantalla LCD?",
            "options": [
                "Porque utiliza lámparas fluorescentes con luz negra en el panel trasero",
                "Porque cada píxel orgánico es autoemisor de luz y para mostrar el color negro el píxel se apaga completamente (0 lúmenes emitidos)",
                "Porque duplica el número de transistores TFT por cada subpíxel",
                "Porque bloquea la luz mediante una capa de cuarzo reflectante"
            ],
            "correct": 1,
            "explanation": "En las pantallas OLED/AMOLED no hay retroiluminación común trasera (backlight): cada píxel genera su propia luz y se apaga por completo al representar negro, logrando negros absolutos y contraste infinito."
        },
        {
            "id": "t3_disp_02",
            "tema": 3,
            "subtema": "Displays y Pantallas",
            "q": "En pantallas táctiles, ¿qué tecnología es mecánicamente flexible, funciona por presión física de dos láminas conductoras y permite operar con guantes o cualquier puntero rígido?",
            "options": [
                "Pantalla capacitiva proyectada (PCAP)",
                "Pantalla táctil resistiva",
                "Pantalla capacitiva de superficie",
                "Pantalla acústica SAW"
            ],
            "correct": 1,
            "explanation": "La pantalla táctil resistiva funciona por presión física: al presionar la lámina superior flexible, esta entra en contacto con la lámina inferior conductora cerrando el circuito. Por ello funciona con guantes, stylus pasivos o cualquier objeto."
        },
        {
            "id": "t3_disp_03",
            "tema": 3,
            "subtema": "Displays y Pantallas",
            "q": "¿Qué ventaja técnica ofrece la tecnología In-Cell frente a las pantallas táctiles tradicionales o On-Cell?",
            "options": [
                "Requiere mayor grosor pero resiste caídas de 10 metros",
                "Integra los electrodos y sensores táctiles dentro de la propia matriz LCD/OLED, reduciendo el grosor, el peso y los reflejos de luz",
                "Añade dos capas de cristal protector adicionales en el exterior",
                "Funciona exclusivamente con tecnología de infrarrojos"
            ],
            "correct": 1,
            "explanation": "La tecnología In-Cell integra la capa táctil directamente dentro de la celda de la pantalla (eliminando capas intermedias de cristal y adhesivo), lo que hace que los paneles sean mucho más delgados, ligeros y con mayor calidad óptica."
        },
        {
            "id": "t3_disp_04",
            "tema": 3,
            "subtema": "Displays y Pantallas",
            "q": "¿Qué tecnología táctil utiliza transductores ultrasónicos en los bordes de un cristal puro y se caracteriza por una claridad óptica máxima del 100%, pero es sensible a gotas de agua y suciedad?",
            "options": [
                "Pantalla SAW (Surface Acoustic Wave / Onda Acústica Superficial)",
                "Pantalla Resistiva analógica",
                "Pantalla PCAP",
                "Malla de infrarrojos perimetral"
            ],
            "correct": 0,
            "explanation": "Las pantallas SAW envían ondas acústicas ultrasónicas por la superficie del cristal. Al tocar con el dedo, se absorbe parte de la onda. Ofrecen máxima transparencia (cristal puro sin capas conductoras), pero el polvo o líquidos alteran la onda acústica."
        },
        {
            "id": "t3_wear_01",
            "tema": 3,
            "subtema": "Wearables y Textillography",
            "q": "¿Qué es la 'Textillography' en el contexto de los dispositivos wearables?",
            "options": [
                "Un método de impresión textil con tinta tradicional para camisetas de publicidad",
                "La ciencia y tecnología que integra componentes electrónicos, sensores y materiales conductores dentro de la propia estructura del tejido y las prendas inteligentes",
                "Un estándar de codificación de compresión de imágenes de ropa en 4K",
                "Un protocolo inalámbrico de bajo consumo para lavadoras inteligentes"
            ],
            "correct": 1,
            "explanation": "Textillography (textiles inteligentes / e-textiles) es el campo transdisciplinar que estudia la integración de electrónica, interconexiones, sensores biométricos y fibras conductoras en los propios tejidos textiles."
        },
        {
            "id": "t3_wear_02",
            "tema": 3,
            "subtema": "Wearables y Textillography",
            "q": "¿Cuáles son dos de los principales desafíos técnicos a los que se enfrenta la tecnología de Textillography y la ropa inteligente?",
            "options": [
                "La falta de pantallas en color y la velocidad de la memoria RAM",
                "La resistencia y degradación ante los ciclos de lavado / torsión mecánica, y la gestión de la alimentación energética / baterías",
                "La incompatibilidad con el protocolo HTTP y la falta de cobertura 5G",
                "El coste excesivo del algodón tradicional"
            ],
            "correct": 1,
            "explanation": "Los grandes retos de las prendas inteligentes (Textillography) son la durabilidad frente a lavados agresivos (humedad, detergentes, centrifugado), la flexibilidad/fatiga mecánica y el suministro continuo de energía con baterías lavables o recolección de energía (energy harvesting)."
        },
        {
            "id": "t3_con_01",
            "tema": 3,
            "subtema": "Conectividad",
            "q": "¿Cuál es la diferencia fundamental entre Bluetooth BLE (Bluetooth Low Energy) y Wi-Fi en cuanto a consumo de energía y caudal de datos?",
            "options": [
                "Wi-Fi consume mucho menos que BLE y tiene menor caudal",
                "BLE está optimizado para transmitir pequeños paquetes de datos con consumo ultra bajo permitiendo años de autonomía con una pila de botón, mientras que Wi-Fi ofrece gran caudal (Mbps/Gbps) con un consumo energético mucho más elevado",
                "Ambos consumen exactamente lo mismo y tienen el mismo ancho de banda",
                "BLE solo funciona si hay visión directa óptica como IrDA"
            ],
            "correct": 1,
            "explanation": "BLE fue diseñado para enviar ráfagas cortas de datos esporádicos (sensores de pulso, balizas, wearables) manteniendo el transmisor dormido la mayor parte del tiempo, permitiendo autonomías de meses o años con pila de botón, a diferencia de Wi-Fi que requiere alta potencia continua."
        },
        {
            "id": "t3_con_02",
            "tema": 3,
            "subtema": "Conectividad",
            "q": "Al comparar Bluetooth con NFC (Near Field Communication), ¿cuál de las siguientes afirmaciones es correcta?",
            "options": [
                "NFC tiene un alcance de hasta 100 metros y requiere emparejamiento manual con código PIN",
                "NFC opera a una distancia máxima de escasos centímetros (< 4-10 cm) mediante acoplamiento inductivo a 13.56 MHz, lo que proporciona gran seguridad intrínseca para pagos móviles y emparejamiento instantáneo sin configuración",
                "Bluetooth opera a 13.56 MHz y NFC en la banda de 2.4 GHz",
                "NFC no permite transferir ningún dato y solo sirve para encender el teléfono"
            ],
            "correct": 1,
            "explanation": "NFC opera por proximidad extrema (< 4-10 cm) en la banda de 13.56 MHz. Su cortísimo alcance físico garantiza que nadie intercepte la señal a distancia, haciéndolo ideal para pagos (Apple Pay / Google Wallet) y emparejamiento rápido 'tocar y listo'."
        },
        {
            "id": "t3_con_03",
            "tema": 3,
            "subtema": "Conectividad",
            "q": "¿Qué protocolo inalámbrico en la banda de 2.4 GHz está especialmente diseñado para redes de domótica y sensores industriales gracias a su topología de red en malla (Mesh) y consumo reducido?",
            "options": [
                "IrDA",
                "Zigbee (IEEE 802.15.4)",
                "Wi-Fi 802.11a",
                "NFC"
            ],
            "correct": 1,
            "explanation": "Zigbee está basado en IEEE 802.15.4 y se caracteriza por crear topologías en malla (Mesh), donde cada nodo puede reenviar paquetes de otros nodos, ideal para sensores domóticos y automatización con bajo consumo."
        },
        {
            "id": "t3_con_04",
            "tema": 3,
            "subtema": "Conectividad",
            "q": "¿En qué ámbito destaca principalmente el protocolo ANT / ANT+ frente a Bluetooth tradicional?",
            "options": [
                "En la transmisión de vídeo 4K en tiempo real",
                "En el ecosistema deportivo y monitorización de fitness (pulsómetros, bandas de pecho, potenciómetros de ciclismo) con conexión ultraligera de uno a muchos",
                "En la navegación web de alta velocidad",
                "En el control de satélites espaciales"
            ],
            "correct": 1,
            "explanation": "ANT y ANT+ son protocolos propietarios ultraligeros de ultra bajo consumo enfocados tradicionalmente al fitness y sensores deportivos, permitiendo que un sensor envíe datos a múltiples relojes o ciclocomputadores simultáneamente."
        },
        {
            "id": "t3_con_05",
            "tema": 3,
            "subtema": "Conectividad",
            "q": "¿Cuál es la principal diferencia entre una etiqueta RFID pasiva y la tecnología Bluetooth?",
            "options": [
                "La etiqueta RFID pasiva no tiene batería propia y se energiza mediante la onda electromagnética emitida por el lector, mientras que Bluetooth requiere siempre su propia fuente de alimentación",
                "Bluetooth no requiere batería y RFID consume 20 vatios",
                "RFID alcanza 2 kilómetros y Bluetooth solo 1 milímetro",
                "RFID requiere conectarse a una red Wi-Fi previa"
            ],
            "correct": 0,
            "explanation": "Los tags RFID pasivos carecen de batería: utilizan la inducción electromagnética del campo emitido por la antena lectora para alimentarse y devolver su identificador. Los dispositivos Bluetooth son activos y requieren batería."
        }
    ]
    t3_all = t3_curated + t3_extra

    all_curated = t1_all + t2_all + t3_all
    
    # Validar IDs únicos
    seen_ids = set()
    final_questions = []
    for q in all_curated:
        qid = q['id']
        if qid in seen_ids:
            qid = f"{qid}_bis"
            q['id'] = qid
        seen_ids.add(qid)
        final_questions.append(q)

    print(f"Total preguntas curadas estrictas: {len(final_questions)}")
    print(f"Tema 1: {len([q for q in final_questions if q['tema'] == 1])}")
    print(f"Tema 2: {len([q for q in final_questions if q['tema'] == 2])}")
    print(f"Tema 3: {len([q for q in final_questions if q['tema'] == 3])}")

    with open('all_questions.json', 'w', encoding='utf-8') as f:
        json.dump(final_questions, f, ensure_ascii=False, indent=2)

    return final_questions

if __name__ == '__main__':
    build_curated_database()
