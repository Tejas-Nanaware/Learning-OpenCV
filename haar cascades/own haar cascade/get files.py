import urllib.request
import cv2
import numpy as np
import os
print("Hi")
def store_raw_images():
    print("getting url")
	# neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00007846'
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    print("Got URL")
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 1
    print(pic_num)
    if not os.path.exists('neg'):
        os.makedirs('neg')
        print("made dir")
    for i in neg_image_urls.split('\n'):
        try:
            print(str(pic_num) + "\t" + i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (500, 500))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))

store_raw_images()