import pyglet

window = pyglet.window.Window(width=400, height=400, caption="game")

x = 100
y = 100
width = 100
height = 100

image = pyglet.resource.image('kitten.png')
sprite = pyglet.sprite.Sprite(image)
sprite.x = x
sprite.y = y

batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

pyglet.sprite.Sprite(image, batch=batch, group=background)
vertex_list = batch.add(2, pyglet.gl.GL_POINTS, foreground,
    ('v2i', (10, 15, 30, 35)),
    ('c3B', (0, 0, 255) * 2)
)

label = pyglet.text.Label('Hello, world',
	font_name='Times New Roman', font_size=36,
	x=window.width//2, y=window.height//2,
	anchor_x='center', anchor_y='center'
)

pyglet.font.add_file('font.ttf')
font = pyglet.font.load('font')
pyglet.text.Label('Hello, world', font_name="font", batch=batch, group=foreground)

red = .5
green = .2
blue = 1
alpha = 1

color = (red, green, blue, alpha) * 4

pressed_keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(pressed_keys)

@window.event
def on_draw():
	window.clear()

	pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
		 ('v2i', (x,y , x+width,y , x+width,y+height , x,y+height)),
		 ('c4f', color)
	)

	sprite.draw()
	label.draw()
	batch.draw()

	image.blit(x, y)

speed = 400

def update(dt,ex_dt):
	global x
	global y

	if pressed_keys[pyglet.window.key.W]:
		y += int(speed * dt)
	if pressed_keys[pyglet.window.key.S]:
		y -= int(speed * dt)
	if pressed_keys[pyglet.window.key.A]:
		x -= int(speed * dt)
	if pressed_keys[pyglet.window.key.D]:
		x += int(speed * dt)

pyglet.clock.schedule(update, 1/60.0)
pyglet.app.run()

'''

mouse events:
	def on_mouse_motion(x, y, dx, dy):
	def on_mouse_press(x, y, button, modifiers):
	def on_mouse_release(x, y, button, modifiers):
	def on_mouse_drag(x, y, dx, dy, buttons, modifiers):

EX: button = pyglet.window.mouse.LEFT / RIGHT / MIDDLE

'''
