import stealth_requests as requests
import pymupdf

import os
from os import path

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0', 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 
        'Accept-Encoding': 'gzip, deflate, br, zstd', 
        'Sec-GPC': '1', 
        'Connection': 'keep-alive', 
        'Cookie': '__ddg1_=EKc899XJwoULGPq3PAqO', 
        'Upgrade-Insecure-Requests': '1', 
        'Sec-Fetch-Dest': 'document', 
        'Sec-Fetch-Mode': 'navigate', 
        'Sec-Fetch-Site': 'cross-site', 
        'DNT': '1', 
        'Priority': 'u=0, i', 
        'Pragma': 'no-cache', 
        'Cache-Control': 'no-cache', 
        'TE': 'trailers'
}

PDF_URL = "https://docs.cspu.ru/raspisanie-zanyatiy/och/fizmat(Inf)/Raspisanie/1k.pdf"
PDF_FILENAME = "full_schedule.pdf"
IMG_FULLPATH = path.join(os.getcwd(), "img", "schedule.png")

r = requests.get(PDF_URL, headers=HEADERS)

if (r.status_code != 200):
    print(f"Error status code: {r.status_code}:\n{r.text}")
    quit()

with open(PDF_FILENAME, "wb") as f:
    f.write(r.content)
    print("pdf saved")

schedule_pdf = pymupdf.open(PDF_FILENAME)
out_image = schedule_pdf[1].get_pixmap()
out_image.save(IMG_FULLPATH)

print("image saved")

