from functions import directory_changer, pdf_to_docx, docx_to_pdf, image_compress, delete
if __name__ == '__main__':
    function_lst = [directory_changer, pdf_to_docx, docx_to_pdf, image_compress, delete]
    while True:
        pathc = 0
        choice = int(input('Select a function\n'
                           '0. Change working directory\n'
                           '1. Convert PDF to DOXC\n'
                           '2. Convert DOXC to PDF\n'
                           '3. Shrink an image\n'
                           '4. Delete a group of files\n'
                           '5. Exit\n'
                           'Your choice is: '))
        if choice == 0:
            path = function_lst[choice](input('Enter a path: '))
            pathc += 1
            continue
        elif choice == 5:
            break
        if pathc:
            function_lst[choice](path)
        else:
            function_lst[choice]()