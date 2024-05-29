'''
  FONT 16x32 for OLED
'''
# ' ' - '~' 0x20 - 0x7E
Font_16x32 = bytes(b'\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\xE0\xE0\xE0\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x07\xFF\x07\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x87\x80\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x03\x07\x07\x03\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\xC0\xF0\x7C\x3C\x1C\xC0\xF0\x7C\x3C\x18\x00\x00\x00\
\x00\x00\x02\x01\x00\x00\x00\x02\x01\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\xE0\x00\x00\x00\x00\x00\x00\xE0\x00\x00\x00\
\x00\x0C\x0C\x0C\xFC\x0D\x0C\x0C\x0C\x0C\x0C\xFC\x0F\x0C\x0C\x00\
\x00\x18\x18\x98\x1F\x18\x18\x18\x18\x18\x98\x1F\x18\x18\x18\x00\
\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x80\xC0\x60\x20\xF8\x20\x20\x40\xC0\x80\x00\x00\
\x00\x00\x00\x0F\x3F\x38\x70\xE0\xFF\x80\x80\x06\x07\x03\x00\x00\
\x00\x00\xE0\xF0\x70\x00\x00\x00\xFF\x03\x03\x0F\xFE\xF8\x00\x00\
\x00\x00\x00\x01\x02\x04\x04\x04\x3F\x04\x06\x02\x01\x00\x00\x00\
\x00\xC0\x60\x20\x60\xC0\x00\x00\x00\x00\x00\x80\x60\x00\x00\x00\
\x3F\xFF\x80\x00\x80\xFF\x3F\x00\xC0\x38\x8E\x81\x80\x00\x00\x00\
\x00\x00\x01\x01\x81\x60\x1C\x07\xFC\xFF\x01\x00\x01\xFF\xFC\x00\
\x00\x00\x00\x04\x03\x00\x00\x00\x00\x03\x06\x04\x06\x03\x00\x00\
\x00\x00\x80\xC0\x60\x20\x20\xE0\x80\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x9F\xFF\xE0\x40\x30\x1F\x07\x80\x80\x80\x80\x80\x80\x00\
\xF8\xFE\x01\x00\x03\x0F\x3C\x70\xE0\xC0\x60\x0F\x00\x00\x00\x80\
\x00\x01\x03\x06\x04\x04\x04\x02\x01\x01\x03\x06\x04\x04\x02\x01\
\x00\x00\x18\x1C\xFC\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x02\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xC0\x60\x30\x08\x04\x00\
\x00\x00\x00\x00\x00\x00\x00\xE0\xFC\x0F\x01\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x0F\x7F\xE0\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x07\x0C\x18\x20\x40\x00\
\x00\x04\x08\x30\x60\xC0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x01\x0F\xFC\xE0\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\xE0\x7F\x0F\x00\x00\x00\x00\x00\x00\x00\
\x00\x40\x20\x18\x0C\x07\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x30\x30\x70\x60\xC0\x80\x8E\xFF\x8F\xC0\xC0\x60\x70\x30\x30\
\x00\x18\x18\x1C\x0C\x06\x06\xE3\xFF\xE3\x02\x06\x0C\x1C\x18\x18\
\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\xFE\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x01\x01\x01\x01\x01\x01\xFF\x01\x01\x01\x01\x01\x01\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x80\x86\x47\x3F\x1E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x03\x07\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xE0\x38\x04\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\xC0\x30\x0C\x03\x00\x00\x00\x00\
\x00\x00\x00\x00\xC0\x30\x0C\x03\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x20\x1C\x07\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x80\xC0\x40\x20\x20\x20\x60\xC0\x80\x00\x00\x00\
\x00\x00\xF0\xFE\x07\x00\x00\x00\x00\x00\x00\x00\x07\xFE\xF8\x00\
\x00\x00\x1F\x7F\xE0\x00\x00\x00\x00\x00\x00\x00\xE0\x7F\x1F\x00\
\x00\x00\x00\x00\x01\x03\x02\x04\x04\x04\x06\x03\x01\x00\x00\x00\
\x00\x00\x00\x80\x80\x80\x80\xC0\xE0\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x04\x04\x04\x06\x07\x07\x06\x04\x04\x04\x00\x00\x00\
\x00\x00\x00\x00\x40\x00\x20\x20\x20\x20\x20\x60\xC0\x80\x00\x00\
\x00\x00\x0F\x0C\x00\x00\x00\x00\x00\x00\x00\x80\xE0\x7F\x1F\x00\
\x00\x00\x00\x80\x40\x20\x10\x08\x04\x02\x03\x01\x00\x80\xE0\x00\
\x00\x00\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x06\x07\x00\x00\
\x00\x00\x00\xC0\x00\x20\x20\x20\x20\x20\x60\xC0\x80\x00\x00\x00\
\x00\x00\x07\x06\x00\x00\x00\x80\x80\x80\xC0\x60\x3F\x0F\x00\x00\
\x00\x00\xE0\xE0\x00\x00\x00\x00\x00\x00\x01\x01\x03\xFE\x78\x00\
\x00\x00\x00\x03\x02\x04\x04\x04\x04\x04\x06\x02\x03\x01\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xC0\xE0\x00\x00\x00\x00\
\x00\x00\x00\x00\x80\x60\x10\x0C\x02\x01\xFF\xFF\x00\x00\x00\x00\
\x00\x10\x1C\x13\x10\x10\x10\x10\x10\x10\xFF\xFF\x10\x10\x10\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x07\x07\x04\x00\x00\x00\
\x00\x00\x00\x00\xE0\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x00\
\x00\x00\x00\xF0\x83\x40\x20\x20\x20\x20\x20\x60\xC0\x80\x00\x00\
\x00\x00\xF0\x71\x00\x00\x00\x00\x00\x00\x00\x00\x81\xFF\x7E\x00\
\x00\x00\x00\x00\x02\x00\x04\x04\x04\x04\x06\x02\x03\x01\x00\x00\
\x00\x00\x00\x00\x00\x80\x40\x60\x20\x20\x20\x20\xC0\x80\x00\x00\
\x00\x00\xF0\xFE\x87\xC0\x40\x20\x20\x20\x20\x60\xC1\x81\x00\x00\
\x00\x00\x1F\xFF\xC1\x00\x00\x00\x00\x00\x00\x00\x80\xFF\x7E\x00\
\x00\x00\x00\x00\x01\x03\x06\x04\x04\x04\x04\x02\x03\x01\x00\x00\
\x00\x00\x00\xE0\xE0\x60\x60\x60\x60\x60\x60\x60\x60\xE0\x60\x00\
\x00\x00\x07\x01\x00\x00\x00\x00\x00\x40\x10\x04\x01\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\xE0\xFC\x03\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x80\xC0\x60\x20\x20\x20\x20\x60\xC0\x80\x00\x00\x00\
\x00\x00\x0F\x3F\x70\xE0\xE0\xC0\x80\x80\xC0\x20\x3F\x0F\x00\x00\
\x00\xF8\xFC\x06\x01\x00\x00\x00\x01\x03\x03\x0F\xFE\xF8\x00\x00\
\x00\x00\x01\x03\x02\x04\x04\x04\x04\x04\x02\x03\x01\x00\x00\x00\
\x00\x00\x80\xC0\x40\x20\x20\x20\x20\x20\x40\x80\x00\x00\x00\x00\
\x00\xFE\xFF\x81\x00\x00\x00\x00\x00\x00\x00\x81\xFF\xF8\x00\x00\
\x00\x00\x81\x83\x06\x04\x04\x04\x04\x02\x83\xF0\x3F\x07\x00\x00\
\x00\x00\x03\x03\x04\x04\x04\x04\x06\x03\x01\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x60\xF0\xF0\x60\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x03\x07\x07\x03\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x60\x60\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x66\x1E\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x40\x20\x00\x00\
\x00\x00\x00\x80\xC0\x60\x30\x18\x0C\x06\x03\x00\x00\x00\x00\x00\
\x00\x00\x01\x03\x06\x0C\x18\x30\x60\xC0\x80\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x04\x08\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x00\
\x00\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x04\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x20\x40\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x03\x06\x0C\x18\x30\x60\xC0\x80\x00\x00\x00\
\x00\x00\x00\x00\x00\x80\xC0\x60\x30\x18\x0C\x06\x03\x01\x00\x00\
\x00\x00\x08\x04\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x80\xC0\x40\x20\x20\x20\x20\x20\x40\xC0\x80\x00\x00\
\x00\x00\x1E\x3F\x38\x00\x00\x00\x00\x80\xC0\x40\x60\x3F\x1F\x00\
\x00\x00\x00\x00\x00\x00\x00\x9E\x81\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x03\x07\x07\x03\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x80\xC0\x60\x20\x20\x20\x20\x40\x80\x00\x00\x00\
\x00\xF0\xFE\x07\x01\x80\xF0\x3C\x06\x02\xF6\x7E\x00\x03\xFC\x00\
\x00\x0F\x7F\xE0\x00\x1F\x3F\x20\x00\x1C\x3F\x20\x00\x88\x43\x00\
\x00\x00\x00\x01\x03\x02\x04\x04\x04\x04\x04\x02\x03\x01\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\xE0\xF0\xC0\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x80\x78\x07\x00\x03\x3F\xF8\x80\x00\x00\x00\x00\
\x00\x00\xC0\x78\x07\x04\x04\x04\x04\x04\x07\x7F\xF8\x80\x00\x00\
\x04\x06\x07\x04\x04\x00\x00\x00\x00\x00\x00\x04\x07\x07\x04\x04\
\x00\x20\x20\xE0\xE0\x20\x20\x20\x20\x20\x20\x60\xC0\xC0\x00\x00\
\x00\x00\x00\xFF\xFF\x80\x80\x80\x80\x80\x80\x40\x60\x3F\x1F\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x01\x01\x02\xFE\xF8\
\x00\x04\x04\x07\x07\x04\x04\x04\x04\x04\x04\x04\x02\x03\x01\x00\
\x00\x00\x00\x00\x80\x40\x60\x20\x20\x20\x20\x40\xC0\xC0\x00\x00\
\x00\xF0\xFE\x07\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x06\x00\
\x00\x1F\x7F\xE0\x00\x00\x00\x00\x00\x00\x00\x00\x00\xC0\x30\x00\
\x00\x00\x00\x01\x03\x02\x04\x04\x04\x04\x04\x02\x01\x00\x00\x00\
\x00\x20\x20\xE0\xE0\x20\x20\x20\x20\x20\x40\xC0\x80\x00\x00\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x01\x07\xFE\xF8\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x80\xE0\x7F\x0F\
\x00\x04\x04\x07\x07\x04\x04\x04\x04\x06\x02\x03\x01\x00\x00\x00\
\x00\x20\x20\xE0\xE0\x20\x20\x20\x20\x20\x20\x20\x60\xE0\xE0\x00\
\x00\x00\x00\xFF\xFF\x80\x80\x80\x80\x80\xC0\xF0\x00\x00\x01\x03\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x01\x07\x00\x00\x00\xC0\
\x00\x04\x04\x07\x07\x04\x04\x04\x04\x04\x04\x04\x06\x06\x07\x00\
\x00\x20\x20\xE0\xE0\x20\x20\x20\x20\x20\x20\x20\x60\x60\xE0\x00\
\x00\x00\x00\xFF\xFF\x80\x80\x80\x80\x80\x80\xC0\xF0\x00\x01\x03\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x01\x07\x00\x00\x00\
\x00\x04\x04\x07\x07\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x80\x40\x60\x20\x20\x20\x40\x40\xC0\x00\x00\x00\
\x00\xF0\xFE\x07\x01\x00\x00\x00\x00\x00\x00\x00\x01\x06\x00\x00\
\x00\x0F\x7F\xE0\x80\x00\x00\x00\x00\x00\x02\x02\xFE\xFE\x02\x02\
\x00\x00\x00\x01\x03\x02\x04\x04\x04\x04\x04\x02\x01\x01\x00\x00\
\x20\x20\xE0\xE0\x20\x20\x00\x00\x00\x00\x20\x20\xE0\xE0\x20\x20\
\x00\x00\xFF\xFF\x80\x80\x80\x80\x80\x80\x80\x80\xFF\xFF\x00\x00\
\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\
\x04\x04\x07\x07\x04\x04\x00\x00\x00\x00\x04\x04\x07\x07\x04\x04\
\x00\x00\x00\x20\x20\x20\x20\xE0\xE0\x20\x20\x20\x20\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x04\x04\x04\x04\x07\x07\x04\x04\x04\x04\x00\x00\x00\
\x00\x00\x00\x00\x00\x20\x20\x20\x20\xE0\xE0\x20\x20\x20\x20\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\
\x00\x70\x70\xF0\x80\x80\x80\x40\x60\x3F\x0F\x00\x00\x00\x00\x00\
\x00\x20\x20\xE0\xE0\x20\x20\x00\x00\x00\x20\xE0\x60\x20\x20\x00\
\x00\x00\x00\xFF\xFF\x80\xC0\xE0\xD8\x04\x03\x01\x00\x00\x00\x00\
\x00\x00\x00\xFF\xFF\x01\x00\x00\x03\x0F\x3C\xF0\xC0\x00\x00\x00\
\x00\x04\x04\x07\x07\x04\x04\x00\x00\x00\x00\x04\x07\x07\x04\x04\
\x00\x20\x20\xE0\xE0\x20\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\xC0\x00\
\x00\x04\x04\x07\x07\x04\x04\x04\x04\x04\x04\x04\x06\x07\x00\x00\
\x20\x20\xE0\xE0\xC0\x00\x00\x00\x00\x00\x00\x00\xC0\xE0\xE0\x20\
\x00\x00\xFF\x03\x3F\xFC\xC0\x00\x00\x00\xE0\x1E\x01\xFF\xFF\x00\
\x00\x00\xFF\x00\x00\x03\x7F\xF8\xF0\x3E\x01\x00\x00\xFF\xFF\x00\
\x04\x04\x07\x04\x04\x00\x00\x07\x03\x00\x00\x04\x04\x07\x07\x04\
\x20\x20\xE0\xE0\xE0\x80\x00\x00\x00\x00\x00\x20\x20\xE0\x20\x20\
\x00\x00\xFF\x00\x03\x0F\x3E\xF8\xE0\x80\x00\x00\x00\xFF\x00\x00\
\x00\x00\xFF\x00\x00\x00\x00\x00\x03\x0F\x3E\xF8\xE0\xFF\x00\x00\
\x04\x04\x07\x04\x04\x00\x00\x00\x00\x00\x00\x00\x03\x07\x00\x00\
\x00\x00\x00\x80\xC0\x40\x20\x20\x20\x20\x40\xC0\x80\x00\x00\x00\
\x00\xF0\xFE\x07\x00\x00\x00\x00\x00\x00\x00\x00\x07\xFE\xF0\x00\
\x00\x0F\x7F\xE0\x00\x00\x00\x00\x00\x00\x00\x00\xC0\x7F\x0F\x00\
\x00\x00\x00\x01\x03\x02\x04\x04\x04\x04\x02\x03\x01\x00\x00\x00\
\x00\x20\x20\xE0\xE0\x20\x20\x20\x20\x20\x20\x40\xC0\x80\x00\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x80\xC0\x7F\x1F\x00\
\x00\x00\x00\xFF\xFF\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\
\x00\x04\x04\x07\x07\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x80\xC0\x40\x20\x20\x20\x20\x40\xC0\x80\x00\x00\x00\
\x00\xF0\xFE\x07\x00\x00\x00\x00\x00\x00\x00\x00\x07\xFE\xF0\x00\
\x00\x1F\x7F\xC0\x80\x60\x20\x20\x60\xC0\x00\x00\xC0\xFF\x1F\x00\
\x00\x00\x00\x01\x03\x02\x04\x04\x04\x07\x1F\x3E\x31\x30\x08\x00\
\x00\x20\x20\xE0\xE0\x20\x20\x20\x20\x20\x20\x60\xC0\xC0\x00\x00\
\x00\x00\x00\xFF\xFF\x80\x80\x80\x80\x80\x80\x40\x60\x3F\x1F\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x03\x1F\x7E\xF0\xC0\x00\x00\x00\
\x00\x04\x04\x07\x07\x04\x04\x00\x00\x00\x00\x01\x07\x07\x04\x04\
\x00\x00\x00\x80\xC0\x60\x20\x20\x20\x20\x40\x40\xC0\xC0\x00\x00\
\x00\x00\x1F\x3F\x70\x60\xC0\xC0\x80\x80\x80\x00\x01\x07\x00\x00\
\x00\x00\x30\xC0\x00\x00\x00\x00\x01\x01\x03\x03\x0E\xFE\xF8\x00\
\x00\x00\x00\x07\x03\x02\x00\x04\x04\x04\x04\x06\x03\x01\x00\x00\
\x00\x00\xE0\x60\x20\x20\x20\xE0\xE0\x20\x20\x20\x20\xE0\x00\x00\
\x00\x03\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x03\x00\
\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x04\x04\x07\x07\x04\x04\x00\x00\x00\x00\x00\
\x20\x20\xE0\xE0\x20\x20\x00\x00\x00\x00\x20\x20\xE0\x20\x20\x00\
\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\
\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\
\x00\x00\x00\x03\x02\x04\x04\x04\x04\x04\x02\x01\x00\x00\x00\x00\
\x00\x20\x20\xE0\xE0\x20\x00\x00\x00\x00\x00\x20\x20\xE0\x20\x20\
\x00\x00\x00\x01\x1F\xFE\xE0\x00\x00\x00\x00\xE0\x1E\x01\x00\x00\
\x00\x00\x00\x00\x00\x01\x1F\xFE\xE0\xE0\x1E\x01\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x01\x07\x01\x00\x00\x00\x00\x00\x00\
\x20\xE0\xE0\x20\x00\x00\x20\xE0\xE0\x20\x00\x00\x20\xE0\x60\x20\
\x00\x01\xFF\xFC\x00\x00\x00\xF0\x7F\xFE\x00\x00\xE0\x0F\x00\x00\
\x00\x00\x00\x7F\xFE\xF0\x0F\x00\x00\x7F\xFF\xFC\x03\x00\x00\x00\
\x00\x00\x00\x00\x07\x01\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\
\x00\x20\x20\xE0\xE0\xE0\x20\x00\x00\x00\x20\xA0\xE0\x20\x20\x00\
\x00\x00\x00\x00\x03\x0F\x3E\xF8\xE0\x30\x0C\x03\x00\x00\x00\x00\
\x00\x00\x00\x00\xC0\x30\x0C\x03\x03\x0F\x3C\xF0\xC0\x00\x00\x00\
\x00\x04\x04\x06\x05\x04\x00\x00\x00\x00\x04\x05\x07\x07\x04\x04\
\x00\x20\x60\xE0\xE0\x20\x00\x00\x00\x00\x20\x20\xE0\x20\x20\x00\
\x00\x00\x00\x01\x0F\x3E\xF0\xC0\x00\xC0\x38\x07\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x01\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x04\x04\x07\x07\x04\x04\x00\x00\x00\x00\x00\
\x00\x00\x00\xE0\xE0\x60\x20\x20\x20\x20\x20\x20\xE0\xE0\x20\x00\
\x00\x00\x03\x01\x00\x00\x00\x80\xE0\x78\x1C\x07\x03\x00\x00\x00\
\x00\x00\x00\x80\xE0\x78\x1E\x07\x01\x00\x00\x00\x00\x00\xC0\x00\
\x00\x04\x07\x07\x05\x04\x04\x04\x04\x04\x04\x04\x06\x07\x00\x00\
\x00\x00\x00\x00\x00\x00\xFC\x04\x04\x04\x04\x04\x04\x04\x00\x00\
\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x3F\x20\x20\x20\x20\x20\x20\x20\x00\x00\
\x00\x00\x00\x70\xE0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x01\x0F\x3C\xE0\x80\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x01\x07\x3C\xF0\x80\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x1E\x70\x40\x00\
\x00\x00\x04\x04\x04\x04\x04\x04\x04\xFC\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\x00\x00\x00\
\x00\x00\x20\x20\x20\x20\x20\x20\x20\x3F\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x20\x10\x08\x0C\x04\x0C\x0C\x10\x20\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x04\x04\x0C\x0C\x08\x10\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x80\xC0\x40\x20\x20\x20\x20\x20\x60\xC0\x80\x00\x00\x00\
\x00\xC0\xF1\x31\x18\x08\x08\x00\x04\x04\x04\xFF\xFF\x00\x00\x00\
\x00\x01\x03\x06\x04\x04\x04\x04\x04\x02\x02\x03\x07\x04\x04\x03\
\x00\x20\x20\xE0\xF0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\xFF\xFF\x80\x40\x00\x20\x20\x20\x60\xC0\x80\x00\x00\
\x00\x00\x00\xFF\xFF\x01\x00\x00\x00\x00\x00\x00\x00\xFF\x7F\x00\
\x00\x00\x00\x07\x03\x02\x04\x04\x04\x04\x04\x02\x03\x01\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x80\xC0\x60\x20\x20\x20\x20\x60\xC0\x80\x00\x00\
\x00\x00\x7E\xFF\x81\x00\x00\x00\x00\x00\x00\x00\x03\x03\x40\x00\
\x00\x00\x00\x01\x03\x02\x06\x04\x04\x04\x04\x04\x02\x01\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x20\xE0\xF0\x00\x00\
\x00\x00\x00\x80\xC0\x40\x20\x20\x20\x20\x00\x40\xFF\xFF\x00\x00\
\x00\x00\x7E\xFF\x01\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\
\x00\x00\x00\x01\x03\x02\x04\x04\x04\x04\x02\x01\x07\x03\x02\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x80\x40\x20\x20\x20\x20\x20\x40\xC0\x80\x00\x00\
\x00\x00\x7E\xFF\x88\x08\x08\x08\x08\x08\x08\x08\x08\x0F\x8E\x00\
\x00\x00\x00\x01\x03\x02\x06\x04\x04\x04\x04\x04\x02\x01\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x80\xC0\x60\x20\x20\x20\x20\xC0\xC0\
\x00\x00\x20\x20\x20\x20\xFF\xFF\x20\x20\x20\x20\x20\x00\x01\x01\
\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x04\x04\x04\x07\x07\x04\x04\x04\x04\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\xC0\x40\x20\x20\x20\x20\x40\xC0\x80\x60\x60\x00\
\x00\x00\x00\xC7\xFF\x30\x20\x20\x20\x20\x10\x1F\x07\x00\x00\x00\
\x00\x00\x38\x7C\x43\xC3\x83\x83\x83\x83\x83\xC2\x46\x7E\x3C\x00\
\x00\x20\x20\xE0\xF0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\xFF\xFF\x80\x40\x00\x20\x20\x20\x60\xC0\x80\x00\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\
\x00\x04\x04\x07\x07\x04\x04\x00\x00\x00\x04\x04\x07\x07\x04\x04\
\x00\x00\x00\x00\x00\x00\x00\x60\xE0\x60\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x20\x20\x20\x20\xE0\xF0\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x04\x04\x04\x04\x07\x07\x04\x04\x04\x04\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\xE0\xE0\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x20\x20\x20\x20\xE0\xF0\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\
\x00\x00\x00\x60\xE0\x80\x80\x80\x80\x40\x60\x3F\x1F\x00\x00\x00\
\x00\x20\x20\xE0\xF0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x20\xA0\x60\x20\x20\x20\x00\
\x00\x00\x00\xFF\xFF\x10\x18\x0C\x1E\x39\xF0\xC0\x80\x00\x00\x00\
\x00\x04\x04\x07\x07\x04\x04\x00\x00\x00\x00\x05\x07\x06\x04\x04\
\x00\x00\x00\x20\x20\x20\x20\xE0\xF0\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x04\x04\x04\x04\x07\x07\x04\x04\x04\x04\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x20\xE0\xF0\x40\x20\x20\x20\xE0\xC0\x40\x20\x20\x20\xE0\xC0\
\x00\x00\xFF\xFF\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\xFF\xFF\
\x00\x04\x07\x07\x04\x00\x00\x04\x07\x07\x04\x00\x00\x04\x07\x07\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x20\x20\xE0\xF0\x80\x40\x00\x20\x20\x20\x60\xC0\x80\x00\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\
\x00\x04\x04\x07\x07\x04\x04\x00\x00\x00\x04\x04\x07\x07\x04\x04\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\xC0\x40\x60\x20\x20\x20\x20\x40\xC0\x00\x00\x00\
\x00\x00\x7E\xFF\x81\x00\x00\x00\x00\x00\x00\x00\x81\xFF\x7E\x00\
\x00\x00\x00\x01\x03\x02\x04\x04\x04\x04\x04\x02\x03\x01\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x20\x20\xE0\xF0\x80\x40\x20\x20\x20\x20\x60\xC0\x80\x00\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x80\xFF\x7E\x00\
\x00\x80\x80\xFF\xFF\x83\x82\x04\x04\x04\x04\x02\x03\x01\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x80\xC0\x40\x20\x20\x20\x20\x40\xC0\xC0\xE0\x00\x00\
\x00\x00\x7E\xFF\x01\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\
\x00\x00\x00\x01\x03\x06\x04\x04\x04\x04\x82\x83\xFF\xFF\x80\x80\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x20\x20\x20\x20\xF0\xF0\x00\x80\x40\x40\x20\x20\xE0\xC0\x00\
\x00\x00\x00\x00\x00\xFF\xFF\x03\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x04\x04\x04\x04\x07\x07\x04\x04\x04\x04\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x80\xC0\x40\x20\x20\x20\x20\x20\x40\xC0\xC0\x00\x00\
\x00\x00\xC0\x03\x07\x0C\x0C\x18\x18\x18\x30\x30\xE0\xC1\x00\x00\
\x00\x00\x07\x07\x02\x04\x04\x04\x04\x04\x04\x02\x03\x01\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x20\x20\x20\x30\xF8\xFF\x20\x20\x20\x20\x20\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x80\x00\x00\
\x00\x00\x00\x00\x00\x00\x01\x03\x06\x04\x04\x04\x02\x01\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x20\x20\xE0\xF0\x00\x00\x00\x00\x00\x20\x20\xE0\xF0\x00\x00\
\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\
\x00\x00\x00\x01\x03\x06\x04\x04\x04\x04\x02\x01\x07\x03\x02\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x20\x20\xE0\xE0\xE0\x20\x00\x00\x00\x00\x20\xE0\xE0\x20\x20\
\x00\x00\x00\x00\x03\x1F\x7C\xF0\x80\x80\x60\x1C\x03\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x03\x07\x03\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x20\x60\xE0\xE0\x20\x00\x20\x60\xE0\xE0\x20\x00\x00\x20\xE0\x20\
\x00\x00\x03\x3F\xFC\xE0\xE0\x1E\x07\x3F\xFC\xC0\xE0\x1E\x01\x00\
\x00\x00\x00\x00\x01\x07\x01\x00\x00\x00\x01\x07\x01\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x20\x20\x60\xE0\xE0\x20\x00\x20\xA0\x60\x20\x20\x00\x00\
\x00\x00\x00\x00\x00\xC1\x67\x1F\x3E\x7A\xE1\x80\x00\x00\x00\x00\
\x00\x04\x04\x06\x07\x04\x00\x00\x00\x04\x05\x07\x06\x04\x04\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x20\x20\xE0\xE0\x20\x20\x00\x00\x00\x20\xE0\x60\x20\x20\x00\
\x00\x00\x00\x00\x07\x1F\xFC\xE0\x80\xE0\x1C\x03\x00\x00\x00\x00\
\x00\x00\xC0\xC0\xC0\x80\x00\x13\x07\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\xC0\xE0\x20\x20\x20\x20\x20\xA0\xE0\xE0\x20\x00\x00\x00\
\x00\x00\x03\x00\x80\xE0\x70\x3C\x0E\x07\x01\x00\x00\xC0\x00\x00\
\x00\x00\x06\x07\x07\x05\x04\x04\x04\x04\x04\x06\x07\x01\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xF0\x08\x04\x04\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x7F\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\xFC\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1F\x20\x40\x40\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x04\x04\x08\xF0\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x7F\x80\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\xFC\x02\x01\x01\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x40\x40\x20\x1F\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x08\x06\x01\x01\x01\x03\x06\x0C\x18\x30\x20\x20\x20\x18\x04\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
')