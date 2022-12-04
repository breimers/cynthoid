from blessed import Terminal
from notes import *
from waves import *


class KeyInput:
    """KeyInput
    
    Keyboard input (works only on Unix Systems)
    """
    def __init__(self):
        self.term = Terminal()

        self.columns = 22
        self.rows = 10
        
        self.natural_keys = 'asdfghjkl;'
        self.sharp_keys = 'wetyuop'
        self.waveform = SinWave

        self.octave = 1.0
        
        self.NATURAL_SCALE = [
            C(octave = self.octave),
            D(octave = self.octave),
            E(octave = self.octave),
            F(octave = self.octave),
            G(octave = self.octave),
            A(octave = self.octave),
            B(octave = self.octave),
            C(octave = self.octave*2),
            D(octave = self.octave*2),
            E(octave = self.octave*2)
        ]

        self.SHARP_SCALE = [
            C(octave = self.octave).sharp(),
            D(octave = self.octave).sharp(),
            F(octave = self.octave).sharp(),
            G(octave = self.octave).sharp(),
            A(octave = self.octave).sharp(),
            C(octave = self.octave*2).sharp(),
            D(octave = self.octave*2).sharp()
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

    def draw(self):
        print(self.term.home + self.term.tomato4_on_tomato4 + self.term.clear)
        height = self.term.height
        width = self.term.width
        column_width = int(width / self.columns)
        row_height = int(height / self.rows)
        
        for i in range(1, self.columns, 1):
            if i%2 == 0:
                x = column_width * i
                for j in range(10, row_height*8, 1):
                    y =  j
                    with self.term.location(x, y):
                        print(self.term.white_on_tomato4 + "|" * column_width + self.term.tomato4_on_tomato4)
            if i%2 != 0 and i not in [1, 7, 15, 21]:
                x = column_width * i
                for j in range(8, row_height*5, 1):
                    y =  j
                    with self.term.location(x, y):
                        print(self.term.gray4_on_tomato4 + "#" * column_width + self.term.tomato4_on_tomato4)

    def highlight_section(self, x, y, right, down):
        pass
    
    def unhighlight_section(self, x, y, right, down):
        pass
    
    def start(self):
        with self.term.cbreak():
            val = ''
            self.draw()            
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
                    print(self.term.home + self.term.green_on_black + self.term.clear)
                    break
                if val in self.natural_keys:
                    freq = self.natkey_freq_map[val]
                    # self.highlight_section()
                    self.waveform(
                        frequency=freq,
                        length=1.0
                    ).play()
                    # self.unhighlight_section()
                if val in self.sharp_keys:
                    freq = self.sharpkey_freq_map[val]
                    # self.highlight_section()
                    self.waveform(
                        frequency=freq,
                        length=1.0
                    ).play()
                    # self.unhighlight_section()


class MidiInput:
    pass


class ElectronInput:
    pass