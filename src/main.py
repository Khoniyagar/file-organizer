from known_dir import known_dir
from custom_dir import custom_dir


def main():
    print("1- Use this directory")
    print("2- Custom directory")

    mode = input("Enter the mode: ")

    if mode == "1":
        known_dir()
    elif mode == "2":
        custom_dir()
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()