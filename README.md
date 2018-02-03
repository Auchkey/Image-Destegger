# Image-Destegger

**WORK IN PROGRESS**

Finds and extracts images hidden within an image via LSB steganography.

Currently contains a small, python test script for normalising larger bit ranges into smaller ones. The idea being to eventually convert every pixel in an image to reveal another image hidden using a lower significant-bit colour encoding scheme.

The test script current lets the user to define a bit higher range (i.e. 8-bits for 256 colours) and a lower bit range (i.e. 2-bits). It then normalises the smaller bit range. More information found here: https://stackoverflow.com/a/28121940  and  https://en.wikipedia.org/wiki/Normalization_(image_processing)

Progress may be slow, as I cannot allocate much time to this project. I also need to do more research on the viability of it. I may even change to coding this in Java at some point.

**TO DO**: Add a way to normalise a range of bits rather than singular values (see bitValueTest)

**CONCERNS**: What if the pixels colours are encoded in floats?
