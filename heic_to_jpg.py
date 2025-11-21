import os
from PIL import Image
import pillow_heif

def convert_folder(input_folder, output_folder):
    # garante que a pasta de saída existe
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, file)

            # força a troca correta da extensão
            base_name = os.path.splitext(file)[0]   # remove a extensão .heic/.HEIC
            output_path = os.path.join(output_folder, base_name + ".jpg")

            heif = pillow_heif.read_heif(input_path, convert_hdr_to_8bit=False)
            img = Image.frombytes(heif.mode, heif.size, heif.data, "raw")

            img.save(output_path, "JPEG", quality=100, subsampling=0, optimize=True)
            print("Convertido:", output_path)

# EXEMPLO DE USO
convert_folder("imagens/", "convertidas/")
