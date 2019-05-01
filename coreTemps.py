import argparse
import approximations as apx

parser = argparse.ArgumentParser(description='''Insert Decription Here''')
parser.add_argument('filename', help='name of .txt file containing input data')
args = parser.parse_args()

infile = args.filename

#cores = fn.loadData(infile)
cores = apx.testerData()
cores2 = apx.testerData2()

#print("p = %.1f + %.1fx" % (c0, c1))
#print("p = %f + %fx" % (c0, c1))

c = apx.leastSquares(cores[0])
print("p = %.1f + %.1fx" % (c[0], c[1]))
print("\n")

coef = apx.linear(cores[0])
i = 0
for c in coef:
    print("P%s(x) = %.1f + %.1fx" % (i, c[0], c[1]))
    i += 1
print("\n")

coef = apx.cubicSpline(cores2[0])
i = 0
for c in coef:
    print("S%s(x) = %.3f + %.3f(x-?) + %.3f(x-?)^2 + %.3f(x-?)^3" % (i, c[0], c[1], c[2], c[3]))
    i += 1
print("\n")


