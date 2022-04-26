class lzwItem:
    def __init__(self, _prefix=0, _suffix=0):
        self.Prefix = _prefix
        self.Suffix = _suffix

class LzwDecompress:
    def __init__(self):
        self.MAX_CODES = 8192
        self.tempDecompressBuffer = [0] * self.MAX_CODES
        self.lzwLookupTable = [lzwItem() for _ in range(self.MAX_CODES)]
        self.tempBufferIndex = 0
        self.codeCount = 257
        self.finalByteBuffer = []

    def decompress(self, rawbytes):
        skip_it = False

        byteArrayIndex = 0
        shift = 1
        currentShift = 1

        prevCode = 0
        middleCode = 0
        lookupIndex = 0
        firstCode = rawbytes[byteArrayIndex]

        while True:
            if currentShift >= 9:
                currentShift -= 8
                if firstCode != 0:
                    byteArrayIndex += 1
                    middleCode = rawbytes[byteArrayIndex]
                    firstCode = (firstCode << currentShift + 8) | (middleCode << currentShift)
                    byteArrayIndex += 1
                    middleCode = rawbytes[byteArrayIndex]
                    tempCode = middleCode >> (8 - currentShift)
                    lookupIndex = firstCode | tempCode
                    skip_it = True
                else:
                    byteArrayIndex += 1
                    firstCode = rawbytes[byteArrayIndex]
                    byteArrayIndex += 1
                    middleCode = rawbytes[byteArrayIndex]
            else:
                byteArrayIndex += 1
                middleCode = rawbytes[byteArrayIndex]

            if not skip_it:
                lookupIndex = (firstCode << currentShift) | (middleCode >> 8 - currentShift)
                if lookupIndex == 256:  # time to move to a new lookup table
                    shift = 1
                    currentShift += 1
                    firstCode = rawbytes[byteArrayIndex]
                    self.tempDecompressBuffer = [0] * self.MAX_CODES
                    self.tempBufferIndex = 0
                    self.lzwLookupTable = [lzwItem() for _ in range(self.MAX_CODES)]
                    self.codeCount = 257
                    continue
                elif lookupIndex == 257:  # EOF marker, better than using the string size
                    return self.finalByteBuffer

            # skipit
            skip_it = False

            if prevCode == 0:
                self.tempDecompressBuffer[0] = lookupIndex

            if lookupIndex < self.codeCount:
                self.SaveItemToLookupTable(lookupIndex)
                if self.codeCount < self.MAX_CODES:
                    self.lzwLookupTable[self.codeCount] = lzwItem(prevCode, self.tempDecompressBuffer[self.tempBufferIndex])
                    self.codeCount += 1
            else:
                self.lzwLookupTable[self.codeCount] = lzwItem(prevCode, self.tempDecompressBuffer[self.tempBufferIndex])
                self.codeCount += 1
                self.SaveItemToLookupTable(lookupIndex)

            firstCode = (middleCode & (0xff >> currentShift))
            currentShift += shift

            if self.codeCount in [511, 1023, 2047, 4095]:
                shift += 1
                currentShift += 1

            prevCode = lookupIndex

    def SaveItemToLookupTable(self, compressedCode):

        self.tempBufferIndex = -1
        while (compressedCode >= 258):
            self.tempBufferIndex += 1
            self.tempDecompressBuffer[self.tempBufferIndex] = self.lzwLookupTable[compressedCode].Suffix
            compressedCode = self.lzwLookupTable[compressedCode].Prefix

        self.tempBufferIndex += 1
        self.tempDecompressBuffer[self.tempBufferIndex] = compressedCode
        values = list(range(self.tempBufferIndex+1))
        values.reverse()
        for i in values:
            self.finalByteBuffer.append(self.tempDecompressBuffer[i])
