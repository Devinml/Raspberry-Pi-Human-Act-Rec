import time
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import datetime
import pandas as pd

class GetData(object):

    def __init__(self, activity, test, data_points):
        self.mpu = self.setup()
        self.activity = activity
        now = datetime.datetime.now()
        self.day = now.day
        self.hour = now.hour
        self.minute = now.minute
        self.second = now.second
        self.test = test
        self.data_points = data_points

    def setup(self):
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
        return mpu


    def collect_data(self):
        fp = f'data/testactivity_{self.activity}_{self.day}_{self.hour}_{self.minute}.txt'
        with open(fp,'w') as f:
            f.write('X, Y, Z, alpha, gamma, beta, activity,test\n')
            count = 0
            while count < self.data_points:
                x,y,z = self.mpu.readAccelerometerMaster()
                alpha, gamma, beta = self.mpu.readGyroscopeMaster()
                f.write(f'{x},{y},{z},{alpha},{gamma},{beta}, {self.activity}, {self.test} \n')
                count += 1
                time.sleep(.02)

    def list_of_data(self):
        data_init = {'X': [],
                    'Y': [],
                    'Z': [],
                    'alpha': [],
                    'gamma': [],
                    'beta': []}
        data_df = pd.DataFrame()
        while len(data_df) < self.data_points:
            x, y, z = self.mpu.readAccelerometerMaster()
            alpha, gamma, beta = self.mpu.readGyroscopeMaster()
            data = {'alpha': alpha,
                    'gamma': gamma,
                    'beta': beta,
                    'X': x,
                    'Y': y,
                    'Z':z,}
            data_df = data_df.append(data, ignore_index=True)
            time.sleep(.02)
        return data_df

