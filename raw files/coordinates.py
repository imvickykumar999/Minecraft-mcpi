
# pip install mcpi

# Import the api
from mcpi.minecraft import Minecraft

# Initialize the api (MCPI must be open and in a world at this time)
mc = Minecraft.create(address="127.0.0.1", port=58750)

# Post to chat
mc.postToChat("Hello world!")

print(help(mc))




# # Get the player's position
# pos = mc.player.getTilePos()

# # Print the player's x,y,z
# print("X:", pos.x)
# print("Y:", pos.y)
# print("Z:", pos.z)

# # Get the player's rotation
# rot = mc.player.getRotation()

# # Print the player's roll, yaw and pitch
# print("Roll:", rot.roll)
# print("Yaw:", rot.yaw)
# print("Pitch:", rot.pitch)

# # We need only X, Z, and Yaw
# print(pos.x, pos.z, rot.yaw)
