#! /usr/bin/env python3

def calculate(arg):
	stack = []
	tokens = arg.split()
	print(tokens)

def main():
	while True:
		calculate(input("rpn calc> "))


if __name__ == '__main__':
	main()

