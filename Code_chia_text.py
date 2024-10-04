import os

def save_paragraphs_to_txt(text, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    paragraphs = text.split('\n\n')
    count = 5001
    for i, paragraph in enumerate(paragraphs):
        if i % 2 == 0:
            filename = os.path.join(folder_path,f"00{count}_3.txt")
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(paragraph)
        elif i % 2 != 0:
            filename = os.path.join(folder_path,f"00{count}_4.txt")
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(paragraph)
            count += 1

folder_path = r'D:/text'
text = """

"""

save_paragraphs_to_txt(text,folder_path)
