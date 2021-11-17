from pydantic import BaseModel, Field


class OrderSchema(BaseModel):
    """
    Order Details Schema class
    """
    drinks: list = Field(...)
    desserts: list = Field(...)
    pizzas: list = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "drinks": [],
                "desserts": [2055835],
                "pizzas": [2055830, 2055832],
            }
        }


def ResponseModel(data, message, code=200):
    """
    This function get -
    :param data: List - data that return as request
    :param message: str - message to return
    :param code: HTTP Status - status to return
    :return: dict of all the above

    only use when the response is 2**
    """
    return {
        "data": [data],
        "code": code,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    """
    This function get -
    :param error: str - error to return
    :param code: HTTP Status - status to return
    :param message: str - message to return
    :return: dict of all the above
    only use when the response is 4** and above
    """
    return {"error": error, "code": code, "message": message}
