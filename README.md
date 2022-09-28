# elgato_stream_deck_python_script_button

Associate a python script to each button of the Elgato Stream Deck. The correct behaviour has been tested on PoP_OS.

# Working mode
The function of the script is the following:
- Open a new instance of the program 
- if the program is already running, highlight the window of the program.

# Requirements
on Linux systems, install `xdotool` (e.g. `sudo apt install xdotool`)

# Code explanation

``` python
system("xdotool search --desktop 0 --class Brave-browser windowactivate")
``` 
highlight 
