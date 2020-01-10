# Not Done Yet Lmao
import arcade 
import math 
import random
import os

WIDTH = 800
HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.player_list = None
        self.rocks_list = None
        self.bullets_list = None

        self.player_sprite = None 

    def setup(self): 
        arcade.set_background_color(arcade.color.CADMIUM_ORANGE)

        # Sprite Lists 
        self.player_list = arcade.SpriteList()
        self.rocks_list = arcade.SpriteList()
        self.bullets_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(center_x=WIDTH//2, center_y=100)
        self.player.texture = arcade.make_soft_square_texture(50, arcade.color.BLUE, outer_alpha=255)
        self.player_list.append(self.player_sprite)

        self.rock_texture = arcade.make_soft_circle_texture(40, 
                         arcade.color.GRAY, outer_alpha=255)
        
        self.bullets_texture = arcade.make_soft_circle_texture(15, 
                         arcade.color.BLACK, outer_alpha=255)

        self.total_time = 0.0 
        self.score = 0

        for _ in range(40):
            rock = arcade.Sprite()
            rock.center_x = random.randrange(0, WIDTH) 
            rock.center_y = (HEIGHT + 200)
            rock.texture = self.rock_texture
            rock.speed = random.randrange(10, 60)
            rock.angle = random.uniform(math.pi, math.pi * 2)
            self.rocks_list.append(rock) 
           
            

    def on_draw(self):
        arcade.start_render()  # keep as first line

        self.player_sprite.draw()
        self.rocks_list.draw()
        self.bullets_list.draw()
        self.hearts_list.draw()

        minutes = int(self.total_time) // 60 
        seconds = int(self.total_time) % 60 

        output = f"Time: {minutes:02d}:{seconds:02d}"

        arcade.draw_text(output, WIDTH - 200, 50, arcade.color.BLACK, 30)

        arcade.draw_text("Lives", 100, 500, arcade.color.BLACK, 36)

        arcade.draw_text(f"Score: {self.score}", WIDTH - 200, HEIGHT - 490, 
                         arcade.color.BLUE, 36)
        arcade.draw_text(f"Score: {self.score}", WIDTH - 198, HEIGHT - 490, 
                         arcade.color.BABY_BLUE, 36)

    def update(self, delta_time):
        for rock in self.rocks_list:
            rock.center_y -= rock.speed * delta_time
            bullets_hit = rock.collides_with_list(self.bullets)
            player_hit = rock.collides_with_sprite(self.player_sprite)
            if bullets_hit:
                rock.kill()
                self.score += 1 
                for bullet in bullets_hit:
                    bullet.kill()  
            if player_hit:
                self.hearts_list.remove(heart)
            if rock.center_y < 0 or self.score < 55:
                self.player_sprite.kill()
            elif self.score == 55:
                arcade.draw_text("You Win", WIDTH//2, HEIGHT//2, arcade.color.BLACK, 36)



        # if output > "1:00":
        #     arcade.draw_text("You Win", WIDTH - 200, 50, arcade.color.BLACK, 30)

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
        self.player_sprite.center_x = x 
        self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        bullet = arcade.Sprite()
        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y
        bullet.change_y = 5 
        bullet.texture = self.bullets_texture
        bullet.width = 5

        self.bullets.append(bullet)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game") 
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

"""
Fix How to Win and Lose Games 
Reorganize Code 
"""
