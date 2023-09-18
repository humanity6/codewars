import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

# test cases

print(domain_name("http://google.com"))
print(domain_name("http://bingchillin.co.jp"))