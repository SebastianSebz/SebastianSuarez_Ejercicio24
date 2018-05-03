Graph.png: RadioactGraph.py RadioactGraph.txt
	python RadioactGraph.py

RadioactGraph.txt: Radioact.py
	python Radioact.py > RadioactGraph.txt
