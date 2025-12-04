import matplotlib.pyplot as plt

def create_dashboard(daily, weekly, df):
    fig, axs = plt.subplots(3, 1, figsize=(12, 14))

    axs[0].plot(daily['timestamp'], daily['kwh'])
    axs[0].set_title("Daily Electricity Consumption")

    axs[1].bar(weekly['timestamp'], weekly['kwh'])
    axs[1].set_title("Weekly Electricity Consumption")

    axs[2].scatter(df['timestamp'], df['kwh'])
    axs[2].set_title("Scatter Plot of All Readings")

    plt.tight_layout()
    plt.savefig("output/dashboard.png")
    plt.close()
