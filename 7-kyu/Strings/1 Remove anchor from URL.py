"""
Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
"""


def remove_url_anchor(url: str) -> str:
    if '#' not in url:
        return url
    url_index = url.index('#')
    return url[:url_index]


def remove_url_anchor_two_method(urls):
    return urls.split('#')[0]


# ['www.codewars.com/katas/', 'asdfjsdaklfj'] split bu # kadan ikkinchi list qiladi va va biz 0 chi element ni olamiz

url = "www.codewars.com/katas/#asdfjsdaklfj"
print(remove_url_anchor(url))
