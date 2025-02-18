from fastapi import FastAPI

from sample import validate_xml_with_xslt

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    xml_file_path = 'input.xml'
    xslt_file_path = 'schematron.xslt'

    validate_xml_with_xslt(xml_file_path, xslt_file_path)
    return {"message": f"Hello {name}"}
