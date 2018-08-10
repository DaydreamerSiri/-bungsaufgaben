# -*- coding: utf-8 -*-

num_dict = {'a': 529, 'b': 25, 'c': 17, 'd': 54, 'e': 715, 'f': 13, 'g': 8, 'h': 25, 'i': 125, 'j': 99, 'k': 210, 'l': 75,
            'm': 20, 'n': 25, 'o': 17, 'p': 54, 'q': 35, 'r': 13, 's': 17, 't': 25, 'u': 99, 'v': 54, 'w': 11, 'x': 13,
            'y': 1, 'z': 1}

plus_str = '++++++++++'

# Werte extrahieren
values = sorted(num_dict.values())
# Maximum bestimmen
val_max = max(values)

# Anzahl an Klassen
class_counter = len(plus_str)
# Anzahl an Elementen jeder Klasse
class_range = round(float(len(values)) / class_counter)
# Jeden n-ten Wert aus Liste als Grenze aufnehmen
class_list = values[0::int(class_range)]

# Original dict kopieren
plus_dict = num_dict.copy()

# Prüfe für jeden Wert in welcher Klasse er liegt
for key, val in plus_dict.items():
    # Größter Wert bekommt maximale Anzahl an +
    if val == val_max:
        plus_dict[key] = plus_str
    else:
        cl_num = 0
        for cl in class_list:
            cl_num += 1
            if val <= cl:
                # Weise Buchstaben die Anzahl an + zu die der Klasse entsprechen
                plus_dict[key] = plus_str[:cl_num]
                break

# Liste ausgeben
for key, val in plus_dict.items():
    print key, val