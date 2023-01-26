def main() -> None:
    """print bottle of beer on the wall"""
    for beer in range(99, 2, -1):
        print(gettext("{} bottles of beer on the wall,")).format(beer)
        print(gettext"{} bottles of beer on the wall,")).format(beer)
        print(gettext("Take one down pass it around"))
        print(gettext("{} bottles of beer on the wall,")).format(beer -1)
    print(gettext("{} bottles of beer on the wall,")).format(beer)
    print(gettext("{} bottles of beer on the wall,")).format(beer)
    print("Take one down pass it around")
    print("No more bottles of beer on the wall,")


if __main__ == "__main__":
    main()

