import spacy
from typing import Any
from models.ModelInterface import ModelInterface
from nltk.corpus import stopwords
import torch


class ModelSpacy(ModelInterface):

    def __init__(self):
        if torch.cuda.is_available():
            spacy.require_gpu()
        ModelSpacy.nlp = spacy.load('en_core_web_lg')
        ModelSpacy.nlp.add_pipe('merge_entities', last=True)
        ModelSpacy.stop_words = set(stopwords.words('english'))

    @staticmethod
    def get_spacy_instance(text):
        return ModelSpacy.nlp(text)

    @staticmethod
    def predict(input: str) -> Any:
        return ModelSpacy.get_spacy_instance(input)

    @staticmethod
    def get_amount_of_sentences(text):
        return len(list(ModelSpacy.predict(text).sents))

    @staticmethod
    def get_sentences(text):
        sentences = list(ModelSpacy.predict(text).sents)
        result = [sent.text for sent in sentences]
        return result

    @staticmethod
    def get_part_of_speech_dictionary(text):
        dictionary = dict()
        for token in ModelSpacy.predict(text):
            dictionary[str(token)] = token.pos_
        return dictionary

    @staticmethod
    def get_noun_chunk_and_entity_type_array(text):
        dictionary = dict()
        for chunk in ModelSpacy.predict(text).noun_chunks:
            if chunk.text not in ModelSpacy.stop_words:
                dictionary[chunk.text] = chunk.root.ent_type_
        array = list(dictionary.items())
        return array
