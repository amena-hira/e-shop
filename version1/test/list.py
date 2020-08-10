lst = [{'id':'1234','name':'Jason'},
        {'id':'2345','name':'Tom'},
        {'id':'3456','name':'Art'}]

def build_dict(seq, key):
    return dict((d[key], dict(d, index=index)) for (index, d) in enumerate(seq))

info_by_name = build_dict(lst, key="name")
tom_info = info_by_name.get("Tom")
print(tom_info)