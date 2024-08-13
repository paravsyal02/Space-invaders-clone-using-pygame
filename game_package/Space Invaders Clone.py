import pygame
import sys
import random
import os
import tkinter as tk
from tkinter import simpledialog

# define globally game_volume
game_volume = 0.5

# Define a global variable to hold high scores
highscores = []

# Initialize Pygame
pygame.init()

# Define the screen dimensions
screen_width = 900
screen_height = 600

# Set up the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders Clone")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load background image for the main menu
background_menu_image = pygame.image.load(r"D:\First project\game_package\images\pexels-matthiasgroeneveld-4200740.jpg").convert_alpha()
background_menu_image = pygame.transform.scale(background_menu_image, (screen_width, screen_height))

# Load button images
button_width = 200
button_height = 50
button_image = pygame.Surface((button_width, button_height))
button_image.fill((100, 100, 100))
button_hover_image = pygame.Surface((button_width, button_height))
button_hover_image.fill((150, 150, 150))

# Font
font = pygame.font.Font(None, 36)

# Function to draw background
def draw_background():
    screen.blit(background_menu_image, (0, 0))

# Function to display main menu
def display_main_menu(buttons, hover_states):
    # Draw background
    draw_background()


    # Display buttons
    for button, hover in zip(buttons, hover_states):
        if hover:
            screen.blit(button_hover_image, button)
        else:
            screen.blit(button_image, button)

    # Display labels
    labels = ["Play", "Highscore", "About"]
    for i, label in enumerate(labels):
        label_render = font.render(label, True, WHITE)
        screen.blit(label_render, (buttons[i].centerx - label_render.get_width() // 2, buttons[i].centery - label_render.get_height() // 2))
     # Update the display
    pygame.display.flip()

# Function to handle main menu events
def handle_main_menu_events(buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, button in enumerate(buttons):
                if button.collidepoint(event.pos):
                    return i  # Return the index of the clicked button
    return None

# Function to load highscores
def load_highscores():
    global highscores
    highscores = []
    if os.path.exists(highscore_file):
        with open(highscore_file, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, score = parts
                    highscores.append((name, int(score)))
                elif len(parts) == 1:
                    if parts[0].isdigit():
                        highscores.append(("Player 1", int(parts[0])))
                    else:
                        highscores.append((parts[0], 0))
    else:
        highscores.append(("Player 1", 0))  # Add a default entry if the highscore file does not exist
    return highscores

# Function to save highscores
def save_highscores():
    with open(highscore_file, "w") as file:
        for name, score in highscores:
            file.write(f"{name},{score}\n")

# Function to update highscores
def update_highscore(name, score):
    global highscores
    # Append the new score to highscores list
    highscores.append((name, score))
    # Sort highscores list by score in descending order
    highscores.sort(key=lambda x: x[1], reverse=True)
    # Save the updated highscores
    save_highscores()

# Function to display a congratulations message and prompt for name
def congratulate_and_get_name(score):
    # Display congratulations message
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    tk.messagebox.showinfo("Congratulations!", f"You achieved a new high score of {score}!")
    # Prompt for the player's name
    name = simpledialog.askstring("Enter Your Name", "Congratulations! You achieved a new high score! Please enter your name:")
    if name:
        return name
    else:
        return "Anonymous"  # If the player cancels the dialog, use a default name

# Main game loop
def game_loop():
    import pygame
    import sys
    import random
    import os
    import pygame.mixer
     
    global highscores


    # Initialize Pygame
    pygame.init()

    # Define the screen dimensions
    screen_width = 900
    screen_height = 600

    # Set up the game window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders Clone")

    # Load the background image
    background_image = pygame.image.load(r"D:\First project\game_package\images\Background2.jpg")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Load the background sound
    pygame.mixer.music.load(r"D:\First project\game_package\sounds\navante.mp3")  
    pygame.mixer.music.set_volume(0.5)  # Adjust the volume (0.0 to 1.0)

    # Load laser hit sound effect
    laser_hit_sound = pygame.mixer.Sound(r"D:\First project\game_package\sounds\sfx_laser1.ogg")

    # Define a global variable to hold the game's volume
    game_volume = 0.5  # Default volume

    # Load game over sound effect
    game_over_sound = pygame.mixer.Sound(r"D:\First project\game_package\sounds\fly.mp3")
    game_over_sound.set_volume(0.3)

    # Function to draw replay button
    def draw_replay_button():
        font = pygame.font.Font(None, 36)
        replay_text = font.render("Replay", True, (255,255,0))
        replay_rect = replay_text.get_rect(center=(screen_width // 2, screen_height * 2 // 3))
        button_rect = pygame.Rect(replay_rect.x - 20, replay_rect.y - 20, replay_rect.width + 40, replay_rect.height + 40)

        # Fill the button rectangle with a light gray color
        pygame.draw.rect(screen, (200, 200, 200), button_rect)

        # Check if the mouse is hovering over the button
        hover = button_rect.collidepoint(pygame.mouse.get_pos())

        # Change the color of the text and button rectangle if the mouse is hovering over the button
        if hover:
            replay_text = font.render("Replay", True, WHITE)
            pygame.draw.rect(screen, (150, 150, 150), button_rect)
        else:
            replay_text = font.render("Replay", True, (255,255,0))
            pygame.draw.rect(screen, (200, 200, 200), button_rect)

        screen.blit(replay_text, replay_rect)
        return replay_rect
    

    # Function to play game over sound
    def play_game_over_sound():
        # Play game over sound
        game_over_sound.play()

    # Function to draw background
    def draw_background():
        screen.blit(background_image, (0, 0))

    # Define the path to the highscore file
    highscore_file = "highscore.txt"

    # Function to save highscore
    def save_highscore(highscore):
        with open(highscore_file, "w") as file:
            file.write(str(highscore))

    # Function to load highscore
    def load_highscore():
        if os.path.exists(highscore_file):
            try:
                with open(highscore_file, "r") as file:
                    highscores = [line.strip().split(",") for line in file.readlines()]
                    # Filter out improperly formatted entries and convert scores to integers
                    highscores = [(name, int(score)) for name, score in highscores if name and score.isdigit()]
                    return max(highscores, key=lambda x: x[1])[1] if highscores else 0
            except Exception as e:
                print(f"Error loading highscores: {e}")
                return 0
        else:
            return 0  # Return 0 if the highscore file does not exist


    # Function to display highscore
    def display_highscore(highscore):
        font = pygame.font.Font(None, 36)
        highscore_text = font.render("Highscore: " + str(highscore), True, WHITE)
        screen.blit(highscore_text, (10, 50))

    # Load the settings icon image
    settings_icon = pygame.image.load(r"D:\First project\game_package\images\setting.png").convert_alpha()
    settings_icon = pygame.transform.scale(settings_icon,(30,30))
    
    # Define the settings button rectangle
    settings_button_rect = settings_icon.get_rect(topright=(screen_width - 10, 10))  # Position in top-right corner

    # Function to display the settings button
    def display_settings_button():
        screen.blit(settings_icon, settings_button_rect)
     

    # Function to handle clicks on the settings button
    def handle_settings_button_click():
        global running
        mouse_pos = pygame.mouse.get_pos()
        if settings_button_rect.collidepoint(mouse_pos):
            # Pause the game
            running = False
            # Open settings menu to adjust volume
            open_settings_menu()
    
    # Function to open the settings menu
    def open_settings_menu():
        global game_volume
        # Pause the background music
        pygame.mixer.music.pause()

        # Display a simple volume slider using Tkinter
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        volume = simpledialog.askfloat("Adjust Volume", "Set the volume (0.0 to 1.0):", initialvalue=game_volume)
        if volume is not None:
            game_volume = max(0.0, min(volume, 1.0))  # Ensure volume is within range
            # Update the background music volume
            pygame.mixer.music.set_volume(game_volume)
    
        # Resume the game
        resume_game()

    # Fuction to resume the game
    def resume_game():
        global running
        running = True
        # Resume the background music
        pygame.mixer.music.unpause()

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    

    # Define Player class
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load(r"D:\First project\game_package\images\playerShip1_blue.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.centerx = screen_width // 2
            self.rect.bottom = screen_height - 20
            self.speed = 5
            self.score = 0
        
        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
            # Keep player within the screen bounds
            self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width)) 
   

    new_width = 40
    new_height = 40


    class Alien(pygame.sprite.Sprite):
        def __init__(self, x, y, powerful=False, infinite=False):
            super().__init__()
            if powerful:
                self.image = pygame.image.load(r"D:\First project\game_package\images\enemyGreen3.png").convert_alpha()
            elif infinite:
                self.image = pygame.image.load(r"D:\First project\game_package\images\enemyRed3.png").convert_alpha()
            else:
                self.image = pygame.image.load(r"D:\First project\game_package\images\enemyBlack4.png").convert_alpha()
            
            self.image = pygame.transform.scale(self.image, (new_width, new_height))  # Adjust the size here
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed_x = 10  # Increased speed for horizontal movement
            self.speed_y = 30  # Speed for vertical movement
            self.direction_x = 1  # Initial direction (1 for right, -1 for left)
            self.direction_y = 1  # Initial direction (1 for down)
            self.step_count = 0  # Counter to track steps
            self.hit = False  # Attribute to track whether the alien has been hit or not



        def update(self):
            # Update alien's position horizontally
            self.rect.x += self.speed_x * self.direction_x

            # If alien reaches the edge of the screen horizontally, change direction and move down
            if self.rect.right >= screen_width or self.rect.left <= 0:
                self.direction_x *= -1  # Change horizontal direction (left to right or right to left)
                self.rect.y += self.speed_y  # Move down

            # Increment step count
            self.step_count += 1

            # If step count reaches 60 (twice the previous value), reset the step count
            if self.step_count == 60:
                self.step_count = 0

    # Define Bullet class
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load(r"D:\First project\game_package\images\laserBlue07.png").convert_alpha()  # Load laser image
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.bottom = y
            self.speed = -10  # Negative value to move upwards

        def update(self):
            self.rect.y += self.speed
            # Remove the bullet if it goes off-screen
            if self.rect.bottom < 0:
                self.kill()  # Remove the bullet from all sprite groups

    # Function to create powerful aliens
    def create_powerful_aliens():
        powerful_aliens = pygame.sprite.Group()
        for row in range(num_rows):
            for col in range(num_cols):
                alien_x = 100 + col * alien_spacing_x
                alien_y = 50 + row * alien_spacing_y  # Adjust the vertical position calculation
                alien = Alien(alien_x, alien_y , powerful = True)  # Using the Alien class for powerful aliens
                all_sprites.add(alien)
                powerful_aliens.add(alien)
        return powerful_aliens

    # Function to create infinite powerful aliens
    def create_infinite_aliens():
        infinite_aliens = pygame.sprite.Group()
        for row in range(1000):
            for col in range(num_cols):
                alien_x = 100 + col * alien_spacing_x
                alien_y = -200 - row * alien_spacing_y  # Start above the screen
                alien = Alien(alien_x, alien_y, infinite=True)
                all_sprites.add(alien)
                infinite_aliens.add(alien)
        return infinite_aliens


    # Define the number of rows and columns for the alien formation
    num_rows = 3
    num_cols = 15

    # Define the gap between rows and columns
    alien_spacing_x = 50  # Increase the horizontal gap between columns
    alien_spacing_y = 100  # Increase the vertical gap between rows

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Create player
    player = Player()
    all_sprites.add(player)

    # Create aliens in multiple layers
    for row in range(num_rows):
        for col in range(num_cols):
            alien_x = 100 + col * alien_spacing_x
            alien_y = 50 + row * alien_spacing_y  # Adjust the vertical position calculation
            alien = Alien(alien_x, alien_y)
            all_sprites.add(alien)
            aliens.add(alien)



    # Main game loop
    running = True
    clock = pygame.time.Clock()  # Initialize clock

    # Load the highscore at the beginning of the game
    highscore = load_highscore()

    powerful_aliens = None
    infinite_aliens = None
    start_time = None  # Initialize start time
    update_start_time = pygame.time.get_ticks()  # Initialize update start time for infinite aliens

    # Define game over line
    game_over_line_y = player.rect.top - 8  # Adjust the position as needed

    # Game over flag
    game_over = False

    powerful_hits = {}  # Initialize powerful_hits outside the game loop

    infinite_aliens_hit = {}

    # Start playing background music
    pygame.mixer.music.play(loops=-1)  # Play the background music in an infinite loop

    while running:  # Run the game loop
        current_time = pygame.time.get_ticks()  # Get current time
        # Limit frame rate
        clock.tick(30)  # Adjust the frame rate (e.g., 30 FPS)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Stop the game loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Player shoots bullet when spacebar is pressed
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_settings_button_click()

        # Render game graphics
        screen.fill(BLACK)
        draw_background()  # Draw the background only once per frame

        # Check for collisions between bullets and powerful aliens
        if bullets and powerful_aliens:
            powerful_hits = pygame.sprite.groupcollide(bullets, powerful_aliens, True, True)
            for bullet, alien_hit in powerful_hits.items():
                for alien in alien_hit:
                    if not alien.hit:  # Check if the alien has not been hit before
                        if not game_over:  # Ensure the game is not over before updating the score
                            player.score += 5
                        alien.hit = True  # Mark the alien as hit to prevent multiple score increments
                        laser_hit_sound.play()  # Play laser hit sound effect
        
        # Increment player's score for each hit on powerful aliens
        if powerful_hits:
            if powerful_hits:
                for bullet, alien_hit in powerful_hits.items():
                    for alien in alien_hit:
                        if not alien.hit:  # Check if the alien has not been hit before
                            player.score += 5
                            alien.hit = True  # Mark the alien as hit to prevent multiple score increments

        # Check if score reaches 90 and powerful aliens group is not yet created
        if player.score >= 90 and powerful_aliens is None:
            powerful_aliens = create_powerful_aliens()
            start_time = pygame.time.get_ticks()  # Record
    
        # Update powerful aliens' speed after 3 seconds
        if powerful_aliens and pygame.time.get_ticks() - start_time >= 3000:  # Check if 3 seconds have passed
            for alien in powerful_aliens:
                alien.speed_x += 0.05  # Increase horizontal speed

        # Check for collisions between bullets and regular aliens
        if not game_over:  # Only update bullets if the game is not over
            hits = pygame.sprite.groupcollide(bullets, aliens, True, True) 
            for bullet, alien_hit in hits.items():
                laser_hit_sound.play()  # Play laser hit sound effect
            for bullet, alien_hit in hits.items():
                player.score += len(alien_hit)
        
        # Increment player's score for each hit on regular aliens
        for bullet, alien_hit in hits.items():
            player.score += len(alien_hit)

        # Check for collisions between bullets and infinite aliens
        if not game_over and bullets and infinite_aliens:  # Only update if the game is not over
            infinite_aliens_hit = pygame.sprite.groupcollide(bullets, infinite_aliens, True, True)
        for bullet, alien_hit in infinite_aliens_hit.items():
            for alien in alien_hit:
                if not alien.hit:  # Check if the alien has not been hit before
                    player.score += 10 * len(alien_hit)  # Increase score by 10 for each hit
                    alien.hit = True  # Mark the alien as hit to prevent multiple score increments
                    laser_hit_sound.play()

        # Increment player's score for each hit on infinite aliens
        if infinite_aliens_hit:
            for bullet, alien_hit in infinite_aliens_hit.items():
                for alien in alien_hit:
                    if not alien.hit:  # Check if the alien has not been hit before
                        player.score += 10 * len(alien_hit)  # Increase score by 10 for each hit
                        alien.hit = True  # Mark the alien as hit to prevent multiple score increments


        # Check if any alien crosses the game over line
        for alien in aliens:
            if alien.rect.bottom >= game_over_line_y:
                game_over = True  # Set game over flag

        # Check if any powerful alien crosses the game over line
        if powerful_aliens:
            for alien in powerful_aliens:
                if alien.rect.bottom >= game_over_line_y:
                    game_over = True  # Set game over flag

        if not game_over:  # If game is not over, update game state
            # Update game state
            all_sprites.update()

        # Check if score reaches 315 and infinite aliens group is not yet created
        if player.score >= 315 and infinite_aliens is None:
            infinite_aliens = create_infinite_aliens()
            start_time = pygame.time.get_ticks()  # Record the start time

        # Update infinite aliens' position after 3 seconds
        if infinite_aliens and current_time - update_start_time >= 3000:  # Check if 3 seconds have passed
            for alien in infinite_aliens:
                alien.rect.y +=  2  # Update vertical position of infinite aliens



        # Update game state for infinite aliens
        if infinite_aliens:
            for alien in infinite_aliens:
                alien.update()

        # Check if any infinite alien crosses the game over line
        if infinite_aliens:
            for alien in infinite_aliens:
                if alien.rect.bottom >= game_over_line_y:
                    game_over = True  # Set game over flag

        # Load highscores from the file
        highscores = load_highscores()

        # Render game graphics
        screen.fill(BLACK)
        draw_background()  # Draw the background only once per frame

        if not game_over:
            all_sprites.draw(screen)
        else:
            # Stop background music volume
            pygame.mixer.music.stop()  # Adjust volume as needed
            # Play game over sound
            play_game_over_sound()
            # Display "Game Over" if game over flag is True
            game_over_font = pygame.font.Font(None, 72)  # Larger font size
            game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))  # Bright red color
            game_over_text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(game_over_text, game_over_text_rect)
            
            # Display replay button
            replay_rect = draw_replay_button()
            # Check for mouse click on replay button
            mouse_pos = pygame.mouse.get_pos()
            if replay_rect.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Stop the game over sound
                    game_over_sound.stop()
                    # Restart the game
                    game_loop()
            
            # Check if the player's score is a new high score
            if player.score > highscores[0][1]:  # Check if the player's score is a new high score
                # Display congratulations message and prompt for the player's name
                name = congratulate_and_get_name(player.score)
                # Update the high scores with the new score and player's name
                update_highscore(name, player.score)
        
        # Display the settings button
        display_settings_button()

        # Display player's score
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(player.score), True, WHITE)
        screen.blit(score_text, (10, 10))

        # Display highscore
        display_highscore(highscore)

        # Draw game over line
        pygame.draw.line(screen, (255, 0, 0), (0, game_over_line_y), (screen_width, game_over_line_y), 2)

        # Update display
        pygame.display.flip()

        # Limit frame rate
        clock.tick(30)  # Adjust the frame rate (e.g., 30 FPS)

    # Quit Pygame
    pygame.quit()
    sys.exit()


# Define button rectangles
button_spacing = 20
button_top_margin = screen_height // 2 - (button_height * 3 + button_spacing * 2) // 2
buttons = [
    pygame.Rect(screen_width // 2 - button_width // 2, button_top_margin + (button_height + button_spacing) * i, button_width, button_height)
    for i in range(3)
]
hover_states = [False] * len(buttons)

running = True
clock = pygame.time.Clock()  # Initialize clock

# Define the path to the highscore file
highscore_file = "highscore.txt"

# Function to reset highscore table
def reset_highscores():
    # Check if the highscore file exists
    if os.path.exists(highscore_file):
        # Remove the highscore file
        os.remove(highscore_file)
        print("Highscore table has been reset.")
    else:
        print("Highscore table does not exist.")
    
# Call the function to reset highscores
#reset_highscores()

# Function to display high scores screen
def display_highscores_screen():
    # Load the background image
    background_img = pygame.image.load(r"D:\First project\game_package\images\pexels-googledeepmind-17483811.jpg").convert()
    background_img = pygame.transform.scale(background_img, (screen_width, screen_height))
    
    # Blit the background image onto the screen
    screen.blit(background_img, (0, 0))

    # Create a bold font
    font = pygame.font.Font(None, 36)
    bold_font = pygame.font.Font(None, 36)
    bold_font.set_bold(True)
    font_title = pygame.font.Font(None, 48)
    title_text = font_title.render("Top 10 Highscores", True, (255,0,0))
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))

    highscores = load_highscores()
    y = 100  # Starting y-coordinate for the first score
    for i, (name, score) in enumerate(highscores):
        score_text = font.render(f"{i+1}. {name}: {score}", True, (255,255,0))
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, y))
        y += 50  # Increment y-coordinate for the next score

    pygame.display.flip()


