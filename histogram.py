def histogram(points, bins):
	n = len(points)
	k = len(bins)
	all_densities = []
	i = 0

	for x,y in bins:
		count = 0
		while i < n and points[i] < x:
			i += 1

		start_index = i
		while i < n and points[i] < y:
			i += 1
		count = i - start_index

		width = y-x
		density= count/(n* width)
		all_densities.append(density)

	return all_densities