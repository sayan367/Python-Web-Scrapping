import requests
from bs4 import BeautifulSoup
from googlesearch import search

# Dictionary to store university names and their corresponding websites
university_websites = {
    "Delhi University": "https://www.du.ac.in",
    "University of Delhi": "https://www.du.ac.in/index.php?page=under-graduate",
    "DU": "https://www.du.ac.in",
    # Add more universities to the list
}

def get_university_url(university_name_or_url):
    """
    This function takes a university name or URL as input and returns the corresponding URL.
    
    If the input is a URL, it returns the URL as is.
    If the input is a university name, it checks if the name is in the dictionary and returns the corresponding URL.
    If the university is not found in the dictionary, it searches for the university website using Google search.
    """
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
    """
    This function takes a URL as input and returns the HTML content of the webpage.
    
    It uses the requests library to send a GET request to the URL and returns the response content.
    If an error occurs, it prints the error message and returns None.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def parse_html(html):
    """
    This function takes HTML content as input and returns a BeautifulSoup object.
    
    It uses the BeautifulSoup library to parse the HTML content and returns the parsed object.
    If an error occurs, it prints the error message and returns None.
    """
    try:
        soup = BeautifulSoup(html, "html.parser")
        return soup
    except Exception as e:
        print(f"Error: {e}")
        return None

def extract_course_list(soup):
    """
    This function takes a BeautifulSoup object as input and returns a list of courses.
    
    It finds all unordered lists (ul) in the HTML and extracts the text from each list item (li).
    """
    course_list = []
    for ul in soup.find_all("ul"):
        for li in ul.find_all("li"):
            course_list.append(li.text.strip())
    return course_list

def main():
    """
    This is the main function that takes user input and calls the other functions to extract the course list.
    """
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