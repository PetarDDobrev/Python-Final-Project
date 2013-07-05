import unittest
import pygame
import sounds
from animated_texture import*
from collision import*


pygame.init()


class SoundTest(unittest.TestCase):
    def setUp(self):
        self.sounds_manager = sounds.SoundManager()

    def test_volume_distance_one(self):
        volume = self.sounds_manager.volume(Vector2(2000, 0), Vector2(0, 0))
        self.assertEqual(volume, 0)

    def test_volume_distance_two(self):
        volume = self.sounds_manager.volume(Vector2(2000, 0), Vector2(1000, 0))
        self.assertEqual(volume, 0.5)

    def test_volume_distance_three(self):
        volume = self.sounds_manager.volume(Vector2(2000, 0), Vector2(1500, 0))
        self.assertEqual(volume, 0.75)

    def test_volume_distance_four(self):
        volume = self.sounds_manager.volume(Vector2(2000, 0), Vector2(1900, 0))
        self.assertEqual(volume, 0.95)

    def test_volume_distance_five(self):
        volume = self.sounds_manager.volume(Vector2(2000, 0), Vector2(2000, 0))
        self.assertEqual(volume, 1)


class AnimationTest(unittest.TestCase):
    def setUp(self):
        self.anim = AnimatedTexture("Assets/expl_fire_1.png", 6, 5)
        self.surface = surf_map = Surface((200, 1000), pygame.SRCALPHA)

    def test_animation_pause_one(self):
        self.anim.paused = True
        for n in range(20):
            self.anim.draw(self.surface, Vector2(0, 0))
            self.assertEqual(self.anim.frame, 0)

    def test_animation_pause_two(self):
        self.anim.paused = False
        for n in range(self.anim.speed):
            self.anim.draw(self.surface, Vector2(0, 0))
        self.assertEqual(self.anim.frame, 1)

    def test_animation_one(self):
        self.anim.paused = False
        self.anim.frame = 0
        anim_loops_number = 5
        for n in range(anim_loops_number):
            for i in range(self.anim.max_frame):
                self.assertEqual(self.anim.frame, i)
                for y in range(self.anim.speed):
                    self.anim.draw(self.surface, Vector2(0, 0))
            self.anim.draw(self.surface, Vector2(0, 0))

    def test_animation_two(self):
        self.anim = AnimatedTexture("Assets/enemy_flying_1.png", 8, 12)
        self.anim.paused = False
        self.anim.frame = 0
        anim_loops_number = 3
        for n in range(anim_loops_number):
            for i in range(self.anim.max_frame):
                self.assertEqual(self.anim.frame, i)
                for y in range(self.anim.speed):
                    self.anim.draw(self.surface, Vector2(0, 0))
            self.anim.draw(self.surface, Vector2(0, 0))


CAMERA = Vector2(0, 0)
collision_manager = CollisionManager()
level = Map("Assets/level1.png", "Assets/level1_collision2.png")
player = Player(Vector2(100, 100), "Assets/player.png")
player_bullets = []
enemy_bullets = []
enemies = []


