import matplotlib.pyplot as plt


def generate_figures():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'sample_data.csv')
    df = load_data(data_path)

    # Example: plot the first two columns if they exist
    if df.shape[1] >= 2:
        plt.figure(figsize=(8, 5))
        plt.plot(df.iloc[:, 0], df.iloc[:, 1], marker='o')
        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])
        plt.title('Sample Data Plot')
        plt.tight_layout()
        fig_path = os.path.join(os.path.dirname(__file__), 'sample_figure.png')
        plt.savefig(fig_path)
        plt.close()
        print(f"Figure saved to {fig_path}")
        print("Not enough columns to plot.")

#if __name__ == "__main__":
#    generate_figures()