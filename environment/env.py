import random
import numpy as np
import pandas as pd

from environment.data import DataGenerator


class Reshuffling:
    def __init__(self, data_src, num_piles=4, max_height=4):
        self.data_src = data_src
        self.num_piles = num_piles
        self.max_height = max_height

        if type(self.data_src) is DataGenerator:
            self.df = self.data_src.generate()
        else:
            self.df = pd.read_excel(data_src, engine='openpyxl')

    def step(self, action):
        done = False

        next_state = self._get_state()
        reward = self._calculate_reward(action)

        return next_state, reward, done

    def reset(self):
        if type(self.data_src) is DataGenerator:
            self.df = self.data_src.generate()
        else:
            self.df = pd.read_excel(self.data_src, engine='openpyxl')

        initial_state = self._get_state()

        return initial_state

    def _calculate_reward(self, action):

        return reward

    def _get_state(self):

        return state