from flask import Flask, render_template, request
from waifu import get_current_waifu
from waitress import serve


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/waifu')
def get_waifu():
    waifu = request.args.get('waifu')
    waifu_type = get_current_waifu(waifu)

    
    return render_template (
        "waifu.html",
        title = waifu_type["url"],
        waifu_img= waifu_type["url"]
    )

if __name__ == "__main__":
    serve(app,host="0.0.0.0", port=10006)