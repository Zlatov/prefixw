import sublime, sublime_plugin, pprint, subprocess, re
from pprint import pprint
import os

class CurrentPathStatusCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view # вьюха открытого файла?
		window = view.window() # экземпляр окна сублайма?
		file_path = view.file_name()
		if file_path == None:
			return None
		# Определён полный путь к открытому файлу
		# pprint(file_path)

		project_path = window.project_file_name()
		if project_path == None:
			project_path = window.folders()[0]
		else:
			project_path = os.path.dirname(project_path)

		if project_path == None:
			view.set_status('current_path', file_path)
			return None
		project_path_len = len(project_path)
		# pprint(project_path)
		# pprint(file_path[:project_path_len])
		if file_path[:project_path_len] == project_path:
			current_path = file_path[project_path_len:]
		else:
			current_path = file_path
		view.set_status('current_path', current_path)

class EventListener(sublime_plugin.EventListener):
	def on_activated_async(self, view):
		projectSettings = self.loadProjectSettings(view)
		if projectSettings:
			if projectSettings["on"] == True:
				self.renameTab()
				view.run_command('current_path_status')
		else:
			self.renameTab()
			view.run_command('current_path_status')

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
			# pprint(output)
		elif version_numbers[0] == '3':
			output = subprocess.check_output("~/.config/sublime-text-3/Packages/Prefixw/prefixw.sh", shell=True)
			output = output.decode("utf-8").rstrip('\n')
			if output!='done':
				pprint(output)
