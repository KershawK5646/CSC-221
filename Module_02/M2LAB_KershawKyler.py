# RollDieKDynamic
"""Dynamicaly graphing frequencies if die rolls"""
from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys

def update(frame_number, rolls, faces, frequencies):
    """configure bar plot contents for each animation frame"""
    # roll dice and update frequencies
    for i in range(rolls):
        frequencies[random.randrange(1,7) - 1] += 1
        
    # Reconfigure plot for update die frequencies
    plt.cla() # clear old contents
    axes = sns.barplot(faces, frequencies, palette = "bright")
    axes.set_title(f'Die frequencies for {sum(frequencies):,} Rolls')
    axes.set(xlabel = 'Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)
    
    # Display frequency and percentage above each bar
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() /2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')
    
# Read command line arguments for # frames and rolls per frame
number_of_frames = int (sys.argv[1])
rolls_per_frame = int(sys.argv[2])

sns.set_style('whitegrid')
figure = plt.figure('Rolling a Six-Sided Die')
values = list(range(1,7))
frequencies = [0] * 6

# configure and start animation
die_animation = animation.FuncAnimation(
        figure, update, repeat=False, frames=number_of_frames, interval=33,
        fargs = (rolls_per_frame, values, frequencies))

plt.show() # Display the window
input("Press any key to close the program")