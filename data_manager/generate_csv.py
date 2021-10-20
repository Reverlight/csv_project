import csv
from data_manager.generate_values import gen_data


def write_csv2(filename, columns, quantity):
    with open(filename + '', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns.column_names)
        for _ in range(quantity):
            row_items = []
            for type in columns.type_names:
                row_item = gen_data(type)
                row_items.append(row_item)
            writer.writerow(row_items)
