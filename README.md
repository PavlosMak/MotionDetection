# Motion_Detection
Motion detection using the frame differencing technique. 

## Dependencies ##
In order for the script to work you will have to install OpenCV for Python. You can do that by running the following in your terminal.
```
$pip install opencv-python
```

## Frame differencing ##
Probably the simplest way to detect motion. The script subtracts the last two frames and then calculates the mean of the difference. If the mean is greater than a defined threshold it assumes that motion happened. 
