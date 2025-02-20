import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

# Function to extract faculty data from karachi's website
import requests
from bs4 import BeautifulSoup


def extract_cfd_faculty_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    all_data = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    serial_number = 152
    departments_tag = soup.find('div', class_='kc-elm kc-css-633007 kc_row kc_row_inner')
    departments = departments_tag.find_all('div', class_='kc_col-sm-3')
    for dept in departments:
        department_name = dept.find('div', class_='content-desc').text.strip()
        department_link = dept.find('a')['href']
        response_inner = requests.get(department_link, headers=headers)
        faculty = BeautifulSoup(response_inner.text, 'html.parser')
        faculty_cards = faculty.find_all('div', class_="col-md-3 col-sm-6 col-xs-12")
        for card in faculty_cards:
            try:
                # Extract profile page link
                profile_link_tag = card.find('a', href=True)
                profile_link = profile_link_tag['href'] if profile_link_tag else 'N/A'
                response_inner_inner = requests.get(profile_link, headers=headers)
                profile = BeautifulSoup(response_inner_inner.text, 'html.parser')
                # Find the <li> containing the <span> with text "Ext:"
                teacher_address = profile.find('ul', class_='teacher__address')
                # Find the <li> where <span> contains "Ext:"
                ext_li = teacher_address.find_all('li')
                print(profile_link)

                # Extract the extension number by removing "Ext:" text
                extension = ext_li[3].get_text(strip=True).replace("Ext:", "").strip() if ext_li[3] else 'N/A'
                education = 'N/A'
                education_tag = profile.find('div', class_='htc__skill__container progress__bar--2')
                education = 'N/A'
                if education_tag.find('p'):
                    education = education_tag.find_all('p')[0].text
                if education_tag.find('li'):
                    education = education_tag.find_all('li')[0].text

                education = education.replace("\n", " ").strip()
                # Extract image URL
                image_tag = card.find('img')
                image_url = image_tag['src'] if image_tag else 'N/A'

                # Extract name
                name_tag = card.find('h4')
                name = name_tag.text.strip() if name_tag else 'N/A'

                # Extract designation
                designation_tag = card.find('h6')
                designation = designation_tag.text.strip() if designation_tag else 'N/A'

                # Check for HEC approval
                hec_approved = 'HEC approved PhD Supervisor' in card.text

                # Extract email
                email_tag = card.find('p')
                email = email_tag.text.strip() if email_tag else 'N/A'
                # Store extracted data
                all_data.append({
                    'ID': serial_number,
                    'Name': name,
                    'Designation': designation,
                    'HEC Approved PhD Supervisor': hec_approved,
                    'Highest Education': education,  # Needs separate extraction from profile page
                    'Email': email,
                    'Department': department_name,
                    'Extension': extension,
                    'ImageURL': image_url,
                })
                serial_number += 1

            except Exception as e:
                print(f"Error processing faculty card: {e}")
                continue

    return all_data


def save_csv(dataframe, name):
    # Clean and format data
    dataframe['HEC Approved PhD Supervisor'] = dataframe['HEC Approved PhD Supervisor'].astype(bool)
    dataframe['Extension'] = dataframe['Extension'].astype(int)
    dataframe['ID'] = dataframe['ID'].astype(int)
    dataframe = dataframe.drop_duplicates().reset_index(drop=True)
    dataframe.to_csv(name, index=False)


# Main execution
url = "https://cfd.nu.edu.pk/all-departments/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    faculty_data = extract_cfd_faculty_data(response.text)
    df = pd.DataFrame(faculty_data)

    # Clean and format data

    df['HEC Approved PhD Supervisor'] = df['HEC Approved PhD Supervisor'].astype(bool)
    df = df.drop_duplicates().reset_index(drop=True)

    print(f"Scraped {len(df)} faculty members from {df['Department'].nunique()} departments")
    print("Departments found:", df['Department'].unique())

    # Save to CSV
    df.to_csv('nu_faculty_data.csv', index=False)
    print("Data saved to nu_faculty_data.csv")

else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
