# pingme
Little python command line app to send messages to discord.

Currently, only linux is supported.

### Prerequisites
* Make
* Python 3
* Setup Discord Integration

## Setup
Run `make init`

This will install python dependencies and create the log directory.

## Usage
All usages are executed from the project root directory.

If `make` is installed, a basic test message can be sent by executing
    
    $ make

To send a message

    $ ./pingme.py "Test Message"

If `/usr/bin/python` doesn't point to python3 then specify python3 before
executing

    $ python3 ./pingme.py "Test Message"

## Setup Discord Integration
1. Create Discord account
2. Create a discord server for recieving pings
3. Create a webhook for the server. 
[Discord Webhooks](https://support.discord.com/hc/en-us/articles/360045093012a)
4. Create a hookurls.txt at the project root and add your hook url.
Multiple hook urls can be added to this file with each on their own line.



