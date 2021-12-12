from ursina import *

from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
ground = Entity(model='cube', collider='mesh', scale=(100, 1, 100))
ground.color = color.rgb(98, 125, 47)
Sky()



player = FirstPersonController()

entity1 = Entity(model='cube', collider='mesh', color=color.rgb(255, 255, 255), position= (5, 0.5, 5), scale=(5, 5, 5))
entity1.billboard = False

entity1_hit = None





player.jump_duration = 1
player.jump_height = 5
player.speed = 10

wp = WindowPanel(
    title='Custom Window',
    content=(
        Text('Name:'),
        InputField(name='name_field'),
        Button(text='Submit', color=color.azure),
        Slider(),
        Slider(),
        ),
        popup=True,
        enabled=False
    )

    



window.title = "Lo da Game"
#audio = Audio("audio/Lo")

#audio.play()
#audio.volume = 0.5
window.fullscreen = False

def input(key):
    if key == 'b':
        player.position = (0, 10, 0)
    if key == 'f':
        player.speed += 2
    if key == 'g':
        player.speed -= 2

def update():
    if player.speed <= 0:
        player.speed = 10



app.run()