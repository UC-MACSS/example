import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def process_data(data):
    '''
    Input: CSV filename (str)
    Returns: Pandas DataFrame (processed and ready to analyze)
    '''
    df = pd.read_csv("data.csv")
    return df

def plot(data, save_fig=False):
    '''
    Input: `data`: Pandas DataFrame with two columns of data (float64),
           `save_fig`: bool indicating whether to save figure to file or not
    Returns: Nothing (produces plot and optionally saves to file)
    '''
    sns.lmplot(x="column1",
               y="column2",
               data=data)
    plt.title("Column 2 vs. Column 1")

    if save_fig:
        plt.savefig("/figures/figure1.tiff",
                    dpi=300,
                    format="tiff",
                    bbox_inches="tight",
                    pil_kwargs={"compression": "tiff_lzw"})

if __name__ == "__main__":
    df = process_data('data.csv')
    plot(data=df, save_fig=True)
