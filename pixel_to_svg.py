from PIL import Image
import numpy as np

def pixel_to_svg(image_path, output_svg_path):
    # Bild laden
    image = Image.open(image_path).convert("RGBA")
    width, height = image.size
    pixels = np.array(image)

    # SVG Header
    svg_header = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" shape-rendering="crispEdges">'
    svg_footer = "</svg>"

    # Pixel in SVG-Rechtecke umwandeln
    rects = []
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[y, x]
            if a > 0:  # Nur sichtbare Pixel speichern
                hex_color = f"#{r:02x}{g:02x}{b:02x}"
                rects.append(f'<rect x="{x}" y="{y}" width="1" height="1" fill="{hex_color}" />')

    # Datei speichern
    svg_content = svg_header + "".join(rects) + svg_footer
    with open(output_svg_path, "w") as svg_file:
        svg_file.write(svg_content)

    print(f"SVG gespeichert: {output_svg_path}")

# Beispielaufruf
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Verwendung: python pixel_to_svg.py input.png output.svg")
    else:
        pixel_to_svg(sys.argv[1], sys.argv[2])
