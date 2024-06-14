import ast
from pyodide.ffi import create_proxy, to_js
import ast
import js

def get_render_ast(a,b):
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
            js.render(to_js(p))


def ast_to_dict(node):
    out = dict()
    name = type(node).__name__
    out["name"] = name

    if isinstance(node, ast.Constant):
        out["value"] = node.value
    elif isinstance(node, ast.BinOp):
        out["name"] = type(node.op).__name__
    elif isinstance(node, ast.BoolOp):
        out["name"] = type(node.op).__name__
    elif isinstance(node, ast.Call):
        out["name"] = str("Call" +node.func)
    # more data for various AST node types.
    # if node.id is not None:
    #     out["id"] = node.id


    out["children"] = []
    for child in ast.iter_child_nodes(node):
        out["children"].append(ast_to_dict(child))

    return out

js.code.on("change",create_proxy(get_render_ast))
