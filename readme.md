# s/Voldemort/Donald Trump Bot

[http://twitter.com/s_volde_trump](@s_volde_trump)

Pretty simple bot that replaces all instances of *Voldemort* with **Donald Trump**, and all instances of *Harry Potter* with **Justin Trudeau**.

## Method

### Text Generation

I like to cheat with text generation and pre-generate everything ahead of time. This way there's as few moving pieces to break as possible.

I downloaded all Harry Potter book raw text from archive.org. Did a few find and replaces in Sublime Text, and then used the following crazy regex to find all paragraphs that only had Donald Trump (Voldemort) in them and select the surrounding paragraph:

```
^\r?\n(?:.+\r?\n)*.*\bholds\b.*\r?\n(?:.+\r?\n)*(?=\r?\n)
```

Found that regex on [this Stack Overflow answer](http://stackoverflow.com/questions/32594792/regex-matching-text-within-paragraphs).

I got rid of all line breaks and made each pasasge fit on one line. I also did a `Permute Lines -> Random` in Sublime Text, to pre-randomize the entries. 


### Image Generation

Had to generate these tweets as images, because almost no passages fit in 140 charachters. So I am creating an image for each tweet with text, that is max 540 x 203 pixels, the max size a media post can be before expanding is required.

The image manipulation library I use is PIL. It' has sort of ugly text rendering but, oh well.

Using a free usage yellowed paper background for tweets to make things a bit more interesting. Using the font Crimson Text to hopefully get a kind of book-ish vibe.

Nothing special about writing out the text, just loop through each line of text and write it out. I am wrapping it so it will fit using `textwrap`. Also cropping the extra bottom of the image so there's not a bunch of extra white space at the bottom of short passages.

I pre-generated all imags on my Mac, because the font rendering there is far far better than doing it on a random Linux server, for some reason.

