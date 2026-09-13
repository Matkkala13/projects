from statistics_funcs import permutator

numbers = [str(i) for i in list(range(0,10))]
letters = ['a', 'b', 'c', 'd', 'e', 'f']
chars = numbers.copy()
for i in letters:
    chars.append(i)
gradient = permutator(chars, 2)


def hex_to_rgb(hex:str)->str:
    '''
    It accepts a hex string and returns an rgb string
    '''
    red = gradient.index(hex[1:3])
    green = gradient.index(hex[3:5])
    blue = gradient.index(hex[5:])

    rgb = f"({red}, {green}, {blue})"

    return rgb

hex = '#45aaf9'
rgb = hex_to_rgb(hex)
print(rgb)



