SCENE=Main

video:
	manim -pql main.py $(SCENE) 

watch:
	while true; do inotifywait -e modify main.py; make video; done

.PHONY: video


all: video
