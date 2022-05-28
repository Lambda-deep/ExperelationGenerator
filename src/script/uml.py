from functools import singledispatch, update_wrapper
START_TAG = "@startuml name"
END_TAG = "@enduml"

class Uml:
    title = ""
    members = {}
    relations = {}

    def __init__(self, title):
        self.title = title

    def addMember(self, member):
        self.members[member.key] = member

    def addMembers(self, members):
        for member in members:
            self.addMember(member)

    def addRelation(self, rel):
        self.relations[rel.relNum] = rel

    def addRelations(self, rels):
        for rel in rels:
            self.addRelation(rel)

    def toStringMember(self):
        ret = ""
        for k,m in self.members.items():
            ret += f"object {m.name} {m.color}" + " {\n"
            if (m.color != ""): ret += (f"color = {m.color}\n")
            if (m.arms != ""): ret += (f"arms = {m.arms}\n")
            if (m.job != ""): ret += (f"job = {m.job}\n")
            ret += "}\n"
        return ret

    def toStringRelation(self):
        ret = ""
        for k,r in self.relations.items():
            ret += self.members[r.fromKey].name
            ret += f" -{r.style}-> "
            ret += self.members[r.toKey].name
            ret += f" : {r.note}\n"
        return ret

    def toString(self):
        ret = START_TAG + "\n"
        ret += f"title {self.title}\n"
        ret += "skinparam ObjectBorderColor #000\n\n"

        ret += self.toStringMember()
        ret += "\n"
        ret += self.toStringRelation()

        ret += END_TAG

        return ret

class Member:
    key = ""
    name = ""
    color = ""
    arms = ""
    job = ""

    def __init__(self, key, name, color, arms, job):
        self.key = key
        self.name = name
        self.color = color
        self.arms = arms
        self.job = job

class Relation:
    relNum = ""
    fromKey = ""
    toKey = ""
    style = ""
    note = ""

    def __init__(self, relNum, fromKey, toKey, style, note):
        self.relNum = relNum
        self.fromKey = fromKey
        self.toKey = toKey
        self.style = f"[{style}]"
        self.note = note
    
    def toString(self):
        ret = ""
        ret += f"relNum = {self.relNum}\n"
        ret += f"note = {self.note}\n"

        return ret