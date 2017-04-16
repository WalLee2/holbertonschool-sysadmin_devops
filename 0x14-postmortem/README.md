## Issue Summary:
The duration of the outage was from 2:07 A.M. PST to 2:43 A.M. PST. The impact it had caused final production line and HSM server to stop. The production line associate was unable to pair key fobs to the vehicle because the application threw an error. The error stated that the key generation failed. The root cause of the issue was that the extension name of the file was spelled incorrectly. The HSM server could not verify if backup keys were made.
* Timeline:
	* 2:07 A.M. The issue was discovered by line associate. Key pairing application throws the error "Key generation failed".
	* 2:10 A.M. Line side testing application resulted in failure for keys pairing successfully for multiple back to back cars.
	* 2:13 A.M. After it was deemed unable to be fixed by leads and supervisors the Firmware Integration engineers were contacted.
	* 2:26 A.M. After assessing the situation the vehicle configuration team was contacted and they were able to look at the HSM server
	* 2:33 A.M. The HSM server was first evaluated. The assumption is that if none of the security tests were passing and no key fobs could be paired to the car than there is something wrong with the HSM server.
	* 2: 43 A.M. Incident was solved by correcting the file extension of a file that was supposed to end in .sql

## Root Cause:
The file extension used to store the key backups in a separate HSM server was named incorrectly which resulted in the HSM server to throw errors. The verification of backup keys could not be made. If the backups could not be made properly, the key themselves do not actually get paired to the car and are not stored in the database. Since the keys could not be verified in the database of the HSM server, the testing application will throw an error.
## Short term fix:
The issue was found and fixed by using the strace command that detailed the whole process, through system calls and signals, of pairing a key to the car. It was observed that the key could not be paired to the car because the backups were not being stored in the second HSM server. After the file was named correctly, keys were properly being made in the backup HSM server after pairing them to the car.
## Long term fix / Preventative Measures:
Have a database of correctly written file extension names and not allowing the file to be saved if the file extension does not match the ones in the database. If the file extension name is correct, the responsibility of writing the correct file extension in the file will be with them. The file will be uploaded Github and any modification will be tracked. Notifications via Slack and Email will be sent out asking everyone to please update their file. Set-up a monitoring system for the key pairing station and notify both the Firmware Integration team when both the testing application and key pairing station fails via email.

