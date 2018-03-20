import sublime, sublime_plugin, pprint, subprocess, re
from pprint import pprint

class EventListener(sublime_plugin.EventListener):
	def on_activated_async(self, view):
		projectSettings = self.loadProjectSettings(view)
		if projectSettings:
			if projectSettings["on"] == True:
				self.renameTab()
		else:
			self.renameTab()

	def on_activated(self, view):
		self.renameTab()

	def loadProjectSettings(self, view):
		return view.settings().get("prefixw")

	def renameTab(self):
		version_numbers = re.findall(r"(\d)\d+", sublime.version())
		if len(version_numbers) == 0:
			return None

		if version_numbers[0] == '2':
			output = subprocess.Popen(
	            ["/bin/bash", "-c", "~/.config/sublime-text-2/Packages/Prefixw/prefixw.sh"],
	            stdout=subprocess.PIPE,
	            stderr=subprocess.PIPE,
	            stdin=subprocess.PIPE,
	            # startupinfo=startupinfo,
	            # env=proc_env,
	            shell=False)
			pprint(output)
		elif version_numbers[0] == '3':
			output = subprocess.check_output("~/.config/sublime-text-3/Packages/Prefixw/prefixw.sh", shell=True)
			output = output.decode("utf-8").rstrip('\n')
			if output!='done':
				pprint(output)
