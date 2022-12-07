# om-docker-automator
Netmiko Docker Container for Operations Manager

# Instructions
1. Create a new directory on your OM (e.g. /home/root/myscript)
2. Upload the files to the newly created directory:
  - build.sh
  - Dockerfile
  - run.sh
  - test.py
3. Run the build.sh to build the container
4. Run the run.sh to start the container

# Usage
The below scripts assist in creating and starting the container
- build.sh - initially create the Docker image (only need to do this once)
- run.sh - start and run the container

To execute the test.py script, run the below docker exec command...
- docker exec netmiko python3 test.py

To run your own custom script, copy your script to the running container...
- docker cp /local/path/to/myscript.py netmiko:/scripts/myscript.py

To execute your custom script, run the below docker exec command...
- docker exec netmiko python3 myscript.py
