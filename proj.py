#!/usr/bin/env python2.7
import getpass
def interface():
	'''
	The main layout and menu
	'''
	print "Hello user ID:", getpass.getuser()
	
if __name__=='__main__':
	interface()