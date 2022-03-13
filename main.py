from manim import *
from typing import NewType

RADIO = 1
Vertical = NewType('Vertical', bool)
Horizontal = NewType('Horizontal', bool)
VERTICAL: Vertical = Vertical(True)
HORIZONTAL: Horizontal = Horizontal(False)


def generate_rectangles(number: int, sentido: Vertical | Horizontal = HORIZONTAL) -> VGroup:
    val1 = 1 / number
    val2 = lambda ra: TAU * (ra / number)
    horizontal = sentido == HORIZONTAL

    rectangles = []

    for r in list(range(0, RADIO * number + 1)):
        if r == 0 and not horizontal:
            continue
        rectangles += [
            Rectangle(width=val1 if horizontal else val2(r), height=val2(r) if horizontal else val1)
                .set_stroke(RED, 1.5)
                .shift(DOWN * 3)
                .shift(LEFT * (2 if horizontal else 0))
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
        cir = lambda number: VGroup(*[Circle(radius=r / number).set_stroke(circulo.color, 1.5).shift(UP * 2) for r in
                                      list(range(1, RADIO * number, 1))])

        self.play(Create(circulo))
        self.wait(0.2)

        self.play(circulo.animate.set_fill(circulo.color, 1.5), Write(ra), Create(linea))

        circles = VGroup(
            *[Circle(radius=r * 0.1).set_stroke(circulo.color, 1.5) for r in list(range(1, RADIO * 10, 1))])
        self.play(circulo.animate.set_fill(circulo.color, 0), FadeOut(ra), FadeOut(linea))
        self.play(*f_in(circles))

        rectangles = generate_rectangles(10, VERTICAL)
        t_circle = [circle.animate.shift(UP * 2) for circle in circles]
        self.play(circulo.animate.shift(UP * 2), *t_circle)

        c_transform = [TransformFromCopy(circles[j], rectangles[j]) for j in range(len(circles))]
        self.play(TransformFromCopy(circulo, rectangles[len(rectangles) - 1]), *c_transform)

        for val in [15, 20, 40, 60]:
            circles_new = cir(val)
            rectangles_new = generate_rectangles(val, VERTICAL)
            self.play(Transform(rectangles, rectangles_new), Transform(circles, circles_new))
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

        self.play(*[mob.animate.shift(2.5 * LEFT) for mob in self.mobjects])

        self.wait(0.5)

        texto1 = MathTex(r"\frac{b \times h}{2}").shift(RIGHT * 3).shift(UP * 2.5)
        texto2 = MathTex(r"\frac{2 \pi r \times r}{2}").next_to(texto1, DOWN, buff=0.7)
        texto3 = MathTex(r"\pi r \times r").next_to(texto2, DOWN, buff=0.7)
        texto4 = MathTex(r"\pi r^2").next_to(texto3, DOWN, buff=0.7)

        for anim in [Write(t) for t in [texto1, texto2, texto3, texto4]]:
            self.play(anim)
            self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def parte3(self):
        xax = Line([-3, 0, 0], [3, 0, 0]).shift(DOWN * 3)
        yax = Line([0, -3, 0], [0, 4, 0]).shift(LEFT * 2).shift(DOWN * 0.5)
        line = Line([-(r := 1.2), -r * TAU, 0], [r, r * TAU, 0]).set_color(RED).shift(DOWN * 3).shift(
            LEFT * 2).set_stroke(RED, 1.5)
        eq = MathTex(r"p(r) = 2\pi r").shift(DOWN * 3.5).shift(RIGHT * 2)

        self.play(Create(line, run_time=1), Create(xax), Create(yax))
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

        filled_triangle2 = Polygon(*filled_triangle_points2, color=RED).set_fill(RED, 1.5).shift(DOWN * 3).shift(
            LEFT * 2)

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
        texto5 = MathTex(r"2\pi \left[ \frac{r^2}{2} - \frac{0^2}{2}\right]").shift(RIGHT).shift(UP * 2).next_to(texto2,
                                                                                                                 RIGHT,
                                                                                                                 1)
        texto6 = MathTex(r"2\pi \left[ \frac{r^2}{2} \left]").shift(RIGHT).shift(UP * 2).next_to(texto5, DOWN)
        texto7 = MathTex(r"\frac{2\pi r^2}{2}").shift(RIGHT).shift(UP * 2).next_to(
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

        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def parte0(self):
        circulo = Circle(RADIO)
        circulo = circulo.set_stroke(circulo.color, 1.5)
        linea = Line([0, 0, 0], [RADIO, 0, 0]).shift(UP)
        ra = MathTex("r").shift(RIGHT * 0.5).shift(UP * 0.5).shift(UP)

        self.play(Create(circulo))
        self.wait(0.2)

        self.play(circulo.animate.shift(UP))

        self.play(circulo.animate.set_fill(circulo.color, 1.5), Write(ra), Create(linea))
        self.wait(0.2)

        self.play(FadeOut(linea), FadeOut(ra))

        parte = lambda r, n, t: AnnularSector(0, r, TAU / n, t * TAU / n).shift(UP)
        parte_arriba = lambda r, n: AnnularSector(0, r, TAU / n, TAU / 4)
        partes, s_group = None, None

        for num in [16, 32, 64, 128, 128 * 2, 128 * 6]:
            partes_new = VGroup(*[
                parte(1, num, t)
                                .set_fill(circulo.color if t % 2 == 0 else "#8B4513", 1.5)
                                .set_stroke(circulo.color if t % 2 == 0 else "#8B4513", 0.1)
                for t in range(1, num + 1)
            ])

            s_group_new = VGroup()
            for _ in range(int(num / 2)):
                angle = - ((radio := 1) * TAU) / num * 0.5
                valor = TAU / (num * 2)

                p1 = parte_arriba(radio, num) \
                    .rotate_about_origin(angle) \
                    .set_fill(circulo.color, 1.5) \
                    .shift(LEFT * valor / 2)

                p2 = parte_arriba(radio, num) \
                    .rotate_about_origin(angle) \
                    .set_fill("#8B4513", 1.5) \
                    .shift(RIGHT * valor / 2) \
                    .rotate(PI)

                group_new = VGroup(p1, p2)
                s_group_new.add(group_new)

            s_group_new.arrange(LEFT, center=True, buff=-valor)

            if num == 16:
                partes = partes_new
                s_group = s_group_new.shift(DOWN)

                self.play(FadeIn(partes), FadeIn(s_group))
                self.play(FadeOut(circulo))
            else:
                self.play(Transform(partes, partes_new), Transform(s_group, s_group_new.shift(DOWN)))

        circulo2 = circulo.set_fill(circulo.color, 1)
        rect = Rectangle(circulo.color, RADIO, PI).set_fill(circulo.color, 1.5).set_stroke(circulo.color, 0.5).shift(
            DOWN)
        radio = MathTex(r"r").shift(RIGHT * (- 0.5 - PI / 2)).shift(DOWN)
        base = MathTex(r"\pi r").shift(2 * DOWN)

        self.play(FadeIn(circulo2), FadeIn(rect), FadeOut(s_group), Write(radio), Write(base), Write(ra), Create(linea))
        self.play(*[mob.animate.shift(2 * LEFT) for mob in self.mobjects])

        self.wait(1)

        texto1 = MathTex(r"b \times h").shift(RIGHT * 2).shift(UP)
        texto2 = MathTex(r"\pi r \times r").next_to(texto1, DOWN, buff=1)
        texto3 = MathTex(r"\pi r^2").next_to(texto2, DOWN,  buff=1)

        for anim in [Write(t) for t in [texto1, texto2, texto3]]:
            self.play(anim)
            self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def construct(self):
        texto_inicial = Tex(r"Demostración de la fórmula $\pi r^2$")

        self.play(Write(texto_inicial))
        self.wait(1)

        self.play(FadeOut(texto_inicial))

        # Sección 1: El área como un triángulo de círculos extendidos
        titulo = Text("El área como un rectángulo")
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.parte0()

        # Sección 1: El área como un triángulo de círculos extendidos
        titulo = Text("El área como un triángulo")
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.parte1()

        # Sección 2: El área como el área bajo la función de perímetro
        titulo = Text("El área como espacio bajo\n  la función de perímetro")
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))
        self.parte3()

        self.wait()


