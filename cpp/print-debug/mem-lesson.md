

```
uint16_t  bar = 0xABCD
uint8_t   foo = 18      // 0x12
//uint8_t   sia = 0x78

uint32_t  trevor = 0x12345678

--------------------------------------------
Little Endian
"little end" is at the lowest memory address
--------------------------------------------

Addr  Val (in Hex)
--------------------
0x1F
0x1E
0x1D
0x1C
----
0x1B
0x1A
0x19
0x18
----
0x17
0x16
0x15
0x14
----
0x13
0x12
0x11
0x10
----
0x0F
0x0E
0x0D
0x0C
----
0x0B
0x0A
0x09
0x08  
----
0x07  12        trevor
0x06  34        trevor
0x05  56        trevor
0x04  78        trevor < address of variable
----
0x03  00        could be garbage
0x02  12        foo
0x01  AB        bar
0x00  CD        bar

```

32 bit variables are stored in memory on a 4 byte boundary

A 32 bit variable will only ever have addresses that end with


0x0
0x4
0x8
0xC



