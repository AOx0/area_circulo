lrvl:
    just render_local manim_very_low.cfg 360p15

lrl:
    just render_local manim_low.cfg 720p30

lrf:
    just render_local manim.cfg 2160p60


openk:
    open /Users/alejandro/area_circulo/media/videos/main/2160p60/AreaCirculo.mp4 -a "QuickTime Player"

render_local config quality:
    qil QuickTime
    manim \
        -v WARNING \
        -p \
        -c cfg/{{config}} \
        main.py
    open /Users/alejandro/area_circulo/media/videos/main/{{quality}}/AreaCirculo.mp4 -a "QuickTime Player"
