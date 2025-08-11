auto={
    "marca":"ford",
    "modelo":"mustang",
    "año":2022,
    "color": "naranja",
    "pais": "estados unidos",
    "auto_deportivo":"fake"
}
print(auto)
print(auto["modelo"])
auto["año"]=2023
auto["color"]="rojo"
auto["auto_deportivo"]="true"
del auto["modelo"]
auto.pop("marca")
print(auto)
