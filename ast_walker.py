import ast
import json


def ast_to_dict(root):
    out = dict()
    for node in ast.walk(root):
        if isinstance(node, ast.AST):
            if isinstance(node, ast.operator):
                connections = node._fields
    
    out['_type'] = node.__class__.__name__
    for attr in dir(node):
        if attr.startswith("_"):
            continue
        out[attr] = get_value(getattr(node, attr))
    return out

def get_value(attr_value):
    print(attr_value)
    if attr_value is None:
        return attr_value
    if isinstance(attr_value, BUILTIN_PURE):
        return attr_value
    if isinstance(attr_value, BUILTIN_BYTES):
        return decode_bytes(attr_value)
    if isinstance(attr_value, BUILTIN_STR):
        return decode_str(attr_value)
    if isinstance(attr_value, complex):
        return str(attr_value)
    if isinstance(attr_value, list):
        return [get_value(x) for x in attr_value]
    if isinstance(attr_value, AST):
        return ast2json(attr_value)
    if isinstance(attr_value, type(Ellipsis)):
        return '...'
    else:
        raise Exception("unknown case for '%s' of type '%s'" % (attr_value, type(attr_value)))

if __name__ == "__main__":
    print(ast_to_dict(ast.parse('x = 1; y = 2', mode='single')))