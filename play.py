import configparser
import sys
import time

import keyboard
from twitchobserver import Observer
from key_names import key_names

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('./config.cfg')

    # Twitch bot info
    nickname = config['TWITCH']['Nickname']
    password = config['TWITCH']['Password']
    channel = config['TWITCH']['Channel']

    # Twitch command to key press map
    keys = {}
    keymap = config['KEYMAP']
    for command, key_alias in keymap.items():
        if command[0] == '!':
            command = command[1:]

        if key_alias not in key_names:
            print('Unrecognized key alias: {}'.format(key_alias), file=sys.stderr)
            continue

        keys[command] = key_names[key_alias]

    def press_and_release(hotkey, hold_time=0.0):
        """Press the given hotkey for the specified time and then release.

        Note:
            Some programs might not register a key press if the hold time is
            zero.

        :param hotkey: The key to press
        :param hold_time: The length of time in seconds to hold the key.
        """
        keyboard.press(hotkey)

        if hold_time > 0:
            time.sleep(hold_time)

        keyboard.release(hotkey)

    print('Connecting to Twitch')
    with Observer(nickname, password) as observer:
        print('Joining channel {} as {}'.format(channel, nickname))
        observer.join_channel(channel)
        print('Press Ctrl + C to quit')

        while True:
            try:
                # Process Twitch chat events
                for event in observer.get_events():
                    if event.type == 'TWITCHCHATMESSAGE':
                        # Only consider messages staring with '!'
                        if event.message[0] != '!':
                            continue

                        # Get the key for the given command
                        command = event.message[1:]
                        key = keys.get(command)

                        if key:
                            print('{}: {}'.format(event.nickname, key))
                            press_and_release(key, 0.125)

                time.sleep(0.125)

            except KeyboardInterrupt:
                break

        observer.leave_channel(channel)
        print('Left channel {}'.format(channel))
