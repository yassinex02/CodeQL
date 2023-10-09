from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    name = request.args.get('name', 'World')
    # Vulnerable to XSS
    return render_template_string(f'Hello, {name}!')


if __name__ == "__main__":
    app.run(debug=False)
