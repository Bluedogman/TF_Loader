# Change all cli things to gui based in another version
from pathlib import Path
import sys, json


class Mod:  # Is this a bad name?
    def __init__(self, name: str, location: Path, description: str = "") -> None:
        self.active = False  # All mods are disabled by default, willing to change
        self.name = name
        self.path = location
        self.description = description


def set_custom_path():
    return Path(input("Enter the path to tf/custom "))


def main():
    name = input("What is ur name? ")
    mods: list[Mod] = []
    custom_path = set_custom_path()
    script_path = Path(__file__).resolve()
    disabled_path = Path()
    config_path = script_path / "config.json"

    def make_mod():  # Make a mod object from a file path
        mod_path = Path(input("Mod file path: "))
        mod_name = mod_path.name
        print(mod_name)
        mods.append(Mod(mod_name, mod_path))

    def close():
        closing_data = json.dumps(
            {
                "username": name,
                "tf_custom_path": custom_path,
                "script_path": script_path,
            }
        )
        config_path.write_text(closing_data, "UTF-8")
        sys.exit()

    running = True  # almost never use this tbh
    while running:
        user_input = input(f"[{name}]$ ").strip().lower()

        if user_input == "q" or user_input == "quit":
            close()
        elif user_input == "make mod":
            make_mod()
        elif user_input == "ls":
            for mod in mods:
                print(f"name:{mod.name}\npath:{mod.path}\nstatus:{mod.active}")
                """
                name:<>
                path:<>
                status:<>
                """
        elif "enable" in user_input:
            user_split = user_input.split(" ")
            mod_of_choice = user_split[1]  # This is just a string of the file name
            for mod in mods:  # ehh idk how I feel about this tbh
                if mod.name == mod_of_choice:
                    # WOW WE FOUND IT!!!!!11!1..
                    mod.active = True
                    continue
            print("well shoot, it looks like I didn't find it")


main()
