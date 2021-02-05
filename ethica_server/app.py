"""

"""

from flask import jsonify

from ethica_model import data
from ethica_model import model
from ethica_server import create_app, ethica

app = create_app()


@ethica.route("/load/raw-text")
def load_raw_text():
    chapters = data.load_text()
    res_chapters = []
    for i, chapter in enumerate(chapters):
        res_chapters.append({"id": i, "content": chapter})
    return jsonify({"content": res_chapters})


@ethica.route("/load/text")
def load_text():
    text = model.Text()
    text.analyse()
    entities = text.parts
    chapters = [[entity for entity in entities if entity.chapter == i] for i in range(1, 6)]
    res_chapters = []
    for i, chapter in enumerate(chapters):
        res_chapter = []
        # print(type(chapter))
        for j, entity in enumerate(chapter):
            res_chapter.append({"id": j, "content": entity.text, "entityType": entity.__class__.__name__})
            # print(entity)
        res_chapters.append({"id": i, "content": res_chapter})
    return jsonify({"content": res_chapters})


if __name__ == "__main__":
    app.register_blueprint(ethica, url_prefix="/ethica")
    app.run(debug=True, port=5010)
