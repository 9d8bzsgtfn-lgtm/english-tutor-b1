/**
 * APP.JS - Lógica principal de la aplicación
 * English Tutor B1 - UNED
 */

const App = {
    // Estado de la aplicación
    state: {
        currentLesson: null,
        currentSection: 'grammar',
        lessons: [],
        isLoading: false
    },

    // Elementos DOM
    elements: {},

    /**
     * Inicializa la aplicación
     */
    async init() {
        console.log('Iniciando English Tutor B1...');

        // Cachear elementos DOM
        this.cacheElements();

        // Cargar datos del curso
        await this.loadCourseData();

        // Renderizar navegación
        this.renderLessonsNav();

        // Configurar event listeners
        this.setupEventListeners();

        // Inicializar módulos
        SpeechManager.init();
        PodcastPlayer.init();

        // Configurar callbacks de Speech
        this.setupSpeechCallbacks();

        // Seleccionar lección 1 por defecto
        if (this.state.lessons.length > 0) {
            this.selectLesson(1);
        }

        console.log('English Tutor B1 inicializado');
    },

    /**
     * Cachea elementos DOM frecuentes
     */
    cacheElements() {
        this.elements = {
            lessonsNav: document.getElementById('lessonsNav'),
            lessonTitle: document.getElementById('lessonTitle'),
            lessonDescription: document.getElementById('lessonDescription'),
            sectionTabs: document.getElementById('sectionTabs'),
            sectionContent: document.getElementById('sectionContent'),
            chatMessages: document.getElementById('chatMessages'),
            chatInput: document.getElementById('chatInput'),
            sendBtn: document.getElementById('sendBtn'),
            voiceBtn: document.getElementById('voiceBtn'),
            voiceText: document.getElementById('voiceText'),
            voiceStatus: document.getElementById('voiceStatus'),
            autoVoice: document.getElementById('autoVoice'),
            progressFill: document.getElementById('progressFill'),
            progressText: document.getElementById('progressText')
        };
    },

    /**
     * Carga los datos del curso
     */
    async loadCourseData() {
        try {
            const response = await fetch('data/course.json');
            const data = await response.json();
            this.state.lessons = data.lessons;
            console.log('Datos del curso cargados:', this.state.lessons.length, 'lecciones');
        } catch (error) {
            console.warn('No se pudo cargar course.json, usando datos por defecto');
            this.state.lessons = this.getDefaultLessons();
        }
    },

    /**
     * Datos por defecto si no hay course.json
     */
    getDefaultLessons() {
        return [
            {
                id: 1,
                title: "Present Tenses",
                description: "Present Simple vs Present Continuous",
                completed: false,
                sections: {
                    grammar: true,
                    vocabulary: true,
                    practice: true,
                    test: true
                }
            },
            { id: 2, title: "Past Tenses", description: "Past Simple vs Past Continuous", completed: false },
            { id: 3, title: "Present Perfect", description: "Present Perfect Simple and Continuous", completed: false },
            { id: 4, title: "Future Forms", description: "Will, Going to, Present Continuous for future", completed: false },
            { id: 5, title: "Comparatives & Superlatives", description: "Comparing things and people", completed: false },
            { id: 6, title: "Modal Verbs", description: "Can, Could, Must, Should, May, Might", completed: false },
            { id: 7, title: "Conditionals", description: "Zero, First and Second Conditional", completed: false },
            { id: 8, title: "Passive Voice", description: "Present and Past Passive", completed: false },
            { id: 9, title: "Reported Speech", description: "Reporting what people said", completed: false },
            { id: 10, title: "Relative Clauses", description: "Who, Which, That, Where", completed: false },
            { id: 11, title: "Phrasal Verbs", description: "Common phrasal verbs", completed: false },
            { id: 12, title: "Review & Exam Practice", description: "Full course revision", completed: false }
        ];
    },

    /**
     * Renderiza la navegación de lecciones
     */
    renderLessonsNav() {
        const nav = this.elements.lessonsNav;
        nav.innerHTML = '';

        this.state.lessons.forEach(lesson => {
            const btn = document.createElement('button');
            btn.className = `lesson-btn ${lesson.completed ? 'completed' : ''} ${this.state.currentLesson?.id === lesson.id ? 'active' : ''}`;
            btn.dataset.lessonId = lesson.id;
            btn.textContent = `${lesson.id}. ${lesson.title}`;
            btn.addEventListener('click', () => this.selectLesson(lesson.id));
            nav.appendChild(btn);
        });

        this.updateProgress();
    },

    /**
     * Selecciona una lección
     * @param {number} lessonId - ID de la lección
     */
    async selectLesson(lessonId) {
        const lesson = this.state.lessons.find(l => l.id === lessonId);
        if (!lesson) return;

        this.state.currentLesson = lesson;

        // Actualizar UI
        this.elements.lessonTitle.textContent = `Lesson ${lesson.id}: ${lesson.title}`;
        this.elements.lessonDescription.textContent = lesson.description;

        // Actualizar navegación
        document.querySelectorAll('.lesson-btn').forEach(btn => {
            btn.classList.toggle('active', parseInt(btn.dataset.lessonId) === lessonId);
        });

        // Cargar contenido de la sección actual
        await this.loadSection(this.state.currentSection);

        // Cargar podcast
        PodcastPlayer.load(lessonId);

        // Informar a la API del contexto
        API.setLessonContext(lesson);

        console.log('Lección seleccionada:', lesson.title);
    },

    /**
     * Carga el contenido de una sección
     * @param {string} section - Nombre de la sección
     */
    async loadSection(section) {
        this.state.currentSection = section;

        // Actualizar tabs
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.section === section);
        });

        // Mostrar loading
        this.elements.sectionContent.innerHTML = '<div class="loading"></div>';

        try {
            const lessonId = this.state.currentLesson?.id;
            if (!lessonId) {
                throw new Error('No lesson selected');
            }

            // Intentar cargar contenido del archivo
            const response = await fetch(`content/lesson-${lessonId}/${section}.html`);

            if (response.ok) {
                const content = await response.text();
                this.elements.sectionContent.innerHTML = content;
            } else {
                // Usar contenido por defecto
                this.elements.sectionContent.innerHTML = this.getDefaultSectionContent(section);
            }

            // Setup interactivo según la sección
            this.setupSectionInteractivity(section);

        } catch (error) {
            console.warn('Error cargando sección:', error);
            this.elements.sectionContent.innerHTML = this.getDefaultSectionContent(section);
        }
    },

    /**
     * Contenido por defecto para cada sección
     * @param {string} section - Nombre de la sección
     */
    getDefaultSectionContent(section) {
        const lesson = this.state.currentLesson;
        if (!lesson) return '<p>Select a lesson to begin.</p>';

        const contents = {
            grammar: `
                <h3>Grammar: ${lesson.title}</h3>
                <div class="box-importante">
                    <span class="tag tag-importante">IMPORTANTE</span>
                    <p>El contenido de gramática para esta lección se cargará desde los archivos del curso.</p>
                    <p>Mientras tanto, puedes preguntar al tutor sobre este tema en el chat.</p>
                </div>
                <div class="box-info">
                    <span class="tag tag-info">TIP</span>
                    <p>Usa el chat para practicar. Por ejemplo, pregunta: "Can you explain ${lesson.title}?"</p>
                </div>
            `,
            vocabulary: `
                <h3>Vocabulary: ${lesson.title}</h3>
                <div class="vocab-grid">
                    <div class="vocab-card">
                        <div class="vocab-word">Example word</div>
                        <div class="vocab-phonetic">/ɪɡˈzɑːmpl/</div>
                        <div class="vocab-translation">Palabra de ejemplo</div>
                        <div class="vocab-example">"This is an example sentence."</div>
                        <button class="vocab-speak-btn" onclick="SpeechManager.speak('Example word')">🔊 Listen</button>
                    </div>
                </div>
                <div class="box-complementario">
                    <span class="tag tag-complementario">NOTA</span>
                    <p>El vocabulario completo se cargará desde los archivos del curso.</p>
                </div>
            `,
            practice: `
                <h3>Practice: ${lesson.title}</h3>
                <div class="exercise">
                    <div class="exercise-question">
                        <p>Practice exercises will be loaded from the course files.</p>
                    </div>
                </div>
                <div class="box-info">
                    <span class="tag tag-info">PRACTICE TIP</span>
                    <p>Use the chat to practice with the tutor. Say something using ${lesson.title} and the tutor will correct you if needed.</p>
                </div>
            `,
            test: `
                <h3>Test: ${lesson.title}</h3>
                <div class="box-importante">
                    <span class="tag tag-importante">TEST</span>
                    <p>The test for this lesson will be available once you complete the Grammar, Vocabulary and Practice sections.</p>
                </div>
                <div class="test-results hidden" id="testResults">
                    <div class="test-score">0%</div>
                    <p>Your score will appear here after completing the test.</p>
                </div>
            `
        };

        return contents[section] || '<p>Content not available.</p>';
    },

    /**
     * Configura la interactividad de cada sección
     * @param {string} section - Nombre de la sección
     */
    setupSectionInteractivity(section) {
        switch (section) {
            case 'vocabulary':
                // Los botones de pronunciación ya tienen onclick inline
                break;
            case 'practice':
                this.setupPracticeExercises();
                break;
            case 'test':
                this.setupTest();
                break;
        }
    },

    /**
     * Configura ejercicios de práctica
     */
    setupPracticeExercises() {
        document.querySelectorAll('.exercise-option').forEach(option => {
            option.addEventListener('click', (e) => {
                const exercise = e.target.closest('.exercise');
                const options = exercise.querySelectorAll('.exercise-option');
                const feedback = exercise.querySelector('.exercise-feedback');
                const isCorrect = option.dataset.correct === 'true';

                // Desmarcar otras opciones
                options.forEach(opt => opt.classList.remove('selected'));
                option.classList.add('selected');

                // Mostrar si es correcta o no
                if (isCorrect) {
                    option.classList.add('correct');
                    feedback?.classList.add('correct', 'show');
                    feedback?.classList.remove('incorrect');
                } else {
                    option.classList.add('incorrect');
                    feedback?.classList.add('incorrect', 'show');
                    feedback?.classList.remove('correct');
                }
            });
        });
    },

    /**
     * Configura el test
     */
    setupTest() {
        // TODO: Implementar lógica de test
    },

    /**
     * Configura event listeners generales
     */
    setupEventListeners() {
        // Tabs de sección
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', () => this.loadSection(btn.dataset.section));
        });

        // Chat - Enviar por click
        this.elements.sendBtn?.addEventListener('click', () => this.sendChatMessage());

        // Chat - Enviar por Enter
        this.elements.chatInput?.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendChatMessage();
        });

        // Botón de voz
        this.elements.voiceBtn?.addEventListener('click', () => this.toggleVoice());
    },

    /**
     * Configura callbacks del Speech Manager
     */
    setupSpeechCallbacks() {
        SpeechManager.onStart = () => {
            this.elements.voiceBtn?.classList.add('listening');
            this.elements.voiceBtn?.classList.remove('processing', 'speaking', 'error');
            this.elements.voiceText.textContent = 'ESCUCHANDO...';
            this.elements.voiceStatus.textContent = 'Habla ahora';
            this.elements.voiceStatus.className = 'voice-status listening';
        };

        SpeechManager.onEnd = () => {
            this.elements.voiceBtn?.classList.remove('listening');
            if (!this.state.isLoading) {
                this.elements.voiceText.textContent = 'HABLAR';
                this.elements.voiceStatus.textContent = 'LISTO';
                this.elements.voiceStatus.className = 'voice-status';
            }
        };

        SpeechManager.onResult = (finalTranscript, interimTranscript) => {
            if (finalTranscript) {
                this.elements.chatInput.value = finalTranscript;
                this.sendChatMessage();
            } else if (interimTranscript) {
                this.elements.chatInput.value = interimTranscript;
            }
        };

        SpeechManager.onError = (error) => {
            this.elements.voiceBtn?.classList.add('error');
            this.elements.voiceBtn?.classList.remove('listening', 'processing', 'speaking');
            this.elements.voiceText.textContent = 'ERROR';
            this.elements.voiceStatus.textContent = error;
            this.elements.voiceStatus.className = 'voice-status error';

            setTimeout(() => {
                this.elements.voiceBtn?.classList.remove('error');
                this.elements.voiceText.textContent = 'HABLAR';
                this.elements.voiceStatus.textContent = 'LISTO';
                this.elements.voiceStatus.className = 'voice-status';
            }, 3000);
        };

        SpeechManager.onSpeakStart = () => {
            this.elements.voiceBtn?.classList.add('speaking');
            this.elements.voiceBtn?.classList.remove('listening', 'processing', 'error');
            this.elements.voiceText.textContent = 'HABLANDO...';
            this.elements.voiceStatus.textContent = 'Escucha';
            this.elements.voiceStatus.className = 'voice-status speaking';
        };

        SpeechManager.onSpeakEnd = () => {
            this.elements.voiceBtn?.classList.remove('speaking');
            this.elements.voiceText.textContent = 'HABLAR';
            this.elements.voiceStatus.textContent = 'LISTO';
            this.elements.voiceStatus.className = 'voice-status';
        };
    },

    /**
     * Alterna el reconocimiento de voz
     */
    toggleVoice() {
        if (SpeechManager.isListening) {
            SpeechManager.stopListening();
        } else {
            SpeechManager.startListening();
        }
    },

    /**
     * Envía un mensaje de chat
     */
    async sendChatMessage() {
        const message = this.elements.chatInput.value.trim();
        if (!message) return;

        // Limpiar input
        this.elements.chatInput.value = '';

        // Añadir mensaje del usuario al chat
        this.addChatMessage('user', message);

        // Mostrar estado de procesamiento
        this.state.isLoading = true;
        this.elements.voiceBtn?.classList.add('processing');
        this.elements.voiceBtn?.classList.remove('listening', 'speaking', 'error');
        this.elements.voiceText.textContent = 'PENSANDO...';
        this.elements.voiceStatus.textContent = 'Procesando';
        this.elements.voiceStatus.className = 'voice-status processing';

        try {
            // Enviar a la API
            const response = await API.sendMessage(message, {
                lesson: this.state.currentLesson,
                section: this.state.currentSection
            });

            // Añadir respuesta al chat
            this.addChatMessage('tutor', response);

            // Leer respuesta en voz alta si está activado
            if (this.elements.autoVoice?.checked) {
                SpeechManager.speak(response);
            }

        } catch (error) {
            console.error('Error:', error);
            this.addChatMessage('tutor', 'Sorry, there was an error. Please try again.');
        } finally {
            this.state.isLoading = false;
            if (!SpeechManager.isSpeaking) {
                this.elements.voiceBtn?.classList.remove('processing');
                this.elements.voiceText.textContent = 'HABLAR';
                this.elements.voiceStatus.textContent = 'LISTO';
                this.elements.voiceStatus.className = 'voice-status';
            }
        }
    },

    /**
     * Añade un mensaje al chat
     * @param {string} author - 'user' o 'tutor'
     * @param {string} text - Texto del mensaje
     */
    addChatMessage(author, text) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${author === 'user' ? 'user-message' : 'tutor-message'}`;

        messageDiv.innerHTML = `
            <span class="message-author">${author === 'user' ? 'You:' : 'Tutor:'}</span>
            <p>${text}</p>
        `;

        this.elements.chatMessages.appendChild(messageDiv);
        this.elements.chatMessages.scrollTop = this.elements.chatMessages.scrollHeight;
    },

    /**
     * Actualiza la barra de progreso
     */
    updateProgress() {
        const completed = this.state.lessons.filter(l => l.completed).length;
        const total = this.state.lessons.length;
        const percent = (completed / total) * 100;

        this.elements.progressFill.style.width = `${percent}%`;
        this.elements.progressText.textContent = `${completed} / ${total} completadas`;
    },

    /**
     * Marca una lección como completada
     * @param {number} lessonId - ID de la lección
     */
    completeLesson(lessonId) {
        const lesson = this.state.lessons.find(l => l.id === lessonId);
        if (lesson) {
            lesson.completed = true;
            this.renderLessonsNav();
            this.saveCourseProgress();
        }
    },

    /**
     * Guarda el progreso en localStorage
     */
    saveCourseProgress() {
        const progress = this.state.lessons.map(l => ({
            id: l.id,
            completed: l.completed
        }));
        localStorage.setItem('englishTutorProgress', JSON.stringify(progress));
    },

    /**
     * Carga el progreso desde localStorage
     */
    loadCourseProgress() {
        try {
            const saved = localStorage.getItem('englishTutorProgress');
            if (saved) {
                const progress = JSON.parse(saved);
                progress.forEach(p => {
                    const lesson = this.state.lessons.find(l => l.id === p.id);
                    if (lesson) lesson.completed = p.completed;
                });
            }
        } catch (error) {
            console.warn('Error loading progress:', error);
        }
    }
};

// Iniciar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => App.init());

// Exportar
window.App = App;
