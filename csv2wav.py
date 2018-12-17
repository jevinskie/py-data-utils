#!/usr/bin/env python3

import sys

import numpy
import scipy.io.wavfile

data_raw, none = numpy.loadtxt(open(sys.argv[1]), delimiter=',', skiprows=5, unpack=True)
print(data_raw[:5])

mean_raw = numpy.mean(data_raw)
print('mean_raw: {}'.format(mean_raw))
min_raw = numpy.min(data_raw)
max_raw = numpy.max(data_raw)
print('min_raw: {} max_raw: {}'.format(min_raw, max_raw))
rng_raw = max_raw - min_raw
print('range_raw: {}'.format(rng_raw))


data = data_raw - mean_raw
print(data[:5])

mean = numpy.mean(data)
print('mean: {}'.format(mean))

minn = numpy.min(data)
maxx = numpy.max(data)
print('min: {} max: {}'.format(minn, maxx))
rng = maxx - minn
print('range: {}'.format(rng))


data_norm = data * (2 / rng)
print(data_norm[:5])

mean_norm = numpy.mean(data_norm)
print('mean_norm: {}'.format(mean_norm))

min_norm = numpy.min(data_norm)
max_norm= numpy.max(data_norm)
print('min_norm: {} max_norm: {}'.format(min_norm, max_norm))
rng_norm = max_norm - min_norm
print('range_norm: {}'.format(rng_norm))


data_norm2 = data_norm - (max_norm - 1)
print(data_norm2[:5])

mean_norm2 = numpy.mean(data_norm2)
print('mean_norm2: {}'.format(mean_norm2))

min_norm2 = numpy.min(data_norm2)
max_norm2= numpy.max(data_norm2)
print('min_norm2: {} max_norm2: {}'.format(min_norm2, max_norm2))
rng_norm2 = max_norm2 - min_norm2
print('range_norm2: {}'.format(rng_norm2))

norm3_scale = 1
if max_norm > 1:
	norm3_scale = 1 / max_norm
else: # min_norm < -1
	norm3_scale = -1 / min_norm
print('norm3_scale: {}'.format(norm3_scale))
data_norm3 = data_norm * norm3_scale
print(data_norm3[:5])

mean_norm3 = numpy.mean(data_norm3)
print('mean_norm3: {}'.format(mean_norm3))

min_norm3 = numpy.min(data_norm3)
max_norm3= numpy.max(data_norm3)
print('min_norm3: {} max_norm3: {}'.format(min_norm3, max_norm3))
rng_norm3 = max_norm3 - min_norm3
print('range_norm3: {}'.format(rng_norm3))

scipy.io.wavfile.write(sys.argv[2], 100*1000, data_norm3)

