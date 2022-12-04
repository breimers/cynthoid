"""Waves

The wave module contains parameters and logic related to the creation of different waves based on a fourier series of sine functions.

"""
import numpy as np
import sounddevice as sd

SYSTEM_SAMPLE_RATE = sd.query_devices(kind='output')['default_samplerate']  # type: ignore
DEFAULT_SAMPLE_RATE = SYSTEM_SAMPLE_RATE if SYSTEM_SAMPLE_RATE >= 1 else 44100


class Wave:
    """Wave
    Represents a Sin function given parameters, used to generate a series
    
    Attributes:
        frequency (int, optional): Frequency in HZ. Defaults to 260.
        amplitude (float, optional): Amplitude of the wave. Defaults to 0.2.
        length (float, optional): Length in seconds. Defaults to 1.0.
        x (int, optional): First element of wave series. Defaults to 1.
        harmonics (int, optional): Number of iterations. Defaults to 1.
        step (int, optional): Movement through iterations. Defaults to 1.
    """
    def __init__(self, frequency:int=260, amplitude:float=0.2, length:float=1.0, x:int=1, harmonics:int=1, step:int=1):
        self.frequency = frequency
        self.amplitude = amplitude
        self.length = length
        self.x = x
        self.harmonics = harmonics
        self.step = step

    def series(self, samplerate:int=DEFAULT_SAMPLE_RATE):
        """Series
        Generates a series of discrete values in a numpy array that represents the wave function

        Args:
            samplerate (_type_, optional): Audio device sample rate. Defaults to DEFAULT_SAMPLE_RATE.

        Returns:
            data: Numpy array representing the finite wave series.
        """
        t = np.linspace(0, self.length, int(self.length * samplerate))
        data = np.sin(2 * np.pi * self.frequency * t) * self.amplitude
        if self.harmonics <= 1:
            return data
        for i in range(self.x, self.harmonics, self.step):
                data += np.sin(i * 2 * np.pi * self.frequency/i * t) * self.amplitude
        return data
        
    def play(self, samplerate:int=DEFAULT_SAMPLE_RATE):
        """Play
        Sends wave series to sound device for playback
        
        Args:
            samplerate (_type_, optional): Audio device sample rate. Defaults to DEFAULT_SAMPLE_RATE.
        """
        sd.play(self.series(), samplerate)


class SinWave(Wave):
    """SinWave
    Implements Wave
    Parents: Wave (_type_): Represents a Sin function given parameters, used to generate a series
    """
    pass


class SquareWave(Wave):
    """SquareWave
    Implements Square wave as a finite odd fourier series of a sin wave
    Parent: Wave (_type_): Represents a Sin function given parameters, used to generate a series
    """
    def __init__(self, frequency=260, amplitude=0.2, length=1.0, x=1, harmonics=199, step=2):
        self.frequency = frequency
        self.amplitude = amplitude
        self.length = length
        self.x = x
        self.harmonics = harmonics
        self.step = step


class SawWave(Wave):
    """SquareWave
    Implements Saw wave as a finite hybrid fourier series of a sin wave
    Parent: Wave (_type_): Represents a Sin function given parameters, used to generate a series
    """
    def __init__(self, frequency=260, amplitude=0.2, length=1.0, x=1, harmonics=50, step=1):
        self.frequency = frequency
        self.amplitude = amplitude
        self.length = length
        self.x = x
        self.harmonics = harmonics
        self.step = step


class EvenSawWave(Wave):
    """SquareWave
    Implements Even Saw wave as a finite even fourier series of a sin wave
    Parent: Wave (_type_): Represents a Sin function given parameters, used to generate a series
    """
    def __init__(self, frequency=260, amplitude=0.2, length=1.0, x=2, harmonics=50, step=2):
        self.frequency = frequency
        self.amplitude = amplitude
        self.length = length
        self.x = x
        self.harmonics = harmonics
        self.step = step
