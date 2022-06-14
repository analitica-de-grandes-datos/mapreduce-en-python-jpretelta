#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    dict_letters = dict()

    for line in sys.stdin:
        
        number, letters = line.split("\t")
        letters = letters.strip().split(",")

        for i in letters:
            if i not in dict_letters.keys():
                dict_letters[i] = number
            else:
                dict_letters[i] = dict_letters[i] + ',' + number
         
        tuple_letters = sorted(dict_letters.items(), key=lambda x: x[0])

    for letter, associated_numbers in tuple_letters:        
        unordered_numbers = associated_numbers.split(",") 
        ordered_numbers = sorted(unordered_numbers, key=int)
        ordered_numbers = ",".join(ordered_numbers)

        sys.stdout.write("{}\t{}\n".format(letter, ordered_numbers))