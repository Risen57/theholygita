from flask import Flask, render_template, request, redirect, url_for
from sl import get_shloka

app = Flask(__name__)  # Creates flask app


@app.route("/", methods=["GET", "POST"])
def home():
    # Home screen page
    if request.method == 'POST':
        ch = int(request.form['ch'])
        shlok = int(request.form['shlok'])
        return redirect(url_for('shlok', ch=ch, shlok=shlok))

    return render_template("index.html")


@app.route("/shlok", methods=["GET", "POST"])
def shlok():
    # Shlok page
    ch = request.form.get('ch')
    shlok = request.form.get('shlok')

    shloka = get_shloka(ch, shlok)

    return render_template("shlok.html", shloka=shloka)

# if __name__ == "__main__":
#     app.run(debug=True)
