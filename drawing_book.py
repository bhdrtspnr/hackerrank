

def searchForward(numberOfPages, targetPage):
    if targetPage==1:
        return 0
    else:
        return int(targetPage/2)

def searchBackward(numberOfPages, targetPage):
    if targetPage==numberOfPages or targetPage==numberOfPages-1:
        return 0
    else:
        return (n-1)-int(targetPage/2)


def pageCount(numberOfPages, targetPage):
    backward = searchBackward(numberOfPages,targetPage)
    forward = searchForward(numberOfPages,targetPage)

    if forward <= backward:
        return forward
    else:
        return backward
    


if __name__ == '__main__':
    print(searchForward(5,4))