from pathlib import Path
import pdf2docx
import docx2pdf
from PIL import Image


def directory_changer(path: str) -> Path:
    """Returns new path.

    :param path: The path to the directory
    """
    path = Path(path)
    return path


def pdf_to_docx(path: Path = Path('example_folder')) -> None:
    """Procedure for converting pdf to docx

    :param path: The path to the directory
    :return: Makes new file or files with the same names, but docx extension
    """
    print(f'List of files with the .pdf extension in {path.name}: ')
    pdf_list = []
    for i in path.iterdir():
        if i.suffix == '.pdf':
            pdf_list.append(i)
    for i in range(len(pdf_list)):
        print(i+1, pdf_list[i].name)
    choice = int(input('Enter the file number(enter 0 to convert all): ')) - 1
    if choice == -1:
        for i in pdf_list:
            pdf2docx.Converter(str(i)).convert()
    else:
        pdf2docx.Converter(str(pdf_list[choice])).convert()


def docx_to_pdf(path: Path = Path('example_folder')) -> None:
    """Procedure for converting docx to pdf

    :param path: The path to the directory
    :return: Makes new file or files with the same names, but pdf extension
    """
    print(f'List of files with the .docx extension in {path.name}: ')
    docx_list = []
    for i in path.iterdir():
        if i.suffix == '.docx':
            docx_list.append(i)
    for i in range(len(docx_list)):
        print(i + 1, docx_list[i].name)
    choice = int(input('Enter the file number(enter 0 to convert all): ')) - 1
    if choice == -1:
        for i in docx_list:
            docx2pdf.convert(str(i), str(i)[:-4]+'pdf')
    else:
        docx2pdf.convert(str(docx_list[choice]), str(docx_list[choice])[:-4]+'pdf')
def image_compress(path: Path = Path('example_folder')) -> None:
    """Procedure for compressing image to n% of their initial weight

    :param path: The path to the directory
    :return: The same file but smaller size
    """
    extensions = ('.jpeg', '.gif', '.png', '.jpg')
    print(f"List of files with the {extensions} extension in {path.name}: ")
    image_list = []
    for i in path.iterdir():
        if i.suffix in extensions:
            image_list.append(i)
    for i in range(len(image_list)):
        print(i + 1, image_list[i].name)
    choice = int(input('Enter the file number(enter 0 to compress all): ')) - 1
    compress_params = int(input('Enter the compression parameters(0-100%): '))
    if choice == -1:
        for i in image_list:
            Image.open(i).save(i.name, quality=compress_params)
    else:
        Image.open(image_list[choice]).save(image_list[choice], quality=compress_params)


def delete(path: Path = Path('example_folder')) -> None:
    """Procedure for deleting file or files

    :param path: The path to the directory
    :return: Deleted file or files
    """
    choice = int(input('1. Delete all files starting with...\n'
                       '2. Delete all file ending with...\n'
                       '3. Delete all files contains...\n'
                       '4. Delete all files by extension\n'
                       'Select a function: '))
    if choice == 1:
        start = input('Enter the start symbols: ')
        del_list = list(filter(lambda x: x.stem.startswith(start), path.iterdir()))
    elif choice == 2:
        end = input('Enter the end symbols: ')
        del_list = list(filter(lambda x: x.stem.endwith(end), path.iterdir()))
    elif choice == 3:
        contains = input('Enter symbols: ')
        del_list = list(filter(lambda x: contains in x.stem, path.iterdir()))
    else:
        extension = input('Enter the extension: ')
        del_list = list(filter(lambda x: extension == x.suffix, path.iterdir()))
    for i in del_list:
        Path(i).unlink()