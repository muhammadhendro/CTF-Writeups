# deep

```
# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15+ (default, Nov 27 2018, 23:36:35)
# [GCC 7.3.0]
# Embedded file name: source.py
# Compiled at: 2019-07-11 14:01:32

import marshal
import zlib
import base64

a = 'PCOH2U63N3JUAEB5W2JTRAKCJPUSLFEW4QC6U32AVBC5Z46SQ7SC2ESFN3LKIVU5WSYR2SRBKUSFUIOEIWAIJBFYBDY4JNYAQJ37RGRQGNHEENVI3DPJHGJTWOZTHM4TDL5M6MVNZO2KFXYERI7AHSUEWKQFEUDJVCGDANSUCYVDO4BA2MY2RY2QCNICPICORJNVUHBGIVGYTZYU2QUUCYVGUFHEHTKAZWFDABZVF6MEO7IZKVZD5A2DUBFMCF2EGDQVCDTHOFQKBGSCDXYNF4CSVRPLWPMNNIDB46LELBPTPUP2QIVKLOBIHOZ7B2FT4EAQOJTO3ZJEXKBY46ULVQBGPDN637L5K6C7UNCCOUJ27D5DLZDJAJPKZUUNLNJA4QZY33GZIK7NFSGVETRIOUOSBJZEIPOWG53Q2CD5HBDNXSKRJ52HUVOI445GTFL66V5L2LWXZLLKPOTVKLEJOGWZV737GCCVJA3L7VX4BKE57637VN62CH3CSS7PL6HJS76U4S5A6RJWYFSKL5C6RIXULWCAESR7ISYJGHR4DLVUCAJVSNUF4KK2K54WBLYQOQGJ5RZNCNIZ5ZIOLAHBO6MEFMYVQJZJ36IZTTWTGRUBZ2PTCXD2EMDLH37RK7EDYBQYQGPOHHTEBPBPXDT3BF2AYSKV7CTKUG7RHL6EUICG4Y2DXEVRYLTCS4NG6YONDYSHZHODQFTZTQWFEZTUFYZLCPWWBX3AW3J5OZ5RJ7EVUUUTZGE24W3ILVAGXDWNCXEXDTPBJ3CHEXV3CGT6SN3UTN2U7GHNKCKSKWKWZLWF4HQWWN5UIGLFVPPV2SM7DJFGS332WWW6FXOAVUL53JTSRPFI77FGL66DRPAMONINWDFEWMO3TDDQRJX2LQUXSC2DOWRCVR4NIIRXF3XFDFSJHC73TU4ORMNV5UYNUMC7FOGBA6GZWIZXOA3ZHFCNVWMP7FLBB7FFQ43SYNGRRNRBE7G5VPJDE5EFGHRERWGEHUL4YF3NTVUOHHVOMG63VIOXQKY4HGNCA6DI4TUJ2MGOCP7ACR27QKRA===='

exec marshal.loads(zlib.decompress(base64.b32decode(a)))
# okay decompiling source.pyc
```
<br>

```
import zlib
import marshal
import base64
from uncompyle6.main import decompile
from sys import stdout

tes = 'PCOH2U63N3JUAEB5W2JTRAKCJPUSLFEW4QC6U32AVBC5Z46SQ7SC2ESFN3LKIVU5WSYR2SRBKUSFUIOEIWAIJBFYBDY4JNYAQJ37RGRQGNHEENVI3DPJHGJTWOZTHM4TDL5M6MVNZO2KFXYERI7AHSUEWKQFEUDJVCGDANSUCYVDO4BA2MY2RY2QCNICPICORJNVUHBGIVGYTZYU2QUUCYVGUFHEHTKAZWFDABZVF6MEO7IZKVZD5A2DUBFMCF2EGDQVCDTHOFQKBGSCDXYNF4CSVRPLWPMNNIDB46LELBPTPUP2QIVKLOBIHOZ7B2FT4EAQOJTO3ZJEXKBY46ULVQBGPDN637L5K6C7UNCCOUJ27D5DLZDJAJPKZUUNLNJA4QZY33GZIK7NFSGVETRIOUOSBJZEIPOWG53Q2CD5HBDNXSKRJ52HUVOI445GTFL66V5L2LWXZLLKPOTVKLEJOGWZV737GCCVJA3L7VX4BKE57637VN62CH3CSS7PL6HJS76U4S5A6RJWYFSKL5C6RIXULWCAESR7ISYJGHR4DLVUCAJVSNUF4KK2K54WBLYQOQGJ5RZNCNIZ5ZIOLAHBO6MEFMYVQJZJ36IZTTWTGRUBZ2PTCXD2EMDLH37RK7EDYBQYQGPOHHTEBPBPXDT3BF2AYSKV7CTKUG7RHL6EUICG4Y2DXEVRYLTCS4NG6YONDYSHZHODQFTZTQWFEZTUFYZLCPWWBX3AW3J5OZ5RJ7EVUUUTZGE24W3ILVAGXDWNCXEXDTPBJ3CHEXV3CGT6SN3UTN2U7GHNKCKSKWKWZLWF4HQWWN5UIGLFVPPV2SM7DJFGS332WWW6FXOAVUL53JTSRPFI77FGL66DRPAMONINWDFEWMO3TDDQRJX2LQUXSC2DOWRCVR4NIIRXF3XFDFSJHC73TU4ORMNV5UYNUMC7FOGBA6GZWIZXOA3ZHFCNVWMP7FLBB7FFQ43SYNGRRNRBE7G5VPJDE5EFGHRERWGEHUL4YF3NTVUOHHVOMG63VIOXQKY4HGNCA6DI4TUJ2MGOCP7ACR27QKRA===='

jadi = base64.b32decode(tes)
jadi = zlib.decompress(jadi)
lel = marshal.loads(jadi)
decompile(2.7, lel, stdout)
```