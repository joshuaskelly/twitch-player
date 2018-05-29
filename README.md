# twitch-player

twitch-player turns Twitch chat commands into key presses on your computer!

[![Twitch](https://img.shields.io/badge/twitch-joshuaskelly-red.svg?colorB=4b367c)](https://www.twitch.tv/joshuaskelly) [![Python 3](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)

## Installation

```
$ pip install -r requirements.txt
```

## Configuration
You need to add a config.cfg file to the project root. It should look like:

```cfg
[TWITCH]
; User name of Twitch account. Preferably an alternate from your main Twitch
; account.
Nickname = Nick

; OAuth token acquired from: http://twitchapps.com/tmi
Password = oauth:abcdefghijklmnopqrstuvwxyz0123

; Channel to observe
Channel = channel

[KEYMAP]
; List of viewer commands and the corresponding keys to press.
!left = KEY_LEFT_ARROW
!right = KEY_RIGHT_ARROW
!space = KEY_SPACE
!escape = KEY_ESCAPE
```

## Running
twitch-player must be running on the same machine as the streamed game and the game must have focus.

```
$ python play.py
```

## Contributing
Have a bug fix or a new feature you'd like to see in twitch-player? Send it our way! Please make sure you create an issue that addresses your fix/feature so we can discuss the contribution.

1. Fork it!
2. Create your feature branch: `git checkout -b features/bug-fix-missing-keys`
3. Commit your changes: `git commit -m 'Adding missing key binds'`
4. Push to the branch: `git push origin bug-fix-missing-keys`
5. Submit a pull request.
6. Create an [issue](https://github.com/joshuaskelly/twitch-player/issues/new).

## License

MIT

See the [license](./LICENSE) document for the full text.