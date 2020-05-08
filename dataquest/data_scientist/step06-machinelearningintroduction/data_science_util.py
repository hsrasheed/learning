# Necessary imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as ss
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import sklearn.model_selection as ms
from sklearn import linear_model
import sklearn.metrics as sklm

class data_science_util:
    
    def __init__(self):
        return

    # Function to test the model with the test set

    def set_fold_number(self,df,k):
        rows_per_fold = int(len(df)/k)
        df['fold'] = 1
        for i in range(0,len(df)-1):
            df.loc[i, 'fold'] = int((i+1)/rows_per_fold)+1

    def train_and_test(self,df, feature_cols, target_column,k=2):
        print("Train a test")
        total_rows = len(df)    
        if k > 2:
            # Perform k-cross-fold validation
            # Shuffle the original dataset
            # Split dataset into k parts
            # Train the model on one part, predict labels on the other part
            # Assess the error
            # Switch training and test sets and repeat
            num_folds = k
            shuffled_index = np.random.permutation(df.index)
            df = df.reindex(shuffled_index).copy()
            self.set_fold_number(df, num_folds)
            for i in range(1,num_folds+1):
                print("K-Fold validation - Test fold:"+str(i))
                #feature_cols = list(df.columns)
                if target_column in feature_cols:
                    feature_cols.remove(target_column)
                lr = LinearRegression()
                train = df.loc[df['fold'] != i].copy()
                test = df.loc[df['fold'] == i].copy()
                lr.fit(train[feature_cols],train[target_column])
                test_predictions = lr.predict(test[feature_cols])
                self.evaluate_model(test_predictions,test[target_column].to_numpy(),feature_cols)
            return   
        else:
            #perform k-cross-fold validation
            #test_rmse = 0
            return
        return

    # Functions to transform features

    def remove_missing_values(self,df,threshold=.25):
        total_rows = len(df)
        # df_null_counts is now a series with indexes of column names and values of the number of null rows in that column
        df_null_counts = df.isnull().sum()

        # get a list of all columns with between 1 and the threshold percentage of null values - these are candidates for imputing the missing values
        # columns/features that have more than the threshold percentage of null values will be dropped
        cols_to_keep = df_null_counts[(df_null_counts >= 0) & (df_null_counts < (threshold*total_rows))].index
        col_diff = len(df.columns)-len(cols_to_keep)
        print("Removing %d features because of excess null values" % col_diff)
        #print("Keeping %s " % list(cols_to_keep))
        #print(df_null_counts)
        return df[cols_to_keep]

    def impute_missing_values(self,df,threshold=.05,statistic='mode'):
        total_rows = len(df)
        df_null_counts = df.isnull().sum()
        cols_to_impute = df_null_counts[(df_null_counts > 0) & (df_null_counts < (threshold*total_rows))].copy().index
        print("Imputing values for "+str(len(cols_to_impute))+" columns")
        for col in cols_to_impute:
            if statistic == 'mode':
                df[col] = df[col].fillna(df[col].mode(),inplace=True)
            elif statistic == 'median':
                df[col] = df[col].fillna(df[col].mean(),inplace=True)
        return df

    def convert_categorical_vars(self,df):
        text_cols = df.select_dtypes(include=['object']).columns
        print(" %d features to be converted from text to categorical" % len(text_cols))
        #print(df.dtypes)
        for col in text_cols:
            cat_col = pd.Categorical(df[col])
            df[col] = cat_col.codes
        return df

    def scale_numeric_vars(self,df):
        numeric_cols = df.select_dtypes(include=['int64','float64']).columns
        print(" %d features to be scaled" % len(numeric_cols))
        #print(df.dtypes)
        for col in numeric_cols:
            col_mean = df[col].mean()
            col_range = df[col].max()-df[col].min()
            df[col] = df[col].apply(lambda x: (float(x)-col_mean)/col_range)
        return df

    def encode_categorical_cols(self,df):
        categorical_cols = df.select_dtypes(include=['category']).columns
        print(" %d categorical eatures to be encoded with one-hot encoding" % len(categorical_cols))
        dummy_cols = pd.DataFrame()
        dummy_cols = pd.get_dummies(df, columns=categorical_cols)
        return dummy_cols

    def transform_features(self,df):
        # Perform some basic feature engineering tasks on the data set:
        # 1. Remove features with more than X% missing values
        # 2. Impute values for features where fewer than Y% of the rows have mssing values
        # 3. Convert string/object data in the data frame to categorical type
        # 4. Convert cetegorical features to a one-hot encoding or dummy encoding
        print("Beginning transformation with "+str(len(df.columns))+" features/columns")
        #print(df.columns)
        new_df = self.remove_missing_values(df)
        new_df = self.impute_missing_values(new_df)
        new_df = self.scale_numeric_vars(new_df)
        new_df = self.convert_categorical_vars(new_df)
        new_df = self.encode_categorical_cols(new_df)
        #training_rows = len(new_df)*training_rate
        print("Concluding transformation with "+str(len(new_df.columns))+" features/columns")
        #print(new_df.columns)
        #return new_df[:training_rows]
        return new_df

    def train_test_split(self,df, ratio):
        total_rows = df.shape[0]
        train = df.sample(frac=ratio)
        non_selected_rows = df.index.isin(train.index)
        test = df.loc[~non_selected_rows]
        return train, test

    def print_metrics(self,y_true, y_predicted, n_parameters):
        ## First compute R^2 and the adjusted R^2
        r2 = sklm.r2_score(y_true, y_predicted)
        r2_adj = r2 - (n_parameters - 1)/(y_true.shape[0] - n_parameters) * (1 - r2)

        ## Print the usual metrics and the R^2 values
        print('Mean Square Error      = ' + str(sklm.mean_squared_error(y_true, y_predicted)))
        print('Root Mean Square Error = ' + str(math.sqrt(sklm.mean_squared_error(y_true, y_predicted))))
        print('Mean Absolute Error    = ' + str(sklm.mean_absolute_error(y_true, y_predicted)))
        print('Median Absolute Error  = ' + str(sklm.median_absolute_error(y_true, y_predicted)))
        print('R^2                    = ' + str(r2))
        print('Adjusted R^2           = ' + str(r2_adj))

    def hist_resids(self,y_test, y_score):
        ## first compute vector of residuals. 
        resids = np.subtract(y_test.reshape(-1,1), y_score.reshape(-1,1))
        ## now make the residual plots
        sns.distplot(resids)
        plt.title('Histogram of residuals')
        plt.xlabel('Residual value')
        plt.ylabel('count')
        plt.show()

    def resid_qq(self,y_test, y_score):
        ## first compute vector of residuals. 
        resids = np.subtract(y_test.reshape(-1,1), y_score.reshape(-1,1))
        ## now make the residual plots
        ss.probplot(resids.flatten(), plot = plt)
        plt.title('Residuals vs. predicted values')
        plt.xlabel('Predicted values')
        plt.ylabel('Residual')
        plt.show()

    def resid_plot(self,y_test, y_score):
        ## first compute vector of residuals. 
        resids = np.subtract(y_test.reshape(-1,1), y_score.reshape(-1,1))
        ## now make the residual plots
        sns.regplot(y_score, resids, fit_reg=False)
        plt.title('Residuals vs. predicted values')
        plt.xlabel('Predicted values')
        plt.ylabel('Residual')
        plt.show()

    def evaluate_model(self,predictions, actuals, features):
        #y_score = lin_mod.predict(x_test) 
        self.print_metrics(actuals, predictions, len(features)) 
        self.hist_resids(actuals, predictions)  
        self.resid_qq(actuals, predictions)  
        self.resid_plot(actuals, predictions) 