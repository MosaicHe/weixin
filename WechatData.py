import struct
import base64

HEADLEN = 8
  
def buildPackage(cmd, seq, pbuf=None):
    length = HEADLEN
    package = bytearray()
    if pbuf:
        fmt = '!2B3H%ds' %len(pbuf)
        length += len(pbuf)
        s = struct.Struct(fmt)
        string = s.pack(0xfe, 1, length, cmd, seq, pbuf)
    else:
        s = struct.Struct('!2B3H')
        string = s.pack(0xfe, 1, length, cmd, seq)

    for i in string:
        package.append(i)
        
    return base64.b64encode(package)


if __name__ == '__main__':
    L = buildPackage(0x1001, 0x0a, 'hello')
    print struct.unpack('!2B3H5s',base64.b64decode(L))
    
    
