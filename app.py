import json

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    with open('entities.json', encoding="utf-8") as f:
        entities = json.load(f)
        return render_template("main-all-items.html", entities=entities)


@app.route('/paging')
def paging():
    max_items = 3 # Number of elements per page
    page = int(request.args.get('p', 1))
    with open('entities.json', encoding="utf-8") as f:
        entities = json.load(f)
    total_items = len(entities)
    last_page = total_items // max_items
    items_show = entities[(page-1)*max_items:page*max_items]

    return render_template("main.html", entities=items_show, total_items=total_items, page=page, last_page=last_page)


@app.route('/search')
def search():
    model = request.args.get('model')
    with open('entities.json', encoding="utf-8") as f:
        entities = json.load(f)
        response = []
        if not model:
            response = entities
        else:
            for e in entities:
                if e["model"] == model:
                    response.append(e)
        return render_template("search_ause.html", entities=response)


@app.route('/card/<int:eid>')
def card(eid: int):
    with open('entities.json', encoding="utf-8") as f:
        entities = json.load(f)
        for ent in entities:
            if ent["id"] == eid:
                return render_template("card_full.html", entity=ent)


@app.route('/card/<int:eid>/short')
def card_short(eid: int):
    with open('entities.json', encoding="utf-8") as f:
        entities = json.load(f)
        for ent in entities:
            if ent["id"] == eid:
                return render_template("card_short.html", entity=ent)


if __name__ == '__main__':
    app.run(debug=True)
