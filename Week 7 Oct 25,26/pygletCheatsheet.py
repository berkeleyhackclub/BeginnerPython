# THIS IS A RESOURCE FOR PYGLET
# Make sure you have python3 installed on your computer
# _______________________________________________________

# HOW TO: Import the pyglet module. Make sure you run 'pip install'
import pyglet

# HOW TO: Create a new pyglet window. Set the width, height, and caption properties.
window = pyglet.window.Window(width=400, height=400, caption="game")

# HOW TO: Create some x,y,width, and height variables (used later)
x = 100
y = 100
width = 100
height = 100

# HOW TO: Draw an image. Make sure you have an image in your project folder.
image = pyglet.resource.image('kitten.png')
sprite = pyglet.sprite.Sprite(image)
sprite.x = x
sprite.y = y

# HOW TO: Draw multiple objects to the screen and order them.
batch = pyglet.graphics.Batch() # Creates a batch (easier for rendering)
background = pyglet.graphics.OrderedGroup(0) # Creates orderedGroups that define what goes on top
foreground = pyglet.graphics.OrderedGroup(1)

pyglet.sprite.Sprite(image, batch=batch, group=background)
vertex_list = batch.add(2, pyglet.gl.GL_POINTS, foreground,
    ('v2i', (10, 15, 30, 35)),
    ('c3B', (0, 0, 255) * 2)
)

# HOW TO: Draw text
label = pyglet.text.Label('Hello, world',
	font_name='Times New Roman', font_size=36,
	x=window.width//2, y=window.height//2,
	anchor_x='center', anchor_y='center'
)

# HOW TO: Import font file and draw text
pyglet.font.add_file('font.ttf')
font = pyglet.font.load('font')
pyglet.text.Label('Hello, world', font_name="font", batch=batch, group=foreground)

# HOW TO: Create a color with rgba values
red = .5
green = .2
blue = 1
alpha = 1

color = (red, green, blue, alpha) * 4 # Makes new color (can be used later)

# HOW TO: Make a draw function and update screen
pressed_keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(pressed_keys)

@window.event
def on_draw():
    window.clear() # Clears window of graphics (in order to update again)
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, # Draws rectangle
    	('v2i', (x,y , x+width,y , x+width,y+height , x,y+height)),
    	('c4f', color)
    )
    sprite.draw() # Draws sprite defined above
    label.draw() # Draws label defined above
    batch.draw() # Draws batch defined above
    image.blit(x, y) # Draws image at x and y coordinates

speed = 400 # Declare movement speed
def update(dt,ex_dt):
	global x # make two global x and y coords
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
pyglet.app.run()

# HOW TO: Mouse events:
def on_mouse_motion(x, y, dx, dy):
	pass

def on_mouse_press(x, y, button, modifiers):
	pass

def on_mouse_release(x, y, button, modifiers):
	pass

def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
	pass

#EX: button = pyglet.window.mouse.LEFT / RIGHT / MIDDLE
