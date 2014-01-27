#!/usr/bin/python

import json
import os
import sys
import string

# -- configure me -- #
json_file = '/path/to/api/doc/_build/xml/api/views.json'
md_dir = '../../documentation/api/_build'
# -- end configure me -- #

def is_str(o):
    return isinstance(o, basestring)

def strip_first_slash(s):
    if s.startswith('/'):
        return s[1:]
    return s

def build_responses(json_responses):
    responses = ''
    for response in json_responses:
        responses += "\n+ Response %s\n\n\t\t%s\n" % (response['code'], response['message'])
    return responses


def build_parameters(json_parameters):
    parameters = "\n+ Parameters\n"
    for parameter in json_parameters:
        req_opt = ('optional', 'required')[json.loads(parameter['required'])]
        parameters += "\t+ %s (%s, %s)... %s\n" % (parameter['name'], req_opt, parameter['type'], parameter['description'])
    return parameters

def build_methods(json_data):
    for method in json_data['apis']:
        for operation in method['operations']:
            ressource = "####%s [%s]\n%s\n" % (operation['summary'].replace('/', ' or '), method['path'], operation['notes'])
            ressource += "#####[%s]\n" % (operation['method'])
            #ressource = "####%s %s\n%s\n" % (operation['method'], method['path'], operation['notes'])
            ressource += build_parameters(operation['parameters'])
            ressource += build_responses(operation['responseMessages'])

def build_resources(json_data):
    group = '\n\n###Group %s\n\
Resources related to Scaleway %s.\n' % (json_data['resourcePath'].replace('/', ''), json_data['resourcePath'])


def build_blueprint(json_data):
    print 'none'

def strip_last_slash(s):
    if s.endswith('/'):
        return s[:-1]
    return s

def path_first_part(s):
    stripped = strip_last_slash(s)
    if stripped.count('/') > 1:
        return os.path.split(stripped)[0]
    return stripped


def get_methods(json_):
    modules = json_.get('modules')
    classes = []
    for module in modules:
        classes.extend(module.get('classes', []))
    methods = []
    for class_ in classes:
        methods.extend(class_.get('methods', []))
    return methods


def ensure_dir():
    if not os.path.exists(md_dir):
        os.mkdir(md_dir)

def clear_old():
    for the_file in os.listdir(md_dir):
        file_path = os.path.join(md_dir, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print(e)


def build_reqs(method, path):
    http_info = method["http_domain_info"]

    res = "####%s [%s]\n%s\n" % (http_info['content']['Title'], http_info['http_url'].replace('&amp;', '&'), "<br />".join(method['description']))
    res += "#####[%s]\n" % (http_info['http_method'])

    res += "\n+ Parameters\n"


    path_arguments = http_info["content"].get("Path arguments", [])
    if is_str(path_arguments):
        arg, info = map(string.strip, path_arguments.split('--'))
        res += "\t+ %s (%s, %s)... %s\n" % (arg, 'required', 'string', info)
    else:  # got a list
        for item in path_arguments:
            arg, info = map(string.strip, item.split('--'))
            res += "\t+ %s (%s, %s)... %s\n" % (arg, 'required', 'string', info)
    # -- query params -- #
    query_params = http_info["content"].get("Query params", [])
    if is_str(query_params):
        arg, info = map(string.strip, query_params.split('--'))
        res += "\t+ %s (%s, %s)... %s\n" % (arg, 'required', 'string', info)
    else:  # got a list
        for item in query_params:
            arg, info = map(string.strip, item.split('--'))
            res += "\t+ %s (%s, %s)... %s\n" % (arg, 'required', 'string', info)
    # -- query arguments -- #
    query_arguments = http_info["content"].get("Opt. params", [])
    if is_str(query_arguments):
        arg, info = map(string.strip, query_arguments.split('--'))
        res += "\t+ %s (%s, %s)... %s\n" % (arg, 'required', 'string', info)
    else:  # got a list
        for item in query_arguments:
            arg, info = map(string.strip, item.split('--'))
            res += "\t+ %s (%s, %s)... %s\n" % (arg, 'required', 'string', info)
    res += '\n'
    return res



def build_blueprint(pathes, methods):
    files = {}
    for path in pathes:
        files[path] = '\n\n###group %s\n\
#resources related to scaleway %s.\n' % (path.replace('/', '').capitalize(), path.replace('/', '').capitalize())

    for method in methods:
        http_info = method["http_domain_info"]
        path_stripped = path_first_part(http_info["http_path"])
        files[path_stripped] += build_reqs(method, path_stripped)

    return files

def write_files(files_dict):
    for k, v in files_dict.items():
        fname = strip_first_slash(k)
        with open(os.path.join(md_dir, fname + '.md'), "w") as f:
            f.write(v)

def main():
    ensure_dir()
    clear_old()
    with open(json_file) as f:
        data = f.read()
        json_data = json.loads(data)
        methods = get_methods(json_data)
        pathes = [method["http_domain_info"]["http_path"]
                  for method in methods]
        pathes = set(map(path_first_part, pathes))
        files_to_write = build_blueprint(pathes, methods)
        write_files(files_to_write)

if __name__ == '__main__':
    main()


