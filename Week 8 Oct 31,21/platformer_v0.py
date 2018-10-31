import pyglet

window = pyglet.window.Window(width=400, height=400, caption="game")

image = pyglet.resource.image('kitten.png')

x = 0
y = 0

pressed_keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(pressed_keys)

@window.event
def on_draw():
	window.clear()

	image.blit(x, y)

speed = 400

valcoity = 100

def update(dt,ex_dt):
	global x
	global y

	if pressed_keys[pyglet.window.key.A]:
		x -= int(speed * dt)
	if pressed_keys[pyglet.window.key.D]:
		x += int(speed * dt)

pyglet.clock.schedule(update, 1/60.0)
pyglet.app.run()