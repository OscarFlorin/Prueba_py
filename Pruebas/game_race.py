import turtle
import random

s = turtle.Screen()
s.title("Primer Juego")
s.bgcolor("gray")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("blue", "blue")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("green", "green")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

jugador1.penup()
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-250,225)
jugador1.showturtle()

jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)


jugador2.penup()
jugador2.goto(-250,-170)
jugador2.showturtle()

dado = [1,2,4,5,6]

for i in range(20):
    if jugador1.pos() >= (200,200):
        print("Jugador 1 ha GANADO!")
        break
    elif jugador2.pos() >= (200,-200):
        print("Jugador 2 ha GANADO!")
        break
    else:
        turno1 = input("Presiono la tecla enter para avanzar la tortuga azul.")
        turno1 = random.choice(dado)
        print("Tu numero es: ",turno1,"\nAvanzas: ", turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 = input("Presiono la tecla enter para avanzar la tortuga verde.")
        turno2 = random.choice(dado)
        print("Tu numero es: ",turno2,"\nAvanzas: ", turno2*20)
        jugador2.pendown()
        jugador2.forward(20*turno2)

turtle.done()