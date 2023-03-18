import clang.cindex

operators = dict()
operands = dict()


def call_expression_visitor(node):
    for child in node.get_children():
        call_expression_visitor(child)
    if node.kind == clang.cindex.CursorKind.CALL_EXPR or node.kind == clang.cindex.CursorKind.FUNCTION_DECL or\
            node.kind == clang.cindex.CursorKind.CLASS_DECL or node.kind == clang.cindex.CursorKind.STRUCT_DECL or\
            node.kind == clang.cindex.CursorKind.STRUCT_DECL or node.kind == clang.cindex.CursorKind.UNION_DECL or\
            node.kind == clang.cindex.CursorKind.ENUM_DECL or node.kind == clang.cindex.CursorKind.FIELD_DECL or\
            node.kind == clang.cindex.CursorKind.UNEXPOSED_DECL or\
            node.kind == clang.cindex.CursorKind.COMPOUND_ASSIGNMENT_OPERATOR or\
            node.kind == clang.cindex.CursorKind.DO_STMT or\
            node.kind == clang.cindex.CursorKind.CXX_CATCH_STMT or node.kind == clang.cindex.CursorKind.CXX_TRY_STMT or\
            node.kind == clang.cindex.CursorKind.SEH_TRY_STMT or node.kind == clang.cindex.CursorKind.SEH_EXCEPT_STMT:
        operators.__setitem__(node.spelling, operators[node.spelling] + 1 if node.spelling in operators else 1)
    if node.kind == clang.cindex.CursorKind.IF_STMT:
        operators.__setitem__('if', operators['if'] + 1 if 'if' in operators else 1)
    if node.kind == clang.cindex.CursorKind.RETURN_STMT:
        operators.__setitem__('return', operators['return'] + 1 if 'return' in operators else 1)
    if node.kind == clang.cindex.CursorKind.CASE_STMT:
        operators.__setitem__('case', operators['case'] + 1 if 'case' in operators else 1)
    if node.kind == clang.cindex.CursorKind.SWITCH_STMT:
        operators.__setitem__('switch', operators['switch'] + 1 if 'switch' in operators else 1)
    if node.kind == clang.cindex.CursorKind.WHILE_STMT:
        operators.__setitem__('while', operators['while'] + 1 if 'while' in operators else 1)
    if node.kind == clang.cindex.CursorKind.FOR_STMT:
        operators.__setitem__('for', operators['for'] + 1 if 'for' in operators else 1)
    if node.kind == clang.cindex.CursorKind.CXX_FOR_RANGE_STMT:
        operators.__setitem__('for range', operators['for range'] + 1 if 'for range' in operators else 1)
    if node.kind == clang.cindex.CursorKind.GOTO_STMT:
        operators.__setitem__('goto', operators['goto'] + 1 if 'goto' in operators else 1)
    if node.kind == clang.cindex.CursorKind.BREAK_STMT:
        operators.__setitem__('break', operators['break'] + 1 if 'break' in operators else 1)
    if node.kind == clang.cindex.CursorKind.DEFAULT_STMT:
        operators.__setitem__('default', operators['default'] + 1 if 'default' in operators else 1)
    if node.kind == clang.cindex.CursorKind.PAREN_EXPR:
        operators.__setitem__('()', operators['()'] + 1 if '()' in operators else 1)
    if node.kind == clang.cindex.CursorKind.BINARY_OPERATOR:
        children_list = [i for i in node.get_children()]
        assert len(children_list) == 2
        left_offset = len([i for i in children_list[0].get_tokens()])
        op = [i for i in node.get_tokens()][left_offset].spelling
        operators.__setitem__(op, operators[op] + 1 if op in operators else 1)
    if node.kind == clang.cindex.CursorKind.UNARY_OPERATOR:
        op = ''
        operators.__setitem__(op, operators[op] + 1 if op in operators else 1)

    if node.kind == clang.cindex.CursorKind.VAR_DECL or node.kind == clang.cindex.CursorKind.PARM_DECL or\
            node.kind == clang.cindex.CursorKind.BLOCK_EXPR or\
            node.kind == clang.cindex.CursorKind.FLOATING_LITERAL or\
            node.kind == clang.cindex.CursorKind.STRING_LITERAL or\
            node.kind == clang.cindex.CursorKind.COMPOUND_LITERAL_EXPR:
        operands.__setitem__(node.spelling, operands[node.spelling] + 1 if node.spelling in operands else 1)
    if node.kind == clang.cindex.CursorKind.INTEGER_LITERAL:
        operands.__setitem__(node.spelling, operands[node.spelling] + 1 if node.spelling in operands else 1)


index = clang.cindex.Index.create()

tu = index.parse('my_source.cpp')

root = tu.cursor
call_expression_visitor(root)

print(operators)
print(operands)
