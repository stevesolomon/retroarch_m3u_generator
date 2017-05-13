"""
retroarch_m3u_generator

    Generates M3U files from .cue files with multi-disc games
    included in the same M3U. Writes out M3U files to a new ./m3u
    directory within the provided source directory.

:param SourceDir: The source directory containing .cue files.
"""
import os
import os.path
from sys import argv

"""
Extracts the name of the game.

:param filename: The filename to extract the game name from.
:returns: The game name.
"""
def extractGameName(filename):
    if " (" in filename:
        return filename.partition(" (")[0]
    else:
        return filename.partition(".cue")[0]

if len(argv) < 2:
    print("Usage: ")
    print("ps1_m3u_generator [SourceDir]")
    exit()

files = []
OUT_DIR = os.path.join(argv[1], "m3u")

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

print(OUT_DIR)

for file in os.listdir(argv[1]):
    if file.endswith("cue"):
        files.append(file)

files.sort()
gameFilesBuffer = {}

for i in range(1, len(files)):
    file = files[i]
    gameName = extractGameName(file)

    if gameName in gameFilesBuffer:
        gameFilesBuffer[gameName].append(file)
    else:
        gameFilesBuffer[gameName] = [file]


for gameName, fileNames in gameFilesBuffer.items():
    targetFile = open(os.path.join(OUT_DIR, gameName + ".m3u"), 'w+')

    for fileName in fileNames:
        targetFile.write("..\\" + fileName)
        targetFile.write("\n")

