import numpy as np
class Avatar:
    def __init__(self):
        pass
    @staticmethod
    def listofAvatar():
      AvatarStyle = [str(None),
                     "adventurer",
                     "adventurer-neutral",
                     "avataaars",
                     "avataaars-neutral",
                     "big-ears",
                     "big-ears-neutral",
                     "big-smile",
                     "bottts",
                     "bottts-neutral",
                     "croodles",
                     "croodles-neutral",
                     "fun-emoji",
                     "icons",
                     "identicon",
                     "initials",
                     "lorelei",
                     "lorelei-neutral",
                     "micah",
                     "miniavs",
                     "open-peeps",
                     "personas",
                     "pixel-art",
                     "pixel-art-neutral",
                     "shapes",
                     "thumbs",
                     "no-avatar"]
      return np.random.choice(AvatarStyle)
