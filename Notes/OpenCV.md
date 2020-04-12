[Reference](https://pythonprogramming.net/loading-images-python-opencv-tutorial/)
[Sentdex](https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ) is amazing

## 1 - Read, show and write an image in Open CV

```python
import cv2

img = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Dog', img)
cv2.imwrite('SaveDog.jpg', img)
```

IMREAD_GRAYSCALE -> read in grayscale
IMREAD_COLOR -> read in color (requires lot of processing)

## 2 - Reading web cam video

```python
import cv2

# Number represents the web cam ID
video = cv2.VideoCapture(0)

while True:
    # ret: returns 1 if feed is available else 0
    # frame: returns the frame captured
    ret, frame = video.read()
    cv2.imshow('frame', frame)

    # To break the loop on pressing q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
```
