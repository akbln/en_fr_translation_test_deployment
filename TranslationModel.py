import numpy as np
import json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.saving import load_model

class TranslationModel:
    def __init__(self, model_path, eng_tokenizer_path, fr_tokenizer_path, max_eng_length, max_fr_length):
        self.model_path = model_path
        self.eng_tokenizer_path = eng_tokenizer_path
        self.fr_tokenizer_path = fr_tokenizer_path
        self.max_eng_length = max_eng_length
        self.max_fr_length = max_fr_length
        self.model = None
        self.eng_tokenizer = None
        self.fr_tokenizer = None

        # Load the model and tokenizers
        self.load_model()
        self.load_tokenizers()

    def load_model(self):
        self.model = load_model(self.model_path)


    def load_tokenizers(self):

        with open(self.eng_tokenizer_path, "r") as file:
            self.eng_tokenizer = tokenizer_from_json(json.load(file))
        with open(self.fr_tokenizer_path, "r") as file:
            self.fr_tokenizer = tokenizer_from_json(json.load(file))
        print("Tokenizers loaded successfully.")


    def translate_sentence(self, eng_sentence):
        if not self.model or not self.eng_tokenizer or not self.fr_tokenizer:
            return "Model or tokenizers not loaded."

        eng_sequence = self.eng_tokenizer.texts_to_sequences([eng_sentence])
        eng_sequence = pad_sequences(eng_sequence, maxlen=self.max_eng_length, padding='post')

        # Generate predictions
        predictions = self.model.predict(eng_sequence)

        # Convert predictions to French words
        fr_sentence = []
        for time_step in predictions[0]:
            word_index = np.argmax(time_step)
            if word_index == 0:  # Stop at the padding or end token
                break
            word = self.fr_tokenizer.index_word.get(word_index, '')
            if word:
                fr_sentence.append(word)

        return ' '.join(fr_sentence)
