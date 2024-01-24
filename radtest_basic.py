import subprocess
import time

runnumber = 0
number_accept = 0
number_of_failures = 0

def run_radtest(number_accept, number_of_failures):
    # Define the command as a list of individual arguments
    command = ["radtest", "testing", "password", "1.1.1.1:5560", "0", "RadiusSecret1"]
    
    try:
        # Use subprocess.Popen to run the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()  # Capture the output

        # Check the return code to see if the command was successful
        if process.returncode == 0:
            linerun = stdout.decode("utf-8")
            linerunsplt = linerun.split('"')
            linerunsplt2 = str(linerunsplt).split(" ")
            if linerunsplt2[1] == 'Access-Request':
                print("access accept found")
                number_accept = number_accept + 1
                print(f"number_accept {number_accept}")
                return number_accept, number_of_failures
            else:
                print("ACCESS ACCEPT NOT FOUND")
                number_of_failures = number_of_failures + 1
                return number_accept, number_of_failures
        else:
            print("ACCESS ACCEPT NOT FOUND")
            number_of_failures = number_of_failures + 1
            return number_accept, number_of_failures
            #return f"Error: {stderr.decode('utf-8')}"
    except Exception as e:
        print("ACCESS ACCEPT NOT FOUND")
        #return f"Error: {str(e)}"

# Call the function to run the radtest command 
while True:
    number_accept, number_of_failures = run_radtest(number_accept, number_of_failures)
    print(number_accept, number_of_failures)
    runnumber += 1
    print(f"Number of runs {runnumber}")
    print(f"Number of Access-Accept {number_accept}")
    print(f"Number of Failures? {number_of_failures}")
