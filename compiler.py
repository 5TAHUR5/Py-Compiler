import subprocess


def run(filename):
    result = subprocess.run(
        ['cmd', '/c', 'call', 'python', filename], shell=True)