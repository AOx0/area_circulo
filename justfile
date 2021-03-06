lrvl num="":
    just render_local manim_very_low.cfg 360p15 AreaCirculo{{num}}

lrl num="":
    just render_local manim_low.cfg 720p30 AreaCirculo{{num}}

lrf num="":
    just render_local manim.cfg 2160p60 AreaCirculo{{num}}

openk:
    open /Users/alejandro/area_circulo/media/videos/main/2160p60/AreaCirculo.mp4 -a "QuickTime Player"

render_local config quality scene="AreaCirculo":
    qil QuickTime
    manim \
        -v WARNING \
        -p \
        -c cfg/{{config}} \
        main.py \
        {{scene}}
    open /Users/alejandro/area_circulo/media/videos/main/{{quality}}/{{scene}}.mp4 -a "QuickTime Player"
