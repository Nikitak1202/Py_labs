import cv2
import numpy as np


def task1():
    img = cv2.imread('variant-1.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original Image', img)
    cv2.imshow('Gray Image', gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def task23():
  cap = cv2.VideoCapture(1)
  down_points = (640, 480)

  while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 9, 75, 75)
    ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    contours, h = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        for contour in contours:
          area = cv2.contourArea(contour)
          if 2015 < area < 4694:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            coords = 'x: {}, y:{}'
            cv2.putText(frame, coords.format(x + (w // 2), y + (h // 2)), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
            
          
    cv2.imshow('frame', frame)
    cv2.imshow('mask', thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  cv2.destroyAllWindows()


task1()
task23()