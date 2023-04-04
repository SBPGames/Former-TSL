class Component:
    
    def is_pushed(): #Florian ?
        #return True or False
        pass
        
    def detecter_collision(objet1,objet2,parametres):
        p1 = objet1.position
        p2 = objet2.position
        dx = p2[0]-p1[0]
        dy = p2[1]-p1[1]
        dz = p2[2]-p1[2]
        d = sqrt(dx*dx+dy*dy+dz*dz)
        if d>objet1.rayon+objet2.rayon:
            return -1
        return 0
            
        o1.rayon = 0.5
        o2.rayon = 0.5
        o3.rayon = 0.5
        result = pavage.chercher_collisions(detecter_collision,[])
        print(result)
        pavage.deplacer_objet(0,[5.5,5.2,0.5])
        pavage.deplacer_objet(1,[5.5,5.2,0.5])
        pavage.deplacer_objet(2,[5.3,5.6,0.2])
        result = pavage.chercher_collisions(detecter_collision,[])
        print(result)
     
        
    def deplacement(self, elements):
        x="?"
        y="?"
        z="?"
       bouton="?"
       if bouton1.is_pushed():
           is_puched.collision
           x=+50
       if bouton2.is_pushed():
            is_puched.collision
           x=-50
    elif bouton3.is_pushed():
         is_puched.collision
        y=+50
          
           
        
        
        
        
        
        
        
#vitesse du personnage, retient la localisation, mouvement doux fluide
        