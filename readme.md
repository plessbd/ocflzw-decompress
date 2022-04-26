# OCF LZW Decompress

Implements "OCF decompresion" as used by Cerner.

Python port of https://gist.github.com/pgodwin/7d66729444173146ad698d154f2b9b6c

```python
from ocflzw_decompress.lzw import LzwDecompress
lzw = LzwDecompress()

uncompressed = lzw.decompress(blob_contents)
for bt in uncompressed:
    uncompressed_text += chr(bt)
uncompressed_text = uncompressed_text.rstrip('\x00')
```