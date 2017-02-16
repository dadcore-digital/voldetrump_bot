from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont

TWEET_FILE = 'to-tweet.txt'
TWEET_ARCHIVE = 'tweet-archive.txt'

FONT_NAME = 'fonts/crimsontext.ttf'
FONT_SIZE = 15
FONT_COLOR = (0, 0, 0)
LINE_SPACING = 16
FILENAME = 'tweetme.png'


def get_tweet_text(tweet_file=TWEET_FILE, tweet_archive=TWEET_ARCHIVE):
    """Retrieve a passage to tweet and move to archive of tweets."""
    text = open(tweet_file).readlines()[0]

    # Read top tweet on deck
    with open(TWEET_FILE, 'r') as fin:
        data = fin.readlines()
        text = data[0]

    # Now delete that tweet
    with open(TWEET_FILE, 'w') as fout:
        fout.writelines(data[1:])

    # Archive gif record
    with open(TWEET_ARCHIVE, 'a') as fout:
        fout.writelines(text)

    return text


def gen_image(text, x=20, y=20, wrap_col=72, font_name=FONT_NAME,
              font_size=FONT_SIZE, font_color=FONT_COLOR,
              line_spacing=LINE_SPACING, filename=FILENAME):
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
    filename -- Name of file to save resulting image to

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
    img.save('tweetme.png')
    return filename
