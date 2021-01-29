"""

"""
import os
import re

import matplotlib.pyplot as plt
import networkx as nx

from ethica_model.data import load_text


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
        current_id = 0
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
                parsed_part = TextElement.analyse(text, ic + 1, current_id)
                current_id += 1
                set_couples.add((previous_parsed_part.__class__.__name__,
                                 parsed_part.__class__.__name__,))
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

                parsed_parts.append(parsed_part)
                previous_parsed_part = parsed_part
        self.parts = parsed_parts
        # print("\n".join([str(part) for part in self.parts]))
        # print([previous for previous, current in set_couples if current == "Scholium"])


# region text elements
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

    def __str__(self):
        return f"{self.chapter}-{self.id} {self.__class__.__name__}"

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
        return super(Demonstratio, self).__repr__() + f" {self.associated_proposition}"


class Aliter(TextElement):
    pattern = r"^ALITER"

    def __init__(self, chapter, _id):
        super().__init__(chapter, _id)
        self.associated_demonstration = None

    def __repr__(self):
        return super(Aliter, self).__repr__() + f" {self.associated_demonstration}"


class Corollarium(TextElement):
    pattern = r"COROLLARIUM"

    def __init__(self, chapter, _id):
        super().__init__(chapter, _id)
        self.associated_proposition = None

    def __repr__(self):
        return super(Corollarium, self).__repr__() + f" {self.associated_proposition}"


class Scholium(TextElement):
    pattern = r"(^SCHOLIUM [IVXL]*\.?(:| :) )|(^SCHOLIUM: )"

    def __init__(self, chapter, _id):
        super().__init__(chapter, _id)
        self.associated_proposition = None

    def __repr__(self):
        return super(Scholium, self).__repr__() + f" {self.associated_proposition}"


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
# endregion


