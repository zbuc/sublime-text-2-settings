import sublime, sublime_plugin, os, subprocess

class FilenameCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.file_name():
			self.view.set_status('fp',self.view.file_name())

class ShowFullFilename(sublime_plugin.EventListener):
    def on_load(self, view):
		view.run_command('filename')
