"""
Basic Flask website with Buttons that edit an Element
16.03.2026
L2DTSD
"""

from imports import *
from lib.main import main
from lib.button1 import button1


if __name__ == "__main__":
    app.run(debug=True, port=8000)
    main()  # renders the website
