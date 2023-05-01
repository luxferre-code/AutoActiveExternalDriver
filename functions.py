import os
import subprocess

class Drivers:
    def __init__(self) -> None:
        self.__drivers: set = set()
        self.update()

    def update(self) -> None:
        returned: str = subprocess.check_output(["lsblk", "-l"]).decode("utf-8")
        liste: list = returned.split("\n")
        liste = self.__remove_all_disk(liste)
        liste = self.__remove_all_mounted(liste)
        liste = self.__remove_default(liste)
        self.__drivers = set([elt.split(" ")[0] for elt in liste])
        self.__drivers.remove("")

    def __remove_all_disk(self, liste: list) -> list:
        result: list = []
        for driver in liste:
            if("disk" not in driver.lower()):
                result.append(driver)
        return result
    
    def __remove_all_mounted(self, liste: list) -> list:
        result: list = []
        for driver in liste:
            if(not driver.__contains__("/")):
                result.append(driver)
        return result
    
    def __remove_default(self, liste: list) -> list:
        result: list = []
        for driver in liste:
            if(not driver.__contains__("NAME") or driver == "" or driver == "\n"):
                result.append(driver)
        return result

    def get(self) -> set:
        return self.__drivers
    
    def __str__(self) -> str:
        result: str = ""
        for driver in self.__drivers:
            result += driver + "\n"
        return result
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __len__(self) -> int:
        return len(self.__drivers)
    
    def __contains__(self, driver: str) -> bool:
        return driver in self.__drivers

if __name__ == "__main__":
    driver = Drivers()
    print(driver.get())