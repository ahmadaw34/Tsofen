from enum import Enum


class Status(Enum):
    """
    Enum class to store possible results of compare process.
    """
    Success = "Success"
    Failure = "Failure"
