from googletrans import Translator
from googletrans import LANGUAGES, LANGCODES
from enum import Enum
from pathlib import Path
import json


class Extension(Enum):
    JSON = ".json"
    TXT = ".txt"

    def __eq__(self, other):
        return other.lower() == self.value.lower()


class SpanishTranslator:
    def __init__(self):
        self.translator = Translator()
        self.lang_code = LANGCODES["spanish"]

    def translate(self, phrase):
        return self.translator.translate(phrase, dest=self.lang_code).text

    def read_file(self, file):
        path = Path(file)
        if not path.exists():
            raise FileNotFoundError()
        file_extension = path.suffix
        if file_extension == Extension.TXT:
            with open(path) as file:
                output = file.read()
        elif file_extension == Extension.JSON:
            with open(path) as file:
                content = json.load(file)
            output = content["text"]
        else:
            raise ValueError(f"File Extension {file_extension} not supported!")
        return self.translate(output)


def main():
    translator = SpanishTranslator()
    translation = translator.read_file("data/sentence.txt")
    print(translation)


if __name__ == "__main__":
    main()
