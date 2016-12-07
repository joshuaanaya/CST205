#Christopher Barbarick and Joshua Anaya Lab #12 CST 205
def escapeGame():
  north = false
  south = true
  east = false
  west = false
  secret = false
  win = false
  items = false

  nm = requestString("Let's play ESCAPE (Enter the name of the player)")
  rm = " "
  showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
  while rm != "exit": #exit will exit the game
    if south == true and north == false and east == false and west == false:
      rm = requestString("The room is small with only a bed with a small spring mattress, with some springs on the side of the bed in sight.\n It feels like those rooms you see torture victims live in the cop shows and movies. There is a door opposite of the bed.  \n Do you Wish to leave?").lower()
      if rm  == "leave" or rm == "yes":
        south = false
      elif rm == "help":
       showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there. "+ str(nm)+" doesn\'t know where they are or how long it has been. But "+str(nm)+" dooes know that they have to get out somehow?")
      
      else:
       rm = requestString("Please try again.").lower()
   
    if south == false and north == true and east == false and west == false:
      rm = requestString("There is a window in the room but it is too tall for you to reach and see out. \n Day light is peering into the room. This room\'s floor has some tiles that\n look as though they were recently changed. Do you want to leave?").lower()
      if rm == "leave" or rm == "yes":
        north = false
      elif rm == "help":
       showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
        #you need to type "use scalpel" and also have the scalpel
      elif rm == "use scalpel" and items == true:
        secret = true
        showInformation(str(nm) + " open the new door and find your selves on the street of a city Free. Congratulations.\n")
      else:
        requestString("Wrong Command! Please try again.").lower()
    #this room contains a bear trap that will trap the player and end the game
    #but it will only end the game if you have obtained the scalpel       
    if south == false and north == false and east == true and west == false:
      rm = requestString("The foul smell you were smelling in the last room is coming from something in the corner.\n It looks like an animal corpse, though it is hard to tell what it is due to being mangled and decayed. \n There seems to be a pile of animal paws littered around  open bear traps.\nA There seems to be something under the corpses. \n But you dont know if that thing will help you escape?\n You should try to use somthing to move them with something other than your hand. \n Do you want to leave the room?").lower()
      if rm == "leave" or rm == "yes":
        east = false
      elif rm == "use scalpel" and items == true:
        showInformation(" You use the scalpel to try to move the paws and \n*SNAP*\n The trap closes and you are now stuck, bleeding. \nYou try to move and another bear trap falls onto your head. \n*SNAP!*\n GAME OVER")
        break
      elif rm == "help":
       showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
      else:
        requestString("Wrong Command! Please try again.").lower()
    #this room has an object, a scalpel
    #it is used to escape the main room or could get you caught in the bear trap  
    if south == false and north == false and east == false and west == true and items == false:
      rm = requestString("There is a metal stand at the center with a tray of surgical equipment sitting on top. \n Some appear to be rusted, while others looked like they have just been sterilized.\n A bright light is coming from the ceiling and is being reflected into your eyes by one of the tools on the stand, a scalpel. \n Do you want to leave this room?").lower()
      if rm == "leave" or rm == "yes":
        west = false  
      elif rm == "take scalpel":
        items = true 
        showInformation ("You walked to the table and picked up the shiny scalpel. This might come in handy later.")
      elif rm == "help":
       showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
      else:
        requestString("Wrong Command!Please try again.").lower()
        #dialogue after pickin up the scalpel
    if south == false and north == false and east == false and west == true and items == true:
      rm = requestString("There is a metal stand at the center with a tray of surgical equipment sitting on top. \n Some appear to be rusted, while others looked like they have just been sterilized.\n Do you want to leave this room?").lower()
      if rm == "leave" or rm == "yes":
        west = false  
      elif rm == "help":
       showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
      else:
        requestString("Wrong Command!Please try again.").lower()
    #using the scalpel in the main room to pry the tile will let you out to win the game. Escape!    
    if secret == true:
      showInformation ("You Win!")
      win = true
      break
    #this room is the center and will get you to each room. 
    if south == false and north == false and east == false and west == false:
      rm = requestString("This room is full of clutter and dirt. \n The walls seemed to be stained and torn linen lie in the corner. \n Attatched to the wall are a set of rusted shackles, they seem to be warm.\n  There seems to be a foul odor but you cannot figure out where it is coming from.\n There are doors on all sides of you. One for each direction with the room with the bed being to the south.\n Which direction do you want to enter? North, South, East, or West.").lower()
      if rm == "south":
        south = true
      elif rm == "north":
        north = true
      elif rm == "east":
        east = true
      elif rm == "west":
        west = true
      elif rm == "help":
       showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn\'t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
      else:
        requestString("Wrong Command! Please try again.").lower()
  #if you lose, this text will show
  if win == false:
    showInformation("Thanks for playing an early access version of ESCAPE")