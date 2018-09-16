#! /usr/bin/py
# -*- coding:utf8 -*-

"""
Prepare courses list data
"""

import os
import yaml
import json


from parsers import API_DIR


COURSES_FILE = [
    "formations.cfpmm.yml",
    "formations.polytech.le.citoyen.yml",
    "formations.ucao.yml",
    "formations.upib.yml",
    "formations.verechaguine.ak.yml",
    "formations.esep.le.berger.yml",
    "formations.uac.yml",                  
    "formations.una.yml",     
    "formations.upi.onm.yml",
    "formations.hecm.yml",            
    "formations.uatm.gasa.yml",            
    "formations.unstim.yml",  
    "formations.up.yml"
]

DEST_DIR = os.path.join(os.path.dirname(API_DIR), "app", "src", "store")


def read_yaml_file(file_name):
    with open(os.path.join(os.path.join(API_DIR, "data", "yaml", "formations"), file_name)) as fp:
        data = yaml.safe_load(fp)

    return data


def main():

    courses = []

    for course_file in COURSES_FILE:
        current_data = read_yaml_file(course_file)
        current_courses = current_data["courses"]
        
        # add key university
        for course in current_courses:
            course["university"] = current_data["id"]

        courses += current_courses 


    with open(os.path.join(DEST_DIR, "courses.json"), "w") as fp:
        json.dump(courses, fp)

if __name__ == "__main__":
    main()