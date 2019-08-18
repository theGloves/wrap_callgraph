VERSION = $(shell python -c "from json import load; print(load(open('package.json'))['version'])" )
PROJECT = wrap_callgraph

install:
	pip install -r requirements.txt
	go get -u golang.org/x/tools/cmd/callgraph
	go get -u golang.org/x/tools/cmd/digraph
	
test:
	echo $(VERSION)