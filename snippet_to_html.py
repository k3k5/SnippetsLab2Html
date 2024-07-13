#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@date: 2019-11-20
@author: Sebastian Keck

Rendering SnippetLab Snippets from JSON to HTML
"""

import json

if __name__ == '__main__':

    snippets = []

    with open('snippets.json') as json_file:
        data = json.load(json_file)
        for p in data['Snippets']:
            current_title = p.get('Title')
            for item in p.get('Fragments'):
                snippets.append({current_title: [item.get('Content'), item.get('Note')]})

    with open('file.html', 'w') as file:
        file.write("<!DOCTYPE html><html><head><meta charset='utf-8'><link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css'></head><body>")
        file.write("<div class='container'>")
        for item in snippets:
            for snippet in item.keys():
                file.write("<h3>" + str(snippet) + "</h3>")
                if item.get(snippet)[1] is not None or item.get(snippets)[1] is not '':
                    file.write("\n")
                    file.write("<p>" + str(item.get(snippet)[1]) + "</p>")
                file.write("\n")
                file.write("<pre>" + str(item.get(snippet)[0]) + "</pre>")
                file.write("\n")
                file.write("\n")
