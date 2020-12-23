"""

"""

import re

from data import load_text


class Text:
    def __init__(self):
        self.text = []
        self.parts = []

    def load(self):
        chapters = load_text()
        self.text = " ".join(chapters)
        parts = []
        previous_new_line = False
        for ic, chapter in enumerate(chapters):
            parts.append([[]])
            i = 0
            for line in chapter.split("\n"):
                stripped_line = line.strip()
                if len(stripped_line) == 0:
                    previous_new_line = True
                else:
                    if previous_new_line:
                        parts[ic].append([])
                        i += 1
                    parts[ic][i].append(stripped_line)
        return parts

    def analyse(self):
        parts = []
        in_definition = False
        in_axiom = False
        for ic, chapter in enumerate(self.load()):
            for part in chapter:
                text = " ".join(part)
                parsed_part = Part.analyse(text, ic)
                if parsed_part.__class__.__name__ != Part.__name__:
                    in_definition = False
                    in_axiom = False
                if in_definition:
                    print("definitio")
                    parsed_part = Definitio(parsed_part.chapter)
                    parsed_part.parse(text)
                elif in_axiom:
                    print("axiom")
                    parsed_part = Axiom(parsed_part.chapter)
                    parsed_part.parse(text)
                else:
                    print("")
                if parsed_part.opening_definitions:
                    in_definition = True
                if parsed_part.opening_axioms:
                    in_axiom = True

                parts.append(parsed_part)
        self.parts = parts


class Part:
    def __init__(self, chapter):
        self.text = ""
        self.opening_definitions = False
        self.opening_axioms = False
        self.chapter = chapter

    @staticmethod
    def analyse(text: str, chapter: int):
        print(text)
        if re.match(Definitio.pattern, text):
            print("definitio")
            part = Demonstratio(chapter)
            part.parse(text)
        elif re.match(Explicatio.pattern, text):
            print("explicatio")
            part = Explicatio(chapter)
            part.parse(text)
        # elif re.match(Axiom.pattern, text):
        #     part = Axiom()
        #     part.parse(text)
        elif re.match(Propositio.pattern, text):
            print("propositio")
            part = Propositio(chapter)
            part.parse(text)
        elif re.match(Corollarium.pattern, text):
            print("corollarium")
            part = Corollarium(chapter)
            part.parse(text)
        elif re.match(Demonstratio.pattern, text):
            print("demonstratio")
            part = Demonstratio(chapter)
            part.parse(text)
        elif re.match(Scholium.pattern, text):
            print("scholium")
            part = Scholium(chapter)
            part.parse(text)
        elif re.match(Caput.pattern, text):
            print("caput")
            part = Caput(chapter)
            part.parse(text)
        elif re.match(Appendix.pattern, text):
            print("appendix")
            part = Appendix(chapter)
            part.parse(text)
        else:
            print("part")
            part = Part(chapter)
            part.text = text
            if re.match(r"^DEFINITIONES", text):
                print("définitions")
                part.opening_definitions = True
            elif re.match(r"^AXIOMATA", text):
                part.opening_axioms = True
        return part


class Definitio(Part):
    pattern = r"^[IVXL]*\."

    def parse(self, text: str):
        self.text = text


class Explicatio(Part):
    pattern = "^EXPLICATIO(:| :) "

    def __init__(self, chapter):
        super().__init__(chapter)
        self.parent = ""

    def parse(self, text: str):
        self.text = text


class Axiom(Part):
    pattern = ""

    def parse(self, text: str):
        self.text = text


class Propositio(Part):
    pattern = r"^PROPOSITIO [IVXL]*\.?(:| :) "

    def parse(self, text: str):
        self.text = text


class Demonstratio(Part):
    pattern = r"^DEMONSTRATIO(:| :) "

    def parse(self, text: str):
        self.text = text


class Corollarium(Propositio):
    pattern = r"COROLLARIUM(:| :) "

    def parse(self, text: str):
        self.text = text


class Scholium(Part):
    pattern = r"(^SCHOLIUM [IVXL]*\.?(:| :) )|(^SCHOLIUM: )"

    def parse(self, text: str):
        self.text = text


class Appendix(Part):
    pattern = r"APPENDIX [IVXL]*"

    def parse(self, text: str):
        self.text = text


class Caput(Part):
    pattern = r"CAPUT [IVXL]*"

    def parse(self, text: str):
        self.text = text
