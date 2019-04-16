import turtle

tortuguita=turtle.Turtle()
##funciones de 1er nivel capaces de invocarces a si
##misma y crear compias de asi misma
otratortuguita=turtle.Turtle()

lentorra=turtle.Turtle()

lentorra.speed(1)

tortuguita.shape('turtle')
tortuguita.color('blue')
tortuguita.fd(50)
tortuguita.speed(5)

otratortuguita.color('green')
otratortuguita.left(90)
otratortuguita.fd(50)
otratortuguita.speed(5)