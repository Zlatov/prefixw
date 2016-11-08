import sublime, sublime_plugin, pprint, subprocess

class EventListener(sublime_plugin.EventListener):
	def on_activated_async(self, view):
		output = subprocess.check_output("~/.config/sublime-text-3/Packages/Prefixw/prefixw.sh", shell=True)
		output = output.decode("utf-8").rstrip('\n')
		if output!='done':
			pprint.pprint(output)