class CollisionTest(unittest.TestCase):
    def empy_object_containers(self):
        del player_bullets[0:len(player_bullets)]
        del enemy_bullets[0:len(enemy_bullets)]
        del enemies[0:len(enemies)]

    def setUp(self):
        CAMERA.x -= CAMERA.x

        level.move(CAMERA)
        player.initialize(Vector2(100, 68))
        self.empy_object_containers()

        #ENEMIES
        #flying soucer
        fs_texture = "Assets/enemy_flying_1.png"
        e_fs_1 = FlyingSoucer(Vector2(100, 84), Vector2(0, 1), 4,
                              fs_texture, 8, 5)
        enemies.append(e_fs_1)

        #walker
        w_text = "Assets/walker_1.png"
        e_walker_1 = Walker(Vector2(100, 96), Vector2(0, 1), 4,
                            w_text, 3, 6)
        enemies.append(e_walker_1)

        #turret
        turret_text = "Assets/turret_bot.png"
        e_turret_1 = Turret(Vector2(100, 94), Vector2(0, 1), 4,
                            turret_text, 6, 10)
        enemies.append(e_turret_1)

        #suicide
        s_text = "Assets/suicide.png"
        e_suicide_1 = Suicide(Vector2(2500, 300), Vector2(0, 0), 5,
                              s_text, 6, 15)
        enemies.append(e_suicide_1)

    def test_map_player_collsion_one(self):
        player_mask = player.texture.get_collision_mask()
        player.position = Vector2(300, 450)
        player_rect = player.get_world_rect(CAMERA)
        colliding = collision_manager.map_collision(level,
                                                    player_rect,
                                                    player_mask)
        self.assertTrue(colliding)

    def test_map_player_collsion_two(self):
        player_mask = player.texture.get_collision_mask()
        player.position = Vector2(4000, 100)
        player_rect = player.get_world_rect(CAMERA)
        colliding = collision_manager.map_collision(level,
                                                    player_rect,
                                                    player_mask)
        self.assertTrue(colliding)

    def test_map_player_collsion_three(self):
        player_mask = player.texture.get_collision_mask()
        player.position = Vector2(9666, 366)
        player_rect = player.get_world_rect(CAMERA)
        colliding = collision_manager.map_collision(level,
                                                    player_rect,
                                                    player_mask)
        self.assertTrue(colliding)

    def test_map_player_collsion_four(self):
        player_mask = player.texture.get_collision_mask()
        player.position = Vector2(1000, 150)
        player_rect = player.get_world_rect(CAMERA)
        colliding = collision_manager.map_collision(level,
                                                    player_rect,
                                                    player_mask)
        self.assertFalse(colliding)

    def test_map_player_collsion_five(self):
        player_mask = player.texture.get_collision_mask()
        player.position = Vector2(6300, 10)
        player_rect = player.get_world_rect(CAMERA)
        colliding = collision_manager.map_collision(level,
                                                    player_rect,
                                                    player_mask)
        self.assertFalse(colliding)

    def test_map_player_collsion_six(self):
        player_mask = player.texture.get_collision_mask()
        player.position = Vector2(12000, 500)
        player_rect = player.get_world_rect(CAMERA)
        colliding = collision_manager.map_collision(level,
                                                    player_rect,
                                                    player_mask)
        self.assertFalse(colliding)

    def test_ppp_collision_one(self):
        for enemy in enemies:
            if enemy.get_type() == FLYING_SOUCER:
                enemy.texture.frame = 0
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertTrue(collide)

                enemy.texture.frame = 1
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

                enemy.texture.frame = 2
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

                enemy.texture.frame = 3
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

                enemy.texture.frame = 4
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertTrue(collide)

                enemy.texture.frame = 5
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

                enemy.texture.frame = 6
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

                enemy.texture.frame = 7
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

    def test_ppp_collision_two(self):
        for enemy in enemies:
            if enemy.get_type() == WALKER:
                enemy.texture.frame = 0
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

                enemy.texture.frame = 1
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

                enemy.texture.frame = 2
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertTrue(collide)

    def test_ppp_collision_three(self):
        for enemy in enemies:
            if enemy.get_type() == TURRET:
                enemy.texture.frame = 0
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

                enemy.texture.frame = 1
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

                enemy.texture.frame = 2
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertTrue(collide)

                enemy.texture.frame = 3
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertTrue(collide)

                enemy.texture.frame = 4
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)

                enemy.texture.frame = 5
                enemy.texture.set_surf_rect()
                collide = collision_manager.are_colliding(player, enemy,
                                                          CAMERA)
                self.assertFalse(collide)


class ProjectileTest(unittest.TestCase):
    def setUp(self):
        del player_bullets[0:len(player_bullets)]
        del enemy_bullets[0:len(enemy_bullets)]

    def test_player_bullets_one(self):
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1300, 50), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1300, 150), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1300, 250), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1300, 350), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1300, 450), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1300, 550), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)

        for bullet in player_bullets:
            bullet.move()
            self.assertTrue(bullet.active)

    def test_player_bullets_two(self):
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1401, 50), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1401, 150), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1401, 250), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1401, 350), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1401, 450), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)
        bullet = PlayerBullet("Assets/basic_gun_bullets.png", 4,
                              Vector2(1401, 550), Vector2(0, 0),
                              player.weapon_power)
        player_bullets.append(bullet)

        for bullet in player_bullets:
            bullet.move()
            self.assertFalse(bullet.active)

    def test_enemy_bullets_one(self):
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1300, 50), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1300, 150), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1300, 250), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1300, 350), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1300, 450), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1300, 550), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)

        for bullet in enemy_bullets:
            bullet.move()
            self.assertTrue(bullet.active)

    def test_enemy_bullets_two(self):
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1401, 50), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1401, 150), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1401, 250), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1401, 350), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1401, 450), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(1401, 550), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)

        for bullet in enemy_bullets:
            bullet.move()
            self.assertFalse(bullet.active)

    def test_enemy_bullets_three(self):
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-20, 50), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-20, 150), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-20, 250), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-20, 350), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-20, 450), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-20, 550), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)

        for bullet in enemy_bullets:
            bullet.move()
            self.assertTrue(bullet.active)

    def test_enemy_bullets_four(self):
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-101, 50), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-101, 150), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-101, 250), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-101, 350), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-101, 450), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)
        bullet = EnemyBullet("Assets/basic_gun_bullets.png", 4,
                             Vector2(-101, 550), Vector2(0, 0),
                             player.weapon_power)
        enemy_bullets.append(bullet)

        for bullet in enemy_bullets:
            bullet.move()
            self.assertFalse(bullet.active)


