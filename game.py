# -*- coding: cp1251 -*-
import xlrd
import random
import time

if __name__ == '__main__':
  rb = xlrd.open_workbook('/home/nowadays/Desktop/GAME.xlsx', encoding_override="cp1251")
  sheet = rb.sheet_by_index(0)
  first_col = sheet.col_values(0)

  print "Total players involved : %s" % len(first_col)

  while (len(first_col) != 1):
    time.sleep(5)
    gamer = random.choice(first_col)
    first_col.remove(gamer)
  
  print "The winner is %s" % first_col[0].encode('utf8')
  
  
