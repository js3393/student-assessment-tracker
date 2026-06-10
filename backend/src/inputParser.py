from pathlib import Path
import csv
import json

class InputParser:
    def __init__(self):
        pass

    @staticmethod
    def csv_to_json(self, file_location, output_file):
        try:
            with open(file_location, mode='r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                with open(output_file, mode='w', encoding='utf-8') as json_file:
                    for row in csv_reader:
                        #Take each line and write as JSON object
                        json_file.write(json.dumps(row) + '\n')
        except FileNotFoundError:
            print("File not found. Try again")
        except PermissionError:
            print("Error: You do not have permission to read this file.")
        except Exception as e:
            print(f"An unexpected error has occurred: {e}")
