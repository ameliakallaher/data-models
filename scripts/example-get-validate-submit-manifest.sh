#!/bin/bash

# generate annotation template for dataset with dummy fastq files
schematic manifest -c schematic-config.yml get -dt FileAnnotationTemplate -p AD.model.jsonld -d syn52236799 --output_xlsx file_annotation_template_test2.xlsx

# validate manifest
schematic model -c schematic-config.yml validate -mp file_annotation_template_test2_filled.csv -dt FileAnnotationTemplate

# submit manifest
schematic model -c schematic-config.yml submit -mp file_annotation_template_test2_filled.csv -d syn52236799 -dl -mrt file_only
