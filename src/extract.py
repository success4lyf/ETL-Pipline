import pandas as pd

class Extract():
    def __init__(self, headerlist):
        self.headerlist = headerlist

    def insert_header(self):
        df = pd.read_csv('data/chesterfield_25-08-2021_09-00-00.csv')
        df.to_csv('data/extracted_chesterfield_data.csv', header=self.headerlist, index=False)

    def extract_data(self):
        new_df = pd.read_csv('data/extracted_chesterfield_data.csv')
        print(new_df)

headerlist = [
    "Timestamp of Purchase", 
    "Store Name", 
    "Customer Name", 
    "Basket Items (Name, Size & Price)", 
    "Total Price", 
    "Cash/Card", 
    "Card Number (Empty if Cash)"
    ]

if __name__ == '__main__':
    obj = Extract(headerlist)
    obj.insert_header()
    obj.extract_data()