# Not Done Yet Lmao
import arcade 
import math 
import random
import settings
import os

WIDTH = 800
HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Initialize the sprite lists 
        self.player_list = None
        self.rocks_list = None
        self.monkeys_list = None 
        self.bullets_list = None
        self.hearts_list = None 

        self.player = None
        self.background = None
    
    def setup(self):

        # Sprite Lists 
        self.player_list = arcade.SpriteList()
        self.rocks_list = arcade.SpriteList()
        self.monkeys_list = arcade.SpriteList()
        self.bullets_list = arcade.SpriteList()

        # Set up the player
        self.player = arcade.Sprite("assets/indiana_jones.png", 0.5)
        self.player.center_x = 50
        self.player.center_y = 50
        self.player_list.append(self.player)

        # Set up Rocks 
        self.rock_texture = arcade.make_soft_circle_texture(40, 
                         arcade.color.GRAY_BLUE, outer_alpha=255)

        # Set up Monkeys 
        self.monkey = arcade.Sprite("assets/monkey.png")

        # Set up Bullets 
        self.bullets_texture = arcade.make_soft_circle_texture(15, 
                         arcade.color.BLACK, outer_alpha=255)

        self.hearts_list = arcade.SpriteList()

        # Put 3 hearts in the top left corner 
        for x in range(50, 190, 60):
            heart = arcade.Sprite("assets/heart.png", 0.025)
            heart.center_y = 500
            heart.center_x = x
            self.hearts_list.append(heart)

        self.total_time = 0.0 
        self.score = 0

        # Setup the falling rocks
        for _ in range(55):
            rock = arcade.Sprite()
            rock.center_x = random.randrange(0, WIDTH) 
            rock.center_y = (HEIGHT + 200)
            rock.texture = self.rock_texture
            rock.speed = random.randrange(10, 60)
            rock.angle = random.uniform(math.pi, math.pi * 2)
            self.rocks_list.append(rock) 

        # Setup the falling monkeys 
        for _ in range(30):
            # monkey = arcade.Sprite()
            # monkey.center_x = random.randrange(0, WIDTH)
            # monkey.center_y = (HEIGHT + 1000)
            # monkey.texture = self.monkey_texture
            # monkey.speed = random.randrange(30, 80)
            # monkey.angle = random.uniform(math.pi, math.pi * 2)
            # self.monkeys_list.append(monkey)


        # Import the jungle background 
            self.background = arcade.load_texture("assets/jungle.PNG")

    def on_draw(self):
        # keep as first line
        arcade.start_render()  
        
        arcade.draw_texture_rectangle(settings.WIDTH // 2, 
                             settings.HEIGHT // 2, settings.WIDTH, 
                             settings.HEIGHT, self.background)

        self.player.draw()
        self.rocks_list.draw()
        # self.monkeys_list.draw()
        self.bullets_list.draw()
        self.hearts_list.draw()

        minutes = int(self.total_time) // 60 
        seconds = int(self.total_time) % 60 
        output = f"Time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output, WIDTH - 200, 50, arcade.color.WHITE, 30)

        arcade.draw_text(f"Score: {self.score}", WIDTH - 200, HEIGHT - 490, 
                         arcade.color.BLUE, 36)
        arcade.draw_text(f"Score: {self.score}", WIDTH - 198, HEIGHT - 490, 
                         arcade.color.BABY_BLUE, 36)

    def update(self, delta_time):
        self.rocks_list.update()
        self.bullets_list.update()
        self.total_time += delta_time

        for rock in self.rocks_list:
            rock.center_y -= rock.speed * delta_time
            bullets_hit = rock.collides_with_list(self.bullets_list)
            player_hit = rock.collides_with_sprite(self.player)
            if bullets_hit:
                rock.kill()
                self.score += 1 
                for bullet in bullets_hit:
                    bullet.kill()  
            if player_hit:
                if  len(self.hearts_list) is not 0:
                    heart = self.hearts_list[0]
                    self.hearts_list.remove(heart)
                    rock.kill()
                else:
                    self.player.kill()
            if rock.center_y < 0 or self.score < 55:
                self.player.kill()
            elif self.score == 55:
                arcade.draw_text("You Win", WIDTH//2, HEIGHT//2, 
                                 arcade.color.BLACK, 36)



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
        self.player.center_x = x 
        if y > 100:
            self.player.center_y = y
        else:
            self.player.center_y = 100
    
    def on_mouse_press(self, x, y, button, key_modifiers):
        bullet = arcade.Sprite()
        bullet.center_x = self.player.center_x
        bullet.center_y = self.player.center_y
        bullet.change_y = 5 
        bullet.texture = self.bullets_texture
        bullet.width = 5

        self.bullets_list.append(bullet)

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
