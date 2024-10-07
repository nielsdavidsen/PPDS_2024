import handin5 as h5
import matplotlib.pyplot as plt
import numpy as np

mnist_data = h5.read_mnist_csv('mnist_test_200.csv')

digit_image_groups = h5.group_by_label(mnist_data)


rand_dig = np.random.randint(0,10)
digit_image = h5.get_image(digit_image_groups, rand_dig)

print(len(digit_image))

plt.imshow(digit_image, cmap='gray')
plt.axis('off')
plt.savefig('random_image.png')