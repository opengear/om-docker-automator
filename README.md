# om-docker-netmiko
Netmiko Docker Container for Opengear Operations Manager

Run Netmiko based Python scripts to send Cisco IOS commands from an Operations Manager to a Cisco IOS device remotely via SSH.

# Instructions
```
1. Create a new directory on your OM (e.g. /home/root/myscript)
2. Upload the files to the newly created directory:
  - build.sh
  - Dockerfile
  - run.sh
  - test.py
  - show_version.py
3. chmod +x build.sh and run.sh
4. Run the build.sh to build the container
5. Run the run.sh to start the container
```

# Usage
```
The below scripts assist in creating and starting the container
- build.sh - initially create the Docker image (only need to do this once)
- run.sh - start and run the container
```
# Examples
```
To execute the test.py script, run the below docker exec command on the running container...
- docker exec netmiko python3 test.py
```
  ```
  To run your own custom script, copy your script to the running container...
  - docker cp /local/path/to/myscript.py netmiko:/scripts/myscript.py

  To execute your custom script, run the below docker exec command on the running container...
  - docker exec netmiko python3 myscript.py
  ```
```
To execute the show_version.py script, edit the 'device1' parameters in the script. 
Copy the script to the running container using the docker cp command or edit prior to building the container.
    
    device1 = {
        'host': '10.0.0.5
        'username': 'oguser',
        'password': 'password
        'device_type': 'cisco_ios',
        'session_log': 'netmiko_log.txt'
    }   
```
