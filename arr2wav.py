import numpy
import scipy.io.wavfile

def arr2wav(data_raw, outf, samplerate):
	data_raw = numpy.array(data_raw)

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

	scipy.io.wavfile.write(outf, samplerate, data_norm3)
