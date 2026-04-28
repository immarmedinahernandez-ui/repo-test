import pygame

# Configuración básica
pygame.init()
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Mario Clone")

# Colores
BLANCO = (255, 255, 255)
AZUL_CIELO = (135, 206, 235)
ROJO = (255, 0, 0)
VERDE = (34, 139, 34)

# Variables del Jugador
jugador_ancho, jugador_alto = 40, 40
jugador_x, jugador_y = 50, ALTO - 100
vel_x = 5
vel_y = 0
gravedad = 0.8
salto_fuerza = -16
en_suelo = False

# Plataformas (x, y, ancho, alto)
plataformas = [
    pygame.Rect(0, ALTO - 50, ANCHO, 50),    # Suelo
    pygame.Rect(200, 450, 150, 30),          # Plataforma 1
    pygame.Rect(450, 350, 150, 30),          # Plataforma 2
    pygame.Rect(150, 250, 100, 30)           # Plataforma 3
]

reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    ventana.fill(AZUL_CIELO)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador_x -= vel_x
    if teclas[pygame.K_RIGHT]:
        jugador_x += vel_x
    if teclas[pygame.K_SPACE] and en_suelo:
        vel_y = salto_fuerza
        en_suelo = False

    # Aplicar Gravedad
    vel_y += gravedad
    jugador_y += vel_y

    # Crear Rectángulo del jugador para colisiones
    rect_jugador = pygame.Rect(jugador_x, jugador_y, jugador_ancho, jugador_alto)

    # Lógica de Colisiones
    en_suelo = False
    for plat in plataformas:
        pygame.draw.rect(ventana, VERDE, plat) # Dibujar plataformas
        
        if rect_jugador.colliderect(plat):
            # Si estamos cayendo y chocamos con la parte superior de la plataforma
            if vel_y > 0: 
                jugador_y = plat.top - jugador_alto
                vel_y = 0
                en_suelo = True

    # Dibujar Jugador
    pygame.draw.rect(ventana, ROJO, rect_jugador)

    # Límites de pantalla
    if jugador_x < 0: jugador_x = 0
    if jugador_x > ANCHO - jugador_ancho: jugador_x = ANCHO - jugador_ancho

    pygame.display.update()
    reloj.tick(60)

pygame.quit()
