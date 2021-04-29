from PIL import Image
import numpy as np

image_path = 'original.png'

# skin
new_rbg = [9,113,44,255]
original_rgb = [88,148,55,255]

def main():
    img = read_image(image_path)
    new_img = convert(img)

    new_img.save("new.png")

def read_image(path):
    try:
        image = Image.open(path)
        return image
    except Exception as e:
        print(e)

def convert(image):
    arr = np.array(image)
    acceptable_values = get_acceptable_values(new_rbg, 50)

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            pixel = np.array(arr[i][j])

            recolor = True
            for k in range(0, len(pixel)):
                if pixel[k] not in acceptable_values[k]:
                    recolor = False
            
            if recolor:
                arr[i][j] = new_rbg

    return Image.fromarray(arr)

def get_acceptable_values(primary_color, threshold):
    list_of_acceptable_rgb_values = []
    for i in range(0, len(primary_color)):
        acceptable_rgb_values = list(range(primary_color[i] - threshold, primary_color[i] + threshold))
        list_of_acceptable_rgb_values.append(acceptable_rgb_values)
    return list_of_acceptable_rgb_values

if __name__ == "__main__":
    main()