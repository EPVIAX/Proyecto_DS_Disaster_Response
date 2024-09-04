import pandas as pd

df = pd.read_csv('disaster_categories.csv')
print(df.columns)
def suma(a,b):
    return a+b

def main():
    res = suma(3,4)
    print(res)

if __name__ == '__main__':
    main()