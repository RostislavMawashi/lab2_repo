
ivan = {

    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],

}
emps = [ivan,darja]
age=18

def children18 (emps, age):
    for emp in emps:
        childrens = emp['children']
        for child in childrens:
            if child ['age'] > age:
                print (emp['name'])

children18 (emps,age)