class AreaCirculo2(Scene):

    def construct(self):
        circulo = Circle(RADIO)
        circulo = circulo.set_stroke(circulo.color, 1.5)
        linea = Line([0, 0, 0], [RADIO, 0, 0]).shift(UP)
        ra = MathTex("r").shift(RIGHT * 0.5).shift(UP * 0.5).shift(UP)

        self.play(Create(circulo))
        self.wait(0.2)

        self.play(circulo.animate.shift(UP))

        self.play(circulo.animate.set_fill(circulo.color, 1.5), Write(ra), Create(linea))
        self.wait(0.2)

        self.play(FadeOut(linea), FadeOut(ra))

        parte = lambda r, n, t: AnnularSector(0, r, TAU / n, t * TAU / n).shift(UP)
        parte_arriba = lambda r, n: AnnularSector(0, r, TAU / n, TAU / 4)
        partes, s_group = None, None

        for num in [16, 32, 64, 128, 128*2, 128*6]:
            partes_new = VGroup(*[
                parte(1, num, t)
                .set_fill(circulo.color if t % 2 == 0 else "#8B4513", 1.5)
                .set_stroke(circulo.color if t % 2 == 0 else "#8B4513", 0.1)
                for t in range(1, num + 1)
            ])

            s_group_new = VGroup()
            for _ in range(int(num / 2)):
                angle = - ((radio := 1) * TAU) / num * 0.5
                valor = TAU / (num * 2)

                p1 = parte_arriba(radio, num) \
                    .rotate_about_origin(angle) \
                    .set_fill(circulo.color, 1.5) \
                    .shift(LEFT * valor/2)

                p2 = parte_arriba(radio, num) \
                    .rotate_about_origin(angle) \
                    .set_fill("#8B4513", 1.5) \
                    .shift(RIGHT * valor/2) \
                    .rotate(PI)

                group_new = VGroup(p1, p2)
                s_group_new.add(group_new)

            s_group_new.arrange(LEFT, center=True, buff=-valor)

            if num == 16:
                partes = partes_new
                s_group = s_group_new.shift(DOWN)

                self.play(FadeIn(partes), FadeIn(s_group))
                self.play(FadeOut(circulo))
            else:
                self.play(Transform(partes, partes_new), Transform(s_group, s_group_new.shift(DOWN)))

        circulo2 = circulo.set_fill(circulo.color, 1)
        rect = Rectangle(circulo.color, RADIO, PI).set_fill(circulo.color, 1.5).set_stroke(circulo.color, 0.5).shift(DOWN)
        radio = MathTex(r"r").shift(RIGHT * (- 0.5 - PI / 2)).shift(DOWN)
        base = MathTex(r"2 \pi r").shift(2 * DOWN)

        self.play(FadeIn(circulo2), FadeIn(rect), FadeOut(s_group), Write(radio), Write(base), Write(ra), Create(linea))
        self.play(*[mob.animate.shift(2 * LEFT) for mob in self.mobjects])

        self.wait(1)


