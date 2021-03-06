#! /usr/bin/env python

# Copied straight from android-greek-ime, http://code.google.com/p/android-greek-ime/
# by Spiros Papadimitriou <spapadim@cs.cmu.edu>
# Under Apache 2.0 Licence http://www.apache.org/licenses/LICENSE-2.0

import sys
import unicodedata

maxCode = 0x500
stepBy = 8

print '// Generated by: %s ' % sys.argv[0]
print
print 'static unsigned short LOWER_CHARS[] = {',

for i in range(0, maxCode, stepBy):
    print '\n   ',
    for j in range(i, i+stepBy):
	print '0x%04x,' % ord(unichr(j).lower()),

print '\n}'

