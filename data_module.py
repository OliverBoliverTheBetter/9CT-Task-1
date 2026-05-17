import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def DisplayData():
    thedisplay = pd.read_csv('Responses_thebest.csv')
    print(thedisplay)

def VisualiseData():
    df = pd.read_csv("Responses_thebest.csv")
    categories = []
    for col in df.columns:
        if col.upper().endswith(" PRE"):
            category = col[:-4]
            post_col = category + " POST"
            if post_col in df.columns:
                categories.append(category)
    pre_means = []
    post_means = []
    for category in categories:
        pre_col = category + " PRE"
        post_col = category + " POST"
        pre_means.append(df[pre_col].mean())
        post_means.append(df[post_col].mean())
    x = np.arange(len(categories))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, pre_means, width, label="PRE")
    ax.bar(x + width/2, post_means, width, label="POST")
    ax.set_title("Average PRE vs POST Scores")
    ax.set_ylabel("Average Score")
    ax.set_xticks(x)
    ax.set_xticklabels([c.title() for c in categories])
    ax.legend()
    plt.tight_layout()
    plt.show()

#testing area