class Chapter:
    def __init__(self, i_chapter):
        self.parts = []
        self.definitions = []
        self.axioms = []
        self.propositions = []
        self.prefaces = []
        self.lemmata = []
        self.caputs = []
        self.demonstrations = []
        self.i_chapter = i_chapter

    def add_definition(self, definition: Definitio):
        self.definitions.append(definition)

    def add_axiom(self, axiom: Axioma):
        self.axioms.append(axiom)

    def add_proposition(self, proposition: Propositio):
        self.propositions.append(proposition)

    def add_preface(self, preface: Praefatio):
        self.prefaces.append(preface)

    def add_lemma(self, lemma: Lemma):
        self.lemmata.append(lemma)

    def add_demonstration(self, demonstratio: Demonstratio):
        self.demonstrations.append(demonstratio)

    def add_caput(self, caput: Caput):
        self.caputs.append(caput)

    def add_demonstratio(self, demonstratio: Demonstratio):
        self.demonstrations.append(demonstratio)

    def add_part(self, part: TextElement):
        self.parts.append(part)
        if isinstance(part, Lemma):
            self.add_lemma(part)
        elif isinstance(part, Caput):
            self.add_caput(part)
        elif isinstance(part, Praefatio):
            self.add_preface(part)
        elif isinstance(part, Definitio):
            self.add_definition(part)
        elif isinstance(part, Propositio):
            self.add_proposition(part)
        elif isinstance(part, Demonstratio):
            self.add_demonstration(part)

    def analyse(self):
        current_proposition = None
        for part in self.parts:
            if isinstance(part, Propositio):
                current_proposition = part
            elif isinstance(part, Demonstratio) or \
                    isinstance(part, Aliter) or \
                    isinstance(part, Scholium) or \
                    isinstance(part, Corollarium):
                part.associated_proposition = current_proposition
            else:
                current_proposition = None

    def __len__(self):
        return len(self.parts)

    @property
    def nodes(self):
        nodes = []
        current_definition = None
        current_lemma = None
        current_caput = None
        current_preface = None
        current_titulus = None
        current_proposition = None
        current_axiom = None
        current_appendix = None
        current_explicatio = None
        current_finis = None

        for part in self.parts:
            if isinstance(part, Propositio):
                current_proposition = part
                nodes.append((str(self), str(part)))
            # elif isinstance(part, Demonstratio) or \
            #         isinstance(part, Aliter) or \
            #         isinstance(part, Scholium) or \
            #         isinstance(part, Corollarium):
            #     nodes.append((str(current_proposition), str(part)))
            #     part.associated_proposition = current_proposition
            # else:
            #     current_proposition = None

            if isinstance(part, Definitio) and not current_definition:
                nodes.append((str(self), str(part)))
            elif isinstance(part, Definitio):
                nodes.append((str(current_definition), str(part)))
            else:
                current_definition = None

            if isinstance(part, Lemma) and not current_lemma:
                nodes.append((str(self), str(part)))
            elif isinstance(part, Lemma):
                nodes.append((str(current_lemma), str(part)))
            else:
                current_lemma = None

            if isinstance(part, Caput) and not current_caput:
                nodes.append((str(self), str(part)))
            elif isinstance(part, Caput):
                nodes.append((str(current_caput), str(part)))
            else:
                current_caput = None

            if isinstance(part, Praefatio) and not current_preface:
                nodes.append((str(self), str(part)))
            elif isinstance(part, Praefatio):
                nodes.append((str(current_preface), str(part)))
            else:
                current_preface = None

            if isinstance(part, Titulus) and not current_titulus:
                nodes.append((str(self), str(part)))
            elif isinstance(part, Titulus):
                nodes.append((str(current_titulus), part))
            else:
                current_titulus = None

            if isinstance(part, Axioma) and not current_axiom:
                nodes.append((str(self), str(part)))
            elif isinstance(part, Axioma):
                nodes.append((str(current_axiom), str(part)))
            else:
                current_axiom = None

            if isinstance(part, Appendix) and not current_appendix:
                nodes.append((str(self), str(part)))
            elif isinstance(part, Appendix):
                nodes.append((str(current_appendix), str(part)))
            else:
                current_appendix = None

            if isinstance(part, Explicatio) and not current_explicatio:
                nodes.append((str(self), str(part)))
            elif isinstance(part, Explicatio):
                nodes.append((str(current_explicatio), str(part)))
            else:
                current_explicatio = None

            if isinstance(part, Finis) and not current_finis:
                nodes.append((str(self), str(part)))
            elif isinstance(part, Finis):
                nodes.append((str(current_finis), str(part)))
            else:
                current_finis = None
        return nodes

    def __str__(self):
        return f"chapter {self.i_chapter+1}"


class Book:
    def __init__(self):
        self.chapters = []

    def add_chapter(self, chapter: Chapter):
        self.chapters.append(chapter)

    def set_text(self, text: Text):
        """
        >>> book = Book()
        >>> book.set_text(Text())

        :param text:
        :return:
        """
        text.analyse()
        i = 0
        self.chapters = [Chapter(i)]
        for part in text.parts:
            if i + 1 == part.chapter:
                self.chapters[i].add_part(part)
            else:
                i += 1
                self.chapters.append(Chapter(i))

    def analyse(self):
        """
        >>> book = Book()
        >>> book.set_text(Text())
        >>> book.analyse()
        >>> book.chapters

        :return:
        """
        for chapter in self.chapters:
            if chapter:
                chapter.analyse()

    @property
    def nodes(self):
        """
        >>> book = Book()
        >>> book.set_text(Text())
        >>> book.tree

        :return:
        """
        nodes = []
        for chapter in self.chapters:
            nodes.append(chapter)
        return nodes

    @property
    def tree(self):
        graph = nx.Graph()
        for node in self.nodes:
            graph.add_edge("book", str(node))
            print(len(node))
            for u, v in node.nodes:
                graph.add_edge(u, v)
        return graph

    def save(self):
        nx.draw(self.tree, node_color="gray", node_size=10, width=1,
                edge_color="gray", with_labels=True, font_size=3)
        plt.draw()

        if not os.path.exists("tree"):
            os.mkdir("tree")
        plt.savefig(os.path.join("tree", "tree.png"), dpi=1000)
        plt.savefig(os.path.join("tree", "tree.pdf"))
        plt.clf()


if __name__ == "__main__":
    b = Book()
    b.set_text(Text())
    b.save()
