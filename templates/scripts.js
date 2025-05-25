
// Enhanced Chat Functionality
class MedicalChatBot {
    constructor() {
        this.chatMessages = document.getElementById('chat-messages');
        this.chatInput = document.getElementById('chat-input');
        this.isTyping = false;
        
        // Medical knowledge base (simplified for demo)
        this.medicalResponses = {
            'headache': {
                response: "Headaches can have various causes. Common types include tension headaches, migraines, and cluster headaches. If you're experiencing severe, sudden headaches or they're accompanied by fever, vision changes, or neck stiffness, please seek immediate medical attention.",
                suggestions: ["Stay hydrated", "Rest in a quiet, dark room", "Apply cold or warm compress", "Consider over-the-counter pain relievers"]
            },
            'fever': {
                response: "Fever is often a sign that your body is fighting an infection. Normal body temperature is around 98.6°F (37°C). Seek medical attention if fever exceeds 103°F (39.4°C) or persists for more than 3 days.",
                suggestions: ["Stay hydrated", "Rest", "Dress lightly", "Monitor temperature regularly"]
            },
            'chest pain': {
                response: "⚠️ IMPORTANT: Chest pain can be serious. If you're experiencing severe chest pain, especially with shortness of breath, sweating, or pain radiating to arm/jaw, call emergency services immediately. Other causes may include muscle strain, heartburn, or anxiety.",
                suggestions: ["Seek immediate medical attention if severe", "Note associated symptoms", "Avoid physical exertion"]
            },
            'stomach ache': {
                response: "Stomach pain can result from various causes including indigestion, gas, food poisoning, or stress. Most mild cases resolve on their own. Seek medical help if pain is severe, persists, or is accompanied by fever, vomiting, or blood.",
                suggestions: ["Stay hydrated", "Eat bland foods (BRAT diet)", "Avoid dairy and fatty foods", "Rest"]
            }
        };
    }

    init() {
        // Enhanced send message function
        window.sendMessage = () => this.sendMessage();
        
        // Auto-resize input
        this.chatInput.addEventListener('input', () => {
            this.chatInput.style.height = 'auto';
            this.chatInput.style.height = this.chatInput.scrollHeight + 'px';
        });
    }

    sendMessage() {
        const message = this.chatInput.value.trim();
        if (!message || this.isTyping) return;

        // Add user message
        this.addMessage(message, 'user');
        this.chatInput.value = '';
        
        // Show typing indicator
        this.showTypingIndicator();
        
        // Simulate AI processing time
        setTimeout(() => {
            this.hideTypingIndicator();
            this.processAIResponse(message);
        }, 1500 + Math.random() * 1000);
    }

    addMessage(content, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `chat-message ${sender}-message fade-in-up`;
        
        if (sender === 'user') {
            messageDiv.innerHTML = `
                <div class="message-avatar">
                    <i class="fas fa-user"></i>
                </div>
                <div class="message-content">${content}</div>
            `;
        } else {
            messageDiv.innerHTML = `
                <div class="message-avatar">
                    <i class="fas fa-robot"></i>
                </div>
                <div class="message-content">${content}</div>
            `;
        }
        
        this.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }

    processAIResponse(userMessage) {
        const lowerMessage = userMessage.toLowerCase();
        let response = "I understand your concern. While I can provide general information, it's important to consult with a healthcare professional for personalized advice. ";
        
        // Check for medical keywords
        const foundCondition = Object.keys(this.medicalResponses).find(condition => 
            lowerMessage.includes(condition)
        );
        
        if (foundCondition) {
            const medicalInfo = this.medicalResponses[foundCondition];
            response = medicalInfo.response;
            
            if (medicalInfo.suggestions.length > 0) {
                response += "\n\nGeneral suggestions:\n";
                medicalInfo.suggestions.forEach(suggestion => {
                    response += `• ${suggestion}\n`;
                });
            }
        } else if (lowerMessage.includes('emergency') || lowerMessage.includes('urgent')) {
            response = "🚨 If this is a medical emergency, please call your local emergency number immediately (911 in the US, 999 in the UK, etc.) or go to the nearest emergency room.";
        } else if (lowerMessage.includes('medication') || lowerMessage.includes('medicine')) {
            response = "I can provide general information about medications, but I cannot prescribe or recommend specific medications. Always consult with a licensed healthcare provider or pharmacist for medication advice.";
        } else if (lowerMessage.includes('covid') || lowerMessage.includes('coronavirus')) {
            response = "For COVID-19 related concerns, please refer to your local health department guidelines or consult with a healthcare provider. Symptoms may include fever, cough, shortness of breath, fatigue, and loss of taste or smell.";
        } else {
            // Generate a more contextual response
            response += this.generateContextualResponse(lowerMessage);
        }
        
        response += "\n\n💡 Remember: This AI assistant provides general information only and should not replace professional medical advice, diagnosis, or treatment.";
        
        this.addMessage(response, 'ai');
    }

    generateContextualResponse(message) {
        if (message.includes('pain')) {
            return "Pain can have various causes. It's important to note the location, intensity (1-10 scale), duration, and any triggering factors. If pain is severe or persistent, please consult a healthcare provider.";
        } else if (message.includes('tired') || message.includes('fatigue')) {
            return "Fatigue can result from poor sleep, stress, dehydration, or underlying health conditions. Ensure adequate sleep, stay hydrated, and maintain a balanced diet.";
        } else if (message.includes('sleep')) {
            return "Good sleep hygiene includes maintaining a consistent sleep schedule, creating a comfortable sleep environment, and avoiding screens before bedtime.";
        } else if (message.includes('diet') || message.includes('nutrition')) {
            return "A balanced diet includes fruits, vegetables, whole grains, lean proteins, and adequate hydration. Consider consulting a nutritionist for personalized advice.";
        } else {
            return "Could you provide more specific details about your symptoms or concerns? This will help me give you more relevant information.";
        }
    }

    showTypingIndicator() {
        this.isTyping = true;
        const typingDiv = document.createElement('div');
        typingDiv.className = 'chat-message ai-message typing-indicator';
        typingDiv.id = 'typing-indicator';
        typingDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas fa-robot"></i>
            </div>
            <div class="message-content">
                <div class="typing-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        `;
        this.chatMessages.appendChild(typingDiv);
        this.scrollToBottom();
    }

    hideTypingIndicator() {
        this.isTyping = false;
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    scrollToBottom() {
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }
}

// Initialize chat bot when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const chatBot = new MedicalChatBot();
    chatBot.init();
});
