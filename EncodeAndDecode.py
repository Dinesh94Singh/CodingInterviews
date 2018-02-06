"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Refer - 1. https://docs.python.org/3/library/random.html
        2. https://docs.python.org/3/library/string.html
        3. https://docs.python.org/3/tutorial/classes.html
        4. https://stackoverflow.com/questions/47142467/joinrandom-choicechars-for-in-rangesize

"""

class Codec:
    def __init__(self):
        self.url_pair = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL."""
        # Get a set of characters that will make up the suffix
        suffix_set = string.ascii_letters + string.digits

        # Make a tinyurl template
        tiny_url = "http://tinyurl.com/".join(random.choice(suffix_set) for _ in range(6))

        # Store the pair in the dictionary
        self.url_pair[tiny_url] = longUrl

        return tiny_url

    def decode(self, shortUrl):
        """Decodes the shortened URL to its original URL."""
        # Return the value from a given key from the dictionary
        return self.url_pair.get(shortUrl)
