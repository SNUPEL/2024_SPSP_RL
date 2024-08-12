import os
import json
import numpy as np

from torch.utils.tensorboard import SummaryWriter
from environment.data import DataGenerator
from environment.env import Reshuffling
from agent.dqn import Agent
from cfg_train import get_cfg


if __name__ == '__main__':
    args = get_cfg()

    if not os.path.exists(args.save_model_dir):
        os.makedirs(args.save_model_dir)

    if not os.path.exists(args.save_log_dir):
        os.makedirs(args.save_log_dir)

    with open(args.save_log_dir + "parameters.json", 'w') as f:
        json.dump(vars(args), f, indent=4)

    with open(args.save_log_dir + "train_log.csv", 'w') as f:
        f.write('episode, mean value, reward\n')

    data_generator = DataGenerator(args.num_plates)
    env = Reshuffling(data_generator, num_piles=args.num_piles, max_height=args.max_height)
    agent = Agent(args)
    writer = SummaryWriter(args.save_log_dir)
