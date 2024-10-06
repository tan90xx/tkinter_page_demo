import pyaudio
from pyaudio import PyAudio, paInt16
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue, freeze_support
import time
import wave
import librosa
# 队列相当于缓存，用于保存数据
q = Queue(10)

def cb(cb_q):
    def callback(in_data, frame_count, time_info, status):  # all parameters are need!
        rt_data = np.frombuffer(in_data, np.dtype('<i2'))
        val_list = np.hsplit(rt_data, 32)
        avg_list = [each.mean() for each in val_list]  # data average
        if cb_q.full():
            cb_q.get()
        cb_q.put(avg_list)
        return None, pyaudio.paContinue
    return callback


class Lintener(Process):
    def __init__(self, _q):
        Process.__init__(self)
        self.q = _q
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100

    def run(self):
        p = pyaudio.PyAudio()
        p.open(format=self.FORMAT,
               channels=self.CHANNELS,
               rate=self.RATE,
               input=True,
               frames_per_buffer=self.CHUNK,
               stream_callback=cb(self.q))
        while True:
            pass


def real_time_show():
    freeze_support()
    fig = plt.figure(1, figsize=(5, 2), facecolor='#000000',)
    x_length = 768
    plt.axes(xlim=(0, x_length), ylim=(-20000, 20000))
    y_data = [0 for _ in range(x_length)]
    line, = plt.plot(y_data)
    plt.axis('off')  # hide axis
    plt.xticks([])  # hide coordinate scale
    plt.yticks([])  # hide coordinate scale
    plt.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    plt.draw()
    t = time.time()
    listener = Lintener(q)
    listener.start()
    while time.time() < t + 1:
    # while True:
        if not q.empty():
            y_data = y_data[32:] + q.get()
            line.set_xdata(np.arange(0, 768, 1))
            line.set_ydata(y_data)
            try:
                fig.canvas.draw()
                fig.canvas.flush_events()
                plt.pause(0.02)
            except TclError:
                print('stream stopped')
                break
    listener.terminate()
if __name__ == '__main__':
    freeze_support()
    real_time_show()