from datetime import datetime

# function to format date
def format_date(date):
    return date.strftime('%m/%d/%y')

# test 
# print(format_date(datetime.now()))


# function to format URL 
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]


# test 
# print(format_url('http://google.com/test/'))
# print(format_url('https://www.google.com?q=test'))


# pluralize filter
def format_plural(amount, word):
    if amount != 1:
        return word + 's'
    return word

# test 
# print(format_plural(2, 'cat'))
# print(format_plural(1, 'dog'))

