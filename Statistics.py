import statistics as s

print('Mean:', s.mean([1,2,3,4,5]))
print('Harmonic mean:', s.harmonic_mean([1,2,3,4,5]))

print('Median:', s.median([1,2,3,4,5]))
print('Median high:', s.median_high([1,2,30,50,51,52]))
print('Median low:', s.median_low([1,2,30,50,51,52]))

print('Mode 1:', s.mode([1,2,1,2,3,1,2,3,4,1]))
print('Mode 2:', s.mode([7,7,7,2,2,2,3,3,3,4,4,4]))

print('Population std deviation:', s.pstdev([1,2,3,4,5]))
print('Population variance:', s.pvariance([1,2,3,4,5]))

print('Sample std deviation:', s.stdev([1,2,3,4,5]))
print('Sample variance:', s.variance([1,2,3,4,5]))