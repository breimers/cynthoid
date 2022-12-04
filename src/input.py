from blessed import Terminal
from notes import *
from waves import SinWave, SquareWave, SawWave, EvenSawWave


class KeyInput:
    """KeyInput
    
    Keyboard input (works only on Unix Systems)
    """
    def __init__(self):
        self.term = Terminal()

        self.natural_keys = 'asdfghjkl;'
        self.sharp_keys = 'wetyuop'
        self.waveform = SinWave

        self.NATURAL_SCALE = [
            C(),
            D(),
            E(),
            F(),
            G(),
            A(),
            B(),
            C(),
            D(),
            E()
        ]

        self.SHARP_SCALE = [
            C().sharp(),
            D().sharp(),
            F().sharp(),
            G().sharp(),
            A().sharp(),
            C().sharp(),
            D().sharp()
        ]
        
        self.natkey_freq_map = dict(
            zip(
                list(self.natural_keys),
                [note.frequency for note in self.NATURAL_SCALE]
            )
        )
        
        self.sharpkey_freq_map = dict(
            zip(
                list(self.sharp_keys),
                [note.frequency for note in self.SHARP_SCALE]
            )
        )

    def start(self):
        with self.term.cbreak():
            val = ''
            while True:
                val = self.term.inkey()
                if val == '1':
                    self.waveform = SinWave
                if val == '2':
                    self.waveform = SquareWave
                if val == '3':
                    self.waveform = SawWave
                if val == '4':
                    self.waveform = EvenSawWave
                if val.code == 361:
                    break
                if val in self.natural_keys:
                    freq = self.natkey_freq_map[val]
                    self.waveform(
                        frequency=freq,
                        length=1.0
                    ).play()
                if val in self.sharp_keys:
                    freq = self.sharpkey_freq_map[val]
                    self.waveform(
                        frequency=freq,
                        length=1.0
                    ).play()


class MidiInput:
    pass


class ElectronInput:
    pass