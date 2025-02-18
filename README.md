This project demonstrates how to use Saxon-CE (Saxon 9.9 or later) in Python to perform XML validation using XSLT and Schematron techniques. The validation is achieved by transforming an XML document through an XSLT stylesheet, which checks certain conditions in the XML data.

Features:
XML Validation with XSLT: The primary functionality of the project is to validate an XML document using a predefined XSLT stylesheet. The XSLT checks the length of <item> elements and outputs errors for items that are too short.

External XML Input: The XML data is read from an external file, which allows you to easily test with different XML files. This flexibility enables you to validate multiple XML documents against the same XSLT rules.

Python Integration with Saxon-CE: The project uses Saxon-CE, a Python wrapper for the Saxon XSLT processor, to execute the transformation and validation. The Saxon processor runs the XSLT, and the result is printed out.

How to Use:
Clone the repository to your local machine.

Place the XML file (e.g., input.xml) and the XSLT file (e.g., validate.xslt) in the same directory as the Python script.

Run the Python script to perform the validation. The script will read the XML from the file, apply the XSLT transformation, and output the results.

Example command:
python sample.py
Modify XML or XSLT: You can modify the XML input or the XSLT validation rules to suit your needs and rerun the validation process.

Files in the Repository:
validate.xslt: The XSLT stylesheet used for validation.
input.xml: Sample XML data to be validated.
sample.py: Python script that reads the XML, applies XSLT transformation, and prints the validation results.
