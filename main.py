from manim import *
from typing import NewType

RADIO = 1
Vertical = NewType('Vertical', bool)
Horizontal = NewType('Horizontal', bool)
VERTICAL: Vertical = Vertical(True)
HORIZONTAL: Horizontal = Horizontal(False)


def fo_all(self):
    self.play(*[FadeOut(mob) for mob in self.mobjects])


def generate_rectangles(number: int, sentido: Vertical | Horizontal = HORIZONTAL) -> VGroup:
    val1 = 1/number
    val2 = lambda r: TAU * (r/number)
    horizontal = sentido == HORIZONTAL

    rectangles = [
        Rectangle(width=val1 if horizontal else val2(r), height=val2(r) if horizontal else val1)
        .set_stroke(RED, 1.5)
        .shift(DOWN * 3)
        .shift(LEFT * (2 if horizontal else 0))
        for r in list(range(0, RADIO * number + 1))
    ]

    if not horizontal:
        for j in range(1, len(rectangles)):
            rectangles[j].next_to(rectangles[j - 1], DOWN, 0)

    rectangles = VGroup(*rectangles)

    if horizontal:
        rectangles.arrange(RIGHT, center=False, aligned_edge=DOWN, buff=0)
    else:
        rectangles.arrange(DOWN, center=True, buff=0)

    if not horizontal:
        for j in range(0, len(rectangles)):
            rectangles[j].shift(DOWN * 0.5)

    return rectangles


