import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def change_brightness(image, value):
    return np.clip(image+value, 0, 255)

def change_contrast(image, value):
    new_img = image.copy()
    factor = (259 * (value + 255)) / (255 * (259 - value))
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            for color_channel in range(3):
                new_img[row, col, color_channel] = int(factor * (image[row, col, color_channel] - 128) + 128)
    return np.clip(new_img, 0, 255)


def grayscale(image):
    new_img = image.copy()
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            r, g, b = image[row, col]
            gray_value = int(0.3 * r + 0.59 * g + 0.11 * b)
            new_img[row, col] = [gray_value] * 3
    return new_img


def blur_effect(image):
    new_img = image.copy()
    kernel = np.array([[0.0625, 0.125, 0.0625],
                       [0.125, 0.25, 0.125],
                       [0.0625, 0.125, 0.0625]])
    for row in range(1, image.shape[0] - 1):
        for col in range(1, image.shape[1] - 1):
            for color_channel in range(3):
                sub_matrix = image[row - 1:row + 2, col - 1:col + 2, color_channel]
                new_img[row, col, color_channel] = np.sum(sub_matrix * kernel)
    return new_img


def edge_detection(image):
    new_img = image.copy()
    kernel = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])
    for row in range(1, image.shape[0] - 1):
        for col in range(1, image.shape[1] - 1):
            for color_channel in range(3):
                sub_matrix = image[row - 1:row + 2, col - 1:col + 2, color_channel]
                detected_value = np.sum(sub_matrix * kernel)
                new_img[row, col, color_channel] = detected_value + 128
                # if 0 <= detected_value + 128 <= 255 else 0 if detected_value + 128 < 0 else 255
    return np.clip(new_img, 0, 255)

def embossed(image):
    new_img = image.copy()
    kernel = np.array([[-1, -1, 0],
                       [-1, 0, 1],
                       [0, 1, 1]])
    for row in range(1, image.shape[0] - 1):
        for col in range(1, image.shape[1] - 1):
            for color_channel in range(3):
                sub_matrix = image[row - 1:row + 2, col - 1:col + 2, color_channel]
                embossed_value = np.sum(sub_matrix * kernel)
                new_img[row, col, color_channel] = embossed_value + 128 # if 0 <= embossed_value + 128 <= 255 else 0 if embossed_value + 128 < 0 else 255
    return np.clip(new_img, 0, 255)


def rectangle_select(image, x, y):
    arr = np.zeros((image.shape[0], image.shape[1]))
    for a in range(x[0],y[0]+1):
        for b in range(x[1],y[1]+1):
            arr[a,b] = 1
    return arr


def magic_wand_select(image, starting_pixel, thres):
    from collections import deque
    height, width = image.shape[:2]
    visited_pixels = np.zeros((height, width), dtype=bool)
    result = np.zeros((height, width), dtype=np.float32)

    pixel_stack = deque([starting_pixel])

    image_r = image[:, :, 0].astype(np.float32)
    image_g = image[:, :, 1].astype(np.float32)
    image_b = image[:, :, 2].astype(np.float32)

    neighbors = np.array([(0, 1), (0, -1), (1, 0), (-1, 0)], dtype=np.int32)

    x, y = starting_pixel

    while pixel_stack:
        current_x, current_y = pixel_stack.pop()

        if visited_pixels[current_x, current_y]:
            continue

        visited_pixels[current_x, current_y] = True
        result[current_x, current_y] = 1

        current_r = image_r[starting_pixel[0], starting_pixel[1]]
        current_g = image_g[starting_pixel[0], starting_pixel[1]]
        current_b = image_b[starting_pixel[0], starting_pixel[1]]

        neighbor_coords = neighbors + np.array([current_x, current_y])

        valid_neighbors = (
            (neighbor_coords[:, 0] >= 0) &
            (neighbor_coords[:, 0] < height) &
            (neighbor_coords[:, 1] >= 0) &
            (neighbor_coords[:, 1] < width)
        )

        valid_coords = neighbor_coords[valid_neighbors]

        for nx, ny in valid_coords:
            if visited_pixels[nx, ny]:
                continue

            diff_r = abs(current_r - image_r[nx, ny])
            diff_g = abs(current_g - image_g[nx, ny])
            diff_b = abs(current_b - image_b[nx, ny])
            r_avg = (current_r + image_r[nx, ny]) / 2

            dist = np.sqrt(
                (2 + r_avg/256) * diff_r**2 +
                4 * diff_g**2 +
                (2 + (255 - r_avg)/256) * diff_b**2
            )

            if dist <= thres:
                pixel_stack.append((nx, ny))
    # print(result)
    return result




def compute_edge(mask):
    rsize, csize = len(mask), len(mask[0])
    edge = np.zeros((rsize,csize))
    if np.all((mask == 1)): return edge
    for r in range(rsize):
        for c in range(csize):
            if mask[r][c]!=0:
                if r==0 or c==0 or r==len(mask)-1 or c==len(mask[0])-1:
                    edge[r][c]=1
                    continue

                is_edge = False
                for var in [(-1,0),(0,-1),(0,1),(1,0)]:
                    r_temp = r+var[0]
                    c_temp = c+var[1]
                    if 0<=r_temp<rsize and 0<=c_temp<csize:
                        if mask[r_temp][c_temp] == 0:
                            is_edge = True
                            break

                if is_edge == True:
                    edge[r][c]=1

    return edge

def save_image(filename, image):
    img = image.astype(np.uint8)
    mpimg.imsave(filename,img)

