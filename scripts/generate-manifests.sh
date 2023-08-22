#!/bin/bash

# use the data type templates listed in the config file
# this should generate an excel manifest for all the templates listed in the config
schematic manifest -c config.yml get -p "./AD.model.jsonld" --output_xlsx "excel/"

schematic manifest -c config.yml get -p "./AD.model.jsonld" -t AD.AssayRNASeqMetadataTemplate -dt AssayRNASeqMetadataTemplate --output_csv AD.AssayRNASeqMetadataTemplate.csv --output_xlsx AD.AssayRNASeqMetadataTemplate.xlsx