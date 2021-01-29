

from ethica_model.model import Text


def script():
    text = Text()
    res = text.load()
    # print(res)
    text.analyse()
    # print(text.parts)


if __name__ == "__main__":
    script()
