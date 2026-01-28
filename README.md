# English Tutor B1 - UNED

Aplicación web para practicar inglés B1 con tutor IA y conversación por voz.

## Estructura

```
english-tutor/
├── index.html              # Página principal
├── css/
│   └── style.css           # Estilos (adaptados neurodivergencia)
├── js/
│   ├── app.js              # Lógica principal
│   ├── speech.js           # STT/TTS (Web Speech API)
│   ├── api.js              # Conexión con Claude
│   └── player.js           # Reproductor de podcasts
├── data/
│   └── course.json         # Estructura del curso
├── content/
│   └── lesson-1/           # Contenido lección 1
│       ├── grammar.html
│       ├── vocabulary.html
│       ├── practice.html
│       └── test.html
├── podcasts/               # MP3 de cada lección
├── scripts/
│   └── generate_podcast.py # Generador de podcasts
└── worker/
    └── claude-proxy.js     # Cloudflare Worker
```

## Configuración

### 1. Cloudflare Worker (Backend)

1. Ve a [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Workers & Pages > Create Application > Create Worker
3. Nombra el worker: `english-tutor`
4. Copia el contenido de `worker/claude-proxy.js`
5. Settings > Variables > Add Variable:
   - Name: `ANTHROPIC_API_KEY`
   - Value: tu API key de Anthropic
   - Encrypt: Yes
6. Deploy
7. Copia la URL del worker (ej: `https://english-tutor.tu-subdominio.workers.dev`)

### 2. Configurar la URL del Worker

Edita `js/api.js` y cambia:

```javascript
workerUrl: 'https://english-tutor.TU_SUBDOMINIO.workers.dev',
```

### 3. Generar Podcasts

```bash
# Instalar dependencias
pip install edge-tts

# Generar podcast de la lección 1
cd scripts
python generate_podcast.py 1

# Ver voces disponibles
python generate_podcast.py --list-voices
```

### 4. Desplegar en GitHub Pages

```bash
# Crear repositorio en GitHub
git init
git add .
git commit -m "English Tutor B1"
git remote add origin https://github.com/TU_USUARIO/english-tutor.git
git push -u origin main

# Activar GitHub Pages
# Settings > Pages > Source: main branch
```

## Uso

1. Abre la web
2. Selecciona una lección en el sidebar
3. Navega por las secciones: Grammar, Vocabulary, Practice, Test
4. Usa el chat para preguntar al tutor
5. Pulsa el botón de micrófono para hablar

## Funcionalidades

| Función | Descripción |
|---------|-------------|
| Chat texto | Escribe y recibe respuestas del tutor |
| Chat voz | Habla con el micrófono (STT → Claude → TTS) |
| Podcasts | Escucha explicaciones de cada lección |
| Ejercicios | Practica con feedback inmediato |
| Tests | Evalúa tu progreso |
| Progreso | Se guarda en localStorage |

## Tecnologías

- **Frontend**: HTML/CSS/JS vanilla
- **LLM**: Claude API (Anthropic)
- **STT/TTS**: Web Speech API (navegador)
- **Podcasts**: edge_tts (Microsoft)
- **Backend**: Cloudflare Workers
- **Hosting**: GitHub Pages

## Adaptaciones neurodivergencia

- Paleta de colores UNED (alto contraste)
- Estructura predecible
- Estados visuales claros
- Sin animaciones innecesarias
- Feedback inmediato
