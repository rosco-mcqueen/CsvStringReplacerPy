#!/usr/bin/env python3

import csv

f = open('test.csv')
f_out = open("test_new.csv", "w", newline="")
includeArtNr = set()
excludeDates = set(('16.02.20', '16.02.20'))

reader = csv.reader(f, delimiter='|')
writer = csv.writer(f_out, delimiter='|')

foundRows = 0

for row in reader:
   s = row[10] + ''
   if s in excludeDates:
      foundRows = foundRows + 1
      print(foundRows)
   else:
      writer.writerow(row)
