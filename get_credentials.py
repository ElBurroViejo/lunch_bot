"""
This can be used as small helper file so that you do not have to save credentials
in clear text in Github (kind of a no no ;))
Just create a file credentials.py in a folder where the sys.path points.
Then add credentials like this:

google_places_key = SOME_KEY

"""

import sys

sys.path.append("../")

import credentials 



