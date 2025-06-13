import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jumping Robot!")

# 🧠 Robot image load করা হচ্ছে
robot_img = pygame.image.load("robot.png")  # ছবির নাম ও একই ফোল্ডারে থাকতে হবে
robot_img = pygame.transform.scale(robot_img, (50, 50))  # ছবির সাইজ ছোট করছি

# 📦 Robot এর পজিশন জানাতে rect বানানো হচ্ছে
robot_rect = robot_img.get_rect()
robot_rect.topleft = (200, 200)  # Initial position

speed = 5
jump = False
jumpC = 10

while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    
    # ⬅️ ➡️ ⬆️ ⬇️ movement
    if keys[pygame.K_LEFT] and robot_rect.x > 0:
        robot_rect.x -= speed
    if keys[pygame.K_RIGHT] and robot_rect.x < 500 - robot_rect.width:
        robot_rect.x += speed
    if keys[pygame.K_UP] and robot_rect.y > 0:
        robot_rect.y -= speed
    if keys[pygame.K_DOWN] and robot_rect.y < 500 - robot_rect.height:
        robot_rect.y += speed

    # 🪂 Jump logic
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jumpC >= -10:
            robot_rect.y -= (jumpC * abs(jumpC)) * 0.5
            jumpC -= 1
        else:
            jump = False
            jumpC = 10

    # 🎨 Drawing everything
    screen.fill((130, 222, 134))  # background
    screen.blit(robot_img, robot_rect)  # robot draw
    pygame.display.update()
