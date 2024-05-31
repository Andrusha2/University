from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image


def pdf_to_docx(path: str) -> None:
    """
    Функция 'pdf_2_docx' принимает параметр 'path' - путь к фалу, который мы хотим конвертировать в формате str,
    Функция 'pdf_2_docx' конвертирует его из формата pdf в docx
    :param path: путь к файлу в формате строки
    :return: None
    """
    pdf_file = path
    docx_file = path[:-3] + 'docx'
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

def docx_to_pdf(path: str) -> None:
    """
    Функция 'docx_2_pdf' принимает параметр 'path' - путь к фалу, который мы хотим конвертировать в формате str
    Функция 'docx_2_pdf' конфертирует файл из формата '.docx' в формат '.pdf'
    :param path: путь к файлу
    :return: None
    """
    convert(path)

def image_compress(path: str, resolution, name) -> None:
    """
    Функция 'compress_pic' принимает параметр 'path' - путь к фалу, который мы хотим сжать в формате str
    Функция 'compress_pic' сжимает файл с заданным параметров от 0 до 100%
    :param path: путь к файлу в формате строки
    :param resolution: процент сжатия файла
    :param name: имя нового файла
    :return: None
    """
    image_file = Image.open(path)
    resolution = resolution
    name = name
    image_file.save(f"{name}.jpg", quality=resolution)

