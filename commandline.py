import subprocess
from subprocess import PIPE

# Open the exe using Popen
p = subprocess.Popen("./stockfish", stdin=PIPE, stdout=PIPE, stderr=PIPE)

# Send commands to this open process by using stdin.write(*command*)
p.stdin.write(b"isready\n")
p.stdin.write(b"uci\n")
p.stdin.write(b"eval")

# Communicate and get the output from the executable
out, err = p.communicate()

# Terminate the process
p.terminate()

# Output
print(out.decode())

