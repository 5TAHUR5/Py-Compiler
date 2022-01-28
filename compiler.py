import subprocess


def run(filename):
    result = subprocess.check_output(
        ['cmd', '/c', 'call', 'python', filename], shell=True)
    return result.decode('utf-8')
