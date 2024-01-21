import cv2
import csv
import os
import json
from time import sleep

def main():
    capture = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    matches = []
    batteries = []

    with open('battery_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            matches.append(row[0].split('_')[-1])
            batteries.append(row[1])

    print(batteries[len(batteries) - 1])
    next_battery = int(batteries[len(batteries) - 1]) + 1

    with open('config.json', 'r') as configfile:
        config = json.load(configfile)

    if (next_battery > config['number_of_batteries']): next_battery = 0
    
    while True:
        match = input('MATCH: ')
        
        if match in matches:
            i = matches.index(match)
            print(f'ALREADY SCANNED: battery {batteries[i]} has already been scanned for match {match}')
            continue

        print('Scan the battery...\n')

        while True:
            cret, frame = capture.read()
            if not cret:
                print('Video capture failed, exiting...')
                exit(1)
            else:
                dret, decoded_info, points, straight_qrcode = detector.detectAndDecodeMulti(frame)
                if dret:
                    if decoded_info[0] != str(next_battery):
                        print(f'WRONG BATTERY: expected battery {next_battery}, got battery {decoded_info[0]}')
                        print("Get expected battery and try again\n")
                        sleep(1)
                        continue
                    print(f'Read battery {decoded_info[0]} for match {match}\n')
                    status = input('STATUS: ')
                    charge = input('CHARGE: ')
                    v0 = input('V0: ')
                    v1 = input('V1: ')
                    v2 = input('V2: ')
                    rint = input('RINT: ')
                    with open('battery_data.csv', 'a') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([config['competition_code'] + '_' + str(config['year']) + '_' + match, decoded_info[0], status, charge, v0, v1, v2, rint])
                    print(f'Saved entry with battery {decoded_info[0]} for match {match}')
                    matches.append(match)
                    batteries.append(decoded_info[0])
                    next_battery += 1
                    if next_battery > config['number_of_batteries']: next_battery = 0
                    print(f'Next battery should be battery {next_battery}\n\n====================\n')
                    break

if __name__ == '__main__':
    if not os.path.exists('battery_data.csv'):
        with open('battery_data.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['MATCH', 'BATTERY', 'STATUS', 'CHARGE', 'V0', 'V1', 'V2', 'RINT'])
    main()