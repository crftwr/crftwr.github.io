import os
import sys
import subprocess
import shutil
import zipfile
import hashlib

PYTHON_DIR = "c:/python33"
PYTHON = PYTHON_DIR + "/python.exe"

subprocess.call( [ PYTHON, "tool/rst2html_pygments.py", "--stylesheet=tool/rst2html_pygments.css", "index.txt", "index.html" ] )
subprocess.call( [ PYTHON, "tool/rst2html_pygments.py", "--stylesheet=tool/rst2html_pygments.css", "lredit/index.txt", "lredit/index.html" ] )
subprocess.call( [ PYTHON, "tool/rst2html_pygments.py", "--stylesheet=tool/rst2html_pygments.css", "keyhac/index.txt", "keyhac/index.html" ] )

