# FSO
## Getting Started (Continued)

2. Prerequisites:
   - Python (3.x recommended)
   - Jupyter Notebook
   - Required Python libraries: pandas, scikit-learn, and matplotlib (install using pip or conda)

3. Open and run the Jupyter Notebook:
   - Launch Jupyter Notebook in the project directory:
     ```bash
     jupyter notebook
     ```
   - Open the `free-space-optical-communication.ipynb` notebook and follow the code to train and evaluate the linear regression model.

## Data

The dataset is stored in the `Dataset/` directory. You should replace the placeholder dataset file with your own data. Ensure that the data is in a CSV format with columns "Visibility Range," "SNR," and "Power."

## Model Training

The Jupyter Notebook contains Python code for:
- Data loading and preprocessing.
- Model selection and training (linear regression).
- Model evaluation using Mean Squared Error (MSE).

## FSO and Power Prediction

Free-Space Optical (FSO) communication is a technology that utilizes optical light to transmit data through the atmosphere. In an FSO system, various factors, including visibility range and SNR, can significantly impact the received power levels. This project aims to build a predictive model to estimate the power levels based on these influential factors. By accurately predicting power levels, FSO system operators can optimize network performance and reliability.

## Results

The model's performance is evaluated using the Mean Squared Error (MSE) metric. A very low MSE indicates a strong fit between the predicted "Power" values and the actual data.


## Acknowledgment

- Under Faculty Dr. Sasithra Anbalagan and Sowmyaa Vathsan .

## Author

- [KumaR Shivam](https://github.com/KumarShivam1908)

Feel free to customize this README with additional sections, explanations, and any other relevant information specific to your project. If you have any more specific details or sections you'd like to add, please let me know, and I'd be happy to assist further.
