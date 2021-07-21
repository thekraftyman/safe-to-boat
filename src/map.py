# map.py
# By: thekraftyman

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Image:

	def __init__(self, src_img):
		self.img = mpimg.imread( src_img )
		self.bw_img = self.get_bw_img( self.img )

    def compute_safety( self, wind_vector ):
        ''' using a wind vector, compute safety (0 safe, 1 dangerous)
        and return as mask '''
        pass

	def is_water(self, pixel):
		''' takes an array including rgb values and returns true if blue
		is greater than green, else returns false '''

		if pixel[1] > pixel[2]:
			return False
		return True

	def is_land( self, pixel ):
		''' returns a bool if pixel is land '''

		if self.is_water( pixel ):
			return False
		return True

	def get_bw_img(self, img):
		'''returns an array of 0s and 1s that make up an image, where 0 is land
		and 1 is water'''

		bw_img = []
		for row in img:
			bw_row = []
			for pixel in row:
				if self.is_water(pixel):
					bw_row.append(1)
				else:
					bw_row.append(0)
			bw_img.append(bw_row)

		return bw_img

