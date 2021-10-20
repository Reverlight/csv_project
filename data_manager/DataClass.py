class ColumnClass():
    # Date
    # Full name
    # Job
    # Phone
    # Email
    def __init__(self, column_name, type_name, order):
        self.column_name = column_name
        self.type_name = type_name
        self.order = order


class ColumnsClass():
    def __init__(self, columns):
        self.columns = sorted(columns, key=lambda i: i.order)
        self.type_names = []
        self.column_names = []
        self.orders = []

        for i in self.columns:
            self.type_names.append(i.type_name)
            self.column_names.append(i.column_name)
            self.orders.append(i.order)
