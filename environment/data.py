import random
import pandas as pd
import numpy as np


class DataGenerator:
    def __init__(self, num_piles=4, max_height=4, num_plates=10,  retrieval_min=1, retrieval_max=5):
        self.num_piles = num_piles
        self.max_height = max_height
        self.num_plates = num_plates
        self.retrieval_min = retrieval_min
        self.retrieval_max = retrieval_max

    def generate(self, file_path=None):
        # 각 강재의 반출일 정보 생성
        retrieval_dates = np.random.choice(range(self.retrieval_min, self.retrieval_max + 1), self.num_plates)
        pile_indices = np.random.choice(np.repeat(range(self.num_piles), self.max_height), self.num_plates, replace=False)
        df = pd.DataFrame({"pile": pile_indices, "retrieval date": retrieval_dates})

        if file_path is not None:
            df.to_excel(file_path, index=False)

        return df


if __name__ == '__main__':
    import os

    num_piles = 4
    max_height = 4

    file_dir = "../input/validation/%d-%d/" % (num_piles, max_height)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    data_src = DataGenerator(num_piles=num_piles, max_height=max_height)

    iteration = 10
    for i in range(1, iteration + 1):
        file_path = file_dir + "instance-{0}.xlsx".format(i)
        df = data_src.generate(file_path=file_path)