import os
import glob
import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(),' games', '*.EVE')).sort()
names = ['type', 'multi2', 'multi3', 'multi4', 'multi4','multi6', 'event']

game_frames = []
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names)
    game_frames.append(game_frame)

games = pd.concat(game_frames)
