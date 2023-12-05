from random import choice

_1_ = "One"

_2_ = "Two"

_3_ = "Three"


def randomFF():
    
    ffs = [
        "OK",
        "OK OK",
        "OK OK OK",
        "OK OK OK OK",
    ]
    
    index = choice("0123")
    
    print(ffs[int(index)])
    
    
# if __name__ == "__main__":
#     randomFF()