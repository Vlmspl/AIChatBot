import numpy as np

character_map = {
    # English uppercase
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
    5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
    15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z',

    # English lowercase
    26: 'a', 27: 'b', 28: 'c', 29: 'd', 30: 'e',
    31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j',
    36: 'k', 37: 'l', 38: 'm', 39: 'n', 40: 'o',
    41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't',
    46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y', 51: 'z',

    # Ukrainian uppercase
    52: 'А', 53: 'Б', 54: 'В', 55: 'Г', 56: 'Ґ',
    57: 'Д', 58: 'Е', 59: 'Є', 60: 'Ж', 61: 'З',
    62: 'И', 63: 'І', 64: 'Ї', 65: 'Й', 66: 'К',
    67: 'Л', 68: 'М', 69: 'Н', 70: 'О', 71: 'П',
    72: 'Р', 73: 'С', 74: 'Т', 75: 'У', 76: 'Ф',
    77: 'Х', 78: 'Ц', 79: 'Ч', 80: 'Ш', 81: 'Щ',
    82: 'Ь', 83: 'Ю', 84: 'Я',

    # Ukrainian lowercase
    85: 'а', 86: 'б', 87: 'в', 88: 'г', 89: 'ґ',
    90: 'д', 91: 'е', 92: 'є', 93: 'ж', 94: 'з',
    95: 'и', 96: 'і', 97: 'ї', 98: 'й', 99: 'к',
    100: 'л', 101: 'м', 102: 'н', 103: 'о', 104: 'п',
    105: 'р', 106: 'с', 107: 'т', 108: 'у', 109: 'ф',
    110: 'х', 111: 'ц', 112: 'ч', 113: 'ш', 114: 'щ',
    115: 'ь', 116: 'ю', 117: 'я',

    # Additional Russian uppercase
    118: 'Ё', 119: 'Ы', 120: 'Э',

    # Additional Russian lowercase
    121: 'ё', 122: 'ы', 123: 'э',

    # Digits
    124: '0', 125: '1', 126: '2', 127: '3', 128: '4',
    129: '5', 130: '6', 131: '7', 132: '8', 133: '9',

    # Common symbols
    134: '!', 135: '@', 136: '#', 137: '$', 138: '%',
    139: '^', 140: '&', 141: '*', 142: '(', 143: ')',
    144: '-', 145: '_', 146: '=', 147: '+', 148: '{',
    149: '}', 150: '[', 151: ']', 152: '|', 153: '\\',
    154: ':', 155: ';', 156: '"', 157: "'", 158: '<',
    159: '>', 160: ',', 161: '.', 162: '?', 163: '/',
    164: '`', 165: '~', 166: ' '
}


def intToBinary(number):
    if number < 0 or number > 255:
        raise ValueError("Number must be between 0 and 255 for an 8-bit binary representation.")
    return format(number, '08b')


def binaryToInteger(binary_str):
    if len(binary_str) != 8 or not all(bit in '01' for bit in binary_str):
        raise ValueError("Input must be an 8-bit binary string.")

    # Convert binary string to integer
    number = int(binary_str, 2)
    return number


def text_to_numerical(text):
    return np.array([character_map.get(c, -1) for c in text])

