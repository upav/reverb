import schroeder as sch
import numpy as np
import soundfile as sf

def gen_sine(filename, fs, f, time):
    time_arr = np.arange(0, time, 1 / fs)
    #print(len(time_arr))
    sig = 0.5 * np.sin(2 * np.pi * f * time_arr)
    sf.write(filename, sig, fs)

if __name__ == "__main__":
    filename = "in.wav"
    gen_sine(filename, 48000, 300, 2)
    sch.proc_wav(filename)

