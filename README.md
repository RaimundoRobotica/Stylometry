# Stylometry
Let's find out who wrote that!

This repository aims to distinguish different styles of writing from a corpus of texts of varying authorship.

The main program consists of two different classes: Text and Corpus. The Text class requires a single text from a single author (or the feature sought) and the Corpus class requires a list of Texts.

The Corpus class has several methods that help to find the best fit between a text and its author. The loading of texts can be done through the script included in read_data.py.

To test the project, 21 novels by three 19th century Spanish authors have been used: Juan Valera, Emilia Pardo Bazán and Benito Pérez Galdós.

The repository has the following folders:

- app: This folder contains a streamlit application with a simplified model. It uses the five most common words in the corpus to estimate the author of the text from simple input data. It is not yet stable.

- docs: Contains Powerpoint files for the presentation of the project.

- notebooks: Jupyter notebooks used to generate and develop the project. It contains:
  
    - The notebooks presentation, data_extraction1, data_extraction2 and test_SVM are intermediate notebooks without much relevance.
    - The notebook dataframes_generator generates and saves relevant dataframes in the folder ./data/processed.
    - The notebook models_generator generates and saves the generated models in pickle format.
    - The notebook plot generates the images and tables used in the presentation.

- src: Python scripts with the classes and functions that perform the model calculations.


The project is still under development and may have several stability or inconsistency issues.
