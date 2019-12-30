import arcade 
import math 
import random

WIDTH = 800
HEIGHT = 600
lives = 3 

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.player = arcade.Sprite(center_x=WIDTH//2, center_y=100)
        self.player.texture = arcade.make_soft_square_texture(50, arcade.color.BLUE, outer_alpha=255)

        self.rock_texture = arcade.make_soft_circle_texture(25, arcade.color.GRAY, outer_alpha=255)
        self.rocks = arcade.SpriteList()

        i = 0
        while i < 60:
            for _ in range(10):
                rock = arcade.Sprite()
                rock.center_x = random.randrange(0, WIDTH) 
                rock.center_y = HEIGHT + 100
                rock.texture = self.rock_texture
                rock.speed = random.randrange(100, 200)
                rock.angle = random.uniform(math.pi, math.pi * 2)
                self.rocks.append(rock) 
            i += 1

    def on_draw(self):
        arcade.start_render()  # keep as first line

        self.player.draw()
        self.rocks.draw()

    def update(self, delta_time):
        self.rocks.update()

        for rock in self.rocks:
            rock.center_y -= rock.speed * delta_time

        for rock in self.rocks:   
            if rock.collides_with_sprite(self.player):
                global_lives -= 1 
                if global_lives == 0: 
                    arcade.draw_text("Game Over") 

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.player.center_x = x 
        self.player.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game") 
    arcade.run()


if __name__ == "__main__":
    main()

"""
Things I still need to do:
Let the objects fall for a specified amount of time. 
When objects hit user, minus 1 life 
When player loses all 3 lives, player dies 
When player survives for the specified amount of time, a key is awarded 
"""
