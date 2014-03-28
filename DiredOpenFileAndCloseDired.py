import sublime, sublime_plugin

class DiredOpenFileAndCloseDired(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("dired_select")
        self.window.run_command("next_view_in_stack")
        self.window.run_command("close")
