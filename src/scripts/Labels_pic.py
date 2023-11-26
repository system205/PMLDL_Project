from matplotlib import pyplot as plt
from scipy import ndimage

def represent_labels(rows, columns, path):
    label_names = ['Apples', 'Bananas', 'Bread', 'Carrot', 'Cheese',
                   'Cucumbers', 'Eggs', 'Meat', 'Milk', 'Sausages', 'Tomatoes']
    labels = [get_label_photos(label_names[i], columns, path) for i in range(rows)]
    k = 2
    f, axarr = plt.subplots(rows, columns, figsize=(3 * k, 12 * k), sharex=True, sharey=True)
    f.subplots_adjust(hspace=0.2)
    for i in range(rows * columns):
        axarr[i // columns, i % columns].imshow(labels[i // columns][i % columns])
        # Add row label as title
        if i % columns == 0:
            axarr[i // columns, i % columns].set_title(label_names[i // 3], fontsize=20)
        axarr[i // columns, i % columns].axis('off')  # Remove the axes
    plt.savefig("labels.png", dpi=500)


# def get_label_photos(label, col, path):
#     image_paths = [path + "/" + label + "/" + label + str(i) + ".jpg" for i in range(1, col + 1)]
#     return [plt.imread(image_path) for image_path in image_paths]


def get_label_photos(label, col, path):
   image_paths = [path + "/" + label + "/" + label + str(i) + ".jpg" for i in range(1, col + 1)]
   images = [plt.imread(image_path) for image_path in image_paths]
   rotated_images = []
   for image in images:
       if image.shape[0] > image.shape[1]: # If height is greater than width
           rotated_images.append(ndimage.rotate(image, 90)) # Rotate by 90 degrees
       else:
           rotated_images.append(image)
   return rotated_images

path_to_dataset = "dataset"
represent_labels(11, 3, path_to_dataset)
