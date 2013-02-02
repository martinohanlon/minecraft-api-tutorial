#www.stuffaboutcode.com
#Raspberry Pi, Minecraft API - the basics

#import the minecraft.py module from the minecraft directory
import minecraft.minecraft as minecraft
#import minecraft block module
import minecraft.block as block
#import time, so delays can be used
import time

if __name__ == "__main__":

    time.sleep(2)
    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create()

    #Post a message to the minecraft chat window 
    mc.postToChat("Hi, Minecraft API, the basics, what can you do? ")

    time.sleep(5)
    
    #Find out your players position
    playerPos = mc.player.getPos()
    mc.postToChat("Find your position - its x=" + str(playerPos.x) + ", y=" + str(playerPos.y) + ", z=" + str(playerPos.z))

    time.sleep(5)
    
    #Using your players position
    # - the players position is an x,y,z coordinate of floats (e.g. 23.59,12.00,-45.32)
    # - in order to use the players position in other commands we need integers (e.g. 23,12,-45)
    # - so round the players position
    playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))

    #Changing your players position
    mc.postToChat("Move your player - 30 blocks UP!")
    time.sleep(2)
    mc.player.setPos(playerPos.x,playerPos.y + 30,playerPos.z)
    # - wait for you to fall!
    time.sleep(5)

    #Interacting with a block
    # - get the type block directly below you
    blockType =  mc.getBlock(playerPos.x,playerPos.y - 1,playerPos.z)
    mc.postToChat("Interact with blocks - the block below you is of type - " + str(blockType))

    time.sleep(5)
    
    # - change the block below you to wood planks
    mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,block.WOOD_PLANKS)
    mc.postToChat("Change blocks - the block below you is now wood planks")

    time.sleep(5)

    #Creating many blocks
    mc.postToChat("Create blocks - making a diamond tower")

    # - loop 20 times
    for up in range(0, 20):
        mc.setBlock(playerPos.x + 1, playerPos.y + up, playerPos.z, block.DIAMOND_BLOCK)
        time.sleep(0.3)
    time.sleep(2)
    
    # - put you on top of the tower
    mc.postToChat("Dont look down, because Im putting you on top of it!")
    time.sleep(1)
    mc.player.setPos(playerPos.x + 1, playerPos.y + 20, playerPos.z)

    time.sleep(5)
    
    mc.postToChat("www.stuffaboutcode.com")

    

    #Setting multiple blocks at once (only works for 2 blocks - wierd!)
    # - create list of arguments
    #towerArgs = []
    
    # - append co-ord to list
    #for up in range(0, 20):
    #    towerArgs.append(playerPos.x + 2)
    #    towerArgs.append(playerPos.y + up)
    #    ccccccc.append(playerPos.z)
    # - append block type to list
    #towerArgs.append(5)

    # - call method
    #mc.setBlocks(*towerBlocks)
    # move player
    #mc.player.setPos(playerPos.x + 1, playerPos.y + 21, playerPos.z)
