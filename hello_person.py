def hello(name, lang):
    greetings = {
        "EL": "HELLO",
        "SP": "HALO",
        "VN": "XIN CHAO"
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)
    
if __name__ == "__main__":
    

    import argparse

    parser = argparse.ArgumentParser(
        description="Provides!"
    )

    parser.add_argument(
        "-n","--name", metavar="name",
        required=True, help="Call name"
    )
    
    parser.add_argument(
        "-l","--lang", metavar="language",
        required=True, choices=["EL","SP","VN"],
        help="The language greeting"
    )

    args = parser.parse_args()

    hello(args.name, args.lang)

    # msg = f"Hello {args.name}"

    # print(msg)