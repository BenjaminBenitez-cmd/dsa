import codecs
import os
from pythonds.basic import Stack


dir = os.path.dirname(__file__)

# validateHTML function uses a stack to easily keep track of open and closing
# html tags


def validateHTML(file):
    filePath = dir + file

    with codecs.open(filePath, 'r', 'utf-8') as fp:
        line = fp.readline()
        tags = Stack()
        res = True

        while line and res != False:
            item = line.strip()
            count = 0
            word = ""
            while count < len(item):
                if item[count] == "<":
                    word = word + item[count]
                elif item[count] == ">":
                    word = word + item[count]

                    if word.startswith("</"):
                        compword = tags.pop()

                        compword = compword[1:]
                        word = word[2:]
                        if compword != word:
                            res = False
                    else:
                        tags.push(word)

                    word = ""
                elif len(word) > 0 and item[count] != " ":
                    word = word + item[count]

                count = count + 1

            line = fp.readline()

        return res


print(validateHTML("/index.html"))
