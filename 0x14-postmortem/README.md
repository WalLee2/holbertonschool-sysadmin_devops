* Issue Summary:
	* Duration of outage: 2:07 A.M. PST to 2:43 A.M. PST
	* Impact:
		* Final Production Line down
		* HSM server down
	* User Experience:
		* Unable to pair key fobs to car
		* Database error
	* Root Cause:
		* Extension name of the file was spelled incorrectly.
		* Instead of .sqll, .sql is the correct file extension name.
* Timeline:
	* Issue was detected at 2:07 A.M. by line associate.
	* How issue was detected:
		* Key pairing application threw an error.
		* Line side testing application resulted in failure for keys pairing successfully for multiple back to back cars. 
		* The HSM server was first evaluated.
		* The assumption is that if none of the security tests were passing and no key fobs could be paired to the car than there is something wrong with the HSM server
		* Incident was solved by correcting the file extension of a file that was supposed to end in .sql
		* The Firmware Integration and Vehicle Configuration Teams were both immediately notified of the incident.
* Root cause:
	* The file extension used to store the key backups in a separate HSM server was named incorrectly which resulted in the HSM server to throw errors. The verification of backup keys could not be made. If the backups could not be made properly, the key themselves do not actually get paired to the car and are not stored in the database. Since the keys could not be verified in the database of the HSM server, the testing application will throw an error.
* Short term fix:
	* The issue was found and fixed by using the strace command that detailed the whole process, through system calls and signals, of pairing a key to the car. It was observed that the key could not be paired to the car because the backups were not being stored in the second HSM server.
	* After the file was named correctly, keys were properly being made in the backup HSM server after pairing them to the car.
* Long term fix / Preventative Measures:
	* Have a database of correctly written file extension names and not allowing the file to be saved if the file extension does not match the ones in the database. If the file extension name is correct, the responsibility of writing the correct file extension in the file will be with them. The file will be uploaded Github and any modification will be tracked. Notifications via Slack and Email will be sent out asking everyone to please update their file.
	* Set-up a monitoring system for the key pairing station and notify both the Firmware Integration team when both the testing application and key pairing station fails via email.

