"""

"""

import re

from data import load_text


current_id = 0


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
        global current_id
        parsed_parts = []

        in_appendix = False
        in_axiom = False
        in_definition = False
        in_postulata = False
        in_praefatio = False
        in_proposition_id = None
        in_scholium = False

        previous_parsed_part = None
        set_couples = set()
        for ic, chapter in enumerate(self.load()):
            for part in chapter:
                text = " ".join(part)
                parsed_part = TextElement.analyse(text, ic, current_id)
                current_id += 1
                set_couples.add((previous_parsed_part.__class__.__name__,
                                 parsed_part.__class__.__name__, ))
                # if isinstance(parsed_part, Scholium):
                #     print("scholium previous "+previous_parsed_part.__class__.__name__)
                if parsed_part.__class__.__name__ != TextElement.__name__:
                    in_axiom = False
                    in_praefatio = False
                    in_appendix = False
                    in_postulata = False
                    in_scholium = False

                if parsed_part.__class__.__name__ not in [TextElement.__name__,
                                                          Explicatio.__name__]:
                    in_definition = False

                if parsed_part.__class__.__name__ not in [Scholium.__name__,
                                                          Corollarium.__name__,
                                                          Demonstratio.__name__]:
                    in_proposition_id = None
                if in_definition:
                    # print("definitio")
                    parsed_part = Definitio(parsed_part.chapter, parsed_part.id)
                    parsed_part.parse(text)
                elif in_proposition_id:
                    # print("in proposition")
                    parsed_part.associated_proposition = in_proposition_id
                elif in_axiom:
                    # print("axiom")
                    parsed_part = Axioma(parsed_part.chapter, parsed_part.id)
                    parsed_part.parse(text)
                elif in_praefatio:
                    parsed_part = Praefatio(parsed_part.chapter, parsed_part.id)
                    parsed_part.parse(text)
                elif in_appendix:
                    parsed_part = Appendix(parsed_part.chapter, parsed_part.id)
                    parsed_part.parse(text)
                elif in_postulata:
                    parsed_part = Postula(parsed_part.chapter, parsed_part.id)
                    parsed_part.parse(text)
                elif in_scholium and not isinstance(parsed_part, Scholium):
                    parsed_part = Scholium(parsed_part.chapter, previous_parsed_part.id)
                    parsed_part.parse(text)
                else:
                    # print("")
                    pass
                if parsed_part.opening_definitions:
                    in_definition = True
                if parsed_part.opening_axioms:
                    in_axiom = True
                if parsed_part.opening_praefatio:
                    in_praefatio = True
                if parsed_part.opening_appendix:
                    in_appendix = True
                if parsed_part.opening_postulata:
                    in_postulata = True
                if isinstance(parsed_part, Scholium):
                    in_scholium = True
                if isinstance(parsed_part, Propositio):
                    in_proposition_id = parsed_part.id

                print(parsed_part)

                parsed_parts.append(parsed_part)
                previous_parsed_part = parsed_part
        self.parts = parsed_parts
        # print([previous for previous, current in set_couples if current == "Scholium"])


