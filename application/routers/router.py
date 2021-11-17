from fastapi import APIRouter, status, Response
from application.menuClass import Menu
from application.models.schemas import ErrorResponseModel, OrderSchema

menu = Menu()

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/drinks", response_description="Retrieve all drinks")
async def get_drinks(response: Response):
    """
    Retrieve all drinks from restaurant
    :param response: HTTP response
    :return: if request succeed return JSON of all drink with status code 200,
    ErrorResponseModel otherwise
    """
    try:
        all_drinks = menu.get_drinks()
        if all_drinks is not None:
            response.status_code = status.HTTP_200_OK
            return {'drinks': all_drinks}
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return ErrorResponseModel("An error occurred.", status.HTTP_404_NOT_FOUND,
                                      'Something went wrong could not get drinks')
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponseModel("An error occurred.", status.HTTP_500_INTERNAL_SERVER_ERROR,
                                  'Something went wrong could not get drinks')


@router.get("/drink/{id}", response_description="Get drink id and return the drink")
async def get_drink(drink_id: int, response: Response):
    """
    Retrieve specific drink from restaurant
    :param drink_id: int - id of a drink
    :param response: HTTP response
    :return: if request succeed return JSON of the drink with status code 200,
    ErrorResponseModel otherwise
    """
    try:
        drink = menu.get_drink(drink_id=drink_id)
        if drink is not None and drink != {}:
            response.status_code = status.HTTP_200_OK
            return {'drink': drink}
        elif drink == {}:
            response.status_code = status.HTTP_404_NOT_FOUND
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return ErrorResponseModel("An error occurred.", status.HTTP_400_BAD_REQUEST,
                                      'Something went wrong could not get drink')
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponseModel("An error occurred.", status.HTTP_500_INTERNAL_SERVER_ERROR,
                                  'Something went wrong could not ge drink')


@router.get("/pizzas", response_description="Retrieve all pizzas")
async def get_pizzas(response: Response):
    """
    Retrieve all pizzas from restaurant
    :param response: HTTP response
    :return: if request succeed return JSON of all pizzas with status code 200,
    ErrorResponseModel otherwise
    """
    try:
        all_pizzas = menu.get_pizzas()
        if all_pizzas is not None:
            response.status_code = status.HTTP_200_OK
            return {'pizzas': all_pizzas}
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return ErrorResponseModel("An error occurred.", status.HTTP_404_NOT_FOUND,
                                      'Something went wrong could not get pizzas')
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponseModel("An error occurred.", status.HTTP_500_INTERNAL_SERVER_ERROR,
                                  'Something went wrong could not get pizzas')


@router.get("/pizza/{id}", response_description="Get pizza id and return the pizza")
async def get_pizza(pizza_id: int, response: Response):
    """
    Retrieve specific drink from restaurant
    :param pizza_id: int - id of specific pizza
    :param response: HTTP response
    :return: if request succeed return JSON of the pizza with status code 200,
    ErrorResponseModel otherwise
    """
    try:
        pizza = menu.get_pizza(pizza_id=pizza_id)
        if pizza is not None and pizza != {}:
            response.status_code = status.HTTP_200_OK
            return {'pizza': pizza}
        elif pizza == {}:
            response.status_code = status.HTTP_404_NOT_FOUND
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return ErrorResponseModel("An error occurred.", status.HTTP_400_BAD_REQUEST,
                                      'Something went wrong could not get pizza')
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponseModel("An error occurred.", status.HTTP_500_INTERNAL_SERVER_ERROR,
                                  'Something went wrong could not ge pizza')


@router.get("/desserts", response_description="Retrieve all desserts")
async def get_desserts(response: Response):
    """
    Retrieve all desserts from restaurant
    :param response: HTTP response
    :return: if request succeed return JSON of all desserts with status code 200,
    ErrorResponseModel otherwise
    """
    try:
        all_desserts = menu.get_desserts()
        if all_desserts is not None:
            response.status_code = status.HTTP_200_OK
            return {'desserts': all_desserts}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return ErrorResponseModel("An error occurred.", status.HTTP_400_BAD_REQUEST,
                                      'Something went wrong could not get desserts')
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponseModel("An error occurred.", status.HTTP_500_INTERNAL_SERVER_ERROR,
                                  'Something went wrong could not get desserts')


@router.get("/dessert/{id}", response_description="Get pizza id and return the pizza")
async def get_dessert(dessert_id: int, response: Response):
    """
    Retrieve specific dessert from restaurant
    :param dessert_id: int - id of specific dessert
    :param response: HTTP response
    :return: if request succeed return JSON of the dessert with status code 200,
    ErrorResponseModel otherwise
    """
    try:
        dessert = menu.get_dessert(dessert_id=dessert_id)
        if dessert is not None and dessert != {}:
            response.status_code = status.HTTP_200_OK
            return {'dessert': dessert}
        elif dessert == {}:
            response.status_code = status.HTTP_404_NOT_FOUND
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return ErrorResponseModel("An error occurred.", status.HTTP_400_BAD_REQUEST,
                                      'Something went wrong could not get dessert')
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponseModel("An error occurred.", status.HTTP_500_INTERNAL_SERVER_ERROR,
                                  'Something went wrong could not ge dessert')


@router.post("/order", response_description="Receives an order and return its total price")
async def get_total_price(order_param: OrderSchema, response: Response):
    """
    Receives an order and return its total price
    :param order_param: OrderSchema
    :param response: HTTP response
    :return: if succeed return {'price': total_price} and status code 200,
    ErrorResponseModel otherwise
    """
    try:
        drinks = order_param.drinks
        pizzas = order_param.pizzas
        desserts = order_param.desserts
        total_price = menu.get_bill(drinks=drinks, pizzas=pizzas, desserts=desserts)
        if total_price is not None:
            response.status_code = status.HTTP_200_OK
            return {'price': total_price}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return ErrorResponseModel("An error occurred.", status.HTTP_400_BAD_REQUEST,
                                      'Something went wrong could not get the bill')
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponseModel("An error occurred.", status.HTTP_500_INTERNAL_SERVER_ERROR,
                                  'Something went wrong could not ge dessert')
