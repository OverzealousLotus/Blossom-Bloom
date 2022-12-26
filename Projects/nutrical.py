'''Nutritional calculator'''

from time import sleep


class Assets():
    """Assets for our program."""

    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        self.user_choice = None
        self.calories = 0
        self.total_fat = 0
        self.transfat = 0
        self.polyfat = 0
        self.satfat = 0
        self.monofat = 0
        self.carbs = 0
        self.sugar = 0
        self.chloe = 0
        self.sodium = 0
        self.protein = 0

    def primer_menu(self):
        '''Main Menu of program'''
        self.user_choice = None
        print('<= Modify =>')
        print('<= View =>')
        print('<= Export =>')
        self.user_choice = input('What would you like to do?: ').upper()
        match self.user_choice:
            case "MODIFY":
                self.modify_menu()
            case "VIEW":
                self.view_info()
            case "EXPORT":
                self.export_info()
            case "EXIT":
                self.user_choice = "Finished"
            case _:
                print("Error, operation does not exist.")

    def caloric_calculator(self):
        """Caloric Calculations"""
        self.user_choice = None
        self.user_choice = int(input('Caloric Increase: '))
        self.calories += self.user_choice
        self.primer_menu()

    def transfat_calculator(self):
        """Transfat Calculations"""
        self.user_choice = None
        self.user_choice = float(input('Transfat increase: '))
        self.transfat += self.user_choice
        self.total_fat = self.transfat + self.satfat + self.polyfat + self.monofat
        self.primer_menu()

    def satfat_calculator(self):
        """Saturated Fat Calculations"""
        self.user_choice = None
        self.user_choice = float(input('Saturated fat increase: '))
        self.satfat += self.user_choice
        self.total_fat = self.transfat + self.satfat + self.polyfat + self.monofat
        self.primer_menu()

    def monofat_calculator(self):
        """Monounsaturated Fat Calculations"""
        self.user_choice = None
        self.user_choice = float(input('Monounsaturated fat increase: '))
        self.monofat += self.user_choice
        self.total_fat = self.transfat + self.satfat + self.polyfat + self.monofat
        self.primer_menu()

    def polyfat_calculator(self):
        """Polyunsaturated Fat Calculations"""
        self.user_choice = None
        self.user_choice = float(input('Polyunsaturated fat increase: '))
        self.polyfat += self.user_choice
        self.total_fat = self.transfat + self.satfat + self.polyfat + self.monofat
        self.primer_menu()

    def carb_calculator(self):
        """Carbohydrate Calculations"""
        self.user_choice = None
        self.user_choice = float(input('Carbohydrate increase: '))
        self.carbs += self.user_choice
        self.primer_menu()

    def sugar_calculator(self):
        """Sugar Calculations"""
        self.user_choice = None
        self.user_choice = float(input('Sugar increase: '))
        self.sugar += self.user_choice
        self.primer_menu()

    def chloe_calculator(self):
        """Cholesterol Calculations"""
        self.user_choice = None
        self.user_choice = float(input('Cholesterol increase: '))
        self.chloe += self.user_choice
        self.primer_menu()

    def sodium_calculator(self):
        """Sodium Calculations"""
        self.user_choice = None
        self.user_choice = float(input('Sodium increase: '))
        self.sodium += self.user_choice
        self.primer_menu()

    def protein_calculator(self):
        """Protein Calculations"""
        self.user_choice = None
        self.user_choice = float(input('Protein increase: '))
        self.protein += self.user_choice
        self.primer_menu()

    def modify_menu(self):
        '''Modification of values'''

        self.user_choice = None
        self.user_choice = str(input('Choose one of the following to modify: ').upper())

        match self.user_choice:
            case "CALORIES":
                self.caloric_calculator()
            case "TRANSFAT":
                self.transfat_calculator()
            case 'SATURATED':
                self.satfat_calculator()
            case 'MONOUNSATURATED':
                self.monofat_calculator()
            case 'POLYUNSATURATED':
                self.polyfat_calculator()
            case 'CARBOHYDRATES':
                self.carb_calculator()
            case 'SUGAR':
                self.sugar_calculator()
            case 'CHOLESTEROL':
                self.chloe_calculator()
            case 'SODIUM':
                self.sodium_calculator()
            case 'PROTEIN':
                self.protein_calculator()
            case "CANCEL":
                self.primer_menu()
            case _:
                print('Invalid macro/micro.')
                self.primer_menu()

    def view_info(self):
        '''View nutritional information'''
        print("\n\n")

        print('<==Calories==>')
        print(f'|Current: {self.calories}Kcal \n')

        print('<==Fat==>')
        print(f'|Current Total: {self.total_fat}g')
        print(f'=>|Transfat: {self.transfat}g')
        print(f'=>|Saturated: {self.satfat}')
        print(f'=>|Monounsaturated: {self.monofat}g')
        print(f'=>|Polyunsaturated: {self.polyfat}g \n')

        print('<==Carbohydrates==>')
        print(f'|Carbs: {self.carbs}g')
        print(f'|Sugars: {self.sugar}g')

        print('<==Misc Macros==>')
        print(f'|Cholesterol: {self.chloe}mg')
        print(f'|Sodium: {self.sodium}mg')
        print(f'|Protein: {self.protein}g')

        print("\n\n")
        self.primer_menu()

    def export_info(self):
        '''Export nutritional information to file'''

    def main(self):
        """Primary execution function of our program."""
        try:
            print('Starting program...')
            sleep(2)
            while self.user_choice != 'Finished':
                self.primer_menu()
            print('Operations completed. Exiting...')
            sleep(1)
        except KeyboardInterrupt:
            print('\nCalculations interrupted by user.')
        except ValueError:
            print('\nPlease use integers or decimals for incrementation')
        except RuntimeError:
            print('\nAn unknown error has occurred. Please try again.')


Nutrients = Assets()


if __name__ == "__main__":
    Nutrients.main()
