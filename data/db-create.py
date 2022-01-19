import sqlite3

conn = sqlite3.connect('diabetes.db')

c = conn.cursor()

try:
    c.execute('DROP TABLE Diabetes')
except Exception:
    ...

c.execute('''
    CREATE TABLE Diabetes(
        Pregnancies NUMBER,
        Glucose NUMBER,
        BloodPressure NUMBER,
        SkinThickness NUMBER,
        Insulin NUMBER,
        BMI NUMBER,
        DiabetesPedigreeFunction NUMBER,
        Age NUMBER,
        Outcome NUMBER
    );
''')

with open("diabetes.csv") as f:
    # Skip column names
    line = f.readline()
    bindings = ','.join(['?'] * len(line.split(',')))

    while True:
        line = f.readline()
        if not line:
            break
        values = line.strip().split(',')
        c.execute(f"INSERT INTO Diabetes VALUES ({bindings})", values)

conn.commit()
