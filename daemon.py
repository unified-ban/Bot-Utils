#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#
# Credits: http://www.jejik.com/articles/2007/02/
#							a_simple_unix_linux_daemon_in_python/www.boxedice.com
# Source code: https://github.com/sarnold/python-daemon/
# License: http://creativecommons.org/licenses/by-sa/3.0/

import sys, os, time, atexit
from signal import SIGTERM 

class Daemon(object):
	startmsg = "Started with pid %s"

	def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
		self.stdin = stdin
		self.stdout = stdout
		self.stderr = stderr
		self.pidfile = pidfile

	def daemonize(self):
		try: 
			pid = os.fork() 
			if pid > 0:
				sys.exit(0) 
		except OSError as e: 
			sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
			sys.exit(1)
		os.chdir("/") 
		os.setsid() 
		os.umask(0) 
		try: 
			pid = os.fork() 
			if pid > 0:
				sys.exit(0) 
		except OSError as e: 
			sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
			sys.exit(1) 
		si = open(self.stdin, 'r')
		so = open(self.stdout, 'a+')
		se = open(self.stderr, 'a+')
		pid = str(os.getpid())
		sys.stderr.write("\n%s\n" % self.startmsg % pid)
		sys.stderr.flush()
		if self.pidfile:
			open(self.pidfile,'w+').write("%s\n" % pid)
		atexit.register(self.delpid)
		os.dup2(si.fileno(), sys.stdin.fileno())
		os.dup2(so.fileno(), sys.stdout.fileno())
		os.dup2(se.fileno(), sys.stderr.fileno())
		
	def delpid(self):
		try:
			os.remove(self.pidfile)
			return True
		except OSError:
			print("OSError")
			return False

	def start(self):
		"""
		Start daemon
		"""
		try:
			pf = open(self.pidfile,'r')
			pid = int(pf.read().strip())
			pf.close()
		except IOError:
			pid = None
		except SystemExit:
			pid = None
		if pid:
			message = "pidfile %s already exist. Daemon already running?\n"
			sys.stderr.write(message % self.pidfile)
			sys.exit(1)
		self.daemonize()
		self.run()

	def get_pid(self):
		try:
			pf = open(self.pidfile, 'r')
			pid = int(pf.read().strip())
			pf.close()
		except IOError:
			pid = None
		except SystemExit:
			pid = None
		return pid

	def stop(self):
		"""
		Stop daemon
		"""
		try:
			pf = open(self.pidfile,'r')
			pid = int(pf.read().strip())
			pf.close()
		except IOError:
			pid = None
		if not pid:
			message = "pidfile %s does not exist. Daemon not running?\n"
			sys.stderr.write(message % self.pidfile)
			return
		try:
			while 1:
				os.kill(pid, SIGTERM)
				time.sleep(0.1)
		except OSError as err:
			err = str(err)
			if err.find("No such process") > 0:
				if os.path.exists(self.pidfile):
					os.remove(self.pidfile)
				else:
					print(str(err))
					sys.exit(1)

	def restart(self):
		"""
		Restart daemon
		"""
		self.stop()
		self.start()

	def run(self):
		print("run")
		return True