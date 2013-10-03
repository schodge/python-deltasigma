from __future__ import division
import numpy as np

def sinc_decimate(x, m, r):
	""" y = sinc_decimate(x,m,r)	
	Decimate x by m-th order sinc of length r.
	"""
	x = x[:]
	for i in range(m):
		x = np.cumsum(x)
		x = np.concatenate((x[:r], x[r:] - x[:-r]), axis=0)/r
	return x[r::r]

def test():
	tv = np.sin(2*np.pi*.1*np.arange(0, 100))
	r = [-1.33907057e-17, -3.55951662e-17, -2.28847549e-18, 
	     -3.55951662e-17, -1.02208548e-16, -4.35275455e-16, 
	      4.97311886e-16, -4.57479916e-16, 4.30698504e-16]
	assert np.allclose(sinc_decimate(tv, 1, 10), r, rtol=1e-5, atol=1e-8)

if __name__ == '__main__':
	test()
