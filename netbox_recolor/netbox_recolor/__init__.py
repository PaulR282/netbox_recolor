from netbox.plugins import PluginConfig
class RecolorConfig(PluginConfig):
    name = 'netbox_recolor'
    verbose_name = 'Netbox Recolor'
    description = 'Netbox Recolor'
    version = '1.0'
    base_url = 'netbox_recolor'

config = RecolorConfig
