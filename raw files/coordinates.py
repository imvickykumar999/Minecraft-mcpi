
# pip install mcpi

# Import the api
from mcpi.minecraft import Minecraft

# Initialize the api (MCPI must be open and in a world at this time)
mc = Minecraft.create(address='localhost', port=4711)

# Post to chat
mc.postToChat("Hello world!")

# Get the player's position
pos = mc.player.getTilePos()

# Print the player's x,y,z
print("X:", pos.x)
print("Y:", pos.y)
print("Z:", pos.z)

# Get the player's rotation
rot = mc.player.getRotation()

# Print the player's roll, yaw and pitch
print("Roll:", rot.roll)
print("Yaw:", rot.yaw)
print("Pitch:", rot.pitch)

# We need only X, Z, and Yaw
print(pos.x, pos.z, rot.yaw)


rf'''
C:\Users\surface\Documents\GitHub\Minecraft-mcpi\raw files>python coordinates.py
Traceback (most recent call last):
  File "C:\Users\surface\Documents\GitHub\Minecraft-mcpi\raw files\coordinates.py", line 45, in <module>
    pos = mc.player.getTilePos()
          ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\surface\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\mcpi\minecraft.py", line 157, in getTilePos
    return CmdPositioner.getTilePos(self, [])
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\surface\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\mcpi\minecraft.py", line 56, in getTilePos
    return Vec3(*list(map(int, s.split(","))))
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: ''

C:\Users\surface\Documents\GitHub\Minecraft-mcpi\raw files>
'''
