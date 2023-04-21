import sys, pygame
from sevenlives.entity.squirrel import Squirrel
from sevenlives.component.location import Location
from sevenlives.component.render import Render

pygame.init()
surface = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Test window")

# Votre initialization de vos objets
ent=Squirrel()
ent.add_component(Location(pygame.Vector2(20,20)))
ent.add_component(Render())

while True:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            pygame.quit()
            sys.exit()
    
    # Vos fonctions/méthodes à appeller à chaque frame
    ent.update_component(1)
    if ent.has_component(Render):
        ent.give_component(Render).draw(surface)
    
    pygame.display.update()