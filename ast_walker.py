# import ast
#
# #
# # def get_value(attr_value):
# #     print(attr_value)
# #     if attr_value is None:
# #         return attr_value
# #     if isinstance(attr_value, BUILTIN_PURE):
# #         return attr_value
# #     if isinstance(attr_value, BUILTIN_BYTES):
# #         return decode_bytes(attr_value)
# #     if isinstance(attr_value, BUILTIN_STR):
# #         return decode_str(attr_value)
# #     if isinstance(attr_value, complex):
# #         return str(attr_value)
# #     if isinstance(attr_value, list):
# #         return [get_value(x) for x in attr_value]
# #     if isinstance(attr_value, AST):
# #         return ast2json(attr_value)
# #     if isinstance(attr_value, type(Ellipsis)):
# #         return '...'
# #     else:
# #         raise Exception("unknown case for '%s' of type '%s'" % (attr_value, type(attr_value)))
#
# if __name__ == "__main__":
#     print(ast_to_dict(ast.parse('x = 1; y = 2', mode='single')))
