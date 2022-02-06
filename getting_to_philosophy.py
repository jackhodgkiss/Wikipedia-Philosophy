import requests
import sys
from bs4 import BeautifulSoup

base_url = "https://en.wikipedia.org"
departure = "/wiki/J/22"
destination = "/wiki/Philosophy"
visited = [departure]
unwanted_elements = ["https", "http", "#", ".php",
                     ":", "(disambiguation)", "wikimedia"]


def getting_to_philosophy():
    """ Travel through wikipedia in search of Philosophy.

    Achieved by searching the current article for anchor tags and their
    respected href attributes. Then by process of elimination picking the next
    article to visit until destination (/wiki/Philosophy) has been reached.

    The first page is scraped outside of a while loop however once the
    departure page is finished with the page a while loop is used to keep
    checking if the destination has been visited.
    """

    # Fetch the desired page and its contents.
    response = get_page(departure)
    # Turn the content into soup using the html parser.
    soup = soupify_page(response.content)
    # Find the section of the page that is just the article.
    article = get_article(soup)
    # Find all of the paragraphs within the article
    paragraphs = get_paragraphs(article)
    # Find all of the anchor tags within the paragraphs found above.
    anchors = get_anchors(paragraphs)
    # Get all of the desired links.
    links = get_links(anchors)

    while destination not in visited:
        # Find the next link on the current page that hasn't be visited.
        next_article = next((link for link in links if link not in visited),
                            None)
        # If there is no viable link exit and tell the user of this issue.
        if next_article is None:
            sys.exit("Wikipedia article: {}, "
                     "contains no viable links".format(
                        soup.find("h1", id="firstHeading").text))

        print("Visiting: {}".format(next_article))

        response = get_page(next_article)

        soup = soupify_page(response.content)

        article = get_article(soup)

        paragraphs = get_paragraphs(article)

        anchors = get_anchors(paragraphs)

        links = get_links(anchors)

        visited.append(next_article)


def get_page(url):
    """ Make a single request for wikipedia article to be returned.

    Args:
        url: A string defining the url of the wanted wikipedia article.

    Returns:
        response: A requests object containing the content of the http request.
    """
    return requests.get(base_url + url)


def soupify_page(content):
    """ Create and returns and BeautifulSoup object using the supplied article.

    Args:
        content: Container with the content of retrieved wikipedia article.

    Returns:
        soup: A BeautifulSoup object is supplied back.
    """
    return BeautifulSoup(content, "html.parser")


def get_article(soup):
    """ Get the article contained within the wikipedia page.

    Args:
        soup: BeautifulSoup object with the required wikipedia article within.

    Returns:
        article: A BeautifulSoup Tag object containing the article.
    """
    return soup.find("div", id="bodyContent")


def get_paragraphs(article):
    """ Get all of the paragraphs contained within the article.

    Args:
        article: BeautifulSoup Tag object containing the desired paragraphs.

    Returns:
        paragraphs: A list of paragraphs (p tags) are sent back.
    """
    return article.find_all("p")


def get_anchors(paragraphs):
    """ Get all of the anchors within the article's paragraph.

    Args:
        paragraphs: List of paragraphs (p tags) containing anchors (a tags)

    Returns:
        anchors: A list all anchors found within paragraphs.
    """
    return [paragraph.find_all("a") for paragraph in paragraphs]


def get_links(anchors):
    """ Create a list of links that meet a series of requirements.

    Args:
        anchors: List of anchors found within the current page paragraphs

    Returns:
        links: A list of links (String) found within that are acceptable.
    """
    links = [link.get("href") for link in
             [anchor for sublist in anchors for anchor in sublist]
             if link.parent.get("id") != "coordinates" and link.text.islower()]

    for link in list(links):
        for element in unwanted_elements:
            if element in link:
                links.remove(link)
                break

    return links

if __name__ == "__main__":
    if len(sys.argv) > 1:
        departure = sys.argv[1]  # If the user has supplied a page use it.
    getting_to_philosophy()
