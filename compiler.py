import subprocess


def run(filename):
    result = subprocess.run(['cmd', '/c', 'call', 'python', filename],
                            stdout=subprocess.PIPE, shell=True)
    return result.stdout.decode('utf-8')