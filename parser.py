import sys
import struct
from datetime import datetime, timezone

CHARACTER_ID = {
    0: "Battler",
    1: "Ange",
    2: "Shannon",
    3: "Kanon",
    4: "Lucifer",
    5: "Chiester 410",
    6: "Ronove",
    7: "EVA Beatrice",
    8: "Virgilia",
    9: "Beatrice",
    10: "George",
    11: "Jessica",
    12: "Rosa",
    13: "Erika",
    14: "Dlanor",
    15: "Willard",
    16: "Bernkastel",
    17: "Lambdadelta",
    18: "BlackBattler",
}

def parse_replay(data, char1_offset, char2_offset):
    char1_id = struct.unpack_from("<B", data, char1_offset)[0]
    char2_id = struct.unpack_from("<B", data, char2_offset)[0]
    team_comp = f"{CHARACTER_ID.get(char1_id, f'Unknown ({char1_id})')}/{CHARACTER_ID.get(char2_id, f'Unknown ({char2_id})')}"
    return team_comp

with open(sys.argv[1], 'rb') as f:
    data = f.read()

version = struct.unpack_from("<B", data, 0x0)[0]

timestamp_offset = struct.unpack_from("<I", data, 0x10)[0]
timestamp = datetime.fromtimestamp(timestamp_offset)

p1 = parse_replay(data, 0x60, 0x62)
p2 = parse_replay(data, 0x64, 0x66)

winner = struct.unpack_from("<B", data, 0x1C)[0]

if winner not in (1, 2):
    print("Unable to get winner")
    sys.exit(1)

print(f"Replay game version: {version}")
print(f"{timestamp}\n")

if winner == 1:
    print(f"P1: {p1} (Winner)")
    print(f"P2: {p2} (Loser)")
else:
    print(f"P1: {p1} (Loser)")
    print(f"P2: {p2} (Winner)")

