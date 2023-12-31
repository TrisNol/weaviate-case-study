import os 
import tqdm
import requests

def downdload_txt_to_file(url: str, filepath: str) -> None:
    with open(filepath, "w", encoding='utf-8') as file:
        response = requests.get(url, stream=True, timeout=120)
        if not response.ok:
            raise Exception()
        file.write(response.text)        


if __name__ == '__main__':
    base_path = "./data"

    if not os.path.isdir(base_path):
        os.mkdir(base_path)

    files = ['germeval2018.test.txt', 'germeval2018.training.txt']
    for file in tqdm.tqdm(files):
        if not os.path.exists(f'{base_path}/{file}'):
            downdload_txt_to_file(f"https://raw.githubusercontent.com/uds-lsv/GermEval-2018-Data/master/{file}", f'{base_path}/{file}')
    


