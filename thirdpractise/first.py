import ast
import json
import struct


def f31(pack_obj):
    dict = {}
    A3 = {}
    C = {}
    C1 = {}
    D5 = {}
    E = {}
    # A
    dict.update({'A1': (struct.unpack(">1f", pack_obj[4:8])[0])})
    dict.update({'A2': (struct.unpack("1b", pack_obj[8:9])[0])})
    A3.update({'B1': (struct.unpack(">1H", pack_obj[9:11])[0])})
    A3.update({'B2': (struct.unpack("1B", pack_obj[11:12])[0])})
    A3.update({'B3': (struct.unpack(">Q", pack_obj[12:20])[0])})
    dict.update({'A3': A3})
    dict.update({'A4': (struct.unpack("1b", pack_obj[20:21])[0])})
    adressC = (struct.unpack(">1H", pack_obj[21:23])[0])
    adressD = (struct.unpack(">1H", pack_obj[adressC:(adressC + 2)])[0])

    C1.update({'D1': (struct.unpack("1b", pack_obj[adressD:adressD + 1])[0])})
    C1.update({'D2': (struct.unpack(">1f", pack_obj[adressD + 1:adressD + 5])[0])})
    C1.update({'D3': (struct.unpack(">i", pack_obj[adressD + 5:adressD + 9])[0])})

    Esize = struct.unpack(">1H", pack_obj[adressD + 9:adressD + 11])[0]
    adressE = struct.unpack(">I", pack_obj[adressD + 11:adressD + 15])[0]

    mas = []
    for i in range(Esize):
        E.update({'E1': (struct.unpack(">1i", pack_obj[adressE + (i * 11):adressE + (i * 11) + 4])[0])})
        E.update({'E2': (struct.unpack(">1b", pack_obj[adressE + (i * 11) + 4:adressE + (i * 11) + 5])[0])})
        E.update({'E3': (struct.unpack(">1I", pack_obj[adressE + (i * 11) + 5:adressE + (i * 11) + 9])[0])})
        E.update({'E4': (struct.unpack(">1H", pack_obj[adressE + (i * 11) + 9:adressE + (i * 11) + 11])[0])})
        mas.append(E.copy())
        E.clear()
    C1.update({'D4': mas})
    adressF = struct.unpack(">1H", pack_obj[adressD + 15:adressD + 17])[0]
    D5.update({'F1': (struct.unpack(">1b", pack_obj[adressF:adressF + 1])[0])})
    D5.update({'F2': (struct.unpack(">1d", pack_obj[adressF + 1:adressF + 9])[0])})
    massize = struct.unpack(">1I", pack_obj[adressF + 9:adressF + 13])[0]
    masadress = struct.unpack(">1I", pack_obj[adressF + 13:adressF + 17])[0]
    mas = []
    for i in range(massize):
        mas.append(struct.unpack(">1H", pack_obj[masadress + i * 2:masadress + (i * 2 + 2)])[0])
    D5.update({'F3': (mas)})
    D5.update({'F4': (struct.unpack(">1b", pack_obj[adressF + 17:adressF + 18])[0])})
    C1.update({'D5': D5})
    C1.update({'D6': (struct.unpack(">I", pack_obj[adressD + 17:adressD + 21])[0])})
    C1.update({'D7': (struct.unpack("1B", pack_obj[adressD + 21:adressD + 22])[0])})
    C.update({'C1': C1})
    C.update({'C2':struct.unpack(">1Q", pack_obj[adressC + 2:adressC + 10])[0]})
    C.update({'C3':struct.unpack(">1H", pack_obj[adressC + 10:adressC + 12])[0]})
    C.update({'C4':struct.unpack(">1d", pack_obj[adressC + 12:adressC + 20])[0]})

    massize = (struct.unpack(">1H", pack_obj[adressC + 20:adressC + 22])[0])
    masadress = (struct.unpack(">1H", pack_obj[adressC + 22:adressC + 24])[0])
    mas = []
    for i in range(massize):
        mas.append(struct.unpack(">1I", pack_obj[masadress + i * 4:masadress + (i * 4 + 4)])[0])
    C.update({'C5': str(mas)})

    massize = struct.unpack(">1I", pack_obj[adressC + 24:adressC + 28])[0]
    masadress = struct.unpack(">1I", pack_obj[adressC + 28:adressC + 32])[0]
    mas = []
    for i in range(massize):
        mas.append(struct.unpack(">1q", pack_obj[masadress + i * 8:masadress + (i * 8 + 8)])[0])
    C.update({'C6': str(mas)})
    C.update({'C7':struct.unpack(">1H", pack_obj[adressC + 32:adressC + 34])[0]})
    dict.update({'A5': C})
    return dict



print(f31(b'UWG\x0b\xbf\x02\x18\x11?\xe0\x809\xb1\xef\xbe\xe4\x15\xc2L\x9cM\x00\x81\xac'
          b'=\xef\xff\x1dBP\xcc\xeaB\xaaF\xe7\x8cM\xc7\xfb&\xf4\xfa\xabE\xb4\x92\xfa'
          b'xG\xc0\x86\x1e\xbc\xf4q\xef\x17\xbf\xcd&\xa4Hr\x05P\x00\x00\x00\x06\x00\x00'
          b'\x00-\x10\x12=\x16\xbdB$\xf8{\xec\x00\x02\x00\x00\x00\x17\x009~R-F'
          b'\x97x\xde\xb5|\x00\x93\x96\x1db\xd1 \xb2\x17\xfc\x83\xe8&\\l\x9b\x0b\xf8T'
          b'J\x0b.\x98a2{\x10\xdc\x00K\xd97\xf5U\x91\xe0\x04\x83\xeb\xcc\xbf\xdb\xc5'
          b'\x881o\xfcx\x00\x04\x00a\x00\x00\x00\x02\x00\x00\x00q\x97\xa6'))
