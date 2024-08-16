import requests
from bs4 import BeautifulSoup

def get_college_url(college_name):
    return f"{college_name}"

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
    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) > 1:
                course_list.append(cols[1].text.strip())
    return course_list

def main():
    college_input = input("Enter the name of the college or its URL: ")

    if "http" in college_input:
        url = college_input
    else:
        college_name = college_input
        url = get_college_url(college_name)

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

    print("$$$$$$$$$$$$$$$$$$$$$$$Courses offered by the college$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:")
    for course in course_list:
        print(course)

if __name__ == "__main__":
    main()