class AreaCirculo(Scene):

    def parte1(self):
        self: Scene

        circulo = Circle(RADIO)
        circulo = circulo.set_stroke(circulo.color, 1.5)
        linea = Line([0, 0, 0], [RADIO, 0, 0])
        ra = MathTex("r").shift(RIGHT * 0.5).shift(UP * 0.5)
        f_out = lambda r: [FadeOut(e) for e in r]
        f_in = lambda r: [FadeIn(e) for e in r]
        cir = lambda number:  [Circle(radius=r/number).set_stroke(circulo.color, 1.5).shift(UP * 2) for r in list(range(1, RADIO * number, 1))]

        self.play(Create(circulo))
        self.wait(0.2)

        self.play(circulo.animate.set_fill(circulo.color, 1.5), Write(ra), Create(linea))

        circles1 = [Circle(radius=r * 0.1).set_stroke(circulo.color, 1.5) for r in list(range(1, RADIO * 10, 1))]
        self.play(circulo.animate.set_fill(circulo.color, 0), FadeOut(ra), FadeOut(linea))
        self.play(*f_in(circles1))

        rectangles = generate_rectangles(10, VERTICAL)
        t_circle = [circle.animate.shift(UP * 2) for circle in circles1]
        self.play(circulo.animate.shift(UP * 2), *t_circle)

        c_transform = [TransformFromCopy(circles1[j], rectangles[j]) for j in range(len(circles1))]
        self.play(TransformFromCopy(circulo, rectangles[len(rectangles) - 1]), *c_transform)

        for val in [15, 20, 40, 60]:
            circles_new = cir(val)
            rectangles_new = generate_rectangles(val, VERTICAL)
            self.play(Transform(rectangles, rectangles_new), *f_in(circles_new))
            self.wait(0.2)

        puntos = [[-TAU * RADIO / 2, 0, 0], [0, RADIO, 0], [TAU * RADIO / 2, 0, 0]]
        triangulo = Polygon(*puntos, color=circulo.color).set_fill(circulo.color, 1.5).shift(DOWN)
        self.play(FadeIn(triangulo), circulo.animate.set_fill(circulo.color, 1.0), *f_out(rectangles))
        self.wait(0.5)

        puntos = [[-TAU * RADIO / 2, 0, 0], [-TAU * RADIO / 2, RADIO, 0], [TAU * RADIO / 2, 0, 0]]
        triangulo2 = Polygon(*puntos, color=circulo.color).set_fill(circulo.color, 1.5).shift(DOWN)
        radio = MathTex(r"r").shift(RIGHT * (- 0.5 - TAU * RADIO / 2)).shift(DOWN / 2)
        base = MathTex(r"2 \pi r").shift(DOWN - 0.5)
        self.play(Transform(triangulo, triangulo2), Write(radio), Write(base))
        self.wait(1)

        fo_all(self)

    def parte2(self):
        texto1 = Tex(r"b := $2 \pi r$")
        texto2 = Tex(r"a := $r$      ")

        texto1.next_to(texto2, UP, 0.5)

        self.play(Write(texto1), Write(texto2))

        self.wait(0.5)

        fo_all(self)

        texto1 = Tex(r"$\frac{b \times h}{2}$")
        texto2 = Tex(r"$\frac{2 \pi r \times r}{2}$")
        texto3 = Tex(r"$\pi r \times r$")
        texto4 = Tex(r"$\pi r^2$")
        self.play(Write(texto1))
        self.wait(1)

        for t in [texto2, texto3, texto4]:
            self.play(Transform(texto1, t, run_time=0.2))
            self.wait(2)

        fo_all(self)

    def parte3(self):
        xax = Line([-3, 0, 0], [3, 0, 0]).shift(DOWN * 3)
        yax = Line([0, -3, 0], [0, 4, 0]).shift(LEFT * 2).shift(DOWN * 0.5)
        line = Line([0, 0, 0], [1, TAU, 0]).set_color(RED).shift(DOWN * 3).shift(LEFT * 2).set_stroke(RED, 1.5)
        eq = MathTex(r"p(r) = 2\pi r").shift(DOWN * 3.5).shift(RIGHT * 2)

        self.play(Create(line), Create(xax), Create(yax))
        self.add_foreground_mobjects(xax, yax)
        self.play(Write(eq))

        rectangles = generate_rectangles(2)
        for rect in rectangles:
            self.play(FadeIn(rect))
        self.wait(0.5)

        for rect_size in [4, 5, 6, 8, 10, 20, 40, 60]:
            rectangles_new = generate_rectangles(rect_size)
            self.play(Transform(rectangles, rectangles_new))

        filled_triangle_points2 = [[0, 0, 0], [1, 0, 0], [1, TAU, 0]]

        filled_triangle2 = Polygon(*filled_triangle_points2, color=RED).set_fill(RED, 1.5).shift(DOWN * 3).shift(LEFT * 2)

        self.play(FadeIn(filled_triangle2))

        shifts = []
        for o in self.mobjects:
            o: Mobject
            shifts += [o.animate.shift(LEFT)]

        self.play(*shifts)

        brace = BraceBetweenPoints([0, 0, 0], [1, 0, 0]).shift(DOWN * 2.8).shift(LEFT * 2.98).set_fill(GREY)
        texto = MathTex(r"r").shift(DOWN * 3.5).shift(LEFT * 2.5)
        texto2 = MathTex(r"\int_0^r 2\pi r \, dr").shift(UP * 2)
        texto3 = MathTex(r"2\pi \int_0^r r \, dr").shift(RIGHT).shift(UP * 2).next_to(texto2, DOWN)
        texto4 = MathTex(r"2\pi \left[ \frac{r^2}{2} \right]_0^r").shift(RIGHT).shift(UP * 2).next_to(texto3, DOWN)
        texto5 = MathTex(r"2\pi \left[ \frac{r^2}{2} - \frac{0^2}{2}\right]").shift(RIGHT).shift(UP * 2).next_to(texto2, RIGHT, 1)
        texto6 = MathTex(r"\frac{2\pi r^2}{2} - \frac{2\pi 0^2}{2}").shift(RIGHT).shift(UP * 2).next_to(texto5, DOWN)
        texto7 = MathTex(r"\pi r^2 - \pi 0^2").shift(RIGHT).shift(UP * 2).next_to(
            texto6, DOWN)
        texto8 = MathTex(r"\pi r^2").shift(RIGHT).shift(UP * 2).next_to(
            texto7, DOWN)

        self.play(Write(texto), Write(brace))
        self.wait(2)
        self.play(Write(texto2), FadeOut(eq))
        self.wait(2)

        for anim in [Write(t) for t in [texto3, texto4, texto5, texto6, texto7, texto8]]:
            self.play(anim)
            self.wait(2)

        self.wait(2)

    def construct(self):
        # Sección 1: El área como un triángulo de círculos extendidos
        titulo = Text("El área como un triángulo")
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.parte1()
        self.parte2()

        # Sección 2: El área como el área bajo la función de perímetro
        titulo = Text("El área como espacio bajo una función")
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.parte3()

        self.wait()

