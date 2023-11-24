band = {
    "vocals": "Me",
    "guitar": "Him"
}
band2 = dict(vocals = "Me 1", guitar = "Him 1")


print(band)
print(band2)
print(type(band))
print(len(band2))


#Access items
print(band["guitar"], band["vocals"])
print(band.get("vocals"))