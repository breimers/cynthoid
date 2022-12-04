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

        self.octave = 5
        
        self.NATURAL_SCALE = [
            C(),
            D(),
            E(),
            F(),
            G(),
            A(),
            B(),
            C(octave = 10),
            D(octave = 10),
            E(octave = 10)
        ]

        self.SHARP_SCALE = [
            C().sharp(),
            D().sharp(),
            F().sharp(),
            G().sharp(),
            A().sharp(),
            C(octave = 10).sharp(),
            D(octave = 10).sharp()
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

        self.key_map = {**self.natkey_freq_map, **self.sharpkey_freq_map}
        
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
                if val == ']':
                    self.octave += 1
                if val == '[':
                    self.octave -= 1
                self.octave = self.octave if self.octave >= 1 else 1
                if val.code == 361:
                    print(self.term.home + self.term.green_on_black + self.term.clear)
                    break
                if val in self.key_map.keys():
                    freq = self.key_map[val]
                    # self.highlight_section()
                    self.waveform(
                        frequency=freq * (self.octave / 5),
                        length=1.0
                    ).play()
                    # self.unhighlight_section()

class MidiInput:
    pass


class ElectronInput:
    pass