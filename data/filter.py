import json
import jmespath

idcards = json.load(open("vo-idcard.json","r"))
query = root[*][?Name == 'ops']"

query = "root[(?Name.contains('dteam') || (?Name == 'ops')].IDCard[].gLiteConf[].FQANs[*].FQAN[][].FqanExpr"
exp = jmespath.compile(query)
filtered = exp.search(idcards)