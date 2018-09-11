from multiprocessing import Pipe, Process, Array
from main import program
from time import sleep as s

def main():
	prog = main()
	print("starting importing to databases")
	prog.start()
	s(45)
	prog.terminate()
	print("done")
main()