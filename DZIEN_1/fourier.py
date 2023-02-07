import numpy as np
import matplotlib.pyplot as plt

samplingFrequency = 100
samplingInterval = 1/samplingFrequency

beginTime = 0
endTime = 10

signal1Frequency = 4
signal2Frequency = 7

time = np.arange(beginTime,endTime,samplingInterval)
amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)

figure,axis = plt.subplots(4,1)
plt.subplots_adjust(hspace=1)
#wykres pierwszej funkcji falowej -> amplitude1

axis[0].set_title('Funkcja falowa -> Amplitude1')
axis[0].plot(time,amplitude1)
axis[0].set_xlabel('Czas')
axis[0].set_ylabel('Amplituda')

#wykres drugiej funkcji falowej -> amplitude2

axis[1].set_title('Funkcja falowa -> Amplitude2')
axis[1].plot(time,amplitude2)
axis[1].set_xlabel('Czas')
axis[1].set_ylabel('Amplituda')

#złożenie funckji aplitude1 i amplitude2

amplitude = amplitude1 + amplitude2

#wykres złożenia dwóch funkcji falowych -> amplitude1 i amplitude2

axis[2].set_title('Złożenie dwóch funkcji falowych -> amplitude1 i amplitude2')
axis[2].plot(time,amplitude)
axis[2].set_xlabel('Czas')
axis[2].set_ylabel('Amplituda')


#transformacja Fouriera

tpCount = len(amplitude)
fourierTransform = np.fft.fft(amplitude)/tpCount

fourierTransform = fourierTransform[range(int(tpCount/2))]

values = np.arange(int(tpCount/2))
timePeriod = tpCount/samplingFrequency
frequencies = values/timePeriod

#wykres tranformacji Fouriera na funckji amplitude

axis[3].set_title('Wykres tranformacji Fouriera na funckji amplitude')
axis[3].plot(frequencies,abs(fourierTransform))
axis[3].set_xlabel('Częstotliwość')
axis[3].set_ylabel('Amplituda')

plt.show()


