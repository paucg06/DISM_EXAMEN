# -*- coding: utf-8 -*-
"""
Full Tema 1 question set (60 comprehensive questions covering all 47 blocks).
"""

def get_tema1_questions():
    qs = [
        {
            "tema": 1,
            "subtema": "Conceptos Generales",
            "q": "¿En qué consiste el desarrollo de aplicaciones móviles según el temario?",
            "options": [
                "Únicamente en el diseño gráfico y maquetación de interfaces para pantallas táctiles",
                "En el conjunto de procesos y procedimientos involucrados en la escritura de software para pequeños dispositivos inalámbricos (smartphones o tablets)",
                "En la adaptación exclusiva de páginas web existentes para que se visualicen en navegadores móviles",
                "En la programación en lenguaje ensamblador de chips de radiofrecuencia para terminales celulares"
            ],
            "correct": 1,
            "explanation": "El desarrollo móvil es el conjunto de procesos y procedimientos involucrados en la escritura de software para pequeños dispositivos inalámbricos como smartphones o tablets."
        },
        {
            "tema": 1,
            "subtema": "Mercado y Estadísticas",
            "q": "¿Qué tienda de aplicaciones genera un mayor volumen de gasto e ingresos brutos a pesar de contar con menos descargas a nivel global?",
            "options": [
                "Google Play Store",
                "Apple App Store",
                "Huawei AppGallery",
                "Amazon Appstore"
            ],
            "correct": 1,
            "explanation": "A nivel mundial, Apple App Store genera casi el doble de gasto e ingresos que Google Play Store, aunque Google Play supera ampliamente a Apple en volumen total de descargas."
        },
        {
            "tema": 1,
            "subtema": "Mercado y Estadísticas",
            "q": "¿Cuál es la categoría de aplicaciones que históricamente acapara la mayor parte del gasto de los usuarios en las tiendas de apps?",
            "options": [
                "Productividad y herramientas de oficina",
                "Videojuegos (Mobile Gaming)",
                "Redes sociales y mensajería",
                "Educación y salud"
            ],
            "correct": 1,
            "explanation": "Los videojuegos móviles generan más del 60-70% del gasto total en aplicaciones de consumo en las tiendas oficiales."
        },
        {
            "tema": 1,
            "subtema": "Ecosistema Móvil",
            "q": "¿Cuáles son las dos principales plataformas dominantes del mercado móvil actual y sus respectivos lenguajes nativos oficiales?",
            "options": [
                "iOS (Swift / Objective-C) y Android (Kotlin / Java)",
                "Windows Mobile (C#) y Symbian (C++)",
                "BlackBerry OS (Java) y Firefox OS (JavaScript)",
                "Tizen (C) y PalmOS (C++)"
            ],
            "correct": 0,
            "explanation": "iOS (respaldado por Apple con Swift y Objective-C) y Android (respaldado por Google con Kotlin y Java) concentran más del 99% del mercado mundial."
        },
        {
            "tema": 1,
            "subtema": "Ecosistema Móvil",
            "q": "¿Cuál de los siguientes es un problema característico de la plataforma Android en comparación con iOS?",
            "options": [
                "La fragmentación de dispositivos, pantallas y versiones del sistema operativo activas",
                "La imposibilidad de programar en lenguajes orientados a objetos",
                "La falta de acceso a hardware como GPS o cámara",
                "Que solo existe un único fabricante de teléfonos en el mundo"
            ],
            "correct": 0,
            "explanation": "La fragmentación (múltiples fabricantes, miles de tamaños y resoluciones de pantalla, y versiones heterogéneas de Android activas simultáneamente) es un reto clásico en Android frente al catálogo cerrado y homogéneo de Apple."
        },
        {
            "tema": 1,
            "subtema": "Enfoques de Desarrollo",
            "q": "¿Qué caracteriza fundamentalmente a una aplicación híbrida?",
            "options": [
                "Está escrita en C++ y compila a bytecode de Java",
                "Utiliza tecnologías web (HTML, CSS y JavaScript) empaquetadas dentro de un contenedor nativo (WebView) con acceso al hardware mediante plugins",
                "Requiere dos terminales distintos conectados por Bluetooth para funcionar",
                "No permite el almacenamiento de datos locales en el dispositivo"
            ],
            "correct": 1,
            "explanation": "Una app híbrida es una aplicación web encapsulada en una vista nativa (WebView) que interactúa con el hardware del terminal a través de un puente nativo."
        },
        {
            "tema": 1,
            "subtema": "Nativo vs Híbrido",
            "q": "¿Cuál de las siguientes afirmaciones sobre el desarrollo nativo frente al híbrido es FALSA?",
            "options": [
                "El desarrollo nativo ofrece el mejor rendimiento y la experiencia de usuario más fluida",
                "El desarrollo híbrido permite reutilizar gran parte del código entre plataformas",
                "El desarrollo híbrido siempre rinde mejor que el nativo en videojuegos con gráficos 3D exigentes",
                "El desarrollo nativo implica habitualmente mantener dos equipos de desarrollo separados"
            ],
            "correct": 2,
            "explanation": "En gráficos 3D y juegos pesados, el desarrollo híbrido rinde notablemente peor debido a la sobrecarga del motor web y el puente de comunicación."
        },
        {
            "tema": 1,
            "subtema": "Frameworks Históricos",
            "q": "¿Qué herramienta pionera desarrollada por Nitobi en 2009 permitía crear apps híbridas antes de ser comprada por Adobe y donada a Apache?",
            "options": [
                "PhoneGap (Apache Cordova)",
                "Xamarin",
                "Ionic v7",
                "Flutter"
            ],
            "correct": 0,
            "explanation": "PhoneGap fue creado por Nitobi, comprado por Adobe en 2011, y donado a Apache como software libre bajo el nombre Apache Cordova."
        },
        {
            "tema": 1,
            "subtema": "Frameworks Históricos",
            "q": "¿Por qué Apache Cordova / PhoneGap quedó desfasado frente a soluciones modernas como Capacitor?",
            "options": [
                "Porque no permitía el uso de HTML5 ni JavaScript",
                "Por su arquitectura rígida de plugins, gestión compleja del proyecto nativo oculta en CLI y falta de integración con TypeScript moderno",
                "Porque solo funcionaba en sistemas Symbian",
                "Porque requería pagar una licencia mensual obligatoria a Apache"
            ],
            "correct": 1,
            "explanation": "Cordova ocultaba los proyectos nativos en carpetas generadas, tenía un sistema de plugins propenso a roturas de compatibilidad y carecía de tipado estricto moderno; Capacitor solventó estos problemas tratando los proyectos de Xcode y Android Studio como artefactos de primer nivel."
        },
        {
            "tema": 1,
            "subtema": "Frameworks Históricos",
            "q": "¿Qué framework multiplataforma basado en el proyecto Mono y C# fue adquirido por Microsoft y posteriormente evolucionó a .NET MAUI?",
            "options": [
                "Xamarin / Xamarin.Forms",
                "PhoneGap",
                "Sencha Touch",
                "Appcelerator Titanium"
            ],
            "correct": 0,
            "explanation": "Xamarin (y Xamarin.Forms) fue la plataforma en C# adquirida por Microsoft en 2016 que sentó las bases para .NET MAUI."
        },
        {
            "tema": 1,
            "subtema": "Ionic Framework",
            "q": "¿Qué es Ionic en la actualidad?",
            "options": [
                "Un sistema operativo móvil basado en Linux para relojes inteligentes",
                "Un framework de interfaz de usuario de componentes web para crear aplicaciones híbridas y PWAs con Angular, React, Vue o JavaScript plano",
                "Un motor gráfico exclusivo para desarrollo de videojuegos 3D",
                "Un lenguaje de programación propietario creado por Apple"
            ],
            "correct": 1,
            "explanation": "Ionic es un toolkit de componentes web de interfaz de usuario que permite crear apps móviles, de escritorio y web usando tecnologías frontend estándar y frameworks como Angular, React o Vue."
        },
        {
            "tema": 1,
            "subtema": "Ionic Framework",
            "q": "¿Qué herramienta moderna de Ionic sustituyó a Apache Cordova para conectar el código web con las APIs nativas del dispositivo?",
            "options": [
                "Capacitor",
                "Electron",
                "NodeJS Core",
                "WebGL"
            ],
            "correct": 0,
            "explanation": "Capacitor es el runtime multiplataforma y puente nativo moderno creado por Ionic para comunicar la WebView con el código nativo de iOS y Android."
        },
        {
            "tema": 1,
            "subtema": "Ionic Framework",
            "q": "¿Cómo viaja una llamada desde JavaScript al hardware nativo en una app de Ionic con Capacitor?",
            "options": [
                "JavaScript compila el teléfono a nivel de silicio",
                "El código JS llama a window.Capacitor.Plugins, el Native Bridge serializa la petición y la transfiere al entorno nativo (Java/Kotlin o Swift/Obj-C) que ejecuta la API del SO",
                "La WebView se conecta a un servidor en internet que envía comandos remotos al móvil por SMS",
                "Mediante un cable USB virtual dentro del sistema de archivos"
            ],
            "correct": 1,
            "explanation": "El Native Bridge inyecta `window.Capacitor.Plugins` en la WebView; cuando JS invoca un plugin, los datos viajan a través del puente al código nativo que accede al hardware del terminal."
        },
        {
            "tema": 1,
            "subtema": "Ionic Framework",
            "q": "¿Cómo estructura Capacitor los proyectos nativos de iOS y Android?",
            "options": [
                "Los esconde en carpetas temporales que se borran y regeneran en cada compilación",
                "Crea carpetas nativas completas e independientes ('android' e 'ios') que se pueden abrir y configurar directamente en Android Studio y Xcode",
                "Genera únicamente un archivo binario bin.hex que se flashea por hardware",
                "Solo permite ejecutar la aplicación dentro del navegador Google Chrome"
            ],
            "correct": 1,
            "explanation": "A diferencia de Cordova, Capacitor considera el código nativo como un ciudadano de primera clase: las carpetas `android` e `ios` forman parte del repositorio y se abren con sus respectivos IDEs oficiales."
        },
        {
            "tema": 1,
            "subtema": "Ionic Framework",
            "q": "¿Qué comando de la CLI de Capacitor sincroniza los activos web compilados y actualiza los plugins nativos en las carpetas nativas?",
            "options": [
                "npx cap sync",
                "npx cap destroy",
                "npm run delete-native",
                "ionic format"
            ],
            "correct": 0,
            "explanation": "`npx cap sync` ejecuta `copy` (copia la carpeta de build web a las carpetas nativas) y `update` (actualiza los plugins y dependencias nativas en Gradle y CocoaPods)."
        },
        {
            "tema": 1,
            "subtema": "Ionic Framework",
            "q": "¿Qué librería / tecnología utiliza el equipo de Ionic bajo el capó para construir sus componentes web (Web Components) estándares y reutilizables en cualquier framework?",
            "options": [
                "Stencil.js",
                "jQuery",
                "Flash",
                "Bootstrap 3"
            ],
            "correct": 0,
            "explanation": "Ionic creó Stencil.js, un compilador que genera Web Components estándar altamente optimizados, permitiendo que la misma biblioteca de componentes funcione con Angular, React, Vue o JS puro."
        },
        {
            "tema": 1,
            "subtema": "Ionic Framework",
            "q": "¿Cómo adapta Ionic automáticamente la apariencia visual de sus componentes según el sistema operativo en el que se ejecuta?",
            "options": [
                "Modo de estilo automático: aplica Material Design ('md') en Android y estilo Cupertino ('ios') en dispositivos Apple",
                "Preguntando al usuario en cada inicio qué color prefiere",
                "Descargando una versión diferente de la app desde internet",
                "Forzando siempre la interfaz clásica de Windows 95"
            ],
            "correct": 0,
            "explanation": "Ionic implementa 'Platform Styling' dinámico, configurando clases y estilos para emular Material Design en Android y la guía de diseño de iOS (Cupertino) en terminales Apple."
        },
        {
            "tema": 1,
            "subtema": "Ionic Framework",
            "q": "¿Cuál es una de las mayores ventajas de Ionic?",
            "options": [
                "Estar basado en estándares web abiertos, permitiendo a desarrolladores web crear aplicaciones con una única base de código para móvil, web y escritorio",
                "Tener mayor velocidad de ejecución que el código en ensamblador",
                "No necesitar compilar nunca para subir la app a la App Store",
                "Ser un sistema operativo completo que sustituye a Android"
            ],
            "correct": 0,
            "explanation": "La mayor ventaja de Ionic es la reutilización del talento y código web existente: una sola base de código para web, Android, iOS y PWA."
        },
        {
            "tema": 1,
            "subtema": "Ionic Framework",
            "q": "¿Cuál es una desventaja notable de Ionic frente a Flutter o aplicaciones nativas?",
            "options": [
                "Que no soporta hojas de estilo CSS",
                "Que su rendimiento gráfico puede degradarse en animaciones complejas de 60/120 fps y procesamiento intensivo por estar atrapado en el hilo de la WebView",
                "Que no se puede depurar desde un navegador web",
                "Que exige que el usuario compre un dispositivo de gama muy alta para abrir un botón"
            ],
            "correct": 1,
            "explanation": "La sobrecarga del DOM y la comunicación por puente en el WebView puede causar pérdidas de frames en animaciones intensivas y transiciones complejas."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "¿Qué es una Progressive Web App (PWA)?",
            "options": [
                "Una aplicación web avanzada que ofrece una experiencia similar a una app nativa (instalable, offline, notificaciones push) utilizando estándares del navegador",
                "Un programa que únicamente funciona si el usuario tiene una conexión por satélite",
                "Una aplicación en lenguaje C que se descarga como un fichero .exe",
                "Una extensión para navegadores que bloquea la publicidad"
            ],
            "correct": 0,
            "explanation": "Una PWA es una solución web que incorpora características de app nativa como trabajo sin conexión, instalación en el launcher y notificaciones."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "¿Cuál es el archivo JSON que proporciona metadatos de la PWA (nombre, tema, orientación, iconos, modo de inicio) al navegador?",
            "options": [
                "Web App Manifest (manifest.json)",
                "package.json",
                "settings.gradle",
                "Info.plist"
            ],
            "correct": 0,
            "explanation": "El Web App Manifest (`manifest.json` o `manifest.webmanifest`) contiene la configuración necesaria para que el navegador sepa cómo instalar y mostrar la aplicación."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "¿Qué componente es el corazón de una PWA que se ejecuta en segundo plano en un hilo separado del DOM e intercepta las peticiones de red?",
            "options": [
                "El Service Worker",
                "El Kernel de Linux",
                "La base de datos MySQL",
                "El compilador JIT"
            ],
            "correct": 0,
            "explanation": "El Service Worker es un script en segundo plano que actúa como proxy entre la aplicación web, el navegador y la red, interceptando llamadas HTTP."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "¿Qué requisito de seguridad fundamental exige el navegador para permitir el registro de un Service Worker (excepto en localhost)?",
            "options": [
                "Que el sitio web se sirva obligatoriamente bajo el protocolo seguro HTTPS",
                "Que el usuario ingrese su contraseña de administrador del teléfono",
                "Que la página web no contenga ninguna imagen",
                "Que el servidor esté alojado físicamente en el mismo país del usuario"
            ],
            "correct": 0,
            "explanation": "Por razones de seguridad contra ataques Man-In-The-Middle, los Service Workers solo se pueden registrar y ejecutar en orígenes seguros mediante HTTPS (o localhost durante el desarrollo)."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "¿En qué orden se suceden las fases iniciales del ciclo de vida de un Service Worker?",
            "options": [
                "Descarga -> Install -> Activate -> Idle / Fetch",
                "Execute -> Compile -> Delete -> Close",
                "Activate -> Install -> Recompile -> Terminate",
                "Fetch -> Install -> Sleep -> Shutdown"
            ],
            "correct": 0,
            "explanation": "Tras descargarse el script, entra en la fase `Install` (donde típicamente se cachea la App Shell), pasa a `Activate` (limpieza de cachés viejas) y finalmente queda escuchando eventos funcionales como `fetch` o `push`."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "En el evento 'install' de un Service Worker, ¿qué método de evento se suele utilizar para evitar que el navegador dé por finalizada la instalación antes de que se complete el cacheado?",
            "options": [
                "event.waitUntil()",
                "event.stopImmediate()",
                "event.terminate()",
                "event.preventDefault()"
            ],
            "correct": 0,
            "explanation": "`event.waitUntil(promise)` extiende la vida del evento de instalación hasta que la promesa que cachea los archivos iniciales se resuelva con éxito."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "En el ciclo de un Service Worker, ¿cuándo toma el control de las páginas abiertas si no se usa 'self.clients.claim()'?",
            "options": [
                "Inmediatamente al empezar a descargar el script",
                "Solo después de que la página actual se cierre y se vuelva a abrir (o se recargue)",
                "Nunca; requiere reiniciar físicamente el terminal",
                "A las 24 horas exactas de la instalación"
            ],
            "correct": 1,
            "explanation": "Por defecto, un nuevo Service Worker no controlará los clientes hasta la siguiente navegación/recarga, a menos que se llame explícitamente a `self.clients.claim()` en el evento `activate`."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "¿Qué estrategia de caché es idónea para recursos estáticos (App Shell, logos, fuentes CSS fijas) que casi nunca cambian?",
            "options": [
                "Network Only",
                "Cache First (Caché primero con respaldo en red)",
                "Network First",
                "Server-Sent Events"
            ],
            "correct": 1,
            "explanation": "Para ficheros estáticos inmutables (App Shell), Cache First ofrece la máxima velocidad de carga offline sin consumir ancho de banda."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "¿Qué estrategia de caché es la más adecuada para feeds de noticias o cotizaciones bursátiles donde se prioriza tener la información más fresca posible pero permitiendo ver datos guardados si no hay conexión?",
            "options": [
                "Cache Only",
                "Network First (Red primero con respaldo en caché)",
                "Cache First",
                "No Cache"
            ],
            "correct": 1,
            "explanation": "Network First intenta obtener los datos en vivo del servidor primero; si la petición falla por falta de cobertura o timeout, recurre a la caché guardada."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "¿Qué estrategia de caché devuelve instantáneamente el recurso almacenado en caché y a la vez lanza una petición en segundo plano para actualizarla para el siguiente uso?",
            "options": [
                "Stale-While-Revalidate",
                "Network Only",
                "Cache Only",
                "Strict Network"
            ],
            "correct": 0,
            "explanation": "'Stale-While-Revalidate' combina inmediatez de respuesta para el usuario y frescura de datos al actualizar la caché asíncronamente en segundo plano."
        },
        {
            "tema": 1,
            "subtema": "PWA",
            "q": "¿Cuál es una limitación histórica de las PWA en el ecosistema iOS (Safari/WebKit) frente a Android?",
            "options": [
                "iOS no permite renderizar HTML5",
                "Menor soporte de APIs avanzadas (Bluetooth web, NFC en segundo plano, soporte tardío de Web Push y cuotas de caché más restringidas)",
                "iOS no permite usar CSS Flexbox",
                "En iOS las PWAs solo pueden ejecutarse en modo horizontal"
            ],
            "correct": 1,
            "explanation": "Apple históricamente ha tenido una adopción más lenta y restrictiva de estándares de PWA en WebKit (Web Push llegó recientemente en iOS 16.4, sin acceso a Bluetooth/NFC en web)."
        },
        {
            "tema": 1,
            "subtema": ".NET MAUI",
            "q": "¿Qué es .NET MAUI y qué tecnología reemplaza formalmente desde mayo de 2022?",
            "options": [
                "Es el reemplazo de Xamarin.Forms para crear apps multiplataforma con C# y XAML",
                "Es un sustituto de Apache Cordova basado en Visual Basic",
                "Es un motor de bases de datos relacionales para teléfonos",
                "Es una distribución de Linux para microcontroladores"
            ],
            "correct": 0,
            "explanation": ".NET MAUI (.NET Multi-platform App UI) es el sucesor oficial de Xamarin.Forms, integrado dentro de la plataforma .NET moderna."
        },
        {
            "tema": 1,
            "subtema": ".NET MAUI",
            "q": "¿Qué patrón arquitectónico utiliza .NET MAUI para mapear sus controles abstractos a los controles visuales nativos de cada sistema?",
            "options": [
                "Patrón Handlers / Mappers",
                "Patrón Proxy WebSocket",
                "Patrón Canvas 2D Blitter",
                "Patrón Virtual DOM Diffing"
            ],
            "correct": 0,
            "explanation": "En .NET MAUI, los 'Handlers' desacoplan la abstracción del control de su representación en la plataforma concreta mediante 'Mappers', mejorando el rendimiento frente a los 'Renderers' de Xamarin."
        },
        {
            "tema": 1,
            "subtema": ".NET MAUI",
            "q": "¿En qué formato se define habitualmente la estructura visual y de diseño de las interfaces en .NET MAUI?",
            "options": [
                "XAML (Extensible Application Markup Language) o código C# fluido",
                "Markdown (.md)",
                "Ficheros binarios de Photoshop (.psd)",
                "Ficheros YAML exclusivamente"
            ],
            "correct": 0,
            "explanation": "La interfaz de usuario en .NET MAUI se define típicamente en XAML (declarativo basado en XML) o mediante código C# (incluyendo C# Markup)."
        },
        {
            "tema": 1,
            "subtema": "Uno Platform",
            "q": "¿Qué es Uno Platform dentro del ecosistema .NET?",
            "options": [
                "Una alternativa a .NET MAUI que lleva la API de WinUI y XAML a iOS, Android, macOS, Linux y WebAssembly (web)",
                "Un sistema de pago para compras integradas en iOS",
                "Un lenguaje nuevo inventado por Google",
                "Un servidor web exclusivo para Internet Explorer"
            ],
            "correct": 0,
            "explanation": "Uno Platform permite ejecutar código WinUI / UWP en múltiples plataformas (incluyendo WebAssembly para navegadores y Linux) compartiendo C# y XAML."
        },
        {
            "tema": 1,
            "subtema": "Flutter",
            "q": "¿Qué lenguaje de programación es el único utilizado para programar aplicaciones en Flutter?",
            "options": [
                "Dart",
                "Kotlin",
                "Swift",
                "Rust"
            ],
            "correct": 0,
            "explanation": "Flutter utiliza el lenguaje de programación Dart, también desarrollado por Google."
        },
        {
            "tema": 1,
            "subtema": "Flutter",
            "q": "¿Cómo se estructuran los componentes de la interfaz de usuario en Flutter?",
            "options": [
                "Todo es un Widget, organizados en un árbol jerárquico (Widget Tree)",
                "En tablas relacionales de base de datos",
                "En documentos HTML enlazados por hipervínculos",
                "En scripts de Bash independientes"
            ],
            "correct": 0,
            "explanation": "En Flutter, prácticamente todo en la interfaz es un Widget (StatelessWidget o StatefulWidget), organizados en una jerarquía en forma de árbol."
        },
        {
            "tema": 1,
            "subtema": "Flutter",
            "q": "¿Qué diferencia a un 'StatelessWidget' de un 'StatefulWidget' en Flutter?",
            "options": [
                "El StatelessWidget nunca puede mostrarse en la pantalla",
                "El StatelessWidget es inmutable y no mantiene estado interno que cambie con el tiempo; el StatefulWidget dispone de un objeto State mutable que provoca el redibujado al cambiar con setState()",
                "El StatefulWidget solo funciona en terminales con Android",
                "El StatelessWidget requiere obligatoriamente una conexión a internet"
            ],
            "correct": 1,
            "explanation": "Un StatelessWidget describe una parte de la UI inmutable dependiente solo de su configuración; un StatefulWidget mantiene información mutable a lo largo de su ciclo de vida."
        },
        {
            "tema": 1,
            "subtema": "Flutter",
            "q": "¿Por qué Flutter no sufre del clásico problema de desajuste visual de controles entre distintas versiones de Android?",
            "options": [
                "Porque no utiliza los componentes de la plataforma; Flutter dibuja cada elemento en el canvas con su propio motor gráfico integrado",
                "Porque solo permite ejecutar aplicaciones en teléfonos fabricados por Google",
                "Porque convierte toda la pantalla en una única fotografía estática",
                "Porque desactiva todas las actualizaciones del sistema operativo"
            ],
            "correct": 0,
            "explanation": "Flutter no invoca los widgets de Android ni de iOS; incluye su propio motor gráfico que rasteriza cada elemento en pantalla, asegurando idéntico aspecto en cualquier versión."
        },
        {
            "tema": 1,
            "subtema": "Flutter",
            "q": "¿Qué nuevo motor de renderizado gráfico de nueva generación sustituyó progresivamente a Skia en Flutter para evitar los tirones ('jank') causados por la compilación de shaders?",
            "options": [
                "Impeller",
                "Blink",
                "Gecko",
                "V8"
            ],
            "correct": 0,
            "explanation": "Impeller es el motor de renderizado desarrollado por el equipo de Flutter para reemplazar a Skia, precompilando shaders en tiempo de construcción para erradicar el 'shader compilation jank'."
        },
        {
            "tema": 1,
            "subtema": "Flutter",
            "q": "¿Qué característica de Flutter permite a los desarrolladores ver los cambios de código reflejados en el emulador o dispositivo en menos de un segundo sin perder el estado de la app?",
            "options": [
                "Stateful Hot Reload",
                "Cold Reboot",
                "Clean Rebuild",
                "AOT Native Dump"
            ],
            "correct": 0,
            "explanation": "Stateful Hot Reload inyecta el código fuente actualizado directamente en la máquina virtual de Dart en ejecución, refrescando la UI instantáneamente y preservando el estado actual de la pantalla."
        },
        {
            "tema": 1,
            "subtema": "React Native",
            "q": "¿Qué empresa lidera el desarrollo de React Native y qué biblioteca de interfaz web sirve de inspiración para su modelo declarativo?",
            "options": [
                "Meta (Facebook), basándose en React",
                "Google, basándose en Angular",
                "Twitter, basándose en Bootstrap",
                "Netflix, basándose en Vue"
            ],
            "correct": 0,
            "explanation": "React Native fue creado por Facebook (Meta) y aplica los conceptos declarativos de React y JSX al desarrollo nativo móvil."
        },
        {
            "tema": 1,
            "subtema": "React Native",
            "q": "¿Qué motor de layout multiplataforma, implementado en C++ y basado en Flexbox, utiliza React Native para calcular el tamaño y posición de las vistas?",
            "options": [
                "Yoga",
                "Skia",
                "DirectX",
                "Cairo"
            ],
            "correct": 0,
            "explanation": "Yoga es la implementación en C++ de Flexbox creada por Meta para calcular el layout en React Native independientemente del sistema operativo."
        },
        {
            "tema": 1,
            "subtema": "React Native",
            "q": "¿Qué motor de JavaScript ligero, optimizado para móviles y con compilación anticipada de bytecode, utiliza React Native por defecto?",
            "options": [
                "Hermes",
                "SpiderMonkey",
                "Chakra",
                "Nashorn"
            ],
            "correct": 0,
            "explanation": "Hermes es el motor de JavaScript desarrollado por Meta y optimizado para reducir el tiempo de inicio (TTI), uso de memoria y tamaño del APK en React Native."
        },
        {
            "tema": 1,
            "subtema": "React Native",
            "q": "¿Cómo se denominan las dos piezas centrales de la 'Nueva Arquitectura' de React Native para el renderizado concurrente y los módulos nativos directos?",
            "options": [
                "Fabric (nuevo sistema de renderizado) y TurboModules (nuevo sistema de módulos nativos sobre JSI)",
                "WebView y Apache Cordova",
                "Mono Runtime y CocoaTouch",
                "Activity y Fragment"
            ],
            "correct": 0,
            "explanation": "Fabric es el motor de renderizado de la nueva arquitectura de React Native y TurboModules permite la carga bajo demanda y comunicación directa síncrona con código nativo mediante JSI."
        },
        {
            "tema": 1,
            "subtema": "Kotlin Multiplatform",
            "q": "¿Qué empresa desarrolla Kotlin y la tecnología Kotlin Multiplatform (KMP)?",
            "options": [
                "JetBrains",
                "Oracle",
                "Apple",
                "Amazon"
            ],
            "correct": 0,
            "explanation": "Kotlin y Kotlin Multiplatform son desarrollados por JetBrains (con gran colaboración y respaldo de Google en Android)."
        },
        {
            "tema": 1,
            "subtema": "Kotlin Multiplatform",
            "q": "En un proyecto de Kotlin Multiplatform, ¿cuál es la palabra clave en el código común para declarar una función que debe ser implementada de forma específica en cada plataforma con 'actual'?",
            "options": [
                "expect",
                "interface",
                "override",
                "virtual"
            ],
            "correct": 0,
            "explanation": "KMP utiliza el mecanismo `expect` (en el código común) y `actual` (en las carpetas de plataforma específica como `androidMain` o `iosMain`) para invocar APIs de cada SO."
        },
        {
            "tema": 1,
            "subtema": "Kotlin Multiplatform",
            "q": "¿Qué tecnología de interfaz multiplataforma basada en Jetpack Compose ha desarrollado JetBrains para permitir compartir también la UI en KMP?",
            "options": [
                "Compose Multiplatform",
                "SwiftUI Web",
                "JavaFX Mobile",
                "XAML Compose"
            ],
            "correct": 0,
            "explanation": "Compose Multiplatform permite utilizar la sintaxis declarativa de Jetpack Compose no solo en Android, sino también en iOS, escritorio y web."
        },
        {
            "tema": 1,
            "subtema": "Tauri",
            "q": "¿Cuál es la principal ventaja de Tauri en comparación con Electron?",
            "options": [
                "Tauri NO empaqueta una copia completa del navegador Chromium ni de Node.js; utiliza el WebView nativo del sistema operativo y un backend seguro en Rust, resultando en aplicaciones mucho más ligeras y rápidas",
                "Tauri solo funciona si el usuario no tiene conexión a internet",
                "Tauri traduce el código a lenguaje Pascal",
                "Tauri no admite hojas de estilo CSS"
            ],
            "correct": 0,
            "explanation": "Electron genera instaladores pesados (>100-200 MB) porque incluye Chromium y Node.js. Tauri utiliza Rust y el WebView ya presente en el SO (WebView2 en Windows, WebKit en macOS/iOS, WebKitGTK en Linux), logrando instaladores diminutos (<5-10 MB)."
        },
        {
            "tema": 1,
            "subtema": "Tauri",
            "q": "¿Cómo se comunican el frontend web y el backend en Rust dentro de una aplicación Tauri?",
            "options": [
                "Mediante un sistema IPC seguro que invoca comandos de Rust definidos con la macro #[tauri::command] a través de window.__TAURI__.core.invoke()",
                "Enviando correos electrónicos automáticos a localhost",
                "Escribiendo en cintas magnéticas virtuales",
                "Mediante llamadas HTTP a servidores públicos en internet exclusivamente"
            ],
            "correct": 0,
            "explanation": "El frontend invoca funciones en Rust de forma asíncrona mediante el comando `invoke('nombre_del_comando', { argumentos })` a través del canal IPC interno y seguro de Tauri."
        },
        {
            "tema": 1,
            "subtema": "Comparativa de Frameworks",
            "q": "¿Qué lenguaje de programación utiliza cada uno de los siguientes frameworks: Flutter, React Native, .NET MAUI y Tauri?",
            "options": [
                "Flutter: Dart | React Native: JS/TS | .NET MAUI: C# | Tauri: Rust (backend) + Web (frontend)",
                "Flutter: Kotlin | React Native: Swift | .NET MAUI: Java | Tauri: C++",
                "Flutter: Python | React Native: PHP | .NET MAUI: Ruby | Tauri: Go",
                "Flutter: C# | React Native: Dart | .NET MAUI: JS | Tauri: Java"
            ],
            "correct": 0,
            "explanation": "Esa es la correspondencia exacta de lenguajes de cada tecnología según el temario."
        },
        {
            "tema": 1,
            "subtema": "Comparativa de Frameworks",
            "q": "¿Qué framework es el más adecuado si el objetivo primordial es crear una app con interfaces nativas reales en Android e iOS, pero reutilizando toda la lógica de negocio, arquitectura y modelos de datos en Kotlin?",
            "options": [
                "Kotlin Multiplatform (KMP)",
                "Apache Cordova",
                "Ionic v1",
                "Electron"
            ],
            "correct": 0,
            "explanation": "KMP es la solución de referencia para compartir lógica de negocio sin renunciar a la experiencia nativa de interfaz de usuario de cada plataforma."
        },
        {
            "tema": 1,
            "subtema": "Comparativa de Frameworks",
            "q": "Si un equipo con amplia experiencia en C# y Visual Studio desea crear una aplicación de gestión empresarial para Windows, macOS, Android e iOS, ¿cuál es la solución nativa más directa de Microsoft?",
            "options": [
                ".NET MAUI",
                "Flutter",
                "React Native",
                "PhoneGap"
            ],
            "correct": 0,
            "explanation": ".NET MAUI es la solución oficial del ecosistema Microsoft para aprovechar los conocimientos en C#, .NET y XAML en todas las plataformas."
        },
        {
            "tema": 1,
            "subtema": "Comparativa de Frameworks",
            "q": "¿Cuál es la principal ventaja de una Progressive Web App (PWA) frente a publicar en Apple App Store o Google Play Store?",
            "options": [
                "No depende de la aprobación ni comisiones de las tiendas de aplicaciones, permitiendo despliegues y actualizaciones inmediatas a través de la web",
                "Tiene acceso ilimitado a todas las instrucciones de la CPU sin permisos",
                "Nunca consume batería en el terminal móvil",
                "Permite compilar a binario sin escribir código"
            ],
            "correct": 0,
            "explanation": "Las PWAs se publican en servidores web estándar, eludiendo los procesos de revisión, demoras y comisiones (del 15% al 30%) de las tiendas de aplicaciones."
        },
        {
            "tema": 1,
            "subtema": "Comparativa de Frameworks",
            "q": "¿Qué framework multiplataforma utiliza un motor propio que NO emplea los widgets de Android ni iOS, asegurando consistencia total en el diseño en cualquier dispositivo?",
            "options": [
                "Flutter",
                "React Native",
                ".NET MAUI",
                "Tauri"
            ],
            "correct": 0,
            "explanation": "Flutter dibuja directamente en la pantalla con su motor gráfico (Skia/Impeller), manteniendo la misma apariencia independientemente del fabricante o versión de SO."
        },
        {
            "tema": 1,
            "subtema": "Comparativa de Frameworks",
            "q": "¿Qué ocurre si una aplicación híbrida en Ionic necesita acceder a una función hardware específica que no está incluida en los plugins oficiales de Capacitor?",
            "options": [
                "Es imposible acceder; hay que reescribir la aplicación en otro lenguaje",
                "Se puede programar un plugin personalizado en Java/Kotlin para Android y en Swift/Objective-C para iOS que exponga esa funcionalidad al Native Bridge",
                "El terminal bloquea la ejecución de la app por seguridad",
                "Se debe contactar con el consorcio W3C para que cambie el estándar web"
            ],
            "correct": 1,
            "explanation": "Capacitor cuenta con una arquitectura de plugins extensible que permite a los desarrolladores escribir plugins personalizados con código nativo en minutos."
        },
        {
            "tema": 1,
            "subtema": "Ciclo de Vida de Software",
            "q": "En el desarrollo de software móvil, ¿qué herramienta de emulación/virtualización se utiliza habitualmente en Android y en iOS?",
            "options": [
                "Android Emulator (basado en QEMU) en Android Studio y el Simulador de iOS en Xcode",
                "VirtualBox para ambos sin necesidad de SDK",
                "MS-DOS Prompt",
                "Un navegador Lynx en modo texto"
            ],
            "correct": 0,
            "explanation": "Android Studio incluye el Emulador de Android con aceleración de hardware (HAXM/Hypervisor), mientras que Xcode incluye el Simulador de iOS."
        },
        {
            "tema": 1,
            "subtema": "Publicación",
            "q": "¿Qué formato de paquete de distribución introdujo Google en sustitución del tradicional archivo .apk para reducir el tamaño de las descargas en Google Play?",
            "options": [
                "Android App Bundle (.aab)",
                ".ipa",
                ".dmg",
                ".tar.gz"
            ],
            "correct": 0,
            "explanation": "Android App Bundle (.aab) es el formato obligatorio en Google Play que permite a Google generar APKs optimizados y reducidos para la arquitectura específica de cada dispositivo."
        },
        {
            "tema": 1,
            "subtema": "Publicación",
            "q": "¿Qué extensión tienen los archivos empaquetados finales que se instalan en dispositivos iOS?",
            "options": [
                ".ipa",
                ".apk",
                ".exe",
                ".deb"
            ],
            "correct": 0,
            "explanation": "En iOS, los paquetes de aplicación instalables tienen la extensión `.ipa` (iOS App Store Package)."
        },
        {
            "tema": 1,
            "subtema": "Resumen General",
            "q": "¿Cuál es la recomendación general para elegir entre nativo, híbrido (Ionic) y cross-platform compilado (Flutter/React Native)?",
            "options": [
                "Nativo para máximo rendimiento y hardware intensivo; Híbrido/PWA para máxima rentabilidad y equipos web; Compilado (Flutter/RN) para experiencia cercana a la nativa compartiendo la mayor parte del código",
                "Usar siempre nativo para cualquier proyecto por simple que sea",
                "Usar siempre PWA para videojuegos con trazado de rayos en 3D",
                "Desarrollar únicamente para la plataforma que menos cuota de mercado tenga"
            ],
            "correct": 0,
            "explanation": "La elección depende del presupuesto, plazo, experiencia del equipo y requerimientos de rendimiento y acceso al hardware de cada aplicación."
        },
        {
            "tema": 1,
            "subtema": "PWA vs Tiendas",
            "q": "¿Qué mecanismo permite a una PWA pedir al usuario que añada la app a la pantalla de inicio en navegadores Chromium?",
            "options": [
                "El evento 'beforeinstallprompt'",
                "El comando 'window.install()'",
                "La etiqueta <meta name='force-install'>",
                "El método 'navigator.downloadApk()'"
            ],
            "correct": 0,
            "explanation": "Los navegadores basados en Chromium disparan el evento `beforeinstallprompt`, permitiendo interceptarlo para mostrar un botón o banner personalizado de instalación."
        }
    ]
    return qs
