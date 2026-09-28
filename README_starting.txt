 ùàà## How to configure and run the hyperchalk on your Mac ##

1) download the zipped file https://github.com/Hyperchalk/Hyperchalk.git

2) Configuring Hyperchalk: in the file named docker-compose.yml

First please don't forget to rename the existing file with docker-compose.yml

	"I've done many changes most of them are fro the official document file and other I
	figured out myself for my Mac"


	DATABASE_URL:I replaced the CHANGE_THIS_PASSWORD with a real password

	HC_SECRET_KEY: I created a secrete key with this small python function "run the file 	named 64-char.py"


	# This is if I want to run It locally just to test it myself:

	HC_ALLOWED_HOSTS: "localhost,127.0.0.1, localhost"
	HC_LINK_BASE: "localhost"

	# And if I want to work on a shared board with many other teams:

			- cloudflared tunnel - 
	
	HC_ADMIN_MAIL: "john@localhost"
	HC_TIME_ZONE: "Europe/Rome"

	# here is the better version for Hyperchalk to get the full potential to design the FolA

	HC_ALLOW_AUTOMATIC_ROOM_CREATION: "true" # every time we run it we can create a new project room
	HC_ALLOW_ANONYMOUS_VISITS: "false" # everyone have to access the room with credential created by the admin
	HC_ENABLE_TRACKING_BY_DEFAULT: "true" # this is the brain of Hyperchalk
	HC_SHOW_CREATE_ROOM_PAGE: "true"
	HC_DEBUG: "true"
	HC_SERVE_FILES: "true"


	# the official version has - ./static:/srv/static_copy

	I changed it with: - static_copy:/srv/static_copy


	# Now we word on the data base setup

 	maria:
    	image: mariadb:latest (change with the latest version i.e. 10.8)

3) in the terminal: docker-compose up -d

4) cloudflared tunnel --url http://localhost:8000