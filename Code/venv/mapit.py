import webbrowser
import sys

sys.argv


def commandDirections():

    if len(sys.argv) > 1:
        commandInput = ' '.join(sys.argv[1:])

    addresses = commandInput.split(',')
    startPoint = addresses[0]
    endPoint = addresses[1]

    webbrowser.open(f'https://www.google.com/maps/dir/{startPoint}/{endPoint}')


if __name__ == "__main__":
    commandDirections()
