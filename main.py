import manim as mn


class Main(mn.Scene):
    def construct(self):
        root = mn.Dot()
        title = mn.Title("Dynamic Programming")
        self.play(mn.Create(title))
        self.add(root)

        def addChildren(node, height):
            height += 1
            child = mn.Dot(node.get_center() + 1/height * mn.LEFT + mn.DOWN)
            child1 = mn.Dot(node.get_center() + 1/height * mn.RIGHT + mn.DOWN)
            animations = (
                mn.Create(mn.Line(node.get_center(), child.get_center())),
                mn.Create(mn.Line(node.get_center(), child1.get_center()))
            )
            return (
                child,
                child1,
                animations
            )

        total_height = 3

        nodes = [root]
        for height in range(total_height):
            next_nodes = []
            for node in nodes:
                node1, node2, animations = addChildren(node, height)
                next_nodes.append(node1)
                next_nodes.append(node2)
                self.add(node1, node2)
                self.play(*animations)
            nodes = next_nodes


#        self.play(
#            mn.Create(mn.Line(root.get_center(), node1.get_center())),
#            mn.Create(mn.Line(root.get_center(), node.get_center()))
#        )
        self.wait(2)
