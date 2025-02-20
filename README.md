# Web Scraping - FAST Faculty Data Collection

## Overview
This Jupyter Notebook project automates the process of extracting faculty member data from different campuses of FAST-NU. The extracted data includes details such as faculty ID, name, designation, highest education, and contact information. The final dataset is saved in structured CSV files for further analysis.

## Data Sources
The notebook scrapes faculty data from the following FAST-NU campus websites:
- **Lahore**: [http://lhr.nu.edu.pk/faculty/](http://lhr.nu.edu.pk/faculty/)
- **Islamabad**: [http://isb.nu.edu.pk/Faculty/allfaculty/](http://isb.nu.edu.pk/Faculty/allfaculty/)
- **Karachi**: [https://khi.nu.edu.pk/faculty-php/](https://khi.nu.edu.pk/faculty-php/)
- **Chiniot-Faisalabad (CFD)**: [https://cfd.nu.edu.pk/all-departments/](https://cfd.nu.edu.pk/all-departments/)
- **Peshawar**: [http://pwr.nu.edu.pk/](http://pwr.nu.edu.pk/)

## Extracted Data Fields
The script collects the following details for each faculty member:
| Field | Description |
|--------|---------------------------------|
| ID | Unique identifier for the faculty member |
| Name | Full name including title |
| Designation | Faculty rank (e.g., Professor, Lecturer) |
| HEC Approved PhD Supervisor | Boolean indicating if the faculty is an HEC-approved PhD supervisor |
| Highest Education | Faculty's highest qualification |
| Email | Contact email address |
| Department | Faculty's department name |
| Extension | Office extension number |
| ImageURL | Profile image URL |

## Steps Performed in the Notebook
### Step 1: Web Scraping
1. Identify the structure of faculty pages across different FAST-NU campuses.
2. Extract faculty details for each department and each campus.
3. Save the extracted data as CSV files (`lhr.csv`, `isb.csv`, `khi.csv`, etc.).

### Step 2: Data Consolidation
1. Load all campus CSV files into data frames.
2. Concatenate all data frames into a single dataset.
3. Save the final consolidated dataset as `fast_faculty.csv`.

## Technologies Used
- **Python**: Core programming language
- **Requests**: To fetch webpage content
- **BeautifulSoup**: For HTML parsing and data extraction
- **Pandas**: For data handling and CSV file operations
- **Jupyter Notebook**: Interactive development environment

## Ethical Considerations
- This project strictly adheres to ethical web scraping practices.
- The extracted data is used solely for academic purposes.
- The terms of use of the websites have been reviewed to ensure compliance.

## How to Use
1. Open the Jupyter Notebook.
2. Run the notebook cells sequentially.
3. The scraped data will be saved as CSV files.
4. Use the consolidated dataset for further analysis or reporting.

## Future Enhancements
- Automate scraping for real-time faculty updates.
- Implement error handling for dynamic webpage structures.
- Develop a dashboard for visualizing faculty statistics.

For any questions or contributions, feel free to reach out!

---
🚀 Happy Scraping!

