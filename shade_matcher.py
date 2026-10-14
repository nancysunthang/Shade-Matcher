def hex_to_rgb(hex_color):
    """Turn a hex color like '#C68E6E' into (198, 142, 110)."""
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b)


if __name__ == "__main__":
    print(hex_to_rgb("#C68E6E"))  # should print (198, 142, 110)
