#! python3


import re
import os
import time
from pygame import mixer
from collections import defaultdict
from difflib import get_close_matches


class Instrument:
    def __init__(self, sound_path):
        self.sound = mixer.Sound(sound_path) 
    
    def play(self, times=1, total_delay=0.25):
        """Plays the sound file"""
        for _ in range(times):
            self.sound.play()
            time.sleep(total_delay / times)


class Drums:
    def __init__(self, tempo):
        mixer.init()
        self._bpm = tempo          # beats per minute
        self.instruments = self.__load_instruments()

    def __load_instruments(self) -> dict[str, list[Instrument]]:
        """Returns the instruments in a dict of lists"""
        path = r'H:\python\Drums\sound_files_wav'
        instruments = defaultdict(list)
        pattern = re.compile(r".*?\d-(\w+)-.*")
        for file in os.listdir(r'H:\python\Drums\sound_files_wav'):
            match_obj = re.match(pattern, file)
            file_path = os.path.join(path, file)
            instrument = Instrument(file_path)
            instrument_name = match_obj.group(1)
            instruments[instrument_name.lower()].append(instrument)
        return instruments
        
    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self, tempo):
        self._bpm = (60 * 1000) / tempo

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            instrument = get_close_matches(attr, list(self.instruments)).pop()
            return self.instruments[instrument]

    def roll(self, delay=0.1):
        self.lotom[1].play(2, delay)
        self.midtom[0].play(2, delay)         
        self.midtom[2].play(2, delay)
        self.hitom[1].play(2, delay)
        self.hitom[3].play(2, delay)
        self.midtom[4].play(2, delay)
        self.crash[4].play(1)


if __name__ == "__main__":
    drums = Drums(120)
    for i in range(100):
        for j in range(1, 5):
            drums.hihatclosed[0].play(1, 0)
            if j == 3:
                drums.snare[2].play(1, 0)
                drums.kick[5].play(2)
            else:    
                drums.kick[5].play(2)
        if i % 4 == 0: 
            drums.crash[4].play(2, 0)
        if i % 7 == 0:
            drums.roll(0.25)
        
            
        
