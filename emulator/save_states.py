"""
save_states.py -- boot the ROM to a known point and save a screenshot to it.

Set MODE below, then run the file. Nothing else needs editing.

    "play"    load STATE_FILE and run it live so you can eyeball it.
              This is the safe default -- it never writes a state.

    "record"  boot from power-on and hand you the controls. Play to the
              exact spot you want, then CLOSE THE WINDOW -- the state is
              written at that moment.
              This OVERWRITES whatever STATE_FILE points at.

Frame numbers are not usable as boot targets here: the title screen waits
for a button press, so a passive boot never advances past it no matter how
many frames you tick. That is why recording is interactive.
"""

from pathlib import Path

from pyboy import PyBoy

# --------------------------------------------------------------------
# config
# --------------------------------------------------------------------

HERE = Path(__file__).parent
ROM = HERE / "tobudx.gb"


#--------------------------EDIT HERE ------------------------#
MODE = "play"
#MODE = "record"

# Which state file this run reads from / writes to.
STATE_FILE = HERE / "state_file.state"      # existing menu state
# STATE_FILE = HERE / "gameplay.state"      # first frame of Plains


# In "play", press A this many frames after loading, to leave the menu.
# Set to None to load the state and do nothing.
PRESS_A_AFTER = 10
# PRESS_A_AFTER = None

# How long "play" runs before quitting. None = until you close the window.
PLAY_FRAMES = 300
# PLAY_FRAMES = None

# 1 = real time, 0 = as fast as possible.
SPEED = 1

SCREENSHOT = HERE / "screenshot.png"


# --------------------------------------------------------------------
# run
# --------------------------------------------------------------------

pyboy = PyBoy(str(ROM), window="SDL2", sound_emulated=False)
pyboy.set_emulation_speed(SPEED)

print(f"cartridge : {pyboy.cartridge_title}")
print(f"mode      : {MODE}")
print(f"state     : {STATE_FILE.name}")

if MODE == "record":
    # You drive. The SDL2 window takes your keyboard, so play the game to
    # wherever you want the snapshot taken, then close the window.
    print()
    print("  RECORDING -- play to the spot you want, then CLOSE THE WINDOW")
    print()

    while pyboy.tick():
        pass

    with open(STATE_FILE, "wb") as f:
        pyboy.save_state(f)

    print(f"saved at frame {pyboy.frame_count} -> {STATE_FILE.name}")

elif MODE == "play":
    with open(STATE_FILE, "rb") as f:
        pyboy.load_state(f)

    print(f"loaded at frame {pyboy.frame_count}")

    if PRESS_A_AFTER is not None:
        pyboy.tick(PRESS_A_AFTER)
        pyboy.button("a")
        print(f"pressed A at frame {pyboy.frame_count}")

    if PLAY_FRAMES is None:
        while pyboy.tick():
            pass
    else:
        pyboy.tick(PLAY_FRAMES)

    print(f"stopped at frame {pyboy.frame_count}")

else:
    raise SystemExit(f"unknown MODE: {MODE!r}")

# Grab the screen fresh, at the end -- pyboy.screen.image returns the
# current frame each time it is read, so reading it early gives you boot.
# In "record" the window is already gone, so this is allowed to fail.
try:
    pyboy.screen.image.save(SCREENSHOT)
    print(f"screenshot -> {SCREENSHOT.name}")
except Exception as e:
    print(f"no screenshot ({e})")

pyboy.stop()
