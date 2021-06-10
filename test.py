import javascript.javascript_types as jsexports

mytype = jsexports.Type("number", "\"Hello!\"")

mytype.build("c")
mytype.app_state("\nlet a = 0\nlet b = 0")
mytype.app_state("\nlet d = 0\nlet c = 0")
mytype.app_state("\nlet e = 2\nlet f = 0")

mytype.jsAssert("d", "c")
mytype.jsAssert("a", "b")
mytype.jsAssert("e", "f")

mytype.close_app()
