import re
import random
import string
from unidecode import unidecode
from .models import URL_IMAGE_THUMBNAIL_BLOG_DEFAULT
from .localized import *


def removeAllSpecialCharacters(string):
    regexString = r'[^A-Za-z0-9\s]+'
    string = re.sub(regexString, '', string)
    return string


def randomStringAndNumber(lengthNumber):
    letters = string.ascii_letters + string.digits
    stringRandom = ''.join(random.choice(letters) for i in range(lengthNumber))
    return stringRandom


def createURLFromTitleBlog(titleBlog):

    title_URL = titleBlog

    title_URL = unidecode(title_URL)
    title_URL = title_URL.replace('-', ' ')

    title_URL = removeAllSpecialCharacters(title_URL)

    title_URL = " ".join(re.split("\s+", title_URL, flags=re.UNICODE))
    title_URL = re.sub("^\s+|\s+$", "", title_URL, flags=re.UNICODE)

    title_URL = title_URL.replace(' ', '-')
    if len(title_URL) != 0:
        title_URL += '-'
    # create random string

    title_URL += randomStringAndNumber(LENGTH_STRING_RANDOM_FOR_URL)
    return title_URL


def getFirstImageInContentBlog(inputContent):
    imageTagRegex = '<img.*?src="(.*?)"[^>]+>'
    listImageSrc = re.findall(imageTagRegex, inputContent)
    if len(listImageSrc):
        firstURL = listImageSrc[0]
        return firstURL[firstURL.index('uploads'):]
    else:
        return URL_IMAGE_THUMBNAIL_BLOG_DEFAULT
