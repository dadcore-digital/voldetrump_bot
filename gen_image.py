from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont

TWEET_TEXT = 'tweet-text.txt'
TEXT_LIMIT = 420
NEXT_TWEET_FILE = 'next-tweet.txt'
FONT_NAME = 'fonts/crimsontext.ttf'
FONT_SIZE = 15
FONT_COLOR = (0, 0, 0)
LINE_SPACING = 16
IMG_DIR = 'images'


def get_tweet(next_tweet_file=NEXT_TWEET_FILE, tweet_text=TWEET_TEXT,
              text_limit=TEXT_LIMIT, img_dir=IMG_DIR):
    """
    Return image and text for next tweet.

    Opens next_tweet_file which contains a counter pointing to the line
    number of the next tweet.

    This line number should point to the same entry in tweet_text and
    a corresponding image file such as `502.png`

    After returning these two values, increment the value in next_tweet_file
    by 1.

    Keyword arguments:
    next_tweet_file -- File keeps track of what number tweet to post next
    tweet_text -- Text of tweet, used for alt text
    text_limit -- Character length limit imposed by twitter API
    img_dir -- Sub directory images are located in

    """
    tweet_num = int(open(next_tweet_file).readlines()[0])
    img = '%s/%s.png' % (img_dir, tweet_num)
    text = open(tweet_text).readlines()[tweet_num][:text_limit]

    tweet_num += 1
    f = open(next_tweet_file, 'w')
    f.write(str(tweet_num))
    f.close()

    return img, text


def gen_image(text, filename, x=20, y=20, wrap_col=72, font_name=FONT_NAME,
              font_size=FONT_SIZE, font_color=FONT_COLOR,
              line_spacing=LINE_SPACING, img_dir=IMG_DIR):
    """Create tweet image from supplied text, Returns file name.

    Arguments:
    text -- Passage of text to create image from (string)
    filename -- Where to output saved file (string)

    Keyword arguments:
    x -- Left margin spacing (int)
    y -- Top margin spacing (int)
    wrap_col -- Width text should be (int)
    font_name -- Name of font to use for rendering (string)
    font_size -- Size of font (int)
    font_color --- Specified as 0-255 3 char tuple (tuple)

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
    img.save('%s/%s.png' % (img_dir, filename))

    return filename


def gen_all_images(tweet_corpus=TWEET_TEXT):
    """Reference function, loop through all tweets and gen images."""
    tweets = open(tweet_corpus).readlines()

    for num, tweet in enumerate(tweets):
        gen_image(tweet, num)
