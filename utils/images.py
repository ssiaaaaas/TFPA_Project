from PIL import Image, ImageDraw, ImageFont
import os

def generate_overlay_image_with_positions(base_image_path, text_positions):
    print(f"Base image path: {base_image_path}")  # Debug
    print(f"Text positions: {text_positions}")  # Debug

    # Open the base image
    image = Image.open(base_image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    # Set font
    font_path = "arial.ttf"
    font = ImageFont.truetype(font_path, 30)  

    # Draw each text at its specified position
    for text, position in text_positions:
        print(f"Adding text: '{text}' at position {position}")  # Debug
        draw.text(position, text, fill=(255, 165, 0, 255), font=font)
        #draw.text(position, text, fill=(255, 165, 0, 255))

    combined = Image.alpha_composite(image, txt_layer)
    output_path = "static/media/cover/overlayed_budget_ld_precise.png"
    combined.save(output_path, format="PNG")
    print(f"Overlay image saved to: {output_path}")  # Debug

    return output_path
