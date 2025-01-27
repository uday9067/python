import sys
import getopt

opts,args = getopt.getopt(sys.argv[1:],"a:b:c:",["a=","b=","c="])

print(opts)
print(args)