import argparse


def get_cfg():
    parser = argparse.ArgumentParser(description="Stacking")

    parser.add_argument("--seed", type=int, default=1, help="random seed")

    parser.add_argument("--load_model", type=int, default=0, help="load the trained model")

    parser.add_argument("--load_model_path", type=str, default=None, help="file to load trained models from")
    parser.add_argument("--save_model_dir", type=str, default="/output/train/model/", help="folder to save trained models")
    parser.add_argument("--save_log_dir", type=str, default="/output/train/log/", help="folder to save logs")
    parser.add_argument("--load_val_dir", type=str, default="./input/validation/4-4/", help="folder to load validation data from")

    parser.add_argument("--num_piles", type=int, default=4, help="number of target piles")
    parser.add_argument("--num_plates", type=int, default=10, help="average number of plates")
    parser.add_argument("--max_height", type=int, default=4, help="maximum number of plates to be stacked in each pile")

    parser.add_argument("--num_episodes", type=int, default=50000, help="number of episodes")
    parser.add_argument("--lr", type=float, default=1e-4, help="learning rate")
    parser.add_argument("--lr_decay", type=float, default=0.9, help="learning rate decay ratio")
    parser.add_argument("--lr_step", type=int, default=10000, help="step size to reduce learning rate")
    parser.add_argument("--gamma", type=float, default=0.99, help="discount ratio")

    parser.add_argument("--eval_every", type=int, default=200, help="Evaluate every x episodes")
    parser.add_argument("--save_every", type=int, default=5000, help="Save a model every x episodes")

    return parser.parse_args()