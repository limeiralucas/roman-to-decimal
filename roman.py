from __future__ import annotations

class RomanNumber:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol.upper()
    
    def __repr__(self) -> str:
        return self.symbol

    def __eq__(self, obj: RomanNumber) -> bool:
        return obj.symbol == self.symbol

    def to_decimal(self) -> int:
        decimal_to_roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        converted_number = 0
        number_at_right = None
        for char in self.symbol[::-1]:
            number = decimal_to_roman_map.get(char)
            
            if number_at_right and number_at_right > number:
                converted_number += number * -1
            else:
                converted_number += number
            number_at_right = number
        
        return converted_number

    @staticmethod
    def _decimal_to_roman_symbol(number: int) -> str:
        decimal_to_roman_map = {
            1: "I", 
            5: "V", 
            10: "X", 
            50: "L", 
            100: "C", 
            500: "D", 
            1000: "M", 
        }

        return decimal_to_roman_map.get(number)
