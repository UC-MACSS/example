import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def process_data(data):
    '''
    Input: CSV filename (str)
    Returns: Pandas DataFrame (processed and ready to analyze)
    '''
    df = pd.read_csv(data)
    return df

def plot(data, save_fig=False, path="./figure1.tiff"):
    '''
    Input: `data`: Pandas DataFrame with two columns of data (float64),
           `save_fig`: bool indicating whether to save figure to file (tiff)
           `path`: string indicating path for saving figure if `save_fig` is
                   True (defaults to "figure1.tiff" in working directory)
    Returns: Nothing (produces plot and optionally saves to file)
    '''
    sns.lmplot(x="column1",
               y="column2",
               data=data)
    plt.title("Column 2 vs. Column 1")

    if save_fig:
        plt.savefig(path,
                    dpi=300,
                    format="tiff",
                    bbox_inches="tight",
                    pil_kwargs={"compression": "tiff_lzw"})

if __name__ == "__main__":
    # When running script in Docker Container, save figure to /figures/
    # directory
    df = process_data("data.csv")
    plot(data=df, save_fig=True, path="/figures/figure1.tiff")