def display_about_screen():
    screen.fill(BLACK)
    
    # Load and scale the background image
    background_image = pygame.image.load(r"D:\First project\game_package\images\pexels-tara-winstead-8386365.jpg").convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    screen.blit(background_image, (0, 0))
    
    font_title = pygame.font.Font(None, 48)
    font_text = pygame.font.Font(None, 24)
    
    # Title
    title_text = font_title.render("About", True, (255,0,0))
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))
    
    # Game information
    game_info_text = font_text.render("This is a Space Invaders Clone created using Pygame.", True, WHITE)
    screen.blit(game_info_text, (50, 150))
    
    # How to play
    how_to_play_title = font_title.render("How to Play", True, (255,0,0))
    screen.blit(how_to_play_title, (screen_width // 2 - how_to_play_title.get_width() // 2, 250))
    
    instructions = [
        "Use the left and right arrow keys to move the player spaceship.",
        "Press the spacebar to shoot lasers.",
        "Destroy aliens by shooting them with lasers.",
        "Avoid letting any alien reach the bottom of the screen.",
        "Score points for each alien destroyed.",
        "The game ends when an alien reaches the bottom of the screen.",
        "Try to achieve the highest score possible!"
    ]
    
    y_offset = 300
    for instruction in instructions:
        instruction_text = font_text.render(instruction, True, WHITE)
        screen.blit(instruction_text, (50, y_offset))
        y_offset += 30
    
    # Update the display
    pygame.display.flip()



# Define a flag to track if the highscore screen is displayed
highscore_displayed = False
about_displayed = False

# Main loop
while running:
    # Display main menu
    display_main_menu(buttons, hover_states)

    # Handle main menu events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, button in enumerate(buttons):
                if button.collidepoint(event.pos):
                    print(f"Button {i + 1} clicked!")  # Index starts from 0
                    if i == 0:
                        print("Starting the game...")
                        # Start the game loop
                        game_loop()
                    elif i == 1:
                        print("Displaying highscore...")
                        # Display highscore
                        highscore_displayed = True
                    elif i == 2:
                        print("Displaying about...")
                        # Display about
                        about_displayed = True

    # Check if the highscore screen is displayed
    if highscore_displayed:
        display_highscores_screen()
        
        # Wait for a mouse click to return to the main menu
        waiting_for_click = True
        while waiting_for_click:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    waiting_for_click = False
                    highscore_displayed = False  # Reset the flag to return to the main menu
    
# Check if the about screen is displayed
    if about_displayed:
        display_about_screen()

        # Wait for a mouse click to return to the main menu
        waiting_for_click = True
        while waiting_for_click:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    waiting_for_click = False
                    about_displayed = False  # Reset the flag to return to the main menu

    # Check for button hover
    mouse_pos = pygame.mouse.get_pos()
    for i, button in enumerate(buttons):
        hover_states[i] = button.collidepoint(mouse_pos)

    # Limit frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
