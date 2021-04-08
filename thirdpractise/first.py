import struct


def f31(pack_obj):
    s = "{"
    # A
    s = s + ("'A1': " + str(struct.unpack(">1f", pack_obj[4:8])[0])) + ",\n"
    s = s + ("'A2': " + str(struct.unpack("1b", pack_obj[8:9])[0])) + ",\n"
    s = s + "'A3': {"
    s = s + ("'B1': " + str(struct.unpack(">1H", pack_obj[9:11])[0])) + ","
    s = s + (" 'B2': " + str(struct.unpack("1B", pack_obj[11:12])[0])) + ","
    s = s + (" 'B3': " + str(struct.unpack(">Q", pack_obj[12:20])[0])) + "},\n"
    s = s + ("'A4': " + str(struct.unpack("1b", pack_obj[20:21])[0])) + ",\n"
    s = s + "'A5': {"
    adressC = (struct.unpack(">1H", pack_obj[21:23])[0])
    # C
    adressD = (struct.unpack(">1H", pack_obj[adressC:(adressC + 2)])[0])
    s = s + "'C1': {"
    s = s + "'D1': " + str(struct.unpack("1b", pack_obj[adressD:adressD + 1])[0]) + ",\n"
    s = s + "'D2': " + str(struct.unpack(">1f", pack_obj[adressD + 1:adressD + 5])[0]) + ",\n"
    s = s + "'D3': " + str(struct.unpack(">i", pack_obj[adressD + 5:adressD + 9])[0]) + ",\n"
    Esize = struct.unpack(">1H", pack_obj[adressD + 9:adressD + 11])[0]
    adressE = struct.unpack(">I", pack_obj[adressD + 11:adressD + 15])[0]
    s = s + "'D4': ["
    for i in range(Esize):
        s = s + "{'E1': " + str(struct.unpack(">1i", pack_obj[adressE + (i * 11):adressE + (i * 11) + 4])[0]) + ",\n"
        s = s + "'E2': " + str(
            struct.unpack(">1b", pack_obj[adressE + (i * 11) + 4:adressE + (i * 11) + 5])[0]) + ",\n"
        s = s + "'E3': " + str(
            struct.unpack(">1I", pack_obj[adressE + (i * 11) + 5:adressE + (i * 11) + 9])[0]) + ",\n"
        if i == Esize - 1:
            s = s + "'E4': " + str(
                struct.unpack(">1H", pack_obj[adressE + (i * 11) + 9:adressE + (i * 11) + 11])[0]) + "}],\n"
        else:
            s = s + "'E4': " + str(
                struct.unpack(">1H", pack_obj[adressE + (i * 11) + 9:adressE + (i * 11) + 11])[0]) + "},\n"
    s = s + "'D5: {'"
    adressF = struct.unpack(">1H", pack_obj[adressD + 15:adressD + 17])[0]

    s = s + "'F1': " + str(struct.unpack(">1b", pack_obj[adressF:adressF + 1])[0]) + ",\n"
    s = s + "'F2': " + str(struct.unpack(">1d", pack_obj[adressF + 1:adressF + 9])[0]) + ",\n"
    massize = struct.unpack(">1I", pack_obj[adressF + 9:adressF + 13])[0]
    masadress = struct.unpack(">1I", pack_obj[adressF + 13:adressF + 17])[0]
    mas = []
    for i in range(massize):
        mas.append(struct.unpack(">1H", pack_obj[masadress + i * 2:masadress + (i * 2 + 2)])[0])
    s = s + ("'F3': " + str(mas)) + ",\n"
    s = s + "'F4': " + str(struct.unpack(">1b", pack_obj[adressF + 17:adressF + 18])[0]) + "},\n"

    s = s + "'D6': " + str(struct.unpack(">I", pack_obj[adressD + 17:adressD + 21])[0]) + ",\n"
    s = s + "'D7': " + str(struct.unpack("1B", pack_obj[adressD + 21:adressD + 22])[0]) + "},\n"

    s = s + "'C2': " + str(struct.unpack(">1Q", pack_obj[adressC + 2:adressC + 10])[0]) + ",\n"
    s = s + "'C3': " + str(struct.unpack(">1H", pack_obj[adressC + 10:adressC + 12])[0]) + ",\n"
    s = s + "'C4': " + str(struct.unpack(">1d", pack_obj[adressC + 12:adressC + 20])[0]) + ",\n"

    massize = (struct.unpack(">1H", pack_obj[adressC + 20:adressC + 22])[0])
    masadress = (struct.unpack(">1H", pack_obj[adressC + 22:adressC + 24])[0])
    mas = []
    for i in range(massize):
        mas.append(struct.unpack(">1I", pack_obj[masadress + i * 4:masadress + (i * 4 + 4)])[0])
    s = s + "'C5': " + str(mas) + ",\n"

    massize = struct.unpack(">1I", pack_obj[adressC + 24:adressC + 28])[0]
    masadress = struct.unpack(">1I", pack_obj[adressC + 28:adressC + 32])[0]
    mas = []
    for i in range(massize):
        mas.append(struct.unpack(">1q", pack_obj[masadress + i * 8:masadress + (i * 8 + 8)])[0])
    s = s + "'C6': " + str(mas) + ",\n"
    s = s + "'C7': " + str(struct.unpack(">1H", pack_obj[adressC + 32:adressC + 34])[0]) + "}"

    s = s + "}"
    return s


print(f31(b'UWG\x0b\xbfn<\xad\x93\x13\xf3\x9d|\xd2\xad\xe2V\xbf\x17\xdb\x00\x00\x80/'
          b'\x1b\xd6p\xdd3\x0bj?\xd4RV\r\x85i\x1aJH\xc8\x99\xe92\x0f!\xff*\xa7:\x00'
          b'?s\x02\x8a\xd8\x9c\x16X\xd9?\xd2KQ\x86\x1c\x87@\x00\x00\x00\x02\x00\x00\x00'
          b'8\xae\xac>\xd9}\x96j\xce\x98i\x00\x03\x00\x00\x00\x17\x00<*\x12\x9cf\xbd'
          b'/k\x889@\xf3\xc1\xa7\t\xc76S\xf5\tVf\x8aWr\xa5\xe9\xf7\xa0W\x94\xcf\x80\xe3'
          b'\x00N\xc67\xb5\xa30\x9f\x92\x0c\x1e]?\xe0\xd1c\xe3\xe0\x19\x08\x00\x03\x00d'
          b'\x00\x00\x00\x02\x00\x00\x00p&\x0f'))