def load_image(filename):
    img = mpimg.imread(filename)
    if len(img[0][0])==4: # if png file
        img = np.delete(img, 3, 2)
    if type(img[0][0][0])==np.float32:  # if stored as float in [0,..,1] instead of integers in [0,..,255]
        img = img*255
        img = img.astype(np.uint8)
    mask = np.ones((len(img),len(img[0]))) # create a mask full of "1" of the same size of the laoded image
    img = img.astype(np.int32)
    return img, mask

def display_image(image, mask):
    # if using Spyder, please go to "Tools -> Preferences -> IPython console -> Graphics -> Graphics Backend" and select "inline"
    tmp_img = image.copy()
    edge = compute_edge(mask)
    for r in range(len(image)):
        for c in range(len(image[0])):
            if edge[r][c] == 1:
                tmp_img[r][c][0]=255
                tmp_img[r][c][1]=0
                tmp_img[r][c][2]=0

    plt.imshow(tmp_img)
    plt.axis('off')
    plt.show()
    print("Image size is",str(len(image)),"x",str(len(image[0])))


def menu():
    img = mask = np.array([])
    if img.size == 0:
        while True:
            print("What do you want to do?")
            print("e - exit")
            print("l - load a picture")
            choice = input("Your choice: ")

            if choice == 'e':
                return
            elif choice == 'l':
                filename = input("Enter the filename: ")
                img, mask = load_image(filename)
                break
            else:
                print("Invalid choice. Please try again.")

    
    display_image(img, mask)

    while True:
        print("What do you want to do?")
        print("e - exit")
        print("l - load a picture")
        print("s - save the current picture")
        print("1 - adjust brightness")
        print("2 - adjust contrast")
        print("3 - apply grayscale")
        print("4 - apply blur")
        print("5 - edge detection")
        print("6 - embossed")
        print("7 - rectangle select")
        print("8 - magic wand select")
        choice = input("Your choice: ")

        if choice == 'e':
            return
        elif choice == 'l':
            filename = input("Enter the filename: ")
            img, mask = load_image(filename)
        elif choice =='s':
            if img.size == 0:
                print("Please load an image first.")
                continue
            filename = input("Enter the filename to save: ")
            save_image(filename, img)
        elif choice == '1':
            if img.size == 0:
                print("Please load an image first.")
                continue
            while True:
                try:
                    value = int(input("Enter the brightness value (-255 to +255): "))
                    if value < -255 or value > 255:
                        print("Error: Value must be between -255 and +255.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter an integer.")
            mask = mask.astype(bool)
            modified_image = change_brightness(img, value)
            output_image = img.copy()
            output_image[mask] = modified_image[mask]
            img = output_image
        elif choice == '2':
            if img.size == 0:
                print("Please load an image first.")
                continue
            while True:
                try:
                    value = int(input("Enter the contrast value (-255 to +255): "))
                    if value < -255 or value > 255:
                        print("Error: Value must be between -255 and +255.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter an integer.")
            mask = mask.astype(bool)
            modified_image = change_contrast(img, value)
            output_image = img.copy()
            output_image[mask] = modified_image[mask]
            img = output_image
        elif choice == '3':
            if img.size == 0:
                print("Please load an image first.")
                continue
            mask = mask.astype(bool)
            modified_image = grayscale(img)
            output_image = img.copy()
            output_image[mask] = modified_image[mask]
            img = output_image
        elif choice == '4':
            if img.size == 0:
                print("Please load an image first.")
                continue
            mask = mask.astype(bool)
            modified_image = blur_effect(img)
            output_image = img.copy()
            output_image[mask] = modified_image[mask]
            img = output_image
        elif choice == '5':
            if img.size == 0:
                print("Please load an image first.")
                continue
            mask = mask.astype(bool)
            modified_image = edge_detection(img)
            output_image = img.copy()
            output_image[mask] = modified_image[mask]
            img = output_image
        elif choice == '6':
            if img.size == 0:
                print("Please load an image first.")
                continue
            mask = mask.astype(bool)
            modified_image = embossed(img)
            output_image = img.copy()
            output_image[mask] = modified_image[mask]
            img = output_image
        elif choice == '7':
            if img.size == 0:
                print("Please load an image first.")
                continue
            while True:
                try:
                    x1 = int(input("Enter the x-coordinate of the top-left corner: "))
                    y1 = int(input("Enter the y-coordinate of the top-left corner: "))
                    x2 = int(input("Enter the x-coordinate of the bottom-right corner: "))
                    y2 = int(input("Enter the y-coordinate of the bottom-right corner: "))
                    if x1 < 0 or y1 < 0 or x2 >= img.shape[0] or y2 >= img.shape[1] or x1 > x2 or y1 > y2:
                        print("Error: Invalid coordinates.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter integers.")
            x = (y1, x1)
            y = (y2, x2)
            mask = rectangle_select(img, x, y)
        elif choice == '8':
            if img.size == 0:
                print("Please load an image first.")
                continue
            while True:
                try:
                    starting_pixel = (int(input("Enter the x-coordinate of the starting pixel: ")),
                                      int(input("Enter the y-coordinate of the starting pixel: ")))
                    if starting_pixel[0] < 0 or starting_pixel[0] >= img.shape[0] or starting_pixel[1] < 0 or starting_pixel[1] >= img.shape[1]:
                        print("Error: Invalid starting pixel coordinates.")
                        continue
                    thres = int(input("Enter the color distance threshold: "))
                    if thres < 0 or thres > 255:
                        print("Error: Threshold must be between 0 and 255.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter integers.")
            mask = magic_wand_select(img, starting_pixel, thres)
        else:
            print("Invalid choice. Please try again.")
            continue

        if img.size > 0:
            display_image(img, mask)


if __name__ == "__main__":
    menu()
