
print("""

█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █ █▀ █░░ ▄▀█ █▄░█   █▀▀ ▄▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█   ░█░ █▄█   ░█░ █▀█ ██▄   █ ▄█ █▄▄ █▀█ █░▀█   █▄█ █▀█ █░▀░█ ██▄
      """)
#explean game msg
print("""
                         __________
                      .~#########%/%;~.
                     /############%/%;`\.
                    /######/~\/~\%/%;,;,\.
                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|
          XX       |##/~~\####%;;;/~~\;,|       XX
        XX..X      |#|  o  \##%;/  o  |.|      X..XX
      XX.....X     |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%/%;;;;,.|     @#%,.@  X.....| X
X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
 X# \.X        @#%,.@                  @#%,.@        X./  #
  ##  X          @#%,.@              @#%,.@          X   #
, "# #X            @#%,.@          @#%,.@            X ##
   `###X             @#%,.@      @#%,.@             ####'
  . ' ###              @#%.,@  @#%,.@              ###`"
    . ";"                @#%.@#%,.@                ;"` ' .
      '                    @#%,.@                   ,.
      ` ,                @#%,.@  @@                `
                          @@@  @@@  

      """)
  
print("choose carfuly to win this game\nThere are tow doors in fron of you . a red door 🚪 and blue door 🚪")
#  ask user first q 
first_q = input("which door do you want to open it ? ")
#  if choose the Rghit one continue the game withe new msg
if first_q.lower()== "blue":
  print("Great now you entered the room")
  #  ask him agine to choose three option
  print("you found three boxes white 🎁  pink 🎁  black 🎁")
  secound_q= input("which box do you want to open ? ")
  if secound_q.lower() == "black":
    print(" Opps!! you did opened a box full of spiders 🕷️🕸️")
    print("""
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣤⠖⠛⠛⠳⢦⣄⡀⠀⠀⠀⣀⣤⠶⠛⠉⠉⠁⠀⠀⠀⠉⠉⠙⠲⢦⣄⠀⠀⠀⠀⣀⣤⠶⠛⠙⠳⢦⣄⠀⠀⠀⠀⠀
⠀⠀⠀⣤⠞⣉⣠⡤⠶⢦⣄⡀⠈⠙⢦⣤⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣴⠞⠉⠀⣀⡤⠶⠤⣤⣈⠛⢦⡀⠀⠀
⠀⠀⢺⣷⠞⠋⠀⠀⠀⠀⠈⠙⢶⣤⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⡴⠟⠉⠀⠀⠀⠀⠉⠛⢦⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡴⠖⠒⠒⠒⠲⠶⣤⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣤⠴⠶⠒⠒⠒⠒⢶⣄⠀⠀⠀
⠀⠀⣰⠏⠀⣠⡤⢤⣤⣄⣀⣀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⣀⣠⣤⣤⢤⣤⡀⠙⢧⡀⠀
⠀⣼⢃⣴⠟⠁⠀⠀⠀⠀⠈⠙⡇⠀⠀⠀⠀⢀⣤⠶⠛⠋⠉⠉⠉⠉⠉⠙⠓⠶⣤⣀⠀⠀⠀⠀⠀⢰⡟⠉⠀⠀⠀⠀⠀⠙⢷⡈⢷⡀
⢠⣯⡞⠁⠀⠀⠀⠀⠀⢀⣀⣀⣿⡀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⣼⣃⣀⣀⠀⠀⠀⠀⠀⠀⠹⣼⡧
⠀⠉⠀⠀⠀⠀⣴⠞⠛⠉⠉⠉⠙⢷⣠⡟⠀⢀⡴⢶⣷⣶⣄⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠈⢷⡀⣰⠏⠉⠉⠉⠙⠛⢦⡀⠀⠀⠀⠈⠀
⠀⠀⠀⠀⠀⣼⠁⢀⡤⠶⠒⠒⠒⢺⡟⠀⠀⣾⠁⢾⣿⣄⣸⡇⠀⠀⠀⣴⠛⢻⣿⠛⣦⠀⠘⣿⠛⠒⠒⠒⠲⢦⣄⠈⢳⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠇⣰⠏⠀⠀⠀⠀⢀⣼⡇⠀⠀⠹⣆⡈⠙⣛⡿⠁⠀⠀⠀⣿⣷⣿⡿⠁⣸⠆⠀⢹⢦⡀⠀⠀⠀⠀⠙⣧⠈⣧⠀⠀⠀⠀
⠀⠀⠀⠀⣿⢰⠏⠀⠀⠀⠀⢠⡞⠙⣧⠀⠀⠀⠈⠉⠉⠉⡀⠘⠀⠰⠂⠙⠦⣤⣤⡴⠋⠀⠀⢸⠀⠹⣆⠀⠀⠀⠀⠘⣧⢹⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠛⠀⠀⠀⠀⢠⡏⠀⢠⡿⢧⣀⠀⠀⠀⠐⠺⣿⡶⠤⣤⣼⣧⡀⠀⠀⠀⠀⠀⢀⣾⣆⠀⠘⣆⠀⠀⠀⠀⠙⠛⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⢀⡿⠀⠀⠙⠳⠦⣤⣀⣀⠉⠀⠀⠈⠋⠀⠀⠀⠀⠀⣀⡴⠟⠁⢹⡆⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠸⣧⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠓⠒⠲⠶⠖⠒⠛⠋⠁⠀⠀⠀⢠⡇⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢏⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
  elif secound_q.lower() =="pink":
    print("Congratulations you have won the treasure 🪙 🏆")
    print(""""
                                                                                                          
                                    ████████████████████████████████████████████████████                  
                ████████████████████████████████████▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░██████              
            ▓▓▓▓▓▓░░░░░░██████░░░░▒▒░░░░████████▓▓████▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░██            
          ██▒▒▒▒░░░░░░░░░░░░████░░░░░░░░░░██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░██          
        ▓▓▒▒▒▒░░░░░░░░░░░░░░░░██▓▓░░░░░░░░░░████████████████████████████████████████████░░░░░░░░▓▓        
        ██▒▒░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████░░░░░░████      
      ▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░██▓▓▒▒░░░░░░░░██████████▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░██▓▓    
    ██▒▒▒▒░░░░░░▒▒████░░░░░░░░░░░░██▒▒▒▒░░░░░░████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░██    
    ██▒▒▒▒░░░░████▓▓████░░░░░░░░░░░░██▒▒░░░░░░░░████▓▓██▓▓████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░██    
    ░░▒▒░░░░██████▓▓▓▓▓▓██░░░░░░░░░░██▒▒▒▒░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░░░  ████  
  ▓▓▒▒▒▒░░░░████▓▓▓▓▓▓▓▓██░░░░░░░░░░░░██▒▒░░░░░░████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░██  
  ██▒▒░░░░░░██████▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░██▒▒░░░░░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░██  
  ██▒▒░░░░▓▓████▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░░░██▒▒░░░░░░██████████████████████████████████████████▓▓██▒▒░░░░░░██  
  ██▒▒░░░░██████████▓▓▓▓▓▓▓▓██░░░░░░░░██▒▒░░░░░░██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▒▒░░░░░░████
  ██▒▒░░░░██████▓▓▓▓██████████░░░░░░░░██▒▒░░░░░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░██
  ██▒▒░░░░████▓▓▓▓▓▓▓▓▓▓▓▓████░░░░░░░░██▒▒▒▒▒▒░░████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░██
  ██▒▒▒▒░░██████▓▓▓▓▓▓▓▓▓▓████░░░░░░░░██▒▒▒▒▒▒▒▒████▓▓▓▓██████▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░██
  ██▒▒▒▒▒▒██████▓▓▓▓▓▓▓▓▓▓████░░░░░░░░██▒▒▒▒▒▒░░██████████▓▓████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████
  ██████▓▓████████████████████▓▓██▓▓▓▓████████▓▓██████████████████████████████████████░░░░░░░░░░░░░░░░████
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░████▒▒░░░░░░░░░░░░░░██
  ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒░░░░░░░░░░░░░░░░░░██▒▒▒▒░░░░▒▒░░░░░░░░░░░░██▒▒▒▒░░░░░░░░░░░░██
  ██▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░██▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░██▒▒▒▒░░░░░░██████░░░░░░██▒▒░░░░░░░░░░░░████
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░██░░░░▒▒▒▒░░░░░░░░░░░░░░██▒▒▒▒░░░░██▓▓▓▓▓▓██░░░░██▒▒░░░░░░░░░░░░██  
  ██████████████████████████████████████████████████████████████▒▒▒▒░░░░██▓▓▓▓████░░░░██████████████████  
  ██▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒░░▒▒▒▒░░██▒▒▒▒▒▒░░██████████▓▓██▒▒▒▒░░░░░░██▓▓██░░░░░░██████████░░░░░░██  
  ██▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒▒▒░░░░████████▓▓▓▓██▒▒▒▒░░░░░░██▓▓██░░░░░░██████████░░░░░░██  
  ██▒▒▒▒░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░████████▓▓▓▓██▒▒▒▒░░░░░░██▓▓██░░░░░░██████▓▓██░░░░░░██  
  ██▒▒▒▒░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░██████▓▓▓▓▓▓██▒▒▒▒░░░░░░██████░░░░░░████▓▓▓▓██░░░░░░██  
  ██▒▒▒▒░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░██████████▓▓██▒▒▒▒░░░░░░░░░░░░░░░░░░████▓▓▓▓██░░░░░░██  
  ██▒▒░░░░████████████████████░░░░░░░░░░██▒▒░░░░░░████████████████▒▒▒▒░░░░░░░░░░░░░░████████████░░░░░░██  
  ██▒▒░░░░██████▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░██████████████████▒▒▒▒▒▒░░░░░░░░████▓▓▓▓▓▓▓▓██░░░░░░██  
  ██▒▒░░░░██████▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░████▓▓▓▓▓▓▓▓████████░░▒▒░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░██  
  ██▒▒░░░░██████▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░████████████▓▓▓▓████▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░██  
  ██▒▒░░░░████▓▓██▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░████▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░██  
  ██▒▒░░░░████████▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████░░░░░░██  
  ██▒▒░░░░████████████████████░░░░░░░░░░██▒▒░░░░░░████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░██  
  ██▒▒░░░░██████████▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░██  
  ██▒▒░░░░██████▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░██  
  ██▒▒░░░░████████▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░██▒▒░░░░░░████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░██  
  ██▒▒░░░░████████████████████░░░░░░░░░░██▒▒░░░░░░██████████████████████████████████████████████▒▒░░░░██  
  ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░██  
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░██  
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██  
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████  

    """)
  elif secound_q.lower() == "white":
    print("Invlied choose 🤡")
  else:
    print("tray agine !")

#  if choose the wrong one shows him the result
elif first_q.lower() == "red":
  print("you choose the wong door end of the game\nyou face Crocodiles 🐊🐊 ")
  print("""
            .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'

        """)
else:
  print("try agine !")


