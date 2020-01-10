# import binascii
import base64

# import pdfkit

from PIL import Image
from io import BytesIO

import img2pdf


def convert_image_to_pdf(b64, pdf_path):

    random_bytes = base64.b64decode(b64, validate=True)

    image = Image.open(BytesIO(random_bytes))
    image = image.convert('RGB')

    buffer = BytesIO()
    # image.save(buffer, format="JPEG2000",
    #            quality_mode='rates', irreversible=True, quality_layers=[100])
    image.save(buffer, format="JPEG", quality=100,
               optimize=True, dpi=(600, 600), progression=True)

    pdf_bytes = img2pdf.convert(buffer.getvalue(), dpi=300)

    with open(pdf_path, "wb") as file:
        file.write(pdf_bytes)
