import os
import string
import termcolor

def get_template_dir_path():
    template_dir_path = None

    if not template_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path

def find_template(temp_file):
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    if not os.path.exists(temp_file_path):
        raise NoTemplateError('Could Not Find: {}'.format(temp_file))
    return temp_file_path