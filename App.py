# Change all cli things to gui based in another version
from pathlib import Path
import sys, json
from typing import Optional

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)


class Mod:  # The data that will be displayed when viewing a mod
    def __init__(
        self, name: str, files: Optional[list[Path]] = None, description: str = ""
    ) -> None:
        self.active = False  # All mods are disabled by default, willing to change
        self.name = name
        self.description = description
        self.icon = None
        if files is not None:
            # Some mods have multiple files to them, or even multiple directories...
            self.files: list[Path] = files
        else:
            self.files = []

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


def toggle_mod(mods: list[Mod], user_input: str):
    user_split = user_input.split(" ")
    mod_of_choice = " ".join(user_split[1:])
    mod_of_choice.strip()
    for mod in mods:
        print(mod.name)
        if mod_of_choice.lower() == mod.name.lower():
            if user_split[0] == "enable":
                mod.active = True
            elif user_split[0] == "disable":
                mod.active = False
            else:
                print(
                    "68 74 74 70 73 3A 2F 2F 6D 75 73 69 63 2E 79 6F 75 74 75 62 65 2E 63 6F 6D 2F 77 61 74 63 68 3F 76 3D 7A 61 5F 6D 37 42 45 61 50 76 73 26 73 69 3D 64 51 65 77 38 42 7A 57 38 73 30 63 65 71 74 41"
                )
            return
        continue
    print("well shoot, it looks like I didn't find it")


class TFLoaderApp:
    def __init__(
        self,
        script_path: Path,
        config_path: Path,
        disabled_path: Path,
    ) -> None:
        super().__init__()
        self.script_path = script_path
        self.config_path = config_path
        self.disabled_path = disabled_path
        self.running = False
        if config_path.exists():
            with open(self.config_path, "r") as f:
                self.config = json.load(f)
        else:
            self.config = json.loads(self.load_config())
        self.name = self.config.get("username")
        self.custom_path = Path(self.config.get("tf_custom_path"))
        self.mods: dict[str, Mod] = {}

    def run(self):
        if not (self.script_path / "coconut.jpeg").exists():
            self.close()
        self.running = True
        self.load_tf_custom()
        while self.running:
            user_input = input(f"[{self.name}]$ ").strip()
            if user_input == "q" or user_input == "quit":
                self.close()
            elif user_input == "make mod":
                # make_mod()
                pass
            elif user_input == "reload":
                self.load_tf_custom()
            elif user_input == "ls":
                for mod in self.mods.values():
                    print(
                        f"---\nname:{mod.name}\nfiles:{mod.files}\nstatus:{mod.active}"
                    )
                    """
                    name:<>
                    files:<>
                    status:<>
                    """
            elif user_input == "clear" or user_input == "clr":
                self.clear_mods()
            elif "enable" in user_input or "disable" in user_input:
                toggle_mod(list(self.mods.values()), user_input)

    def load_tf_custom(self):
        self.mods.clear()
        # Reloads all the files and directories in custom and adds unfound mods into mods
        for item in self.custom_path.iterdir():
            mod_name = item.stem.split(".")[0]
            if mod_name.lower() not in self.mods.keys():
                mod = Mod(mod_name)
                self.mods[mod_name.lower()] = mod
            else:
                mod = self.mods[mod_name.lower()]
            mod.files.append(item)

    def clear_mods(self):
        pass

    def close(self):

        closing_data = json.dumps(
            {
                "username": self.name,
                "tf_custom_path": str(self.custom_path),
                "script_path": str(self.script_path),
            }
        )
        self.config_path.write_text(closing_data, "UTF-8")
        sys.exit()

    def load_config(self):
        print("Leave an input blank if not changing.")
        name = input("What is your name? ")
        custom_path = input("What is the path to tf/custom? ")

        for idx, item in enumerate([name, custom_path]):
            if self.config_path.exists():
                if item == "":
                    match idx:
                        case 0:
                            item = self.config.get("username")
                        case 1:
                            item = self.config.get("tf_custom_path")
            # If config doesn't exist, then we re-prompt you if you left the field blank
            else:
                match idx:
                    case 0:
                        if item.strip() == "":
                            item = input("What is your name? ")
                    case 1:
                        if item.strip() == "":
                            item = input("What is the path to tf/custom? ")
        data = json.dumps(
            {
                "username": name,
                "tf_custom_path": str(custom_path),
                "script_path": str(self.script_path),
            }
        )
        return data


def main():
    script_path = Path(__file__).resolve().parent
    config_path = script_path / "config.json"
    disabled_path = script_path / "mods/"

    App_manager = TFLoaderApp(script_path, config_path, disabled_path)
    # try:
    App_manager.run()
    # except:
    #     app.close()


main()
