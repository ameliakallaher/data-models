'''
Get template names (@id) and display names from all DataType attributes in jsonld data model
The template names are different from the "display names" which are in the csv data model
'''
import json
import pandas as pd
import yaml

### Create template menu from jsonld data model

def get_template_names(jsonld_data_model):
    jsonld_file = open(jsonld_data_model)
    jsonld_model = json.load(jsonld_file)
    graph = jsonld_model['@graph']
    template_name = list()
    display_name = list()
    for i in range(len(graph)):
        if (
            'rdfs:subClassOf' in graph[i] 
            and type(graph[i]['rdfs:subClassOf']) is list  
            and 'bts:DataType' in graph[i]['rdfs:subClassOf'][0].values()
            ):
            template_name.append(graph[i]['@id'].replace('bts:', ''))
            display_name.append(graph[i]['sms:displayName'])
    df = pd.DataFrame({'template_name': template_name,
                       'display_name': display_name})
    return(df)

menu_df = get_template_names("AD.model.jsonld")

# fix the metadata manifest name since I messed up when I made the template in the config repo
menu_df.loc[menu_df.template_name.str.contains("Manifest"), 'display_name'] = 'file_annotation_template'

# add type column based on whether "annotation" is in the display name
menu_df['type'] = menu_df['display_name'].apply(lambda x: 'file' if 'annotation' in x else 'record')

# alphabetize display names
menu_df.sort_values(by = ['type', 'display_name'])


result = menu_df.to_json(orient = 'records')
parsed = json.loads(result)
print(json.dumps(parsed, indent = 4))