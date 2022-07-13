# BotArchitecture
 Crypto Trading Bot Architecture


 # Price prediction folder
 Multiple ML price prediction algos predicting price for multiple time intervals, working in parallel.

 structure:
 1) Data streaming algo uploads data to a cloud sql database.
 3) Data transformation algo, transforming the data so that its readable for ML algos.
 4) ML algos reading the transformed data and predicting the price.
 5) Execution Bot sends the prediction to the user -> trade gets executed.

 ## 1 minute price prediction ML algo

 Binary tree of ML classifiers to approximate probability distribution over future, instantaneous price changes.

 ## 10 minute price prediction ML algo

 LSTM model to predict price changes over 10 minutes.
