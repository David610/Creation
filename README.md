# Creation: A text-generating Web App

## Description
This project is a text generation web application that takes user input and generates text dynamically using a pre-trained language model (distilgpt2). It showcases the utilization of NLP (Natural Language Processing) models in an intuitive web interface, featuring a clean UI built with Bootstrap 4 and a Flask backend with Flask-SocketIO for real-time updates and communication.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Features
- **Text Generation**: Generates text based on user input using the distilgpt2 model.
- **Flask Backend**: Serves the web app and handles API requests for text generation.
- **SocketIO**: Enables real-time communication between client and server.
- **Bootstrap 4**: Provides a responsive and modern UI for desktop and mobile views.
- **Google Fonts & Material Icons**: Enhances user experience with clean fonts and iconography.
- **SVG Graphics**: Includes scalable vector graphics for improved aesthetics.

## Tech Stack
- **Backend**: Python, Flask, Flask-SocketIO
- **Frontend**: HTML5, CSS3 (Bootstrap 4), JavaScript
- **Machine Learning Model**: HuggingFace `distilgpt2` for natural language generation
- **Deployment**: AWS S3 for hosting static files, Flask for backend server
- **Others**: Material Icons, Google Fonts, SVG graphics

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-generation-webapp.git
   cd text-generation-webapp
   ```

2. Make a Python virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open the application:
   Navigate to `http://127.0.0.1:5500/` in your browser.

## Usage
1. Access the homepage with the text generation prompt.
2. Enter a prompt in the input field.
3. Click 'Generate' to process your input.
4. Review the generated text displayed below the input field.

## File Structure
```
.
├── app.py                # Main Flask app and backend API
├── templates
│   └── index.html        # Frontend HTML with Bootstrap and JS
├── static
│   ├── style.css         # Custom styling
│   └── FetchAPI.js       # JavaScript for handling API calls
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## License
This project is licensed under the Apache-2.0 License.
