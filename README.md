# Python Web Scraping Script For Pokémon Data Analysis And "Catch Rate" Prediction Models.

## A functional script featuring automated Selenium web driver for obtaining Pokemon attributes from bulbapedia.bulbagarden.net. Whole code contains 3 jupyter notebooks for Pandas data cleaning and Seaborn plots, Keras neural network and Scikit-learn SVM and Random Forest regression models.

This project was created to feed my passion for Pokémon. I wanted to do something of my own with these creatures, as it took a lot of time from my childhood to play these games. There is much more to add, like a tableau/Power BI dashboard that I'm working on and optimizing the model to produce even better predictions.

**How it works**
  1. Running the Scraper.py script collects data from all, 1025 currently available Pokémon and saves it to a CSV file in your workspace. Abilities.py is another scraping script, but it was needed for obtaining a list of all Pokémon abilities to better clean data in the next step
  2. The first step uses utlis.py, which has all the functions for collecting data and a selenium driver set up. All of them use paths.json which is essential and was time-consuming to create as it contains all the XPaths for each Pokémon attribute, and they change from page to page, so the XPaths were meticulously made to be universal for each of the 1025 pages.
  3. Next, the data_cleaning notebook is used to extract all the information from this dataset in a readable form.
  4. Model and SVR & RFR notebooks are for playing with the data science side of this data and applying principles I learned from a machine learning course to predict the catch rate of a Pokémon.
