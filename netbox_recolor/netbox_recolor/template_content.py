from netbox.plugins import PluginTemplateExtension


class Recolor(PluginTemplateExtension):
    def navbar(self):
        return self.render("netbox_recolor/recolor.html")


template_extensions = [Recolor]
