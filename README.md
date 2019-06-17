# Motion_Detection
A repository containing various motion detection scripts.

## Motion detection by frame subtraction ##
Probably the simplest way to detect motion. The script subtracts the last two frames and then calculates the mean of the difference. If the mean is greater than a defined threshold it assumes that motion happened. 
