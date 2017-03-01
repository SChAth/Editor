from .forms import *
from .models import *

base_form_types = {
        'text_form': TextForm,
        'xml_form': XMLForm,
        }

def file_to_form(): 
    # lookup forms that this filetype can use
    form = XMLForm(initial={"text":f.text})
    # pick the form from the list


def generate_form(form_type_name, typed_file):
    """ Generates and populates a form, looking up the form type by name and 
        passing the form the typed file if appropriate. 

    :form_type_name: String
    :typed_file: TypedFile
    :returns: TODO

    """
    form_types = base_form_types
    form_types.append()
    form_type = form_types[form_type_name]
    #if this file type can be used with this forn type
    print(typed_file.ftype)
    pass
