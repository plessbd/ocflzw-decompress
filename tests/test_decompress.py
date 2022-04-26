import base64
from pathlib import Path

from ocflzw_decompress.lzw import LzwDecompress

TEST_DIR = Path(__file__).resolve().parent

def test_decompress():
    compressed_base64 = 'PZcOR0MwxLhhNxzNMIhRpMZwM4xGQ1GRcMhlMxmGEXjJshMSGAzGcCMxvNx0OhiNkljhmNxpNhcMxjNBhORzMp0GAgKhhNBvNphHZ9PoNBRcOxpMp3NZpNxkGhcOpjg5wm5kmcuOYynhlORyN5yLlXOVHowKgIAAAG9jZl9ibG9iAA=='.encode('utf-8')
    expected = """{\\rtf1\\ansi\\ansicpg1252\\deff0\\deflang1033{\\fonttbl{\\f0\\fnil\\fcharset0 Tahoma;}}\r\n\\viewkind4\\uc1\\pard\\f0\\fs20 error\\par\r\n}\r\n"""
    lzw = LzwDecompress()
    actual = ""
    for bt in lzw.decompress(base64.decodebytes(compressed_base64)):
        actual += chr(bt)
    assert expected == actual
if __name__ == '__main__':
    test_decompress()
