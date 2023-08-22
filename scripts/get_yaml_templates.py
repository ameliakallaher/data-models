
'''
Get template names from dca config template menu and print yaml
The yaml can be copy-pasted into the templates section in the config.yml file
'''
import json
import pandas as pd
import yaml



### Create formatted yaml of template names from data model to paste into config file

def yaml_template_names(template_menu_file):
    menu_json = json.load(open(template_menu_file))
    template_names = list()
    for i in menu_json['manifest_schemas']:
        template_names.append(i['schema_name'])

    print(yaml.dump(template_names, default_flow_style = False, default_style= '"'))

yaml_template_names("dca_template_menu.json")
