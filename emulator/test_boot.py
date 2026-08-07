from pathlib import Path
from pyboy import PyBoy
from PIL import Image
import io






size = (144, 160, 3)
pyboy = PyBoy("tobudx.gb",window="SDL2",sound_emulated=False)
pil_image = pyboy.screen.image

print("cartridge",pyboy.cartridge_title)

#value_of_interest = pyboy.memory[0x000001B8F1867640]

#1680

##Load file
with open("state_file.state","rb") as f:
    pyboy.load_state(f)

#Save file
# with open("state_file.state","rb") as f:
#     pyboy.save_state(f)


step = 0
while pyboy.tick():
    #pyboy.button("left")
    #pyboy.button("up")
    frame = pyboy.screen.ndarray[:, :, :].copy()
    #collision = pyboy.game_area_collision()
    

    step += 1
    if step % 60 == 0:
        print(step, frame.shape, "unique shades:", len(set(frame.flatten())))
        #print(value_of_interest)
        #print(collision)
    #print(pyboy._plugin_manager)
    print(step)


pil_image.save('screenshot.png')



# --- UNCOMMENT IF YOU ARE UPDATING THE STATE ---
# #Save state
# with open("state_file.state","wb") as f:
#     pyboy.save_state(f)

pyboy.stop()








