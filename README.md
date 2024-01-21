# battery-tracker

Python script for battery data tracking at competitions.

## Installation

1. Install Python 3.10 or higher
2. Install pip
3. Install dependencies with `pip install -r requirements.txt`

## Usage

1. Run `python3 battery_tracker.py`
2. The program will prompt you to enter the match number
    - If you enter a match number that has already been scanned into the system, the program will prompt you to enter a new match number
3. The program will prompt you to scan the battery QR code
    - If you scan a battery that is not the expected battery, the program will prompt you to get the correct battery
    - Expected battery is determined by the number of batteries and which batteries have already been scanned into the system
    - Expected batteries are in order from battery `0` to battery `n` (which is defined in the config.json file) and will wrap around to battery `0` after battery `n`
4. Insert the battery terminal into the [Battery Beak](https://www.andymark.com/products/battery-beak-frc-ftc-usage) and read the values
5. The program will prompt you to enter the values you read off of the [Battery Beak](https://www.andymark.com/products/battery-beak-frc-ftc-usage)
6. You can now replace the battery with the next battery and repeat steps 2-5 for each match

## Configuration

The `config.json` file contains the following fields:
- `competition_code`: The competition code for the competition
- `year`: The year of the competition
- `number_of_batteries`: The number of batteries that will be in circulation at the competition

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
