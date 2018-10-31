import pyglet # import pyglet

window = pyglet.window.Window(width=400, height=400, caption="game") # make a new window

image = pyglet.resource.image('resources/character.png') # load an image (in resources)
image_x = 0  # define x position
image_y = 0  # define y position

pressed_keys = pyglet.window.key.KeyStateHandler() # make a new handler for key events
window.push_handlers(pressed_keys) # pass handler to the window

@window.event
def on_draw():
	window.clear()
	image.blit(image_x, image_y)

speed = 400
def update(dt,ex_dt):
	global image_x # Defines the global variable image_x previously defined above

	if pressed_keys[pyglet.window.key.A]: # Use handler, 'A' key
		image_x -= int(speed * dt)
	if pressed_keys[pyglet.window.key.D]: # Use handler, 'D' key
		image_x += int(speed * dt)

pyglet.clock.schedule(update, 1/60.0) # updates the function 60 times a second
pyglet.app.run() # ALWAYS: runs the code above
