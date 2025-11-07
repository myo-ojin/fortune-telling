"""
Routes for the Fortune Telling application.
"""
from flask import Blueprint

# Create a blueprint for main routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    Home page - Hello World for now.
    Will be replaced with the input form in T008.
    """
    html = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Multi-Method Fortune Telling System</title>
        <style>
            body {
                font-family: 'Hiragino Sans', 'Meiryo', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .container {
                text-align: center;
                background: white;
                padding: 3rem;
                border-radius: 20px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            }
            h1 {
                color: #667eea;
                margin-bottom: 1rem;
            }
            p {
                color: #666;
                font-size: 1.1rem;
            }
            .status {
                margin-top: 2rem;
                padding: 1rem;
                background: #f0f0f0;
                border-radius: 10px;
            }
            .check {
                color: #4CAF50;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Multi-Method Fortune Telling System</h1>
            <p>複数占い手法統合システム</p>
            <div class="status">
                <p class="check">Flask Application Running Successfully!</p>
                <p>Phase 1a: MVP Core in progress...</p>
                <p>Current Task: T003 Complete</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

@main_bp.route('/health')
def health():
    """
    Health check endpoint.
    """
    return {'status': 'ok', 'message': 'Fortune Telling System is running'}