class EnemyTest(unittest.TestCase):
    def setUp(self):
        CAMERA.x -= CAMERA.x

        del enemies[0:len(enemies)]

        #ENEMIES
        #flying soucer
        fs_texture = "Assets/enemy_flying_1.png"
        e_fs_1 = FlyingSoucer(Vector2(100, 84), Vector2(0, 1), 4,
                              fs_texture, 8, 5)
        enemies.append(e_fs_1)

        #walker
        w_text = "Assets/walker_1.png"
        e_walker_1 = Walker(Vector2(100, 96), Vector2(0, 1), 4,
                            w_text, 3, 6)
        enemies.append(e_walker_1)

        #turret
        turret_text = "Assets/turret_bot.png"
        e_turret_1 = Turret(Vector2(100, 94), Vector2(0, 1), 4,
                            turret_text, 6, 10)
        enemies.append(e_turret_1)

        #suicide
        s_text = "Assets/suicide.png"
        e_suicide_1 = Suicide(Vector2(2500, 300), Vector2(0, 0), 5,
                              s_text, 6, 15)
        enemies.append(e_suicide_1)

    def test_onscr_pos_one(self):
        for enemy in enemies:
            enemy.position = Vector2(1280, 100)
            self.assertFalse(enemy.is_on_screen(CAMERA))

    def test_onscr_pos_two(self):
        for enemy in enemies:
            enemy.position = Vector2(1279, 100)
            self.assertTrue(enemy.is_on_screen(CAMERA))

    def test_onscr_pos_three(self):
        for enemy in enemies:
            enemy.position = Vector2(-100, 100)
            self.assertFalse(enemy.is_on_screen(CAMERA))

    def test_onscr_pos_four(self):
        for enemy in enemies:
            enemy.position = Vector2(-99, 100)
            self.assertTrue(enemy.is_on_screen(CAMERA))

    def test_flying_soucer(self):
        top_border_crossed = False
        bot_border_crossed = False
        for i in range(1000):
            enemies[0].move(CAMERA)
            if enemies[0].position.y < FS_TOP_BORDER:
                top_border_crossed = True
            if enemies[0].position.y > FS_BOTTOM_BORDER:
                bot_border_crossed = True
        self.assertFalse(top_border_crossed)
        self.assertFalse(bot_border_crossed)

    def test_walker(self):
        enemies[1].position = Vector2(100, 100)
        enemy_center = Vector2(enemies[1].rect.center) - enemies[1].position

        direction = enemies[1].get_dir(Vector2(0, 100) + enemy_center, CAMERA)
        self.assertEqual(Vector2(-1, 0), direction)

        direction = enemies[1].get_dir(Vector2(200, 100) + enemy_center,
                                       CAMERA)
        self.assertEqual(Vector2(1, 0), direction)

        direction = enemies[1].get_dir(Vector2(100, 0) + enemy_center,
                                       CAMERA)
        self.assertEqual(Vector2(0, -1), direction)

        direction = enemies[1].get_dir(Vector2(100, 200) + enemy_center,
                                       CAMERA)
        self.assertEqual(Vector2(0, 1), direction)

    def test_turret(self):
        enemies[2].position = Vector2(100, 100)
        enemy_center = Vector2(enemies[2].rect.center) - enemies[2].position

        direction = enemies[2].get_dir(Vector2(0, 100) + enemy_center, CAMERA)
        self.assertEqual(Vector2(-1, 0), direction)

        direction = enemies[2].get_dir(Vector2(200, 100) + enemy_center,
                                       CAMERA)
        self.assertEqual(Vector2(1, 0), direction)

        direction = enemies[2].get_dir(Vector2(100, 0) + enemy_center, CAMERA)
        self.assertEqual(Vector2(0, -1), direction)

        direction = enemies[2].get_dir(Vector2(100, 200) + enemy_center,
                                       CAMERA)
        self.assertEqual(Vector2(0, 1), direction)

    def test_suicide(self):
        top_border_crossed = False
        bot_border_crossed = False
        for i in range(10000):
            enemies[0].move(CAMERA)
            if enemies[0].position.y < S_TOP_BORDER:
                top_border_crossed = True
            if enemies[0].position.y > S_BOTTOM_BORDER:
                bot_border_crossed = True
        self.assertFalse(top_border_crossed)
        self.assertFalse(bot_border_crossed)


if __name__ == '__main__':
    unittest.main()
  
