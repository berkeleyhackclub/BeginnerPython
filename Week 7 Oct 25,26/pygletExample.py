import pyglet

window = pyglet.window.Window(width=400, height=400)

x = 100
y = 100
width = 100
height = 100

red = 1
green = 0
blue = 1

color = (red, green, blue) * 4

@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
    	('v2i', (x,y , x+width,y , x+width,y+height , x,y+height)),
    	('c3f', color)
    )

pyglet.app.run()

##########################################################
# to add movement move rest of code above pyglet.app.run #
##########################################################

pressed_keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(pressed_keys)

speed = 400
def update(dt,ex_dt):
	global x
	global y

	if pressed_keys[pyglet.window.key.W]: # IF W is pressed
		y += int(speed * dt) # Increase y position
	if pressed_keys[pyglet.window.key.S]:
		y -= int(speed * dt) # Decrease y position
	if pressed_keys[pyglet.window.key.A]:
		x -= int(speed * dt) # Decrease x position
	if pressed_keys[pyglet.window.key.D]:
		x += int(speed * dt) # Increase x position

pyglet.clock.schedule(update, 1/60.0)
