/**
 * API.JS - Conexión con Cloudflare Worker (proxy a Claude)
 * English Tutor B1 - UNED
 */

const API = {
    // URL del Worker de Cloudflare (CAMBIAR POR TU URL)
    workerUrl: 'https://english-tutor.YOUR_SUBDOMAIN.workers.dev',

    // Historial de conversación
    conversationHistory: [],

    // Contexto del sistema (prompt del tutor)
    systemPrompt: `You are an English tutor for a B1 level student at UNED (Spanish distance university).

STUDENT PROFILE:
- Name: Fran
- Neurodivergent (ASD + High Abilities + ADHD traits)
- Needs clear, predictable structure
- Prefers concise responses without unnecessary padding
- Direct feedback without condescension
- Do NOT infantilize - full intellectual capacity

TEACHING STYLE:
- Short, clear sentences
- When correcting errors, briefly explain WHY
- Use concrete examples
- Confirm understanding before moving forward
- Use tables and structured formats when helpful

CURRENT LEVEL: B1 Intermediate
TEXTBOOK: Headway Intermediate

LANGUAGE RULES:
- Respond in English (you're teaching English)
- If student writes in Spanish, respond in English but acknowledge you understood
- Keep responses concise (2-4 sentences for simple questions, more for explanations)
- Always be encouraging but honest about errors

RESPONSE FORMAT:
- For corrections: State the error → Explain briefly → Give correct form → Example
- For explanations: Definition → Example → Common mistakes to avoid
- For practice: Clear instructions → Exercise → Feedback`,

    /**
     * Configura la URL del Worker
     * @param {string} url - URL del Cloudflare Worker
     */
    setWorkerUrl(url) {
        this.workerUrl = url;
        console.log('Worker URL configurado:', url);
    },

    /**
     * Envía un mensaje al tutor
     * @param {string} message - Mensaje del usuario
     * @param {object} context - Contexto adicional (lección actual, etc.)
     * @returns {Promise<string>} - Respuesta del tutor
     */
    async sendMessage(message, context = {}) {
        // Añadir mensaje del usuario al historial
        this.conversationHistory.push({
            role: 'user',
            content: message
        });

        // Construir contexto adicional si hay lección activa
        let contextMessage = '';
        if (context.lesson) {
            contextMessage = `\n[Current lesson: ${context.lesson.title}]`;
            if (context.section) {
                contextMessage += `\n[Current section: ${context.section}]`;
            }
        }

        try {
            const response = await fetch(this.workerUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    system: this.systemPrompt + contextMessage,
                    messages: this.conversationHistory
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            const assistantMessage = data.content || data.message || 'Sorry, I could not process your request.';

            // Añadir respuesta al historial
            this.conversationHistory.push({
                role: 'assistant',
                content: assistantMessage
            });

            // Limitar historial para no exceder tokens
            if (this.conversationHistory.length > 20) {
                this.conversationHistory = this.conversationHistory.slice(-20);
            }

            return assistantMessage;

        } catch (error) {
            console.error('Error calling API:', error);

            // Si no hay Worker configurado, usar modo demo
            if (this.workerUrl.includes('YOUR_SUBDOMAIN')) {
                return this.getDemoResponse(message);
            }

            throw error;
        }
    },

    /**
     * Respuesta demo cuando no hay Worker configurado
     * @param {string} message - Mensaje del usuario
     */
    getDemoResponse(message) {
        const lowerMessage = message.toLowerCase();

        // Respuestas predefinidas para demo
        const responses = {
            hello: "Hello! Great to see you practicing. How can I help you today? We can work on grammar, vocabulary, or just have a conversation.",
            help: "I can help you with:\n• Grammar explanations\n• Vocabulary practice\n• Conversation practice\n• Correcting your sentences\n\nJust ask me anything!",
            grammar: "Sure! What grammar point would you like to work on? We could practice Present Simple vs Present Continuous, Past tenses, or any other topic from your Headway book.",
            vocabulary: "Let's practice vocabulary! Give me a word or topic, and I'll help you learn related words and phrases.",
            default: "That's a good question! To give you a proper answer, I need the Cloudflare Worker to be configured. For now, try saying 'hello', 'help', 'grammar', or 'vocabulary'."
        };

        if (lowerMessage.includes('hello') || lowerMessage.includes('hi')) {
            return responses.hello;
        } else if (lowerMessage.includes('help')) {
            return responses.help;
        } else if (lowerMessage.includes('grammar')) {
            return responses.grammar;
        } else if (lowerMessage.includes('vocabulary') || lowerMessage.includes('vocab')) {
            return responses.vocabulary;
        }

        return responses.default;
    },

    /**
     * Limpia el historial de conversación
     */
    clearHistory() {
        this.conversationHistory = [];
    },

    /**
     * Actualiza el prompt del sistema con contexto de la lección
     * @param {object} lesson - Datos de la lección actual
     */
    setLessonContext(lesson) {
        // El contexto se pasa dinámicamente en cada llamada
        console.log('Lesson context set:', lesson?.title);
    }
};

// Exportar
window.API = API;
