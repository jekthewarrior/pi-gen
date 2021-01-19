# PI Generator
A PI generator that provides randomly generated personal information for development and testing.

## Rudimentary Roadmap
### Generator Variety and Choices
As of right now, the following generators have been implemented:

- Name and Gender (Currently linked due to nature of implementation)
- Telephone Number (Without area code)
- Credit Card Number
- IP Address (Randomly provides IPv4 and IPv6 addresses)

Future generators to be implemented or in consideration:

- SSN
- Username
- Passwords

-----------------------
### Other Features Under Consideration or Being Worked On:
- The ability to choose which generators will be used to create the resulting JSON file
- 
- Generators like the name and gender one will be optimized in the future and/or modified to provide a better, faster experience
- A script for Kafka cluster connectivity (Dependent on the user interface loop being optimized for such usage)

# Usage

After cloning the repository, run the main.py file. The generated JSON file with the PI will be stored in the repository's folder under
the name of "PI.json"

It will prompt you to run a database check. Type "yes" the first time the file is run to ensure that the program is synced with the 
dataset. Every other time the file is run after that, type "no" to skip the step. 

The program will prompt you to provide a number of "people" you want a JSON file generated for. It will work for some time and 
will provide confirmation. At this point, if you would like to generate multiple files, remove or rename the "PI.json" file in the 
pi-gen repo folder. It will prompt you about quitting the program; answer with "Yes" or "No." 

Once complete, you should have a JSON file filled with randomized private information.

# Feedback
If you would like to give some feedback or make feature requests, feel free to do so on this repository. I will take a look and try to
respond when possible. Any work done for this repo is greatly appreciated.
