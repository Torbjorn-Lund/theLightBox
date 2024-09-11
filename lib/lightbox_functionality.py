from rgb_matrix import Matrix_fun

class Lightbox_object(Matrix_fun):
    """
    This class includes all the nececarry functionalety for controlling the Lightbox
    """

    def __init__(self, width: int, height: int, gpio_pin: int) -> None:
        super().__init__(width, height, gpio_pin)
        self.button_count = 1
        self.max_button_count = 6
    
    def change_button_count(self, increment: int) -> None:
        """ Increments the button count, and makes sure the program can move forward to the next event """

        # Increment the button count
        self.button_count += increment

        # Stop current program
        self.run = False

        # Makes shure that the count does not go too far
        if self.button_count > self.max_button_count or self.button_count < 1:
            self.button_count = 1
    
    def set_button_count(self, count: int) -> None:
        """ Sets the button count """
        self.button_count = count
        self.run = False
    
    def change_brightness(self, brightness_percent:int) -> None:
        """ Updates brightness """
        self.run = False
        self.set_brightness(brightness_percent)

my_lightbox = Lightbox_object(16,16,1)

