import pickle
import os

doctype_to_keyword = {}  # mapping of doctypes to keywords in the filenames they associate with
with open("doc_types.txt", "r+") as f:
    for line in f.readlines():
        parts = line.split(":")
        doctype_to_keyword[parts[0]] = [term.strip() for term in parts[1].strip().split(",")]

# need to invert it so that lookup is a *bit* easier
kw_to_doctype = {}
for k, v in doctype_to_keyword.items():
    for kw in v:
        kw_to_doctype[kw] = k

pickle.dump({
    "type_to_kw": doctype_to_keyword, 
    "kw_to_type": kw_to_doctype,
    "doctypes": list(doctype_to_keyword.keys())
    }, open("doc_types.pkl", "wb+"))