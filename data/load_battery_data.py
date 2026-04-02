import scipy.io
import pandas as pd
import os

def load_battery_data(mat_file):
    data = scipy.io.loadmat(mat_file)

    battery = data['B0005'][0][0][0][0]  # structure access

    records = []

    for cycle in battery:
        if cycle[0][0] == 'discharge':
            data_block = cycle[3][0][0]

            temp = data_block[0][0]
            voltage = data_block[1][0]
            current = data_block[2][0]
            time = data_block[5][0]

            for i in range(len(temp)):
                records.append({
                    "temperature": temp[i],
                    "voltage": voltage[i],
                    "current": current[i],
                    "time": time[i]
                })

    df = pd.DataFrame(records)
    return df


if __name__ == "__main__":
    df = load_battery_data("data/B0005.mat")

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/battery_data.csv", index=False)

    print("✅ Converted to CSV!")
    print(df.head())