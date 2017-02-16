import uuid
from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont

TWEET_FILE = 'to-tweet.txt'
TWEET_ARCHIVE = 'tweet-archive.txt'

FONT_NAME = 'fonts/crimsontext.ttf'
FONT_SIZE = 15
FONT_COLOR = (0, 0, 0)
LINE_SPACING = 16
IMG_DIR = 'images'


def get_tweet(img_dir=IMG_DIR):
    """Get top tweet and move to archive list."""
    # Read top tweet on deck
    with open(TWEET_FILE, 'r') as fin:
        data = fin.readlines()
        img_file = data[0]

    # Now delete that tweet
    with open(TWEET_FILE, 'w') as fout:
        fout.writelines(data[1:])

    # Archive gif record
    with open(TWEET_ARCHIVE, 'a') as fout:
        fout.writelines(img_file)

    img_file = img_file.replace('\n', '')
    return '%s/%s' % (img_dir, img_file)


def gen_image(text, x=20, y=20, wrap_col=72, font_name=FONT_NAME,
              font_size=FONT_SIZE, font_color=FONT_COLOR,
              line_spacing=LINE_SPACING, img_dir=IMG_DIR):
    """Create tweet image from supplied text, Returns file name.

    Arguments:
    text -- Passage of text to create image from (string)

    Keyword arguments:
    x -- Left margin spacing (int)
    y -- Top margin spacing (int)
    wrap_col -- Width text should be
    font_name -- Name of font to use for rendering (str)
    font_size -- Size of font (int)
    font_color --- Specified as 0-255 3 char tuple
    filename -- Directory to output image to.

    """
    # Wrap text to fit image, not an exact science.
    text = wrap(text, wrap_col)

    # Load up background image as base to write to
    font = ImageFont.truetype(FONT_NAME, FONT_SIZE)
    img = Image.open("bg.png").convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Write out each line
    for line in text:
        draw.text((25, y), line, font=font, fill=font_color)
        y += line_spacing

    # Crop bottom of image and save
    img = img.crop((0, 0, img.width, y + 20))

    # Save file
    filename = uuid.uuid4().get_hex()
    img.save('%s/%s.png' % (img_dir, filename))

    return filename


def gen_all_images():
    """Reference function, loop through all tweets and gen images."""
    tweets = open('to-tweet.txt').readlines()

    for tweet in tweets:
        gen_image(tweet)
