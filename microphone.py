import sounddevice as sd


class Microphone(sd.Stream):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_vol_thresh


    def start_stream(self):
        pass

    def update(self):
        pass
