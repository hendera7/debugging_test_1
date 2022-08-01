import csv

CSV_PATH = 'coffee.csv'

def open_csv(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            data_list.append(row)
    return data_list


def convert_data_to_dict(data):
    info = {
        "date": data[0],
        "open": data[1],
        "high": data[2],
        "low": data[3],
        "close": data[4],
        "volume": data[5],
        "currency": data[6]
    }
    return info


def price_range(val_a, val_b):
    if val_a > val_b:
        return round(float(val_a) - float(val_b), 2)
        # return val_a + val_b
    else:
        return round(float(val_b) - float(val_a), 2)
        # return val_b + val_a


def insert_to_dict(data_dict, price_range):
    data_dict['price_range'] = price_range
    return data_dict


def insert_to_new_csv(new_dataset, csv_name):
    with open(csv_name, 'w') as new_file:
        keys = new_dataset[0].keys()
        writer = csv.DictWriter(new_file, keys)
        writer.writeheader()
        writer.writerows(new_dataset)


if __name__ == "__main__":
    file_data = open_csv(CSV_PATH)
  
    parsed_dataset = []
    new_dataset = []
    for row in file_data:
        parsed_dataset.append(convert_data_to_dict(row))
    parsed_dataset.pop(0)

    for row in parsed_dataset:
        high = row.get('high')
        low = row.get('low')
        price_range_variable = price_range(high, low)
        new_dict = insert_to_dict(row, price_range_variable)
        new_dataset.append(new_dict)

    insert_to_new_csv(new_dataset, 'coffee_new.csv')
