import numpy
class menu:
    a = (r'''                                                              
  ,ad8888ba,                             88           88      
 d8"'    `"8b                            ""           88      
d8'                                                   88      
88              ,adPPYba,   8b       d8  88   ,adPPYb,88      
88             a8"     "8a  `8b     d8'  88  a8"    `Y88      
Y8,            8b       d8   `8b   d8'   88  8b       88      
 Y8a.    .a8P  "8a,   ,a8"    `8b,d8'    88  "8a,   ,d88      
  `"Y8888Y"'    `"YbbdP"'       "8"      88   `"8bbdP"Y8      
                                                              
                                                              
                                                              
       db                      88                             
      d88b                     ""                             
     d8'`8b                                                   
    d8'  `8b      8b,dPPYba,   88                             
   d8YaaaaY8b     88P'    "8a  88                             
  d8""""""""8b    88       d8  88                             
 d8'        `8b   88b,   ,a8"  88                             
d8'          `8b  88`YbbdP"'   88                             
                  88                                          
                  88                                          
                                                              
 ad88888ba                           88                       
d8"     "8b                          ""                ,d     
Y8,                                                    88     
`Y8aaaaa,     ,adPPYba,  8b,dPPYba,  88  8b,dPPYba,  MM88MMM  
  `"""""8b,  a8"     ""  88P'   "Y8  88  88P'    "8a   88     
        `8b  8b          88          88  88       d8   88     
Y8a     a8P  "8a,   ,aa  88          88  88b,   ,a8"   88,    
 "Y88888P"    `"Ybbd8"'  88          88  88`YbbdP"'    "Y888  
                                         88                   
                                         88                   ''')
    b = (r''' ██████╗ ██████╗ ██╗   ██╗██╗██████╗        
██╔════╝██╔═══██╗██║   ██║██║██╔══██╗       
██║     ██║   ██║██║   ██║██║██║  ██║       
██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║       
╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝       
 ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝        
                                            
 █████╗ ██████╗ ██╗                         
██╔══██╗██╔══██╗██║                         
███████║██████╔╝██║                         
██╔══██║██╔═══╝ ██║                         
██║  ██║██║     ██║                         
╚═╝  ╚═╝╚═╝     ╚═╝                         
                                            
███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
███████╗██║     ██████╔╝██║██████╔╝   ██║   
╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
███████║╚██████╗██║  ██║██║██║        ██║   
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ''')
    c = (r'''╔═╗┌─┐┬  ┬┬┌┬┐  
║  │ │└┐┌┘│ ││  
╚═╝└─┘ └┘ ┴─┴┘  
╔═╗┌─┐┬         
╠═╣├─┘│         
╩ ╩┴  ┴         
╔═╗┌─┐┬─┐┬┌─┐┌┬┐
╚═╗│  ├┬┘│├─┘ │ 
╚═╝└─┘┴└─┴┴   ┴ ''')
    d = (r'''   █████████                        ███      █████       
  ███░░░░░███                      ░░░      ░░███        
 ███     ░░░   ██████  █████ █████ ████   ███████        
░███          ███░░███░░███ ░░███ ░░███  ███░░███        
░███         ░███ ░███ ░███  ░███  ░███ ░███ ░███        
░░███     ███░███ ░███ ░░███ ███   ░███ ░███ ░███        
 ░░█████████ ░░██████   ░░█████    █████░░████████       
  ░░░░░░░░░   ░░░░░░     ░░░░░    ░░░░░  ░░░░░░░░        
                                                         
                                                         
                                                         
   █████████              ███                            
  ███░░░░░███            ░░░                             
 ░███    ░███  ████████  ████                            
 ░███████████ ░░███░░███░░███                            
 ░███░░░░░███  ░███ ░███ ░███                            
 ░███    ░███  ░███ ░███ ░███                            
 █████   █████ ░███████  █████                           
░░░░░   ░░░░░  ░███░░░  ░░░░░                            
               ░███                                      
               █████                                     
              ░░░░░                                      
  █████████                      ███             █████   
 ███░░░░░███                    ░░░             ░░███    
░███    ░░░   ██████  ████████  ████  ████████  ███████  
░░█████████  ███░░███░░███░░███░░███ ░░███░░███░░░███░   
 ░░░░░░░░███░███ ░░░  ░███ ░░░  ░███  ░███ ░███  ░███    
 ███    ░███░███  ███ ░███      ░███  ░███ ░███  ░███ ███
░░█████████ ░░██████  █████     █████ ░███████   ░░█████ 
 ░░░░░░░░░   ░░░░░░  ░░░░░     ░░░░░  ░███░░░     ░░░░░  
                                      ░███               
                                      █████              
                                     ░░░░░               ''')

def menufetch():
    a = numpy.random.randint(0,4)
    if a == 0:
        print(menu.a)
    if a == 1:
        print(menu.b)
    if a == 2:
        print(menu.c)
    if a == 3:
        print(menu.d)
    