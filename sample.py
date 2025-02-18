from saxonche import *

with PySaxonProcessor(license=False) as proc:
    print("SaxonC Sample in Python")
    print(proc.version)
    # print(dir(proc))
    xdmAtomicval = proc.make_boolean_value(False)

    xsltproc = proc.new_xslt30_processor()
    outputi = xsltproc.transform_to_string(source_file="cat.xml", stylesheet_file="test.xsl")
    print("Test1 =", outputi)
    document = proc.parse_xml(xml_text="<out><person>text1</person><person>text2</person><person>text3</person></out>")

    executable = xsltproc.compile_stylesheet(
        stylesheet_text="<xsl:stylesheet xmlns:xsl='http://www.w3.org/1999/XSL/Transform' version='2.0'> <xsl:param name='values' select='(2,3,4)' /><xsl:output method='xml' indent='yes' /><xsl:template name='main'><output><xsl:value-of select='//person[1]'/><xsl:for-each select='$values' ><out><xsl:value-of select='. * 3'/></out></xsl:for-each></output></xsl:template></xsl:stylesheet>")
    if (executable == None):
        print('Executable is None\n')
        if (xsltproc.exception_occurred):
            print("Error message:" + xsltproc.error_message)
            exit()
    executable.set_global_context_item(xdm_item=document)

    output2 = executable.call_template_returning_string("main")
    print(output2)

