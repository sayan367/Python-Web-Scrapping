import requests
from bs4 import BeautifulSoup
from googlesearch import search

university_websites = {
    "Delhi University": "https://www.du.ac.in",
    "University of Delhi": "https://www.du.ac.in/index.php?page=under-graduate",
    "DU": "https://www.du.ac.in",
    # Add more universities to the list
}

def get_university_url(university_name_or_url):
    if university_name_or_url.startswith("http"):
        return university_name_or_url
    else:
        for name, url in university_websites.items():
            if university_name_or_url.lower() in name.lower():
                return url
        else:
            search_query = f"{university_name_or_url} website"
            for url in search(search_query, stop=1):
                return url

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
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
    for ul in soup.find_all("ul"):
        for li in ul.find_all("li"):
            course_list.append(li.text.strip())
    return course_list

def main():
    university_name_or_url = input("Enter the name or URL of the university: ")
    url = get_university_url(university_name_or_url)

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

    print("$$$$$$$$$$$$$$$$$$$$$$$$Courses offered by the university$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:")
    for course in course_list:
        print(course)

if __name__ == "__main__":
    main()