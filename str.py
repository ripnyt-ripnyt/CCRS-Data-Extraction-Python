input_str = b'\xff\xfeT\x00e\x00x\x00t\x00 \x00w\x00i\x00t\x00h\x00 \x00e\x00r\x00r\x00o\x00r\x00s\x00'
unicode_str = input_str.decode('utf-16-le', 'replace')
output_str = unicode_str.encode('utf-8', 'ignore')
print(output_str)
print('\xef')