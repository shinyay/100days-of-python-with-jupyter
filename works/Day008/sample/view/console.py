import os
import string
import termcolor

def get_template_dir_path():
    template_dir_path = None

    if not template_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path