import numpy as np


# y[n] = a * x[n] - a * y[n - k] + x[n - k]
class allpass_first():
    def __init__(self, delay_len, a):
        self.ring_buff = np.zeros(delay_len)
        self.delay_len = delay_len
        self.head = 0
        self.a = a

    def buff_put(self, val):
        self.ring_buff[self.head] = val
        if self.head == self.delay_len - 1:
            self.head = 0
        else:
            self.head += 1

    def proc(self, new_samp):
        out = self.a * new_samp + self.ring_buff[self.head]
        self.buff_put(new_samp - self.a * out)
        return out

# y[n] = x[n] + a * y[n - k]

class feedback_comb():
    def __init__(self, delay_len, a):
        self.ring_buff = np.zeros(delay_len)
        self.delay_len = delay_len
        self.head = 0
        self.a = a

    def buff_put(self, val):
        self.ring_buff[self.head] = val
        if self.head == self.delay_len - 1:
            self.head = 0
        else:
            self.head += 1

    def proc(self, new_samp):
        out = new_samp + self.ring_buff[self.head]
        self.buff_put(self.a * out)
        return out

