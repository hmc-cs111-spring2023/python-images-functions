from PIL import Image

################################################################################
# Flipping
################################################################################


def flipHorizontal(input_filename, output_filename):
    '''Flip an image horizontally'''
    image = load_image(input_filename)
    width, height = image.size
    result = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            result.putpixel((width - x - 1, y), pixel)

    save_image(result, output_filename)


def flipVertical(input_filename, output_filename):
    '''Flip an image vertically'''
    image = load_image(input_filename)
    width, height = image.size
    result = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            result.putpixel((x, height - y - 1), pixel)

    save_image(result, output_filename)

################################################################################
# Rotating
################################################################################


def rotateLeft(input_filename, output_filename):
    '''Rotate an image 90 degrees counter-clockwise'''
    image = load_image(input_filename)
    width, height = image.size
    result = Image.new('RGB', (height, width))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            result.putpixel((y, width - x - 1), pixel)

    save_image(result, output_filename)


def rotateRight(input_filename, output_filename):
    '''Rotate an image 90 degrees clockwise'''
    image = load_image(input_filename)
    width, height = image.size
    result = Image.new('RGB', (height, width))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            result.putpixel((height - y - 1, x), pixel)

    save_image(result, output_filename)

################################################################################
# Grayscale
################################################################################


def grayscale(input_filename, output_filename):
    '''Convert an image to grayscale'''
    image = load_image(input_filename)
    width, height = image.size
    result = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            (r, g, b) = image.getpixel((x, y))
            gray = int((r + g + b) / 3)
            result.putpixel((x, y), (gray, gray, gray))

    save_image(result, output_filename)

################################################################################
# Loading and saving
################################################################################


def load_image(path):
    '''Load an image from file'''
    return Image.open(path)


def save_image(image, path):
    '''Save an image to file'''
    image.save(path)
