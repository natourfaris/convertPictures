# Windows Lockscreen Background Saver

The Windows lockscreen background images are often beautiful, and so I find that I regularly want to save them. This script is a rudimentary attempt to do so.

To use the script, fork the repo into your Pictures folder and create a folder titled 'Output' with two folders inside titled 'Background' and 'Vertical'. Then, in your Command Prompt, navigate to the scripts folder and run

'''
python convert.py YOUR_USERNAME
'''

where YOUR_USERNAME is the name of the username. Make sure you are running as an administrator user, as I have not tested under a standard user. The script also requires the installation of [Pillow](https://pillow.readthedocs.io/en/stable/)

Future improvement:

- Having the script create the folders as required

- Getting rid of Pillow as means to determine image size and use purely built-in libraries

- Is image size constant? Testing on different machines should be done to determine that.
