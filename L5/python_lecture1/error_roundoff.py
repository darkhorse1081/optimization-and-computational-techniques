import numpy as np

if __name__ == '__main__':

    # np.float32 = a single precision number with exact representation
    a32=np.float32(1.+1./2**6)
    print("  a = {:18.18f} \na*a = {:18.18f}".format(a32,a32*a32))

    # np.float16 = a half precision number with exact representation
    a16=np.float16(1.+1./2**6)
    print("  a = {:18.18f} \na*a = {:18.18f}".format(a16,a16*a16))