 # type: ignore
from manim import *

class LagRatios(Scene):
    def construct(self):
        ratios = [0, 0.1, 0.5, 1, 2]    #显示的滞后比率

        #创建点组
        group = VGroup(*[Dot() for _ in range(4)]).arrange_submobjects()
        groups = VGroup(*[group.copy() for _ in ratios]).arrange_submobjects(buff = 1)
        self.add(groups)

        #标签组
        self.add(Text("lag_ratio = ", font_size=36).next_to(groups, UP, buff = 1.5))
        for group, ratio in zip(groups, ratios):
            self.add(Text(str(ratio), font_size=36).next_to(group, UP))

        #有不同滞后比率的动画组
        self.play(AnimationGroup(*[
            group.animate(lag_ratio=ratio, run_time=1.5).shift(DOWN * 2)
            for group, ratio in zip(groups, ratios)
        ]))

        #Tag _ ratio 也可以递归地在嵌套子对象上工作:
        self.play(groups.animate(run_time = 1, lag_ratio =  0.1).shift(UP * 2))