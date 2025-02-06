# Ejercicio de Integración de ChatBot para Smarttie

Este proyecto tiene como objetivo integrar un chatbot inteligente para la empresa **Smarttie**. El chatbot está diseñado para interactuar con los usuarios de manera efectiva utilizando un modelo de lenguaje basado en **LLaMa 3.2-1B-Instruct**.

El chatbot puede responder preguntas, generar respuestas y almacenar el historial de la conversación para mejorar la interacción. Además, tiene un diseño intuitivo creado con la biblioteca **Gradio**.

## Requisitos

Para ejecutar este proyecto, necesitarás instalar las siguientes dependencias:

- Python 3.7 o superior
- PyTorch (con soporte para CUDA)
- Hugging Face Transformers
- Gradio
- dotenv

## Instalación

1. **Clona este repositorio** o descarga los archivos del proyecto.

   ```bash
   git clone https://github.com/BeyondEternalDEV/Smarrtie_Ejercicio.git
   cd Smarrtie_Ejercicio
   ```

2. **Crea un entorno virtual** (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

3. **Instala las dependencias necesarias**:

   ```bash
   pip install -r requirements.txt
   ```

   El archivo `requirements.txt` debe contener:

   ```
   torch
   transformers
   gradio
   python-dotenv
   ```

4. **Configura tus variables de entorno**:

   Asegúrate de tener un archivo `.env` en el directorio raíz del proyecto. Este archivo debe contener el token de acceso a tu Hugging Face.

   Ejemplo de archivo `.env`:

   ```
   HF_TOKEN = tu_clave_api
   ```

## Uso

1. **Ejecuta el chatbot**:

   Para iniciar el chatbot, simplemente ejecuta el siguiente comando:

   ```bash
   python app.py
   ```

   Esto iniciará la interfaz web de **Gradio** donde podrás interactuar con el chatbot.

2. **Interacción con el chatbot**:

   - Puedes escribir un mensaje en el campo de texto y presionar **Enter** o hacer clic en el ícono de flecha **"➡"** para enviar el mensaje.
   - El chatbot tiene una configuración de tokens máximos y temperatura que puedes ajustar para personalizar la generación de texto.

3. **Configuraciones**:
   - **Indicación del Sistema**: Define el comportamiento y el contexto del chatbot.
   - **Tokens máximos**: Ajusta la cantidad máxima de tokens generados por respuesta.
   - **Temperatura**: Controla la creatividad de las respuestas (0.0 para respuestas más conservadoras, 1.0 para respuestas más creativas).

4. **Limpiar el chat**:
   Puedes limpiar el historial de la conversación haciendo clic en el botón **🗑 Limpiar Chat**.

## Tecnología Utilizada

- **LLaMa 3.2-1B-Instruct**: Un modelo de lenguaje avanzado de Hugging Face utilizado para generar respuestas del chatbot.
- **Gradio**: Una biblioteca para crear interfaces de usuario interactivas y fáciles de usar.
- **Transformers**: La biblioteca de Hugging Face para modelos de lenguaje y procesamiento de texto.
- **PyTorch**: La biblioteca utilizada para ejecutar el modelo en la GPU (si está disponible).

## Licencia

Este proyecto está bajo la licencia **MIT**.

---

Si tienes alguna pregunta o necesitas soporte adicional, no dudes en abrir un **issue** en este repositorio o contactar al equipo de desarrollo.
```

### Pasos para usar este archivo:
1. **Clona el repositorio** o guarda este contenido en un archivo llamado `README.md` en la raíz de tu proyecto.
2. Asegúrate de tener un archivo `.env` en tu proyecto si necesitas configuraciones adicionales como claves de API.
3. Sigue las instrucciones de instalación y ejecución que están en el `README.md`.
