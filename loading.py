###Imports
import pandas as pd

###Constants


###Main function
def main_loading(run_loading=False):
    if run_loading:
        # call the function collect_data to get the abstracts
        abstracts = pd.read_csv("arxiv-paper-titles-data-abstracts.csv",
                                header=None,
                                names=["article_ID", "title", "publication_date",
                                       "author", "text"])

        # construction of df_abstracts
        df_abstracts = abstracts[['article_ID', 'title', 'text', 'publication_date', 'author']]

        # save abstracts
        df_abstracts.to_csv('./data/corpus.csv', index=None)
    return
