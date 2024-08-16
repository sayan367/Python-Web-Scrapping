import requests
from bs4 import BeautifulSoup
from googlesearch import search

university_websites = {
    "Delhi University": "https://www.du.ac.in",
    "University of Delhi": "https://www.du.ac.in",
    "DU": "https://www.du.ac.in",
    # Add more universities to the list
}

def get_university_url(university_name):
    for name, url in university_websites.items():
        if university_name.lower() in name.lower():
            return url
    search_query = f"{university_name} course list"
    for url in search(search_query, stop=1):
        return url

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def parse_html(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        return soup
    except Exception as e:
        print(f"Error: {e}")
        return None

def extract_course_list(soup):
    course_list = []
    for table in soup.find_all(["table", "ul", "ol"]):
        for row in table.find_all(["tr", "li"]):
            cols = row.find_all(["td", "span"])
            if len(cols) > 1:
                course_list.append(cols[1].text.strip())
            else:
                course_list.append(row.text.strip())
    return course_list

def main():
    university_name = input("Enter the name of the university: ")
    url = get_university_url(university_name)

    if url is None:
        print("University not found.")
        return

    html = fetch_html(url)
    if html is None:
        return

    soup = parse_html(html)
    if soup is None:
        return

    course_list = extract_course_list(soup)
    if not course_list:
        print("No courses found.")
        return

    print("Courses offered by the university:")
    for course in course_list:
        print(course)

if __name__ == "__main__":
    main()