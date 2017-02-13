from accelerometer.iacceldevice import IAccelDevice
from measure.measure import Measure
import datetime
import math

class MockFixedAccelDevice(IAccelDevice):
	"""Mock Thermometer that always gives the same reading"""

	def __init__(self):
		self.MOCK_X = 2.2
		self.MOCK_Y = -3.1
		self.MOCK_Z = -0.2
		self.MOCK_UNITS = "m/s"
		self.MOCK_VALUE = None
		self._ready = False

	def initialize(self):
		self._ready = True
		self.MOCK_VALUE = calculate_magnitude(self.MOCK_X, self.MOCK_Y,
			self.MOCK_Z)

	@property
	def ready(self) -> bool:
		return self._ready

	def read_accelerometer(self) -> Measure:
		"""This mock accelerometer """
		assert self._ready
		time = datetime.datetime.now()
		vector = Measure(self.MOCK_VALUE,self.MOCK_UNITS, time)
		return vector

	def calculate_magnitude(X, Y, Z):
		"""Calculates the magnitude of the velocity"""
		accel_array = math.sqrt(X**2 + Y**2 + Z**2)
		return accel_array
