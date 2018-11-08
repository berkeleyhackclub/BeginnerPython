import pyglet

window = pyglet.window.Window(width=400, height=400, caption="game")

image = pyglet.resource.image('kitten.png')
player = pyglet.sprite.Sprite(image)
player.scale = .5
player.x = 0
player.y = 0

pressed_keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(pressed_keys)

@window.event
def on_draw():
	window.clear()

	player.draw()

gravity = 98
ground = 0

player.speed = 400
player.jump = 200
player.velocity = 0
player.grounded = True

def update(dt,ex_dt):
	if pressed_keys[pyglet.window.key.A]:
		player.x -= int(player.speed * dt)
	if pressed_keys[pyglet.window.key.D]:
		player.x += int(player.speed * dt)

	if pressed_keys[pyglet.window.key.W] and player.grounded:
		player.velocity += player.jump
		player.grounded = False

	player.y += player.velocity * dt

	if player.y < ground:
		player.y = ground
		player.velocity = 0
		player.grounded = True
	else:
		player.velocity -= gravity * dt

pyglet.clock.schedule(update, 1/60.0)
pyglet.app.run()