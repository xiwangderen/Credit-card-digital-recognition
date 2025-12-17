import cv2

def sort_contours(cnts, method="left-to-right"):
    reverse = False # reverse：要不要反过来排？
    i = 0 # i = 0 → 用 x 坐标 i = 1 → 用 y 坐标

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    # boundingBoxes的结构
    # [
    # (x0, y0, w0, h0),
    # (x1, y1, w1, h1),
    # (x2, y2, w2, h2),
    # ...
    # ]
    boundingBoxes = [cv2.boundingRect(c) for c in cnts] #用一个最小的矩形，把找到的形状包起来x,y,h,w
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    return cnts, boundingBoxes

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized