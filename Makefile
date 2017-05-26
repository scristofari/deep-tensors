build:
	docker build -t tensor:latest .
start: build
	docker run --rm -it -v $(PWD):/root/tuto -w /root/tuto tensor:latest