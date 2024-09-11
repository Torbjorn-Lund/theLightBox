#from rgb_matrix import Matrix
#from internett import Server_functiones
from lib.lightbox_functionality import my_lightbox

# Sets variables
my_lightbox.max_button_count = 5
# Make your own functiones!

def event_loop():
    # sycles through the event loop indeffinently
    button_count = my_lightbox.button_count
        
    
    # What should the matrix do?
    if button_count == 1:
        print(f"Button count is: {button_count}")
        my_lightbox.run = True
        my_lightbox.show_clock((255,255,255))

    elif button_count == 2:
        print(f"Button count is: {button_count}")
        my_lightbox.run = True
        my_lightbox.show_info()
         
    elif button_count == 3:
        print(f"Button count is: {button_count}")
        my_lightbox.run = True
        my_lightbox.show_rainbow_effects(10)

    elif button_count == 4:
        print(f"Button count is: {button_count}")
        my_lightbox.run = True
        my_lightbox.show_smileys(10)
         
    # Displays the different PPM P3 images
    elif button_count == 5:
        print(f"Button count is: {button_count}")
        my_lightbox.run = True
        my_lightbox.show_images_ppm("/images", 5)
        
    # Enters when in sleep mode
    elif button_count == 0:
         pass
    
    # Error handling
    else:
        print("error. button_count out of range")
        return "button_count_error"    