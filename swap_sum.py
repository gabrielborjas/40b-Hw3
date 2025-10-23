def swap_sum(A, B):
	sum_A = sum(A)
	sum_B = sum(B)
	difference = sum_A - sum_B

	if difference % 2 != 0:
		return None

	target = difference // 2 

	i = 0
	j = 0

	len_A = len(A)
	len_B = len(B)

	while i < len_A and j < len_B:
		val = A[i] - B[j]

		if val == target:
			return (i, j)
		elif val < target:
			i += 1
		else:
			j += 1

	return None