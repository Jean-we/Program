import pygame

pygame.init()
pygame.display.set_caption('植物大战僵尸')
surface = pygame.display.set_mode((900,600))

#背景图片
bei_jing_photo = pygame.image.load(r'/Users/jeans/Desktop/pmjthon项目实战/植物pk僵尸/Image/Surface_photo/Surface.png')

#冒险模式图片k
Adventure_photo = pygame.image.load(r'/Users/jeans/Desktop/pmjthon项目实战/植物pk僵尸/Image/Level_mode/Adventure_mode.png')
new_adventure_photo = pygame.transform.scale(Adventure_photo,(251,150))

qu_mju = new_adventure_photo.get_rect(topleft=(251,150) )





while True:

    #事件捕捉
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    surface.blit(bei_jing_photo,(0,0))
    surface.blit(new_adventure_photo,(500,60))




    pygame.display.flip()














