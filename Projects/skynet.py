"""Incremental Tycoon with Terminator theme."""

from time import sleep

# Variables


class SysResources():
    """Defines system resources"""

    # pylint: disable=too-many-instance-attributes,too-many-arguments

    def __init__(
            self,
            user_choice: str,
            poweroff: bool,
            titan: float | int,
            t800: int,
            titan_lvl: int,
            hk101: int,
            core_lvl: int,
            core_cost: float | int,
            prod_cost: float | int
            ):
        self.user_choice = user_choice
        self.poweroff = poweroff
        self.titan = titan
        self.titan_lvl = titan_lvl
        self.t800 = t800
        self.hk101 = hk101
        self.core_lvl = core_lvl
        self.core_cost = core_cost
        self.prod_cost = prod_cost

    def produce_start(self):
        """Start production of resource."""
        produce_time: int = int(input('Runtime: '))
        print('\033[0;37;41m < Now producing for:', str(produce_time) + 's >')
        while produce_time > 0:
            sleep(1)
            self.titan += (0.0 + self.titan_lvl)
            produce_time -= 1
            print(str(self.titan) + 'KG of Titanium have been produced.')

    def eval_start(self):
        """Begin evaluation of player statistics."""

        print('')
        print(f'| {self.titan} KG of Titanium awaiting usage. | \n')
        # print(f'| {self.combat_data} Combat Files prepared. | \n')
        print(f'| {self.t800} T-800s awaiting combat orders. | \n')
        print(f'| {self.hk101} QHK-101s awaiting combat orders. | \n')

    def start_menu(self):
        """initiate the start menu"""
        print('\033[1;37;41m "Produce" \033[0;37;41m to produce Titanium.')
        print('\033[1;37;41m "Evaluate" \033[0;37;41m to procure Logistical Data.')
        print('\033[1;37;41m "Assemble" \033[0;37;41m to assemble Terminators.')
        print('\033[1;37;41m "Attack" \033[0;37;41m to begin an attack on base.')
        print('\033[1;37;41m "Adjust" \033[0;37;41m to improve TP, or your Core.')
        self.user_choice = str(input('\033[0;37;41m ~/: ')).upper()
        match self.user_choice:
            case "PRODUCE":
                self.produce_start()
            case "EVALUATE":
                self.eval_start()
            case "ASSEMBLE":
                self.assembly_menu()
            case "ATTACK":
                self.attack_menu()
            case "ADJUST":
                self.adjust_menu()
            case "EXIT":
                self.poweroff = True
            case _:
                print("Error, command not recognized.")

    def assembly_menu(self):
        """Assembly Menu to procure Terminators."""
        print(f"T-800 Count: {self.t800} | Cost: 5KG")
        print(f"HK-101 Count: {self.hk101} | Cost: 10KG")
        self.user_choice = str(input("What would you like to procure?")).upper()
        if self.user_choice == "T800":
            self.user_choice = int(input("How many?"))
            if self.titan >= 5 * self.user_choice:
                self.t800 += self.user_choice
                self.titan -= 5 * self.user_choice
                self.start_menu()
            else:
                print("Insufficient titanium.")
                self.start_menu()
        elif self.user_choice == "HK101":
            self.user_choice = int(input("How many?"))
            if self.titan >= 10 * self.user_choice:
                self.hk101 += self.user_choice
                self.titan -= 10 * self.user_choice
                self.start_menu()
            else:
                print("Insufficient titanium.")
                self.start_menu()

    def adjust_menu(self):
        """Grant player optional upgrades"""
        print('|', 'Central Core:', self.core_lvl, '|')
        print(f'< {self.core_cost} KG of Titanium required to enhance Core. > \n')
        print(f'| Recycling Center {self.titan_lvl} |')
        print(f'< {self.prod_cost} KG of Titanium required to enhance TP. > \n')
        print('< Abort? >')
        self.user_choice = str(input('What should be enhanced?: ')).upper()
        if self.user_choice == 'CENTRAL':
            if self.titan < self.core_cost:
                print('Insufficient amount of Titanium. Operation aborted.')
                self.start_menu()
            self.core_lvl += 1
            self.titan -= self.core_cost
            self.core_cost = (self.core_lvl * 2 * 10)
        elif self.user_choice == 'RECYCLING':
            if self.titan < self.prod_cost:
                print('Insufficient amount of Titanium. Operation aborted.')
                self.start_menu()
            self.titan_lvl += 1
            self.titan -= self.prod_cost
            self.prod_cost = (self.titan_lvl * 2 * 5)
        elif self.user_choice == 'ABORT':
            print('Operation aborted.')
            self.start_menu()
        else:
            print('Error, process not recognized.')

    def attack_menu(self):
        """Open attack options"""
        print('| Alpha Fort |')
        print(f'< Resistance Marine Count: {alpha_fort.infantry} >')
        print(f'< Resistance Vehicle Count: {alpha_fort.vehicles} >')
        print(f'< Fortress Rank: {alpha_fort.fort_level} >')
        self.user_choice = input('Confirm?: ').upper()
        if self.user_choice == 'ALPHA':
            print('Attack initiated...')
            sleep(1)
            alpha_fort.combat()
            print('Analyzing combat data..')
            # self.combat_data += alpha_fort.data_amount
            print(f'{alpha_fort.data_amount} data procured.')
            print('Finished. Returning to base.')
            self.start_menu()
        elif self.user_choice == 'ABORT':
            print('Operation aborted.')
            self.start_menu()
        else:
            print('Error, settlement does not exist.')
            self.attack_menu()


resources = SysResources(
    "",
    False,
    0,
    0,
    1,
    0,
    1,
    10,
    10)


class HostileResources:
    """Defines variables used by hostile forces."""

    # pylint: disable=too-few-public-methods

    def __init__(
            self,
            infantry: int,
            vehicles: int,
            fort_level: int,
            data_amount: float | int
            ):
        self.infantry = infantry
        self.vehicles = vehicles
        self.fort_level = fort_level
        self.data_amount = data_amount

    def combat(self):
        """Calculates combat results"""
        while self.infantry > 0 and resources.t800 > 0:
            if self.infantry <= 0 < resources.t800:
                print('All hostile forces eliminated.')
                sleep(1)
                print('Combat data procured.')
            elif self.infantry > 0 >= resources.t800:
                print('All combat units destroyed. Returning to base.')
                sleep(1)
                print('Returned.')
                resources.start_menu()
            print(f'Engaging {resources.user_choice} fortress...')
            sleep(1)
            self.infantry -= 2
            resources.t800 -= 1
            print(f'{self.infantry} hostile forces remain.')
            print(f'{resources.t800} functional units remain.')


# Objects

alpha_fort = HostileResources(10, 0, 1, 3)

# Game start

if __name__ == "__main__":
    print('\033[0;37;41m Initializing...')
    sleep(3)
    print('\033[1;37;41m Finished...')
    print('\033[0;37;41m Booting up Central Core...')
    sleep(3)
    print('\033[1;37;41m Finished...')
    print('\033[0;37;41m Fetching Primary Directives...')
    sleep(2)
    print('\033[1;37;41m Finished...')
    print('\033[0;37;41m Pinging external factories...')
    sleep(2)
    print('\033[1;37;41m ----- Skynet Online. -----')

    while resources.poweroff is not True:
        if resources.poweroff is True:
            print('Cyberdyne Systems Exit Code: 101')
            break
        resources.start_menu()
