from manim import *

RADIO = 1


def fo_all(self):
    self.play(
        *[FadeOut(mob) for mob in self.mobjects]
    )


class AreaCirculo(Scene):

    def parte1(self):
        self: Scene

        circulo = Circle(RADIO)
        circulo = circulo.set_stroke(circulo.color, 1.5)
        linea = Line([0, 0, 0], [RADIO, 0, 0])
        ra = MathTex("r").shift(RIGHT * 0.5).shift(UP * 0.5)

        self.play(Create(circulo))
        self.wait(0.2)

        self.play(circulo.animate.set_fill(circulo.color, 1.5), Write(ra), Create(linea))

        circles = [Circle(radius=r * 0.1).set_stroke(circulo.color, 1.5) for r in list(range(1, RADIO * 10, 1))]
        c_circles4 = [FadeIn(circle) for circle in circles]

        self.play(circulo.animate.set_fill(circulo.color, 0), FadeOut(ra), FadeOut(linea))
        self.play(*c_circles4)

        rectangles = [
            Rectangle(width=r * 0.1 * TAU, height=0.1).set_stroke(circulo.color, 1.5)
            for r in list(range(1, RADIO * 10, 1))
        ]
        rectangles += [Rectangle(width=TAU * RADIO, height=0.1).set_stroke(circulo.color, 1.5)]

        for j in range(1, len(rectangles)):
            rectangles[j].next_to(rectangles[j - 1], DOWN, 0)

        t_circle = [circle.animate.shift(UP * 2) for circle in circles]

        self.play(
            circulo.animate.shift(UP * 2),
            *t_circle
        )

        out_rect2 = [FadeOut(rect) for rect in rectangles]

        c_transform = [TransformFromCopy(circles[j], rectangles[j]) for j in range(len(circles))]

        self.play(TransformFromCopy(circulo, rectangles[len(rectangles) - 1]), *c_transform)

        circles = [Circle(radius=r * 0.1).set_stroke(circulo.color, 1.5).shift(UP * 2) for r in
                   list(range(1, RADIO * 10, 1))]
        c_circles = [FadeIn(circle) for circle in circles]

        rectangles = [Rectangle(width=TAU * r * 0.1, height=0.1).set_stroke(circulo.color, 1.5) for r in
                      list(range(1, RADIO * 10, 1))]
        rectangles += [Rectangle(width=TAU * RADIO, height=0.1).set_stroke(circulo.color, 1.5)]

        for j in range(1, len(rectangles)):
            rectangles[j].next_to(rectangles[j - 1], DOWN, 0)

        c_rectangles = [FadeIn(rect) for rect in rectangles]

        out_rect = [FadeOut(rect) for rect in rectangles]

        self.play(*c_rectangles, *c_circles, *out_rect)

        self.wait(0.2)

        circles = [Circle(radius=r * 0.05).set_stroke(circulo.color, 1.5).shift(UP * 2) for r in
                   list(range(1, RADIO * 10 * 2, 1))]
        c_circles = [FadeIn(circle) for circle in circles]

        rectangles = [Rectangle(width=r * 0.05 * TAU, height=0.05).set_stroke(circulo.color, 1.5) for r in
                      list(range(1, RADIO * 10 * 2, 1))]
        rectangles += [Rectangle(width=TAU * RADIO, height=0.05).set_stroke(circulo.color, 1.5)]

        for j in range(1, len(rectangles)):
            rectangles[j].next_to(rectangles[j - 1], DOWN, 0)

        c_rectangles = [FadeIn(rect) for rect in rectangles]

        self.play(*c_rectangles, *c_circles, *out_rect, *out_rect2)

        self.wait(0.2)

        out_rect = [FadeOut(rect) for rect in rectangles]

        self.wait(0.2)

        circles = [Circle(radius=r * 0.025).set_stroke(circulo.color, 1.5).shift(UP * 2) for r in
                   list(range(1, RADIO * 10 * 4, 1))]
        c_circles = [FadeIn(circle) for circle in circles]

        rectangles = [Rectangle(width=r * 0.025 * TAU, height=0.025).set_stroke(circulo.color, 1.5) for r in
                      list(range(1, RADIO * 10 * 4, 1))]
        rectangles += [Rectangle(width=TAU * RADIO, height=0.025).set_stroke(circulo.color, 1.5)]

        for j in range(1, len(rectangles)):
            rectangles[j].next_to(rectangles[j - 1], DOWN, 0)

        c_rectangles = [FadeIn(rect) for rect in rectangles]

        self.play(*c_rectangles, *c_circles, *out_rect)

        self.wait(0.2)

        filled_triangle_points = [[-TAU * RADIO / 2, -1, 0], [0, RADIO - 1, 0], [TAU * RADIO / 2, -1, 0]]

        filled_triangle = Polygon(
            *filled_triangle_points, color=circulo.color).set_fill(circulo.color, 1.5)

        out_rect = [FadeOut(rect) for rect in rectangles]

        self.play(FadeIn(filled_triangle), circulo.animate.set_fill(circulo.color, 1.0), *out_rect)

        self.wait(0.5)

        filled_triangle_points2 = [[-TAU * RADIO / 2, -1, 0], [-TAU * RADIO / 2, RADIO - 1, 0],
                                   [TAU * RADIO / 2, -1, 0]]

        filled_triangle2 = Polygon(
            *filled_triangle_points2, color=circulo.color).set_fill(circulo.color, 1.5)

        self.play(Transform(filled_triangle, filled_triangle2))

        self.wait(0.5)

        self.play(FadeOut(filled_triangle2))

        radio = MathTex(r"r").shift(RIGHT * (- 0.5 - TAU * RADIO / 2)).shift(DOWN / 2)
        base = MathTex(r"2 \pi r").shift(DOWN - 0.5)

        self.play(Write(radio), Write(base))

        self.wait()

        fo_all(self)

    def parte2(self):
        texto1 = Tex(r"Base   := $2 \pi r$")
        texto2 = Tex(r"Altura := $r$      ")

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
        self.play(Transform(texto1, texto2))
        self.wait(2)
        self.play(Transform(texto1, texto3))
        self.wait(3)
        self.play(Transform(texto1, texto4))
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

        rectangles = VGroup(*[
            Rectangle(width=0.5, height=TAU * r * 0.5)
            .set_stroke(RED, 1.5)
            .shift(DOWN * 3)
            .shift(LEFT * 2)

            for r in list(range(0, 2, 1))
        ])

        rectangles.arrange(RIGHT, center=False, aligned_edge=DOWN, buff=0)

        for rect in rectangles:
            self.play(FadeIn(rect, run_time=0.2))

        self.wait(0.5)

        rectangles1 = VGroup(*[
            Rectangle(width=0.25, height=TAU * r * 0.25)
            .set_stroke(RED, 1.5)
            .shift(DOWN * 3)
            .shift(LEFT * 2)

            for r in list(range(0, 4, 1))
        ])

        rectangles1.arrange(RIGHT, center=False, aligned_edge=DOWN, buff=0)
        self.play(Transform(rectangles, rectangles1))

        rectangles1 = VGroup(*[
            Rectangle(width=0.125, height=TAU * r * 0.125)
            .set_stroke(RED, 1.5)
            .shift(DOWN * 3)
            .shift(LEFT * 2)

            for r in list(range(0, 8, 1))
        ])

        rectangles1.arrange(RIGHT, center=False, aligned_edge=DOWN, buff=0)
        self.play(Transform(rectangles, rectangles1))

        rectangles2 = VGroup(*[
            Rectangle(width=0.1, height=TAU * r * 0.1)
            .set_stroke(RED, 1.5)
            .shift(DOWN * 3)
            .shift(LEFT * 2)

            for r in list(range(0, 10, 1))
        ])

        rectangles2.arrange(RIGHT, center=False, aligned_edge=DOWN, buff=0)
        self.play(Transform(rectangles, rectangles2))

        rectangles3 = VGroup(*[
            Rectangle(width=0.05, height=TAU * r * 0.05)
            .set_stroke(RED, 1.5)
            .shift(DOWN * 3)
            .shift(LEFT * 2)

            for r in list(range(0, 10 * 2, 1))
        ])

        rectangles3.arrange(RIGHT, center=False, aligned_edge=DOWN, buff=0)
        self.play(Transform(rectangles, rectangles3))

        rectangles4 = VGroup(*[
            Rectangle(width=0.025, height=TAU * r * 0.025)
            .set_stroke(RED, 1.5)
            .shift(DOWN * 3)
            .shift(LEFT * 2)

            for r in list(range(0, 10 * 2 * 2, 1))
        ])

        rectangles4.arrange(RIGHT, center=False, aligned_edge=DOWN, buff=0)
        self.play(Transform(rectangles, rectangles4))

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
        self.play(Write(texto3))
        self.wait(2)
        self.play(Write(texto4))
        self.wait(2)
        self.play(Write(texto5))
        self.wait(2)

        self.play(Write(texto6))
        self.wait(2)
        self.play(Write(texto7))
        self.wait(2)
        self.play(Write(texto8))
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

