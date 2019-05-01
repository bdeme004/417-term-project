import argparse
#import numpy as np
import ctFunctions as fn
#import sandbox as fn

parser = argparse.ArgumentParser(description='''Insert Decription Here''')
parser.add_argument('filename', help='name of .txt file containing input data')
args = parser.parse_args()

infile = args.filename

#cores = fn.loadData(infile)
cores = fn.testerData()

#x = [time for time in cores[0]]
#y = [cores[0][time] for time in cores[0]]
#n = 2
#
#A = np.array([fn.makeRow(i, x) for i in range(0, n)])
#b = np.array([fn.makeRowinb(i, x, y) for i in range(0, n)])
#
#print(x)
#print(y)
##
##print(A)
##print("----------")
##print(b)
#
#c = np.linalg.lstsq(A, b, rcond=None)
#
#c0, c1 = (c[0])
#
#print("p = %.1f + %.1fx" % (c0, c1))
#print("p = %f + %fx" % (c0, c1))

print(cores[0])
