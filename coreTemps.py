import argparse
import approximations as apx
# import testdata

parser = argparse.ArgumentParser(description='''Insert Decription Here''')
parser.add_argument('filename', help='name of .txt file containing input data')
args = parser.parse_args()

infile = args.filename

cores = apx.load_data(infile)
# cores = testdata.testData1()

for i in range(len(cores)):
    outfile = "core%d.txt" % i
    with open(outfile, 'w') as of:
        of.write(apx.leastSquares(cores[i]).toString())
        of.write(apx.linear(cores[i]).toString())
        of.write(apx.cubicSpline(cores[i]).toString())
