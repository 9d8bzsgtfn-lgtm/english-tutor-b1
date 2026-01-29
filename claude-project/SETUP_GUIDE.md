# Guía de Configuración: Claude Projects como Tutor de Inglés B1

Esta guía te explica paso a paso cómo configurar tu tutor de inglés personalizado usando Claude Projects en claude.ai.

---

## Requisitos Previos

- Cuenta en [claude.ai](https://claude.ai)
- Suscripción Claude Pro (recomendado) o cuenta gratuita
- Los archivos de este proyecto descargados en tu ordenador

---

## Paso 1: Acceder a Claude Projects

1. Ve a [claude.ai](https://claude.ai) e inicia sesión
2. En la barra lateral izquierda, busca la sección **"Projects"**
3. Si no la ves, puede estar en el menú desplegable o necesitas actualizar tu cuenta

![Ubicación de Projects en el menú lateral]

**Dónde hacer clic:** Menú lateral izquierdo → "Projects" (icono de carpeta)

---

## Paso 2: Crear un Nuevo Proyecto

1. Haz clic en **"+ New Project"** o **"Create Project"**
2. Introduce los siguientes datos:
   - **Name:** `English B1 Tutor`
   - **Description:** `Tutor personalizado de inglés nivel B1 para hispanohablantes`

3. Haz clic en **"Create"** o **"Save"**

![Formulario de creación de proyecto]

**Dónde hacer clic:** Botón "New Project" → Rellenar nombre → "Create"

---

## Paso 3: Añadir las Instrucciones del Sistema

Las instrucciones del sistema definen cómo se comportará Claude como tu tutor.

1. Dentro de tu proyecto, busca la sección **"Instructions"** o **"Custom Instructions"**
2. Haz clic en **"Edit"** o en el icono de lápiz ✏️
3. **Copia todo el contenido** del archivo `INSTRUCTIONS.md`
4. **Pega** el contenido en el campo de instrucciones
5. Haz clic en **"Save"**

![Editor de instrucciones]

**Dónde hacer clic:** Project Settings → Instructions → Edit → Pegar → Save

### Contenido a copiar:

```
📋 Abre el archivo INSTRUCTIONS.md y copia TODO su contenido
```

---

## Paso 4: Subir los Archivos de Conocimiento

Los archivos de conocimiento dan a Claude información de referencia sobre gramática, vocabulario y errores comunes.

### 4.1 Acceder a la sección de Knowledge

1. Dentro del proyecto, busca la sección **"Knowledge"** o **"Project Knowledge"**
2. Haz clic en **"Add knowledge"** o **"Upload files"**

![Sección de Knowledge]

### 4.2 Subir los archivos

Sube los siguientes archivos de la carpeta `knowledge/`:

| Archivo | Descripción |
|---------|-------------|
| `grammar_reference.md` | Referencia gramatical completa |
| `vocabulary_list.md` | Lista de vocabulario por temas |
| `common_errors.md` | Errores típicos de hispanohablantes |

**Pasos:**
1. Haz clic en **"Upload"** o arrastra los archivos
2. Selecciona los 3 archivos de la carpeta `knowledge/`
3. Espera a que se procesen (puede tardar unos segundos)
4. Verifica que aparecen listados en la sección Knowledge

![Subida de archivos]

**Dónde hacer clic:** Knowledge → Upload → Seleccionar archivos → Confirmar

---

## Paso 5: Subir el Overview del Curso (Opcional)

También puedes subir `COURSE_OVERVIEW.md` como archivo de conocimiento para que Claude tenga acceso al plan completo del curso:

1. En la sección Knowledge, haz clic en **"Add knowledge"**
2. Sube el archivo `COURSE_OVERVIEW.md`
3. Confirma la subida

---

## Paso 6: Verificar la Configuración

Antes de empezar a usar tu tutor, verifica que todo está configurado:

### Lista de verificación:

- [ ] **Proyecto creado** con nombre "English B1 Tutor"
- [ ] **Instrucciones** copiadas y guardadas
- [ ] **grammar_reference.md** subido
- [ ] **vocabulary_list.md** subido
- [ ] **common_errors.md** subido
- [ ] **COURSE_OVERVIEW.md** subido (opcional)

---

## Paso 7: Iniciar tu Primera Sesión

1. Dentro del proyecto, haz clic en **"New Chat"** o **"Start Conversation"**
2. Claude debería saludarte como Emma, tu tutora
3. Si no lo hace, escribe: `Hello!`

### Mensaje de bienvenida esperado:

```
Hello Francisco! 👋

I'm Emma, your English tutor. How are you feeling today?

What would you like to work on?
- Continue with your current lesson
- Review previous vocabulary
- Practice conversation
- Focus on a specific grammar point

Just let me know, and we'll get started! 🎯
```

---

## Comandos Útiles

Una vez en la conversación, puedes usar estos comandos:

| Comando | Qué hace |
|---------|----------|
| `/lesson 1` | Empieza la lección 1 |
| `/review` | Repaso de vocabulario |
| `/conversation` | Práctica de conversación libre |
| `/grammar present perfect` | Explicación de un tema gramatical |
| `/vocabulary travel` | Lista de vocabulario de un tema |
| `/exercise` | Ejercicio del tema actual |
| `/break` | Solicitar una pausa |
| `/spanish` | Cambiar temporalmente a español |
| `/progress` | Ver tu progreso |

---

## Consejos de Uso

### Para sesiones efectivas:

1. **Duración:** Sesiones de 20-30 minutos son ideales
2. **Frecuencia:** 3-4 sesiones por semana para mantener el ritmo
3. **Variedad:** Alterna entre gramática, vocabulario y conversación
4. **Pausas:** No dudes en usar `/break` cuando lo necesites

### Para maximizar el aprendizaje:

1. **Habla en inglés** todo lo posible, aunque cometas errores
2. **Pide explicaciones** si algo no queda claro
3. **Practica en voz alta** aunque sea solo leyendo las respuestas
4. **Repasa** el vocabulario nuevo al día siguiente

### Para la neurodivergencia:

1. **Avisa a Emma** si necesitas más tiempo o pausas
2. **Pide estructura** si la sesión se vuelve confusa
3. **Usa `/slower`** si va demasiado rápido
4. **Cambia de actividad** si una se vuelve monótona

---

## Solución de Problemas

### Claude no responde como Emma

**Solución:** Verifica que las instrucciones estén guardadas correctamente. Prueba a escribir: "Please act as Emma, my English tutor, as specified in the instructions."

### No encuentra información de vocabulario/gramática

**Solución:** Verifica que los archivos de Knowledge están subidos. Prueba: "Can you check your knowledge files for the grammar reference?"

### Las respuestas son demasiado largas/cortas

**Solución:** Puedes pedir: "Please give me shorter responses" o "Can you explain in more detail?"

### Quiero reiniciar una lección

**Solución:** Escribe: "Let's start lesson X from the beginning, please."

---

## Actualización y Mantenimiento

### Añadir nuevo contenido:

1. Ve a tu proyecto
2. En Knowledge, haz clic en "Add"
3. Sube nuevos archivos según necesites

### Modificar instrucciones:

1. Ve a Project Settings
2. Edita las instrucciones
3. Guarda los cambios

### Exportar conversaciones:

Las conversaciones se guardan automáticamente en el proyecto. Puedes revisarlas en cualquier momento para ver tu progreso.

---

## Estructura de Archivos

```
claude-project/
├── INSTRUCTIONS.md          ← Instrucciones para Claude (copiar en el proyecto)
├── COURSE_OVERVIEW.md       ← Resumen del curso (subir a Knowledge)
├── SETUP_GUIDE.md           ← Esta guía
└── knowledge/
    ├── grammar_reference.md ← Subir a Knowledge
    ├── vocabulary_list.md   ← Subir a Knowledge
    └── common_errors.md     ← Subir a Knowledge
```

---

## Contacto y Soporte

Si tienes problemas con la configuración o el uso del tutor, puedes:

1. Revisar esta guía de nuevo
2. Preguntar directamente a Claude: "I'm having trouble with..."
3. Consultar la documentación oficial de Claude Projects

---

¡Buena suerte con tu aprendizaje del inglés! 🎓
