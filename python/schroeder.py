import filters as filt
import soundfile as sf
import numpy as np
import argparse

# https://ccrma.stanford.edu/~jos/pasp/Schroeder_Reverberator_called_JCRev.html

def mixing_matrix(x0, x1, x2, x3):
    s0 = x0 + x2
    s1 = x1 + x3
    out0 = s0 + s1
    out1 = - out0
    out3 = s0 - s1
    out2 = - out3
    return out0, out1, out2, out3

def proc_wav(filename):
    ap0 = filt.allpass_first(347, 0.7)
    ap1 = filt.allpass_first(113, 0.7)
    ap2 = filt.allpass_first(37,  0.7)

    fbcf0 = filt.feedback_comb(1687, 0.773)
    fbcf1 = filt.feedback_comb(1601, 0.802)
    fbcf2 = filt.feedback_comb(2053, 0.753)
    fbcf3 = filt.feedback_comb(2251, 0.733)

    data, fs = sf.read(filename)
    out0 = np.zeros(len(data))
    out1 = np.zeros(len(data))
    out2 = np.zeros(len(data))
    out3 = np.zeros(len(data))

    for i in range(len(data)):
        samp = ap0.proc(data[i])
        samp = ap1.proc(samp)
        samp = ap2.proc(samp)
        x0 = fbcf0.proc(samp)
        x1 = fbcf1.proc(samp)
        x2 = fbcf2.proc(samp)
        x3 = fbcf3.proc(samp)
        #out0[i], out1[i], out2[i], out3[i] = mixing_matrix(x0, x1, x2, x3)
        out0[i] = x0
        out1[i] = x1
        out2[i] = x2
        out3[i] = x3

    sf.write("out0.wav", out0, fs)
    sf.write("out1.wav", out1, fs)
    sf.write("out2.wav", out2, fs)
    sf.write("out3.wav", out3, fs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help = "file to add schroeder reverb to")
    args = parser.parse_args()
    proc_wav(args.filename)

