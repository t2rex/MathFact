import random


def print_ascii():
    r = open("ascii.txt", 'w')
    for x in range(0, 255, 1):
        r.write(str(x)+"x = "+chr(x)+"\n")
    r.close()


def create_file(debug_on, low, high, count, file_name):
    max_num = len(str(high * high))
    format_str = "%"+str(max_num)+"d"
    my_div = chr(247)
    if debug_on:
        print "Debug Is On"
    else:
        f = open(file_name, 'w')
    pairs = []
    sign = ['x', my_div, '+', '-']
    column_length = 10
    for x in range(0, count, 1):
        pairs.append([random.randint(low, high), random.randint(low, high), sign[random.randint(0, 3)]])
    for x in range(0, count, column_length):
        top_row = ""
        second_row = ""
        bottom_row = ""
        if x+column_length > count:
            column_count = count
        else:
            column_count = x + column_length
        for y in range(x, column_count, 1):
            if pairs[y][2] == my_div:
                top_row += "  "+str(format_str % (pairs[y][0]*pairs[y][1]))+" "*3
            elif pairs[y][2] == '-' and (pairs[y][0] - pairs[y][1] < 0):
                temp = pairs[y][0]
                pairs[y][0] = pairs[y][1]
                pairs[y][1] = temp
                top_row += "  " + str(format_str % pairs[y][0]) + " " * 3
            else:
                top_row += "  "+str(format_str % pairs[y][0])+" "*3
            second_row += " "+str(pairs[y][2])+str(format_str % pairs[y][1])+" "*3
            bottom_row += " "+"_"*max_num+"___ "
        if debug_on:
            print top_row
            print second_row
            print bottom_row
            print
            print
        else:
            f.write(top_row+"\n")
            f.write(second_row+"\n")
            f.write(bottom_row+"\n")
            f.write("\n")
            f.write("\n")
            f.write("\n")

if __name__ == '__main__':
    create_file(False, 5, 11, 100, "Math Fact.txt")
