from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
	camera.resolution = (3280, 2464)
	camera.meter_mode = 'matrix'
	camera.iso = 100
	# Wait for the automatic gain control to settle
	sleep(2)
	# Now fix the values
	g = camera.awb_gains
	camera.awb_mode = 'off'
	camera.awb_gains = g
	for filename in camera.capture_continuous('./photos/img{counter:04d}.jpg'):
		print('Captured %s' % filename)
		sleep(3)
