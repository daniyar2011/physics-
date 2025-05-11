from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Solve', methods=["GET", "POST"])
def Solve():
    result = None
    if request.method == 'POST':
        formula = request.form['formula']
        try:
            if formula == 'F = m * a':
                m = float(request.form['massa'])
                g = float(request.form['uskorenie'])
                result = f"Сила F = {m * g:.2f} Н"
            elif formula == 'a = F / m':
                F = float(request.form['sila'])
                m = float(request.form['massa'])
                result = f"Ускорение a = {F / m:.2f} м/с²"
            elif formula == 'm = F / g':
                F = float(request.form['sila'])
                g = float(request.form['uskorenie'])
                result = f"Масса m = {F / g:.2f} кг"
            elif formula == 'E = 0.5 * m * v^2':
                m = float(request.form['massa'])
                v = float(request.form['skorost'])
                result = f"Кинетическая энергия E = {0.5 * m * v ** 2:.2f} Дж"
        except ValueError:
            result = "Ошибка: введите числовые значения!"

    return render_template("Solve.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
