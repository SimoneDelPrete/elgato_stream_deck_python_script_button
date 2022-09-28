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
os.system("xdotool search --desktop 0 --class Brave-browser windowactivate")
``` 
highlight the window of the program. The structure of the linux command is the following:
```
xdotool search --desktop 0 --class <CLASS> windowactivate
``` 
where `<CLASS>` is the output of the command `xprop | grep 'CLASS'`, in particular the SECOND string of the output.

---

```python
os.system("brave-browser")
```
is the command for opening the program. `os.system()` takes as an input the bash command to open the program
