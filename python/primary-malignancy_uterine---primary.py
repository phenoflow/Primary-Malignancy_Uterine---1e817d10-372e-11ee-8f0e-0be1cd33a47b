# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"16967.0","system":"med"},{"code":"2744.0","system":"med"},{"code":"2890.0","system":"med"},{"code":"31608.0","system":"med"},{"code":"3213.0","system":"med"},{"code":"33617.0","system":"med"},{"code":"43940.0","system":"med"},{"code":"45490.0","system":"med"},{"code":"45793.0","system":"med"},{"code":"46779.0","system":"med"},{"code":"49400.0","system":"med"},{"code":"59097.0","system":"med"},{"code":"68155.0","system":"med"},{"code":"7046.0","system":"med"},{"code":"70729.0","system":"med"},{"code":"72723.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_uterine-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["primary-malignancy_uterine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["primary-malignancy_uterine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["primary-malignancy_uterine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
