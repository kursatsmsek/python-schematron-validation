from saxonche import *

# XML dosyasını dışarıdan oku
def read_xml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# XSLT ile validation işlemi
def validate_xml_with_xslt(xml_file_path, xslt_file_path):
    with PySaxonProcessor(license=False) as proc:
        xsltproc = proc.new_xslt30_processor()  # XSLT 3.0 işlemciyi başlatıyoruz

        # Dışarıdan XML dosyasını yükle
        xml_text = read_xml_file(xml_file_path)
        document = proc.parse_xml(xml_text=xml_text)

        # Validation XSLT dosyasını derle
        executable = xsltproc.compile_stylesheet(stylesheet_file=xslt_file_path)

        # XSLT dönüşümünü gerçekleştir ve çıktı al
        output = executable.transform_to_string(xdm_node=document)

        # Çıktıyı yazdır
        print(output)

# XML ve XSLT dosyalarının yolları
xml_file_path = 'input.xml'  # Dışarıdan alınacak XML dosyasının yolu
xslt_file_path = 'schematron.xslt'  # XSLT dosyasının yolu

# XML dosyasını XSLT ile doğrulama işlemi yap
validate_xml_with_xslt(xml_file_path, xslt_file_path)
