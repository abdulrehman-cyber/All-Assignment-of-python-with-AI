dict={
    "Name": "Abdul",
    "Age" : 26,
    "City" : "Lahore",
}
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("Age"))
dict.update({"Course": "AI"})
print(dict)
dict.pop("Age")
print(dict)
dict.popitem()
print(dict)
dict.clear()
print(dict)