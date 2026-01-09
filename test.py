import os, subprocess

#Settings
TEST_DIR = "."
CODE_FILE = "main.c"
COMPILER_TIMEOUT = 10.0  # seconds
RUN_TIMEOUT = 10.0  # seconds

#Create abosolute paths
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

#Complie the program
print("Building the program...")

try:
    ret = subprocess.run(["gcc", code_path, "-o", app_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            timeout=COMPILER_TIMEOUT)
except Exception as e:
    print("CERROR: Compilation failed:", str(e))
    exit(1)

# Parse output
output = ret.stdout.decode("utf-8")
print(output)
error = ret.stderr.decode("utf-8")
print(error)

#Check to see if the program compiled successfully
if ret.returncode != 0:
    print("CERROR: Compilation failed with return code", ret.returncode)
    exit(1)

#Run the program
print("Running the program...")

try:
    ret = subprocess.run([app_path],
                            stdout=subprocess.PIPE,
                            timeout=RUN_TIMEOUT)
except Exception as e:
    print("RERROR: Execution failed:", str(e))
    exit(1)

# Parse output
output = ret.stdout.decode("utf-8")
print("Program output:\n", output)

#All Tests passed
print("All tests passed successfully.")
exit(0)