import requests
from bs4 import BeautifulSoup
from googlesearch import search

def get_courses_from_url(url):
    # Send a request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []
    
    # Parse the webpage content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Assuming courses are listed under <li> tags inside a specific <ul> or <div>
    # This part will need adjustment based on the actual structure of the webpage
    courses = []
    
    # Example: Extract courses from <li> elements in a <ul> with class 'course-list'
    course_list = soup.find('ul', class_='course-list')
    if course_list:
        for li in course_list.find_all('li'):
            courses.append(li.get_text(strip=True))
    else:
        print("Course list not found on the page.")
    
    return courses

def main():
    # Input from user
    url = input("Enter the URL of the college's course page: ").strip()
    
    # Get courses from the provided URL
    courses = get_courses_from_url(url)
    
    # Display the courses
    if courses:
        print("\nCourses offered:")
        for course in courses:
            print(f"- {course}")
    else:
        print("No courses found.")

if __name__ == "__main__":
    main()