class TextElement:
    def __init__(self, chapter, _id):
        self.text = ""
        self.chapter = chapter
        self.id = _id

        self.opening_appendix = False
        self.opening_axioms = False
        self.opening_definitions = False
        self.opening_postulata = False
        self.opening_praefatio = False

    def parse(self, text: str):
        self.text = text

    @staticmethod
    def analyse(text: str, chapter: int, _id: int):
        if re.match(Definitio.pattern, text):
            # print("definitio")
            part = Definitio(chapter, _id)
            part.parse(text)
        elif re.match(Explicatio.pattern, text):
            # print("explicatio")
            part = Explicatio(chapter, _id)
            part.parse(text)
        elif re.match(Propositio.pattern, text):
            # print("propositio")
            part = Propositio(chapter, _id)
            part.parse(text)
        elif re.match(Corollarium.pattern, text):
            # print("corollarium")
            part = Corollarium(chapter, _id)
            part.parse(text)
        elif re.match(Demonstratio.pattern, text):
            # print("demonstratio")
            part = Demonstratio(chapter, _id)
            part.parse(text)
        elif re.match(Scholium.pattern, text):
            # print("scholium")
            part = Scholium(chapter, _id)
            part.parse(text)
        elif re.match(Caput.pattern, text):
            # print("caput")
            part = Caput(chapter, _id)
            part.parse(text)
        elif re.match(Appendix.pattern_opening, text):
            # print("appendix")
            part = Appendix(chapter, _id)
            part.parse(text)
        elif re.match(Aliter.pattern, text):
            # print("aliter")
            part = Aliter(chapter, _id)
            part.parse(text)
        elif re.match(Axioma.pattern, text):
            # print("axioma")
            part = Axioma(chapter, _id)
            part.parse(text)
        elif re.match(Lemma.pattern, text):
            # print("lemma")
            part = Lemma(chapter, _id)
            part.parse(text)
        elif re.match(Definitio.pattern, text):
            # print("BIZARRE")
            part = Definitio(chapter, _id)
            part.parse(text)
        elif re.match(Finis.pattern, text):
            part = Finis(chapter, _id)
            part.parse(text)
        elif re.match(Titulus.pattern, text):
            # print("titulus")
            part = Titulus(chapter, _id)
            part.parse(text)
            if re.match(Definitio.pattern_opening, text):
                # print("définitions")
                part.opening_definitions = True
            elif re.match(Axioma.pattern_opening, text):
                part.opening_axioms = True
            elif re.match(Postula.pattern_opening, text):
                part.opening_postulata = True
            elif re.match(Praefatio.pattern_opening, text):
                # print("PRAEFITO")
                part.opening_praefatio = True
            elif re.match(Appendix.pattern_opening, text):
                part.opening_appendix = True
        else:
            # print("part")
            part = TextElement(chapter, _id)
            part.text = text
        return part

    def __repr__(self):
        return f"{self.chapter}-{self.id} {self.__class__.__name__} {self.text}"


class Definitio(TextElement):
    pattern = r"^DEFINITIO( |:)"
    pattern_opening = r"^(DEFINITIONES|AFFECTUUM DEFINITIONES|AFFECTUUM GENERALIS DEFINITIO)$"


class Explicatio(TextElement):
    pattern = "^EXPLICATIO(:| :) "

    def __init__(self, chapter, _id):
        super().__init__(chapter, _id)
        self.parent = ""


class Axioma(TextElement):
    pattern = r"^(AXIOMA:|AXIOMA )"
    pattern_opening = r"^AXIOMATA$"


class Propositio(TextElement):
    pattern = r"^PROPOSITIO [IVXL]*\.?(:| :) "


class Demonstratio(TextElement):
    pattern = r"^DEMONSTRATIO(:| :) "

    def __init__(self, chapter, _id):
        super().__init__(chapter, _id)
        self.associated_proposition = None

    def parse(self, text: str):
        super().parse(text)

    def __repr__(self):
        return super(Demonstratio, self).__repr__()+f" {self.associated_proposition}"


class Aliter(TextElement):
    pattern = r"^ALITER"

    def __init__(self, chapter, _id):
        super().__init__(chapter, _id)
        self.associated_demonstration = None

    def __repr__(self):
        return super(Aliter, self).__repr__()+f" {self.associated_demonstration}"


class Corollarium(TextElement):
    pattern = r"COROLLARIUM"

    def __init__(self, chapter, _id):
        super().__init__(chapter, _id)
        self.associated_proposition = None

    def __repr__(self):
        return super(Corollarium, self).__repr__()+f" {self.associated_proposition}"


class Scholium(TextElement):
    pattern = r"(^SCHOLIUM [IVXL]*\.?(:| :) )|(^SCHOLIUM: )"

    def __init__(self, chapter, _id):
        super().__init__(chapter, _id)
        self.associated_proposition = None

    def __repr__(self):
        return super(Scholium, self).__repr__()+f" {self.associated_proposition}"


class Appendix(TextElement):
    pattern_opening = r"^APPENDIX"


class Caput(TextElement):
    pattern = r"CAPUT [IVXL]*"


class Lemma(TextElement):
    pattern = r"^LEMMA"


class Postula(TextElement):
    pattern_opening = r"^POSTULATA$"


class Praefatio(TextElement):
    pattern_opening = r"^PRÆFATIO"


class Titulus(TextElement):
    pattern = r"^[A-ZÆ ]*$"


class Finis(TextElement):
    pattern = r"^Finis"
