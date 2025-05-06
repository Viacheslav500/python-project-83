from bs4 import BeautifulSoup
import requests


def parse_page_content(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        return {
                'title': (
                        soup.find('title').text 
                        if soup.find('title') 
                        else None
                        ),
                'h1': soup.find('h1').text if soup.find('h1') else None,
                'description': (
                    soup.find('meta', attrs={'name': 'description'})['content']
                    if soup.find('meta', attrs={'name': 'description'}) 
                    else None
                    ),
                }
    except Exception:
        return None


def fetch_and_parse_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.content
        parsed_data = parse_page_content(html_content)
        return {
            **parsed_data,
            'status_code': response.status_code
            } if parsed_data else {'error': 'Произошла ошибка при проверке'}
    except requests.RequestException:
        return {'error': 'Произошла ошибка при проверке'}
