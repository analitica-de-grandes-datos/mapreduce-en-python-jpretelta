#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from statistics import mean
import sys

if __name__ == '__main__':

    curkey = None
    tuple_list = []

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)
        
        if key == curkey:
            tuple_list.append(val)
        else:
            if curkey is not None:
                suma = sum(tuple_list)
                avg = mean(tuple_list)
                tuple_list.clear()                

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, avg))

            curkey = key
            tuple_list.append(val)               

    suma = sum(tuple_list)
    avg = mean(tuple_list)
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, avg))