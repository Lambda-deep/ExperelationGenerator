import csv
from uml import Uml 
from uml import Member
from uml import Relation


def main():
    mems = []
    rels = []
    
    csv_member = open("src\data\member.csv", "r")
    f = csv.DictReader(csv_member, delimiter=",")
    for row in f:
        mems.append(Member(**row))

    csv_relation = open("src\data\\relation.csv", "r")
    f = csv.DictReader(csv_relation, delimiter=",")
    for row in f:
        rels.append(Relation(**row))

    uml = Uml("相関図")
    uml.addMembers(mems)
    uml.addRelations(rels)
    
    f = open('src\export\experelation.pu', 'w')
    f.write(uml.toString())

main()