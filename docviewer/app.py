import documentcloud
from flask import abort, Flask, request, render_template

app = Flask(__name__)
DEFAULT_SEARCH = "group:homicide-watch"

@app.route('/')
def index():
    """
    Get the latest documents
    """
    page = request.args.get('page', 1)
    documents = documentcloud.search(DEFAULT_SEARCH, page=page)
    return render_template('index.html', documents=documents)

@app.route('/<document_id>')
def document(document_id):
    """
    Just pass the id along to the template and let DocumentCloud
    do the rest
    """
    return render_template('document.html', document_id=document_id)

if __name__ == "__main__":
    app.run(debug=True)