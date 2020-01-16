# Not Done Yet Lmao
import arcade 
import math 
import random
import settings
import os
from kevin_minigame import KevinView

WIDTH = 800
HEIGHT = 600

# INSTRUCTION_PAGE = 0
# GAME_RUNNING = 1
# GAME_OVER = 2

class CalebMenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to Caleb's Minigame!", settings.WIDTH/2, 
                         settings.HEIGHT//(3/2),
                         arcade.color.BLACK, font_size=40, anchor_x="center")

        arcade.draw_text("Press SPACE to Continue", settings.WIDTH/2, 
                         settings.HEIGHT/2-75, arcade.color.GRAY, 
                         font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            instruction_view = CalebInstructionView()
            self.window.show_view(instruction_view)


class CalebInstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("How to Play?", settings.WIDTH/2, 500,
                         arcade.color.BLACK, font_size=40, anchor_x="center")
        arcade.draw_text("You have 3 lives. Destroy all the rocks, monkeys and kill", settings.WIDTH/2, settings.HEIGHT/2 + 100,
                         arcade.color.BLACK, font_size=18, anchor_x="center")
        arcade.draw_text("the jungle monster to obtain a key to advance to the next level.", settings.WIDTH/2, settings.HEIGHT/2 + 50,
                         arcade.color.BLACK, font_size=18, anchor_x="center")
        arcade.draw_text("Be Careful! If any of them touch you or leave the screen, you will lose a life.", settings.WIDTH/2, settings.HEIGHT/2,
                         arcade.color.BLACK, font_size=18, anchor_x="center")
        arcade.draw_text("Good Luck!", settings.WIDTH/2, settings.HEIGHT/2 - 50,
                         arcade.color.BLACK, font_size=18, anchor_x="center")
        arcade.draw_text("Click SPACE to Start", settings.WIDTH/2, settings.HEIGHT/2-150,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = CalebGameView()
        self.window.show_view(game_view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = CalebGameView()
            self.window.show_view(game_view)

class CalebGameView(arcade.View):
    def __init__(self):
        super().__init__()

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Initialize the sprite lists
        self.player_list = None
        self.rocks_list = None
        self.monkeys_list = None 
        self.banana_list = None 
        self.bullets_list = None
        self.hearts_list = None 
        self.jungle_monster_list = None 
        self.jungle_bullets_list = None 
        self.count = 0 
        self.key_list = None 

        self.player = None
        self.background = None
    
    def on_show(self):

        # Sprite Lists 
        self.player_list = arcade.SpriteList()
        self.rocks_list = arcade.SpriteList()
        self.monkeys_list = arcade.SpriteList()
        self.banana_list = arcade.SpriteList()
        self.bullets_list = arcade.SpriteList()
        self.hearts_list = arcade.SpriteList()
        self.jungle_monster_list = arcade.SpriteList()
        self.jungle_bullets_list = arcade.SpriteList()
        self.key_list = arcade.SpriteList()

        # Set up the player
        self.player = arcade.Sprite("assets/indiana_jones.png", 0.5)
        self.player.center_x = 50
        self.player.center_y = 50
        self.player_list.append(self.player)

        # Set up Rocks 
        self.rock_texture = arcade.make_soft_circle_texture(40, 
                         arcade.color.GRAY_BLUE, outer_alpha=255)

        # Set up Bullets 
        self.bullets_texture = arcade.make_soft_circle_texture(15, 
                         arcade.color.BLACK, outer_alpha=255)

        # Put 3 hearts in the top left corner 
        for x in range(50, 190, 60):
            heart = arcade.Sprite("assets/heart.png", 0.1)
            heart.center_y = 500
            heart.center_x = x
            self.hearts_list.append(heart)

        self.total_time = 0.0 
        self.score = 0

        # Setup the falling rocks
        for _ in range(30):
            rock = arcade.Sprite()
            rock.center_x = random.randrange(0, WIDTH) 
            rock.center_y = HEIGHT + 20000
            rock.texture = self.rock_texture
            rock.speed = random.randrange(30, 60)
            rock.angle = random.uniform(math.pi, math.pi * 2)
            self.rocks_list.append(rock) 

        # Setup the falling monkeys 
        for _ in range(18):
            monkey = arcade.Sprite("assets/monkey.png", 0.20)
            monkey.center_x = random.randrange(100, WIDTH)
            monkey.center_y = HEIGHT + 42500
            monkey.speed_x = 50
            monkey.speed_y = random.randrange(20, 30)
            self.monkeys_list.append(monkey)
      
        # Setup the jungle boss 
        for _ in range(1):
            jungle_monster = arcade.Sprite("assets/junglemonster.PNG")
            jungle_monster.center_x = 400
            jungle_monster.center_y = 500 # HEIGHT + 440
            jungle_monster.speed_x = 0 
            jungle_monster.speed_y = 0
            self.jungle_monster_list.append(jungle_monster) 
        
        # Set up Jungle bullets 
        self.jungle_bullets_texture = arcade.make_soft_circle_texture(10, 
                         arcade.color.GREEN, outer_alpha=255)


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
        self.monkeys_list.draw()
        self.banana_list.draw()
        self.bullets_list.draw()
        self.hearts_list.draw()
        self.jungle_monster_list.draw()
        self.jungle_bullets_list.draw()
        self.key_list.draw()

        # Draw time 
        minutes = int(self.total_time) // 60 
        seconds = int(self.total_time) % 60 
        output = f"Time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output, WIDTH - 200, 50, arcade.color.WHITE, 30)

        # Draw score 
        arcade.draw_text(f"Score: {self.score}", WIDTH - 200, HEIGHT - 490, 
                         arcade.color.BLUE, 36)
        arcade.draw_text(f"Score: {self.score}", WIDTH - 198, HEIGHT - 490, 
                         arcade.color.BABY_BLUE, 36)
    

    def update(self, delta_time):
        self.rocks_list.update()
        self.bullets_list.update()
        self.banana_list.update()
        self.jungle_bullets_list.update()
        self.total_time += delta_time

        for rock in self.rocks_list:
            # Make rocks move 
            rock.center_y -= rock.speed * delta_time
            bullets_hit_rock = rock.collides_with_list(self.bullets_list)
            player_hit_rock = rock.collides_with_sprite(self.player)
            
            # Get rid of rock and bullets when they collide 
            if bullets_hit_rock:
                rock.kill()
                self.score += 1 
                for bullet in bullets_hit_rock:
                    bullet.kill()

            # Get rid of a heart when rock collides with player or leaves screen  
            if player_hit_rock or rock.center_y < 0:
                if len(self.hearts_list) is not 0:
                    heart = self.hearts_list[0]
                    self.hearts_list.remove(heart)
                    rock.kill()

        for monkey in self.monkeys_list:
            # Make monkeys move side to side 
            monkey.center_x += monkey.speed_x * delta_time

            if monkey.center_x < 0:
                monkey.speed_x = 50
            elif monkey.center_x > 800:
                monkey.speed_x = -50

            # Make monkeys move down 
            monkey.center_y -= monkey.speed_y * delta_time 

            bullets_hit_monkey = monkey.collides_with_list(self.bullets_list)
            monkey_hit_player = monkey.collides_with_sprite(self.player)

            # Get rid of monkey and bullet when they collide 
            if bullets_hit_monkey and monkey.center_y <= 600:
                monkey.kill()
                self.score += 1 
                for bullet in bullets_hit_monkey:
                    bullet.kill()
            
            # Get monkeys to shoot bananas
            if monkey.center_y < 600 and random.randrange(200) == 0:
                banana = arcade.Sprite("assets/banana.gif", 0.15)
                banana.center_x = monkey.center_x 
                banana.angle = -90 
                banana.top = monkey.bottom
                banana.change_y = -5
                self.banana_list.append(banana)        

            # Get rid of a heart when a monkey collides with the player
            if monkey_hit_player or monkey.center_y < 0:
                if len(self.hearts_list) is not 0:
                    heart = self.hearts_list[0]
                    self.hearts_list.remove(heart)
                    monkey.kill()
            
        for banana in self.banana_list:
            # If the banana hits the player, the banana is removed 
            if banana.collides_with_sprite(self.player):
                banana.kill()  
                # Get rid of heart 
                if len(self.hearts_list) is not 0:
                    heart = self.hearts_list[0]
                    self.hearts_list.remove(heart)

            # If a bullet hits a banana, the bullet and banana is destroyed
            if banana.collides_with_list(self.bullets_list):
                banana.kill() 
                for bullet in self.bullets_list:
                    bullet.kill()

        # Get jungle monster to shoot at player 
        for jungle_monster in self.jungle_monster_list: 
            jungle_monster.center_y -= jungle_monster.speed_y * delta_time
            if jungle_monster.center_y < 700 and random.randrange(50) == 0:
                start_x = jungle_monster.center_x 
                start_y = jungle_monster.center_y 

                dest_x = self.player.center_x
                dest_y = self.player.center_y

                dist_x = dest_x - start_x
                dist_y = dest_y - start_y 
                angle = math.atan2(dist_y, dist_x)

                jungle_bullets = arcade.Sprite()
                jungle_bullets.texture = self.jungle_bullets_texture
                jungle_bullets_speed = 5 
                jungle_bullets.width = 50
                jungle_bullets.center_x = start_x
                jungle_bullets.center_y = start_y

                jungle_bullets.angle = math.degrees(angle) 

                jungle_bullets.change_x = math.cos(angle) * jungle_bullets_speed
                jungle_bullets.change_y = math.sin(angle) * jungle_bullets_speed
                self.jungle_bullets_list.append(jungle_bullets)


            # Player must hit the jungle monster 25 times to kill him
            bullets_hit_jungle_monster = jungle_monster.collides_with_list(self.bullets_list)
                
            if bullets_hit_jungle_monster and jungle_monster.center_y < 700:
                self.count += 1 
                print(self.count)
                for bullet in bullets_hit_jungle_monster:
                    bullet.kill()
                    if self.count == 1:
                        jungle_monster.kill()  
                        # When jungle monster is killed, show key
                        key_sprite = arcade.Sprite("assets/key.png")
                        key_sprite.center_x = jungle_monster.center_x
                        key_sprite.center_y = jungle_monster.center_y
                        self.key_list.append(key_sprite)

        key_collected = arcade.check_for_collision_with_list(self.player, self.key_list)
        for key in key_collected:
            key.remove_from_sprite_lists()
            completed = True


            if completed is True:
                game_complete = GameCompleteView()
                self.window.show_view(game_complete)

        # If jungle bullets hit player, remove a heart
        for jungle_bullets in self.jungle_bullets_list:
            jungle_bullets_hit_player = jungle_bullets.collides_with_sprite(self.player)
            if jungle_bullets_hit_player:
                if len(self.hearts_list) is not 0:
                    heart = self.hearts_list[0]
                    self.hearts_list.remove(heart)
                    jungle_bullets.kill()  
                        
        
        # If the player doesn't have any hearts left, they lose 
        if len(self.hearts_list) == 0:
            game_over_view = GameOverView()
            self.window.show_view(game_over_view)
     
    def on_key_press(self, key, key_modifiers):
        # If A is pressed, switch to the next view
        if key == arcade.key.A:
            self.director.next_view()

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        # Restricts where the player can go 
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
        

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()


    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", 250, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Press R to Restart", 300, 200, arcade.color.WHITE, 24)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            game_view = CalebGameView()
            self.window.show_view(game_view)
        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

class GameCompleteView(arcade.View):
    def __init__(self):
        super().__init__()


    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Complete", 250, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Press Space to Continue", 300, 200, arcade.color.WHITE, 24)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            next_game = KevinView()
            self.window.show_view(next_game)
        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)
        

if __name__ == "__main__":
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = CalebMenuView()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    # main()
    arcade.run()


"""
Fix How to Win and Lose Games  
Add "Jungle Boss" 
"""
