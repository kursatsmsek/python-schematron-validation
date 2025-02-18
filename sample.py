from saxonche import *

def read_xml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def validate_xml_with_xslt(xml_file_path, xslt_file_path):
    with PySaxonProcessor(license=False) as proc:
        xsltproc = proc.new_xslt30_processor()

        xml_text = read_xml_file(xml_file_path)
        document = proc.parse_xml(xml_text=xml_text)

        executable = xsltproc.compile_stylesheet(stylesheet_file=xslt_file_path)

        output = executable.transform_to_string(xdm_node=document)

        print(output)

xml_file_path = 'input.xml'
xslt_file_path = 'schematron.xslt'

validate_xml_with_xslt(xml_file_path, xslt_file_path)
