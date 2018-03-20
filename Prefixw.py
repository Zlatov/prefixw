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

	def loadProjectSettings(self, view):
		return view.settings().get("prefixw")

	def renameTab(self):
		version_numbers = re.findall(r"(\d)\d+", sublime.version())
		if len(version_numbers) == 0:
			return None
		if version_numbers[0] != '2' and version_numbers[0] != '3':
			return None
		output = subprocess.check_output("~/.config/sublime-text-" + version_numbers[0] + "/Packages/Prefixw/prefixw.sh", shell=True)
		output = output.decode("utf-8").rstrip('\n')
		if output!='done':
			pprint(output)
