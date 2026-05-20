from elsa import cli

from pyvecorg import app


def main():
	cli(app, base_url='http://pyvec.org')


if __name__ == '__main__':
	main()
