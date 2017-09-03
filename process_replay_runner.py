import fnmatch
import os


from runner import run

replay_dir = "C:/Program Files (x86)/StarCraft II/Replays/"

matches = []
for root, dirnames, filenames in os.walk(replay_dir):
    for filename in fnmatch.filter(filenames, '*.SC2Replay'):
        matches.append(os.path.join(root, filename))
matches.sort(key=lambda x: os.path.getmtime(x))

print "found matches: ", matches
print "replaying with: ", matches[-1]


run("pysc2.bin.replay_actions", module_args=["--replays", matches[-1]], method="main")
