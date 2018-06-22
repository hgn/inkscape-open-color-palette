#!/usr/bin/python3


def hex_to_rgb(val):
        val = val.lstrip('#')
        ret = tuple(int(val[i:i+2], 16) for i in (0, 2 ,4))
        return ' '.join(str(x) for x in ret)

def format(color, name):
        print(hex_to_rgb(color), name)

print("GIMP Palette")
print("Name: Open Colors Mod")
print("Columns: 0")
print("# Comments? Hagen Paul Pfeifer <hagen@jauu.net> or via github")
print("# Based on Open Colors but reduced to a usable number of shades")
print("# Original Source: https://yeun.github.io/open-color")

format("#f8f9fa", "GRAY 0")
format("#f1f3f5", "GRAY 1")
format("#e9ecef", "GRAY 2")
format("#dee2e6", "GRAY 3")
format("#ced4da", "GRAY 4")
format("#adb5bd", "GRAY 5")
format("#868e96", "GRAY 6")
format("#495057", "GRAY 7")
format("#343a40", "GRAY 8")
format("#212529", "GRAY 9")
format("#000000", "BLACK")
format("#ffffff", "WHITE")

# 9er
format("#c92a2a", "RED 9")
format("#a61e4d", "PINK 9")
format("#862e9c", "GRAPE 9")
format("#5f3dc4", "VIOLET 9")
format("#364fc7", "INDIGO 9")
format("#1864ab", "BLUE 9")
format("#0b7285", "CYAN 9")
format("#087f5b", "TEAL 9")
format("#2b8a3e", "GREEN 9")
format("#5c940d", "LIME 9")
format("#e67700", "YELLOW 9")
format("#d9480f", "ORANGE 9")

# 5er
format("#ffffff", "SEPARATOR")
format("#ff6b6b", "RED 5")
format("#f06595", "PINK 5")
format("#cc5de8", "GRAPE 5")
format("#845ef7", "VIOLET 5")
format("#5c7cfa", "INDIGO 5")
format("#339af0", "BLUE 5")
format("#22b8cf", "CYAN 5")
format("#20c997", "TEAL 5")
format("#51cf66", "GREEN 5")
format("#94d82d", "LIME 5")
format("#fcc419", "YELLOW 5")
format("#ff922b", "ORANGE 5")

# 2er
format("#ffffff", "SEPARATOR")
format("#ffc9c9", "RED 2")
format("#fcc2d7", "PINK 2")
format("#eebefa", "GRAPE 2")
format("#d0bfff", "VIOLET 2")
format("#bac8ff", "INDIGO 2")
format("#a5d8ff", "BLUE 2")
format("#99e9f2", "CYAN 2")
format("#96f2d7", "TEAL 2")
format("#d8f5a2", "LIME 2")
format("#ffec99", "YELLOW 2")
format("#ffd8a8", "ORANGE 2")
