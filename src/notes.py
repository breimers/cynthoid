"""Notes

The notes module contains data defining a standard collection of notes.

"""

class Note:
    """Note
    
    Represents a musical note.
    
    Attribtues:
        frequency (int): Frequency in Hertz
        length = (float): Abstract unit of time, can be implemented as seconds, beats, etc.
    """
    def __init__(self, frequency:int=0, octave:int=5, length:float=1.0):
        self.frequency = frequency*(octave / 5)
        self.length = length

    def sharp(self):
        self.frequency = self.frequency * 1.0595
        return self
    
    def flat(self):
        self.frequency = self.frequency * (1 / 1.0595)
        return self


class C(Note):
    def __init__(self, frequency:int=261, octave:int=5, length:float=1.0):
        self.frequency = frequency*(octave / 5)
        self.length = length


class D(Note):
    def __init__(self, frequency:int=294, octave:int=5, length:float=1.0):
        self.frequency = frequency*(octave / 5)
        self.length = length


class E(Note):
    def __init__(self, frequency:int=330, octave:int=5, length:float=1.0):
        self.frequency = frequency*(octave / 5)
        self.length = length


class F(Note):
    def __init__(self, frequency:int=350, octave:int=5, length:float=1.0):
        self.frequency = frequency*(octave / 5)
        self.length = length


class G(Note):
    def __init__(self, frequency:int=392, octave:int=5, length:float=1.0):
        self.frequency = frequency*(octave / 5)
        self.length = length


class A(Note):
    def __init__(self, frequency:int=440, octave:int=5, length:float=1.0):
        self.frequency = frequency*(octave / 5)
        self.length = length


class B(Note):
    def __init__(self, frequency:int=494, octave:int=5, length:float=1.0):
        self.frequency = frequency*(octave / 5)
        self.length = length
