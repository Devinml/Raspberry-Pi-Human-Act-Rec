import time
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

mpu = MPU9250(
    address_ak=AK8963_ADDRESS, 
    address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
    address_mpu_slave=None, 
    bus=1,
    gfs=GFS_1000, 
    afs=AFS_8G, 
    mfs=AK8963_BIT_16, 
    mode=AK8963_MODE_C100HZ)
# mpu.calibrate() # Calibrate sensors

mpu.configure() # Apply the settings to the registers.

mpu.calibrateMPU6500() # Calibrate sensors
mpu.configure() # The calibration function resets the sensors, so you need to reconfigure them

abias = mpu.abias # Get the master accelerometer biases
abias_slave = mpu.abias_slave # Get the slave accelerometer biases
gbias = mpu.gbias # Get the master gyroscope biases
gbias_slave = mpu.gbias_slave # Get the slave gyroscope biases

mpu.abias = [0, 0, 0] # Set the master accelerometer biases
mpu.abias_slave = [0, 0, 0] # Set the slave accelerometer biases
mpu.gbias = [0, 0, 0] # Set the master gyroscope biases
mpu.gbias_slave = [0, 0, 0] # Set the slave gyroscope biases
print('X,', 'Y,', 'Z,', 'alpha,', 'gamma,', 'beta')
count = 0
while count < 100:

    x,y,z = mpu.readAccelerometerMaster()
    alpha, gamma, beta = mpu.readGyroscopeMaster()
    print(x, ',', y, ',', z, ',', alpha, ',', gamma, ',', beta)
    # print("\n")
    count += 1
    time.sleep(.02)