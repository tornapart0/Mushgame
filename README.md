# Mushgame

An early mushroom game prototype built with [Tay's Sensible Lang](https://github.com/tornapart0/tays-sensible-lang) and Pygame. Move the mushroom with WASD.

Download a Mac or Windows build from the [Releases page](https://github.com/tornapart0/Mushgame/releases). Each Mac ZIP contains an app. The Windows ZIP contains a folder; extract it and run `Mushgame.exe` inside the folder.

Open this folder in VS Code and start editing `main.mylang`. Set up the environment once, then press Cmd+Shift+B to run it. From the project folder:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python interpreter.py main.mylang
```

On Windows, create the environment with `py -m venv .venv` and use `.venv\Scripts\python.exe` for the remaining commands. Pygame Community Edition is installed for graphics; use `import pygame` in your `.mylang` code. The language runtime is included.

`.wakatime-project` sets the Hackatime project name to Mushgame. The installed editor tracker uses the existing Hackatime configuration.
