#! /usr/bin/env python3
# Using Brophy's rules
import csv
import os
import sys

def getgp(gr): # Just a match case statement with all GPA values
    match gr.lower():
        case "a": 
            return 4
        case "a-":
            return 3.67
        case "b+":
            return 3.33
        case "b":
            return 3
        case "b-":
            return 2.67
        case "c+":
            return 2.33
        case "c":
            return 2
        case "c-":
            return 1.67
        case "d+":
            return 1.33
        case "d":
            return 1
        case "d-":
            return 0.67
        case "f":
            return 0

def main():
    args = sys.argv
    if len(args) >= 2:
        if args[1] == "-u":
            weighted = False
        else:
            weighted = True
    else:
        weighted = True
    csvs = os.listdir("grades")
    csvs = [f"grades/{c}" for c in csvs if c.endswith(".csv")]
    tot_gps = 0
    tot_n = 0
    for fd in csvs:
        gps1 = 0
        gps2 = 0
        gpsy = 0
        n1 = 0
        n2 = 0
        ny = 0
        with open(fd) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                classname = row[0]
                row.pop(0)
                for s,sem in enumerate(row):
                    if s == 0:
                        if sem:
                            if weighted:
                                if classname.lower().startswith("ap"):
                                    gps1 += 1
                                    gpsy += 1
                                    tot_gps += 1
                                elif classname.lower().startswith("honor"):
                                    gps1 += 0.5
                                    gpsy += 0.5
                                    tot_gps += 0.5
                            n1 += 1
                            ny += 1
                            tot_n += 1
                            g = getgp(sem)
                            gps1 += g
                            gpsy += g
                            tot_gps += g
                        else:
                            pass
                    elif s == 1:
                        if sem:
                            if weighted:
                                if classname.lower().startswith("ap"):
                                    gps2 += 1
                                    gpsy += 1
                                    tot_gps += 1
                                elif classname.lower().startswith("honor"):
                                    gps2 += 0.5
                                    gpsy += 0.5
                                    tot_gps += 0.5
                            n2 += 1
                            ny += 1
                            tot_n += 1
                            g = getgp(sem)
                            gps2 += g
                            gpsy += g
                            tot_gps += g
                        else:
                            pass
        print(f"GPAs for {fd}: \nS1: {gps1/n1 if n1 else 0}\nS2: {gps2/n2 if n2 else 0}\nTot: {gpsy/ny if ny else 0}")
    print(f"Total GPA: {tot_gps/tot_n if tot_n else 0}")


if __name__ == "__main__":
    main()
