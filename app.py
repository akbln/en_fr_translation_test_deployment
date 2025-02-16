from flask import Flask, request, render_template

from TranslationModel import TranslationModel

app = Flask(__name__)

model = TranslationModel(model_path="./Model/en_fr.keras",
                         eng_tokenizer_path="./Model/en_tokenizer.json",
                         fr_tokenizer_path="./Model/fr_tokenizer.json",
                         max_fr_length=21,
                         max_eng_length=15
                         )
@app.route('/',methods=["GET"])
def main_route():
    return render_template("index.html")

@app.route('/translate',methods=["POST"])
def translate():
    if request.content_type != "application/json":
        return {"error":"Invalid Content-Type"}, 400

    json_data = request.get_json()
    english_sentence = json_data.get("sentence")
    return {"translation": model.translate_sentence(english_sentence) }, 200


if __name__ == '__main__':
    app.run()
