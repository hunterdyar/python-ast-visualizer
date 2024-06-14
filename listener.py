from pyodide.ffi import create_proxy, to_js
import js

def do_change(a,b):
    valid = False
    try:
        p = ast_to_dict(ast.parse(js.code.doc.getValue('\n')))
        valid = True
    except (SyntaxError,NameError):
        pass
    except TypeError:
        pass
    finally:
        if(valid):
            js.render(p)

js.code.on("change",create_proxy(do_change))
