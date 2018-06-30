import pandas as pd


def azureml_main(dataframe1 = None, dataframe2 = None):

	frames = [dataframe1, dataframe2]
	result = pd.concat(frames)
    return result

def insert_year(df, year):
	df['Year'] = year
	return df


num_cols = ["Dystopia Residual", "Economy (GDP per Capita)", "Family", "Freedom", "Generosity",
            "Health (Life Expectancy)", "Trust (Government Corruption)"] 
           
def happy_scatter(df, cols):
    import matplotlib.pyplot as plt
    import statsmodels.nonparametric.smoothers_lowess as lw
    
    ## Loop over the columns and create the scatter plots
    for col in cols:
        ## first compute a lowess fit to the data
        los = lw.lowess(df['Happiness Score'], df[col], frac = 0.3)
    
        ## Now make the plots
        fig = plt.figure(figsize=(8, 6))
        fig.clf()
        ax = fig.gca()
        df.plot(kind = 'scatter', x = col, y = 'Happiness Score', ax = ax, alpha = 0.05)
        plt.plot(los[:, 0], los[:, 1], axes = ax, color = 'red')
        ax.set_xlabel(col)
        ax.set_ylabel('Happiness Score')
        ax.set_title('Happiness Score vs. ' + col)    
    return 'Done' 



def pct_of_happiness_score(df, cols):
    
    for col in cols:
        df[col] = df[col] / df['Happiness Score']
    
    return 'Done'

pct_of_happiness_score(frame, num_cols)