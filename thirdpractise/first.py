import struct


def f31(pack_obj):
    print("A1: " + str(struct.unpack(">1f", pack_obj[4:8])[0]))
    print("A2: " + str(struct.unpack("1b", pack_obj[8:9])[0]))
    # B
    print("B1: " + str(struct.unpack(">1H", pack_obj[9:11])[0]))
    print("B2:" + str(struct.unpack("1B", pack_obj[11:12])[0]))
    print("B3: " + str(struct.unpack(">Q", pack_obj[12:20])[0]))

    print("A4:" + str(struct.unpack("1b", pack_obj[20:21])[0]))
    adressC = (struct.unpack(">1H", pack_obj[21:23])[0])
    # C
    adressD = (struct.unpack(">1H", pack_obj[adressC:(adressC + 2)])[0])
    print("C2: " + str(struct.unpack(">1Q", pack_obj[adressC + 2:adressC + 10])[0]))
    print("C3: " + str(struct.unpack(">1H", pack_obj[adressC + 10:adressC + 12])[0]))
    print("C4: " + str(struct.unpack(">1d", pack_obj[adressC + 12:adressC + 20])[0]))
    print("C5: " + str(struct.unpack(">2H", pack_obj[adressC + 20:adressC + 24])))
    massize=(struct.unpack(">1H", pack_obj[adressC + 20:adressC + 22])[0])
    masadress=str(struct.unpack(">1H", pack_obj[adressC + 22:adressC + 24])[0])
    mas=[]
    for i in massize:
        mas.add()
    print("C6: " + str(struct.unpack(">2I", pack_obj[adressC + 24:adressC + 32])))
    print("C7: " + str(struct.unpack(">1H", pack_obj[adressC + 32:adressC + 34])[0]))
    # D
    print("D1: " + str(struct.unpack("1b", pack_obj[adressD:adressD + 1])[0]))
    print("D2: " + str(struct.unpack(">1f", pack_obj[adressD + 1:adressD + 5])[0]))
    print("D3: " + str(struct.unpack(">i", pack_obj[adressD + 5:adressD + 9])[0]))
    Esize = struct.unpack(">1H", pack_obj[adressD + 9:adressD + 11])[0]
    adressE = struct.unpack(">I", pack_obj[adressD + 11:adressD + 15])[0]
    print(str(Esize)+"  "+str(adressE))
    adressF = struct.unpack(">1H", pack_obj[adressD+15:adressD+17])[0]
    print(adressF)
    print("D6: " + str(struct.unpack(">I", pack_obj[adressD + 17:adressD + 21])[0]))
    print("D7: " + str(struct.unpack("1B", pack_obj[adressD + 21:adressD + 22])[0]))


f31(b'UWG\x0b\xbf\x02\x18\x11?\xe0\x809\xb1\xef\xbe\xe4\x15\xc2L\x9cM\x00\x81\xac'
    b'=\xef\xff\x1dBP\xcc\xeaB\xaaF\xe7\x8cM\xc7\xfb&\xf4\xfa\xabE\xb4\x92\xfa'
    b'xG\xc0\x86\x1e\xbc\xf4q\xef\x17\xbf\xcd&\xa4Hr\x05P\x00\x00\x00\x06\x00\x00'
    b'\x00-\x10\x12=\x16\xbdB$\xf8{\xec\x00\x02\x00\x00\x00\x17\x009~R-F'
    b'\x97x\xde\xb5|\x00\x93\x96\x1db\xd1 \xb2\x17\xfc\x83\xe8&\\l\x9b\x0b\xf8T'
    b'J\x0b.\x98a2{\x10\xdc\x00K\xd97\xf5U\x91\xe0\x04\x83\xeb\xcc\xbf\xdb\xc5'
    b'\x881o\xfcx\x00\x04\x00a\x00\x00\x00\x02\x00\x00\x00q\x97\xa6')
