import requests
import json

URL = "https://tenbis-static.azureedge.net/restaurant-menu/19156_en"


class _Menu:
    """
    This class is a singleton class - responsible for all the menu data
    """
    menu = None

    def __new__(cls, *args, **kwargs):
        """
        Initialize _Menu class
        :param args:
        :param kwargs: cls of the menu
        """
        try:
            if cls.menu is None:
                response = json.loads(requests.get(URL).text)
                cls.menu = response['categoriesList']
                return cls
            else:
                return cls
        except Exception as e:
            print(e)
            print('problem with getting the data')

    @classmethod
    def update(cls):
        """
        update menu
        :return: cls of the menu
        """
        response = json.loads(requests.get(URL).text)
        cls.menu = response['categoriesList']
        print("update menu")
        return cls

    @classmethod
    def __to_list_meal_by_cat(cls, category) -> list:
        """
        private function
        get category name and return all the meal in this category
        :param category: str - category name
        :return: list of dict
        """
        meals = []
        all_meals = list(filter(lambda elem: elem['categoryName'] == category, cls.menu))
        all_meals = all_meals[0]['dishList']
        for meal in all_meals:
            meals.append({'id': meal['dishId'],
                          'name': meal['dishName'],
                          'description': meal['dishDescription'],
                          'price': int(meal['dishPrice'])})
        return meals

    @classmethod
    def __get_specific_meal_by_cat(cls, category, meal_id) -> dict:
        """
        private function
        get category name and id of a meal - return dict of meal
        :param category: str - category name
        :param meal_id: int - id of the meal
        :return: dict
        """
        all_meals = list(filter(lambda elem: elem['categoryName'] == category, cls.menu))
        all_meals = all_meals[0]['dishList']
        specific_meal = list(filter(lambda elem: elem['dishId'] == meal_id, all_meals))
        if len(specific_meal) == 0:
            return {}
        else:
            specific_meal = specific_meal[0]
            meal = {'id': specific_meal['dishId'],
                    'name': specific_meal['dishName'],
                    'description': specific_meal['dishDescription'],
                    'price': int(specific_meal['dishPrice'])}
            return meal

    @classmethod
    def get_drinks(cls) -> list:
        """
        return list of all drinks from the menu
        :return: list - list of dict if succeed, else otherwise
        """
        try:
            return cls.__to_list_meal_by_cat('Drinks')
        except Exception as e:
            print(e)
            return None

    @classmethod
    def get_drink(cls, drink_id) -> dict:
        """
        get id of a drink and return the drink info
        :param drink_id: int - id of the drink
        :return: dict - information about the drink
        """
        try:
            return cls.__get_specific_meal_by_cat('Drinks', drink_id)
        except Exception as e:
            print(e)
            return None

    @classmethod
    def get_pizzas(cls) -> list:
        """
        return list of all pizzas from the menu
        :return: list - list of dict if succeed, else otherwise
        """
        try:
            return cls.__to_list_meal_by_cat('Pizzas')
        except Exception as e:
            print(e)
            return None

    @classmethod
    def get_pizza(cls, pizza_id) -> dict:
        """
        get id of a pizza and return the pizza info
        :param pizza_id: id of the pizza
        :return: dict - information about the pizza
        """
        try:
            return cls.__get_specific_meal_by_cat('Pizzas', pizza_id)
        except Exception as e:
            print(e)
            return None

    @classmethod
    def get_desserts(cls) -> list:
        """
        return list of all desserts from the menu
        :return: list - list of dict if succeed, else otherwise
        """
        try:
            return cls.__to_list_meal_by_cat('Desserts')
        except Exception as e:
            print(e)
            return None

    @classmethod
    def get_dessert(cls, dessert_id) -> dict:
        """
        get id of a dessert and return the pizza info
        :param dessert_id: int - id of the dessert
        :return: dict - information about the dessert
        """
        try:
            return cls.__get_specific_meal_by_cat('Desserts', dessert_id)
        except Exception as e:
            print(e)
            return None

    @classmethod
    def __get_total(cls, meals: list[int], category: str) -> int:
        """
        private function
        return sum of the price of all the meals in meals in the category
        :param meals: list of ints - all the id meals to calculate
        :param category: str  - category name
        :return: int - total price of the meals
        """
        total = 0
        if len(meals) == 0:
            return total
        else:
            all_meals = list(filter(lambda elem: elem['categoryName'] == category, cls.menu))
            all_meals = all_meals[0]['dishList']
            for meal in meals:
                curr_meal = list(filter(lambda elem: elem['dishId'] == meal, all_meals))
                total += curr_meal[0]['dishPrice']
            return total

    @classmethod
    def get_bill(cls, drinks: list[int], desserts: list[int], pizzas: list[int]) -> int:
        """
        return the total price of all meals in meals
        :param drinks: list - list of ints - all drinks ids
        :param desserts: list - list of ints - all desserts ids
        :param pizzas: list - list of ints - all pizzas ids
        :return: int - total bill
        """
        try:
            total_drinks = cls.__get_total(drinks, 'Drinks')
            total_desserts = cls.__get_total(desserts, 'Desserts')
            total_pizzas = cls.__get_total(pizzas, 'Pizzas')
            return total_drinks + total_desserts + total_pizzas
        except Exception as e:
            print(e)
            return None


# Initialize the singleton _Menu class
def Menu():
    """
    Tis function start the Menu
    :return: pointer to _Menu class
    """
    return _Menu()


def Update_Menu():
    """
    Tis function update the Menu
    :return: pointer to _Menu class
    """
    return _Menu().update()
