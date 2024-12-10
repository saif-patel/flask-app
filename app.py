from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template with buttons for interaction
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Best Player Finder</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        button {
            padding: 10px 20px;
            margin: 10px;
            font-size: 16px;
            cursor: pointer;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
        }
        button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 20px;
            font-size: 20px;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Who is the Best Player?</h1>
    <form method="POST">
        <button name="player" value="nami">Who is the Best Nami Player?</button>
        <button name="player" value="alistar">Who is the Best Alistar Player?</button>
    </form>
    {% if result %}
    <div class="result">{{ result }}</div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def best_player():
    result = None
    if request.method == 'POST':
        player = request.form.get('player')
        if player == 'nami':
            result = "Saif is the Best Nami Player!"
        elif player == 'alistar':
            result = "Saif is the Best Alistar Player!"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
