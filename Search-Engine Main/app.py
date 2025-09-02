from flask import Flask, render_template, request
from duckduckgo_search import DDGS

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    q = request.args.get("q", "").strip()
    results, error = [], None
    if q:
        try:
            with DDGS() as ddgs:
                for r in ddgs.text(q, max_results=10):
                    results.append({"title": r.get("title","(no title)"), "url": r.get("href","")})
        except Exception as e:
            error = str(e)
    return render_template("index.html", query=q, results=results, error=error)

if __name__ == "__main__":
    app.run(debug=True)


