import pyglet
window = pyglet.window.Window()

image = pyglet.resource.image("resources/character.png")
sprite = pyglet.sprite.Sprite(image)
sprite.x = 100
sprite.y = 100

@window.event
def on_draw():
    window.clear()
    sprite.draw()

pressed_keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(pressed_keys)

speed = 400
velY = 0
jump = 500
grounded = True
G = 500
def update(dt,ex_dt):
    global velY
    global grounded

    if pressed_keys[pyglet.window.key.A]:
        sprite.x -= int(speed * dt)
    if pressed_keys[pyglet.window.key.D]:
        sprite.x += int(speed * dt)
    if pressed_keys[pyglet.window.key.W] and grounded:
        velY = jump
        grounded = False

    sprite.y += velY * dt
    if sprite.y <= 100:
        velY = 0
        grounded = True
    else:
        velY -= G * dt

pyglet.clock.schedule(update, 1/60.0)
pyglet.app.run()
