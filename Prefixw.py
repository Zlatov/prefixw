# 
import sublime, sublime_plugin, pprint, subprocess, random

class EventListener(sublime_plugin.EventListener):
	def on_activated_async(self, view):
		# print('[listener] pre save event', self.view.id(), view.file_name())
		random.seed()
		rand = random.randint(0, 9999)
		pprint.pprint(rand)
		s = "999"
		status = ""
		output = ""
		status = subprocess.call("~/.config/sublime-text-3/Packages/Prefixw/prefixw.sh", shell=True)
		# status = subprocess.call("./prefixw.sh")
		output = subprocess.check_output("pwd")
		pprint.pprint(status)
		pprint.pprint(output)

class ExampCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		s = 'Hello, world.'
		pprint.pprint(s)
		# print s
		# sublime_plugin.TextCommand.view.insert(edit, 0, "#Hello, World!\n")

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
		self.view.run_command('examp')

