import sys
import pygame
import pygame.mixer
from collision import*
from info_bar import*
from menu import Button, Menu, MainMenu
from particles import*
from sounds import SoundManager

FPS = 30
fps_clock = pygame.time.Clock()
WINDOWWIDTH = WINDOW_WIDTH
WINDOWHEIGHT = WINDOW_HEIGHT

global FPSCLOCK, DISPLAYSURF, CAMERA
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('R Type')

CAMERA = Vector2(10000, 0)

game_state = MENU
game_state_old = MENU
collision_manager = CollisionManager()
particle_manager = ParticleManager()
sounds_manager = SoundManager()
info = Bar()
menu = MainMenu()

level = Map("Assets/level1.png", "Assets/level1_collision2.png")
player = Player(INIT_PLAYER_POS, "Assets/player.png")
player_bullets = []
enemy_bullets = []
enemies = []


def main():
    initialize()
    while True:  # main game loop
        DISPLAYSURF.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        update()
        draw()
        pygame.display.update()
        fps_clock.tick(FPS)


def initialize():
    CAMERA.x -= CAMERA.x

    particle_manager.restart()
    player.initialize(INIT_PLAYER_POS)

    del player_bullets[0:len(player_bullets)]
    del enemy_bullets[0:len(enemy_bullets)]
    del enemies[0:len(enemies)]

    #ENEMIES
    #flying soucer
    fs_texture = "Assets/enemy_flying_1.png"
    e_fs = FlyingSoucer(Vector2(1500, 200), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(1580, 150), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(1660, 100), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(1740, 150), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(1820, 200), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(1900, 250), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(1980, 300), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(2060, 250), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)

    e_fs = FlyingSoucer(Vector2(4550, 200), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(4630, 150), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(4710, 100), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(4780, 150), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(4860, 200), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(4940, 250), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(5020, 300), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(5100, 250), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)

    e_fs = FlyingSoucer(Vector2(6200, 200), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(6280, 150), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(6360, 100), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(6440, 150), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(6520, 200), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(6600, 250), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(6660, 300), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(6720, 250), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)

    e_fs = FlyingSoucer(Vector2(8200, 200), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(8300, 150), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(8400, 100), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(8500, 150), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(8600, 200), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(8700, 250), Vector2(0, -1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(8800, 300), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)
    e_fs = FlyingSoucer(Vector2(8900, 250), Vector2(0, 1), 4, fs_texture,
                        8, 5)
    enemies.append(e_fs)

    #walker
    w_text = "Assets/walker_1.png"
    e_walker = Walker(Vector2(1500, 420), Vector2(0, 1), 4, w_text, 3, 6)
    enemies.append(e_walker)
    e_walker = Walker(Vector2(3400, 420), Vector2(0, 1), 4, w_text, 3, 6)
    enemies.append(e_walker)
    e_walker = Walker(Vector2(5350, 420), Vector2(0, 1), 4, w_text, 3, 6)
    enemies.append(e_walker)
    e_walker = Walker(Vector2(8000, 355), Vector2(0, 1), 4, w_text, 3, 6)
    enemies.append(e_walker)
    e_walker = Walker(Vector2(9050, 420), Vector2(0, 1), 4, w_text, 3, 6)
    enemies.append(e_walker)
    e_walker = Walker(Vector2(10700, 420), Vector2(0, 1), 4, w_text, 3, 6)
    enemies.append(e_walker)

    #turret
    turret_text = "Assets/turret_bot.png"
    e_turret = Turret(Vector2(2000, 390), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    turret_text = "Assets/turret_top.png"
    e_turret = Turret(Vector2(4450, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(4800, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(5075, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(5910, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(6150, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(6520, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(7640, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(7850, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(8340, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(8570, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(8800, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(10270, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(10370, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(10540, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(10670, 120), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)
    e_turret = Turret(Vector2(9540, 60), Vector2(0, 1), 4, turret_text,
                      6, 10)
    enemies.append(e_turret)

    #suicide
    s_text = "Assets/suicide.png"
    e_suicide = Suicide(Vector2(2500, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(2600, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(2700, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(2800, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(2900, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(3000, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(3100, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(3200, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(3300, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)

    e_suicide = Suicide(Vector2(6800, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(6900, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(7000, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(7100, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(7200, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(7300, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(7400, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(7500, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(7600, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(7700, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)
    e_suicide = Suicide(Vector2(7800, 300), Vector2(0, 0), 5, s_text, 6, 15)
    enemies.append(e_suicide)


def update():

    global game_state
    global game_state_old
    key_pressed = pygame.key.get_pressed()

    if game_state is PAUSED:
        if key_pressed[K_y]:
            game_state = MENU
        if key_pressed[K_n]:
            game_state = game_state_old
        return
    if game_state is MENU:
        if menu.update() is True:
            game_state_old = game_state
            game_state = PLAYING
        return

    if CAMERA.x >= LEVEL_END:
        game_state_old = game_state
        game_state = COMPLETED

    if key_pressed[K_ESCAPE]:
        game_state_old = game_state
        game_state = PAUSED

    if key_pressed[K_r]:
        game_state = PLAYING
        initialize()

    if key_pressed[K_e]:
        player.lives += 1

    if player.lives < 1:
        return

    if game_state is COMPLETED:
        return
    update_movement()

    collision()

    update_states()


def update_movement():

    if CAMERA.x < LEVEL_END:
        CAMERA.x += CAMERA_SPEED
    level.move(CAMERA)
    if player.move(Vector2(WINDOW_WIDTH, level.texture.get_rect().bottom)):
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(player.rect.center), Vector2(1, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        player.reset_charge()
        sounds_manager.player_blast.play()

    for enemy in enemies:
        if enemy.move(CAMERA):
            enemy_type = enemy.get_type()
            if enemy_type == FLYING_SOUCER:
                vec_dir = Vector2(-1, 0)
            elif enemy_type == WALKER or enemy_type == TURRET:
                vec_dir = enemy.get_dir(player.rect.center, CAMERA)

            bullet = EnemyBullet("Assets/bullet_small.png", 1,
                                 Vector2(enemy.rect.center)-CAMERA,
                                 vec_dir, 0)
            enemy_bullets.append(bullet)
            volume = sounds_manager.volume(player.get_onscr_pos(CAMERA),
                                           enemy.get_onscr_pos(CAMERA))
            blast_sound = pygame.mixer.Sound(sounds_manager.enemy_blast)
            blast_sound.set_volume(volume)
            blast_sound.play()

    for bullet in player_bullets:
        bullet.move()

    for bullet in enemy_bullets:
        bullet.move()

    particle_manager.update()


def update_states():
    update_bullets()
    update_enemies()


def update_bullets():
    dead_bullets = []
    dead_index = 0
    for bullet in player_bullets:
        if not bullet.active:
            dead_bullets.insert(0, dead_index)
        dead_index += 1
    for index in dead_bullets:
        player_bullets.pop(index)

    dead_bullets = []
    dead_index = 0
    for bullet in enemy_bullets:
        if not bullet.active:
            dead_bullets.insert(0, dead_index)
        dead_index += 1
    for index in dead_bullets:
        enemy_bullets.pop(index)


def update_enemies():
    dead_enemies = []
    dead_index = 0
    for enemy in enemies:
        if not enemy.active:
            dead_enemies.insert(0, dead_index)
        dead_index += 1
    for index in dead_enemies:
        enemies.pop(index)


def collision():
    player_mask = player.texture.get_collision_mask()
    colliding = collision_manager.map_collision(level,
                                                player.get_world_rect(CAMERA),
                                                player_mask)

    if colliding:
        if player.immortal is False:
            explosion = Explosion(EXP_TEXTURE, EXP_FRAMES,
                                  Vector2(player.get_onscr_pos(CAMERA)),
                                  Vector2(-1, 0), CAMERA_SPEED)
            particle_manager.add_particle(explosion)
        sounds_manager.player_explosion.play()
        player.kill(INIT_PLAYER_POS)
    for enemy in enemies:
        if not enemy.is_on_screen(CAMERA):
            continue
        colliding = collision_manager.are_colliding(player, enemy, CAMERA)
        if colliding:
            explosion = Explosion(EXP_TEXTURE, EXP_FRAMES,
                                  enemy.get_onscr_pos(CAMERA), Vector2(-1, 0),
                                  CAMERA_SPEED)
            particle_manager.add_particle(explosion)
            if player.immortal is False:
                explosion = Explosion(EXP_TEXTURE, EXP_FRAMES,
                                      Vector2(player.get_onscr_pos(CAMERA)),
                                      Vector2(-1, 0), CAMERA_SPEED)
                particle_manager.add_particle(explosion)
            player.add_score(enemy.get_points())
            enemy.kill()
            player.kill(INIT_PLAYER_POS)
            sounds_manager.player_explosion.play()
        for bullet in player_bullets:
            colliding = collision_manager.are_colliding(enemy, bullet, CAMERA)
            if colliding:
                explosion = Explosion(EXP_TEXTURE, EXP_FRAMES,
                                      enemy.get_onscr_pos(CAMERA),
                                      Vector2(-1, 0), CAMERA_SPEED)
                particle_manager.add_particle(explosion)
                if not bullet.is_max_power():
                    bullet.kill()
                enemy.kill()
                player.add_score(enemy.get_points())
                volume = sounds_manager.volume(player.get_onscr_pos(CAMERA),
                                               enemy.get_onscr_pos(CAMERA))
                sounds_manager.enemy_explosion.set_volume(volume)
                sounds_manager.enemy_explosion.play()

    for bullet in enemy_bullets:
        colliding = collision_manager.are_colliding(player, bullet, CAMERA)
        if colliding:
            if player.immortal is False:
                explosion = Explosion(EXP_TEXTURE, EXP_FRAMES,
                                      Vector2(player.get_onscr_pos(CAMERA)),
                                      Vector2(-1, 0), CAMERA_SPEED)
                particle_manager.add_particle(explosion)
            bullet.kill()
            player.kill(INIT_PLAYER_POS)


def draw():
    if game_state is MENU:
        menu.draw(DISPLAYSURF)
        return
    level.draw(DISPLAYSURF)
    info.draw(DISPLAYSURF, player.get_charge(), player.score, player.lives)
    particle_manager.draw(DISPLAYSURF)

    for bullet in player_bullets:
        bullet.draw(DISPLAYSURF)
    for bullet in enemy_bullets:
        bullet.draw(DISPLAYSURF)

    player.draw(DISPLAYSURF)

    for enemy in enemies:
        enemy.draw(DISPLAYSURF, CAMERA)

    if game_state is COMPLETED:
        font = pygame.font.SysFont(FONT, 100)
        completed = font.render("Level Completed", 1, (0, 0, 255))
        DISPLAYSURF.blit(completed, (250, 150))
        font = pygame.font.SysFont(FONT, 50)
        game_score = player.score + player.lives * 1000
        score = font.render("Your score is:  " + str(game_score), 1,
                            (0, 0, 255))

        DISPLAYSURF.blit(score, (400, 300))
        font.set_italic(True)
        restart = font.render("Press  R  to restart", 1, (0, 0, 255))
        DISPLAYSURF.blit(restart, (400, 370))

    if player.lives < 1:
        font = pygame.font.SysFont(FONT, 60)
        game_over = font.render("GAME OVER", 1, (255, 0, 0))
        DISPLAYSURF.blit(game_over, (500, 300))
        font = pygame.font.SysFont(FONT, 20)
        font.set_italic(True)
        restart = font.render("Press  R  to restart", 1, (255, 0, 0))
        DISPLAYSURF.blit(restart, (550, 370))

    if game_state is PAUSED:
        font = pygame.font.SysFont(FONT, 80)
        wanna_quit = font.render("Quit ?", 1, (0, 0, 255))
        DISPLAYSURF.blit(wanna_quit, (570, 230))
        font = pygame.font.SysFont(FONT, 60)
        quit_yn = font.render("Y / N", 1, (0, 0, 255))
        DISPLAYSURF.blit(quit_yn, (600, 300))

if __name__ == "__main__":
    main()
