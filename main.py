def get_robots_txt(client: httpx.Client, target: str, response: str) -> None:
    """Check link for Robot.txt, and if found, add link to robots dataset.

    Args:
        target (str): URL to be checked.
        response (object): Response object containing data to check.
    """
    cprint("[*]Checking for Robots.txt", "yellow")
    url = target
    target = "{0.scheme}://{0.netloc}/".format(urlsplit(url))#good
    client.get(target + "robots.txt")
    print(target + "robots.txt")
    matches = re.findall(r"Allow: (.*)|Disallow: (.*)", response)
    for match in matches:
        match = "".join(match)
        if "*" not in match:
            url = target + match
            robots.add(url)
        cprint("Robots.txt found", "blue")
        print(robots)
#yes
  def display_webpage_description(soup: BeautifulSoup) -> None:
    """Print all meta tags found in page.

    Args:
        soup (object): Processed HTML object.
    """
    cprint("[*]Checking for meta tag", "yellow")
    metatags = soup.find_all("meta")
    for meta in metatags:
        print("Meta : ", meta)
