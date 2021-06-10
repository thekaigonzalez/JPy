import os
import javascript.javascript_export


class Type:
    def __init__(self, typename: str, value):
        self.name = typename
        self.fexport = javascript.javascript_export.export("typeexport")
        self.value = value
    def build(self, alias: str):
        self.fexport.write("var __" + alias + " = " + self.value)

    def app_state(self, statement: str):
        self.fexport.write(statement + "\n")
    def close_app(self):
        self.fexport.close()
    def jsAssert(self, one: str, two: str):
        self.fexport.write('\nif (' + one + "!==" + two + ") { \n\t\tconsole.log(\"Assertion failed. " + one + "!=" + two + ". Program terminated \") \n} ")